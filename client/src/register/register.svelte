<script>

    import { fetchAllUsersData } from '../store/registrationStore.js';

    async function onSubmit(e) {
        const formData = new FormData(e.target);

        let response = await fetch('/register', {
        method: 'POST',
        body: formData
        });

        const data = await response.json();
        console.log(data['success']);
        fetchAllUsersData.getRegistrationData();
        if(data['success']) {
            window.location.href = "#/login";
        }else{
            alert("Somthing wrong with registration please try again");
        }
        

        
    }

</script>

<div class="center">
    <form on:submit|preventDefault={onSubmit}>

        <div class="container">
            <h1>Register</h1>
            <p>Please fill in this form to create an account.</p>
            <hr>
            
            <label for="fname"><b>Full Name</b></label>
            <input type="text" placeholder="Enter Full Name" name="username" id="username" value="" required>

            <label for="role"><b>Role</b></label>
            <input type="text" placeholder="Enter Role" id="role" name="role" value="" required>
            
            <label for="email"><b>Email</b></label>
            <input type="text" placeholder="Enter Email" id="email" name="email" value="" required>
        
            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" id="password" name="password" value="" required>
        
            <!-- <label for="psw-repeat"><b>Repeat Password</b></label>
            <input type="password" placeholder="Repeat Password" name="psw-repeat" id="psw-repeat" required> -->
            <hr>
            <p>By creating an account you agree to our <a href="#">Terms & Privacy</a>.</p>
        
            <button type="submit" class="registerbtn">Register</button>
          </div>
          
          <div class="container signin">
            <p>Already have an account? <a href="#/login">Log in</a>.</p>
          </div>
        
    </form>  
</div>

<style>
    * {
        box-sizing: border-box;
    }

    /* Add padding to containers */
    .container {
        padding: 16px;
        background-color: white;
    }

    /* Full-width input fields */
    input[type=text], input[type=password] {
        @apply rounded-md;
        width: 100%;
        padding: 15px;
        margin: 5px 0 22px 0;
        display: inline-block;
        border: none;
        background: #f1f1f1;
    }

    input[type=text]:focus, input[type=password]:focus {
        background-color: #ddd;
        outline: none;
    }

    hr {
        border: 1px solid #f1f1f1;
        margin-bottom: 25px;
    }

    .registerbtn {
        @apply rounded-md;
        background-color: #04AA6D;
        color: white;
        padding: 16px 20px;
        margin: 8px 0;
        border: none;
        cursor: pointer;
        width: 100%;
        opacity: 0.9;
    }

    .registerbtn:hover {
        opacity: 1;
    }

    a {
        color: dodgerblue;
    }

    .signin {
        background-color: #f1f1f1;
        text-align: center;
    }

    .center{
        display: flex;
        justify-content: center;
    }
</style>
