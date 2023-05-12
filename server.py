import os
from io import BytesIO
from django.shortcuts import redirect
from flask import Flask, request, send_from_directory, jsonify, send_file,redirect,url_for, session
from flask_sqlalchemy import SQLAlchemy

import random

from matplotlib.image import thumbnail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/user.db'
db = SQLAlchemy(app)
app.secret_key = 'SECRETKEY'


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(20),unique=True, nullable=False)

class UserContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(20),unique=True, nullable=False)
    thfilename = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(120), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/register", methods=["POST"])
def register():
    try:
        print(request.form)
        username = request.form['username']
        role     = request.form['role']
        email    = request.form['email']
        password = request.form['password']

        user = User(username=username, role=role, email=email, password=password)
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify({'success': False}) 
    
    return jsonify({'success': True}) 

@app.route("/login", methods=['POST'])
def login():
    print(request.form)
    password = request.form['password']
    email    = request.form['email']
    user     = User.query.filter_by(email=email).first()
    print(user.id)
    if user.password != '' and user.password == password:
        print("login successfull")
        return jsonify({'success': True})
    else:
        print("login fail")
        return jsonify({'success': False})
        
@app.route("/upload", methods=['POST'])
def testUpload():
    try:
        print(request.form)
        email = request.form['email']
        title = request.form['title']
        file = request.files['file']
        thumbnailFile = request.files['thFile']
        print(file)
        userContent = UserContent(email=email, title=title, filename=file.filename,thfilename=thumbnailFile.filename)
        db.session.add(userContent)
        db.session.commit()
        static_file_name = str(userContent.id) + file.filename
        static_thfile_name = str(userContent.id) + thumbnailFile.filename
        file.save(os.path.join('static/videos', static_file_name))
        thumbnailFile.save(os.path.join('static/thumbnill', static_thfile_name))
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})


@app.route("/deleteUserContent/<email>", methods=['POST'])
def deleteUserContent(email):
    try:
        uc = UserContent.query.filter_by(email=email).first()
        fileName = "static/videos/"+str(uc.id)+uc.filename
        thFileName = "static/thumbnill/"+str(uc.id)+uc.thfilename
        os.remove(fileName)
        os.remove(thFileName)
        UserContent.query.filter_by(email=email).delete()
        db.session.commit()
        
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})


@app.route("/deleteUser/<email>", methods=['POST'])
def deleteUser(email):
    try:
        User.query.filter_by(email=email).delete()
        db.session.commit()
        
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})


@app.route("/updateUserContent/<email>", methods=['POST'])
def updateUserContent(email):
    try:
        print(request.form)
        title = request.form['title']
        thFile = request.files['thFile']

        uc = UserContent.query.filter_by(email=email).first()
        
        new_thFileneme = str(uc.id)+thFile.filename
        thFile.save(os.path.join('static/thumbnill', new_thFileneme))
        
        uc.thfilename = thFile.filename
        uc.title = title
        db.session.commit()
        
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})

@app.route("/getUserDetailsByEmail/<email>", methods=['GET'])
def getUserDetails(email):
    try:
        print(request.form)
        userDetails = UserContent.query.filter_by(email=email).first()
        file_name = str(userDetails.id)+userDetails.filename
        thfile_name = str(userDetails.id)+userDetails.thfilename
        jsonData = {
                    'email':userDetails.email,
                    'title':userDetails.title,
                    'url':url_for('static', filename='videos/' + file_name),
                    'th_url':url_for('static', filename='thumbnill/' + thfile_name)
                   }
        return jsonify({'single_data': [jsonData]})
    except:
        return jsonify({'single_data': []})

@app.route("/getAllUsersDetails", methods=['GET'])
def getAllUsersData():
    try:
        # print(request.form)
        userDetails = UserContent.query.all()
        allData = []
        for data in userDetails:
            file_name = str(data.id)+data.filename
            thfile_name = str(data.id)+data.thfilename
            jsonData = {
                        'username':getUsernameByEmail(data.email),
                        'email':data.email,
                        'title':data.title,
                        'url':url_for('static', filename='videos/' + file_name),
                        'th_url':url_for('static', filename='thumbnill/' + thfile_name)
                       }
            allData.append(jsonData)
        return jsonify({'all_data': allData})
    except:
        return jsonify({'all_data': []})


@app.route("/getAllUsers", methods=['GET'])
def getAllUsers():
    try:
        # print(request.form)
        user = User.query.all()
        allData = []
        for data in user:
            jsonData = {
                        'email':data.email,
                        'role':data.role,
                        'username': data.username
                       }
            allData.append(jsonData)
        return jsonify({'all_data': allData})
    except:
        return jsonify({'all_data': []})


@app.route("/getSingleUserRegistrationData/<email>", methods=['GET'])
def getSingleUserRegistrationData(email):
    try:
        print(request.form)
        userDetails = User.query.filter_by(email=email).first()
        
        jsonData = {
                    'email':userDetails.email,
                    'role':userDetails.role,
                    'username':userDetails.username
                   }
        return jsonify({'single_data': [jsonData]})
    except:
        return jsonify({'single_data': []})
    

@app.route("/storeEmailInSession/<email>", methods=['POST'])
def storeEmailInSession(email):
    try:
        print(email) 
        session['email'] = email
        session['status'] = True
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})

@app.route("/getEmaiFromSession", methods=['GET'])
def getEmailFromSession():
    try:
        email = session['email']
        status = session['status']
        jsonData = {
                    'email': email,
                    'status':status
                }
        return jsonify({'session_data': [jsonData]})
    except:
        return jsonify({'session_data': []})    


@app.route("/removeEmaiFromSession", methods=['GET'])
def removeEmailFromSession():
    try:
        session.pop('emai', None)
        session.pop('status', None)
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})


def getUsernameByEmail(email):
    user = User.query.filter_by(email=email).first()
    return user.username


if __name__ == "__main__":
    app.run(debug=True)
