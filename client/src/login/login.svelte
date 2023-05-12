<script >
    import {fetchSingleData, isUpload,isLoggedIn} from '../store/profileStore.js';
    import {saveSessionData} from '../store/sessionStore.js';

    let isRegister = false;
    let isLogin    = false;

    let singleData = fetchSingleData;

    redirectBasedSessionData();

    async function redirectBasedSessionData(id){
        // debugger;
        const parseJSON = (resp) => (resp.json ? resp.json() : resp);
        const checkStatus = (resp) => {
            if (resp.status >= 200 && resp.status < 300) {
                return resp;
            }
            return parseJSON(resp).then((resp) => {
                throw resp;
            });
        };
        const headers = {
            'Content-Type': 'application/json',
        };
        try {
            const res = await fetch('/getEmaiFromSession', {
                method: "GET",
                    headers: {
                        'Content-Type': 'application/json'
                    },
            }).then(checkStatus)
            .then(parseJSON);
            // debugger;
            let sessionData = res.session_data;
            
            let email = sessionData[0].email;
            fetchSingleData.featchSingleUserData(email);
            if(sessionData.length>0){
                isLoggedIn.set(true);
                redirectToLoginOrRegister(id);
            } 
            
        } catch (e) {
            console.log(e)
            
        }
    }




    async function onSubmit(e) {
      const formData = new FormData(e.target);

      const data = {};
      for (let field of formData) {
        const [key, value] = field;
        data[key] = value;
      }
      let email = data.email;
      
      try{

        let response = await fetch('/login', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        isLogin = data['success'];

        if(isLogin){
            isLoggedIn.set(true)
            console.log(email);
            saveSessionData.storeEmailInSession(email);
            fetchSingleData.featchSingleUserData(email);
            isUpload.set(false);
            // fetchSingleData.featchSingleUserRegistrationData(email);
            window.location.href = "#/userDetails";
        }else{
            alert("Wrong Pmail or Password!!!");
        }

      }catch(e){
            isLoggedIn.set(false);
            isLogin = false;
            console.log(e);
            alert("Wrong Pmail or Password!!!");

      }

      
    }

    function sendToRegister(){
        // debugger;
        let navbarItem = ["home-col","profile-col","contact-col"];
        navbarItem.forEach(e =>{
            document.getElementById(e).style.backgroundColor = "#333";
        });
        window.location.href = "#/register";
        isRegister = true;
    }
</script>


<div class="center pt-10">
    <div>
        <form on:submit|preventDefault={onSubmit}>
            <div class="container">
                <label for="uname"><b>Email</b></label>
                <input type="text" placeholder="Enter email" id="email" name="email" value="" required>
            
                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" id="password" name="password" value="" required>
                    
                <button class="login-btn" type="submit">Login</button>
            </div>
            
        </form> 
        <div class="pt-6 flex justify-center">
            <p class="p-1 pr-3">If you don't have any account please sign up here</p>
            <button class="center rounded-md w-20 bg-blue-600 text-white p-1" on:click={()=>sendToRegister()}>Sign up</button>
        </div> 
        <!-- <div class="center border-2 rounded-md" on:click={()=>sendToRegister()}>Register</div>  -->
    </div>
</div>

<style>
    .center{
        display: flex;
        justify-content: center;
    }

    form {
        @apply rounded-md;
        border: 3px solid #f1f1f1;
    }

    input[type=text], input[type=password] {
        @apply rounded-md;
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        box-sizing: border-box;
    }

    .login-btn {
        @apply rounded-md;
        background-color: #04AA6D;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        cursor: pointer;
        width: 100%;
    }

    button:hover {
        opacity: 0.8;
    }

    
    .container {
        @apply rounded-md;
        padding: 16px;
    }

    
</style>

