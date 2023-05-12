<script>
  import {fetchSingleData,isLoggedIn} from '../store/profileStore.js';

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



</script>


<div class="container">
    <div style="text-align:center">
      <h2 class="font-bold text-2xl">Contact Us</h2>
      <p class="font-medium">Swing by for a cup of coffee, or leave us a message:</p>
    </div>
    <div class="row">
      <div class="column">
        <img class="mt-8" src="/image/map.jpg" style="width:100%">
      </div>
      <div class="column">
        <form action="/action_page.php">
          <label for="fname">First Name</label>
          <input type="text" id="fname" name="firstname" placeholder="Your name..">
          <label for="lname">Last Name</label>
          <input type="text" id="lname" name="lastname" placeholder="Your last name..">
          <label for="country">Country</label>
          <select id="country" name="country">
            <option value="australia">Australia</option>
            <option value="canada">Canada</option>
            <option value="usa">USA</option>
          </select>
          <label for="subject">Subject</label>
          <textarea id="subject" name="subject" placeholder="Write something.." style="height:170px"></textarea>
          <input type="submit" value="Submit">
        </form>
      </div>
    </div>
  </div>
<style>
    input[type=text], select, textarea {
        @apply rounded-md;
        width: 100%;
        padding: 12px;
        border: 1px solid #ccc;
        margin-top: 6px;
        margin-bottom: 16px;
        resize: vertical;
    }

    input[type=submit] {
        @apply rounded-md;
        background-color: #04AA6D;
        color: white;
        padding: 12px 20px;
        border: none;
        cursor: pointer;
    }

    input[type=submit]:hover {
        background-color: #45a049;
    }

    /* Style the container/contact section */
    .container {
        border-radius: 5px;
        background-color: #f2f2f2;
        padding: 10px;
    }

    /* Create two columns that float next to eachother */
    .column {
        float: left;
        width: 50%;
        margin-top: 6px;
        padding: 20px;
    }

    /* Clear floats after the columns */
    .row:after {
        content: "";
        display: table;
        clear: both;
    }

/* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .column, input[type=submit] {
    width: 100%;
    margin-top: 0;
  }
}

</style>  