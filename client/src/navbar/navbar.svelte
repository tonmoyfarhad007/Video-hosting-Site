<script>
    import { link } from "svelte-spa-router";
    import { isLoggedIn } from '../store/profileStore.js';
    import {fetchAllUsersData} from '../store/registrationStore.js';
    
    export const login = "/login";
    export const home = "/";
    export const about = '/about';
    export const contact = '/contact'

    let navbarItem = ["home-col","profile-col","contact-col"];
    let alluserData = fetchAllUsersData;
    alluserData.getRegistrationData();

    function changeColor(id){
      // debugger;

      if(id === "profile-col"){
        if($isLoggedIn){
          window.location.href = "#/userDetails";
        }else{
          window.location.href = "#/login";
        }
      }


      document.getElementById(id).style.backgroundColor = "green";
      
      navbarItem.forEach(e =>{
          if(e !== id){
            document.getElementById(e).style.backgroundColor = "#333";          
               
          }
      });
    }

    function redirectToLoginOrRegister(id){
      if(id==="login"){
        if($isLoggedIn){
          window.location.href = "#/userDetails";
          alert('Already logged in')
        }else{
          window.location.href = "#/login";
        }
        
      }else if(id==="register"){
        window.location.href = "#/register";
      }

      navbarItem.forEach(e =>{
        document.getElementById(e).style.backgroundColor = "#333";
      });

    }
  
</script>

<nav class="sticky top-0">
    <div class="topnav">
        <div class="flex justify-around">
            <div class="ml-48">
              <a id="home-col" href on:click={()=>changeColor("home-col")} use:link={home}> Home</a>
              <a class="cursor-pointer" id="profile-col" on:click={()=>changeColor("profile-col")}>Profile</a>
              <!-- <a id="about-col" href on:click={()=>changeColor("about-col")} use:link={about}>About</a> -->
              <a id="contact-col" href on:click={()=>changeColor("contact-col")} use:link={contact}>Contact</a>
            </div>

            <div class="flex">
              <div class="login mr-2" on:click={()=>redirectToLoginOrRegister("login")}>Login</div>
              <div class="register" on:click={()=>redirectToLoginOrRegister("register")}>Register</div>
            </div>
        </div>
    </div>
</nav>

<style>

  .login{
    @apply flex w-20 h-8 mt-3 justify-center cursor-pointer rounded-md bg-blue-600 text-white p-1;
  }
  .register{
    @apply flex w-20 h-8 mt-3 justify-center cursor-pointer rounded-md bg-blue-600 text-white p-1;
  }


.topnav {
  overflow: auto;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* .topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #04AA6D;
  color: white;
} */

</style>