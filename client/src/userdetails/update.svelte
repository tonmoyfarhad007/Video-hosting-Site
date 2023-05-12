<script>

    import {fetchSingleData, isUpdate} from "../store/profileStore.js";
    export let email;
    console.log(email);

    async function onSubmit(e){
        // debugger;

        const formData = new FormData(e.target);
        let url ='/updateUserContent/'+email;
        let response = await fetch(url, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        console.log(data);
        if(data['success']){
            fetchSingleData.featchSingleUserData(email);
            isUpdate.set(false);
        }
    }
</script>

<div>
    <form on:submit|preventDefault={onSubmit}>

        <div class="container">
            <h1>Update Your Content</h1>
            <hr>
            
            <label for="fname"><b>Title</b></label>
            <input type="text" placeholder="Write the title of your video" name="title" id="username" value="" required>

            <label for="thumbnill"><b>Choose Thumbnill image</b></label>
            <input type="file" placeholder="select thumbnill image" id="thFile" name="thFile" value="" required>
            <br>
            
            <button type="submit" class="registerbtn">Upload</button>
          </div>
          
        
    </form>
</div>

<style>
    * {
    box-sizing: border-box;
    }

    /* Add padding to containers */
    .container {
        padding: 4px 11px;
        background-color: white;
    }

    input[type=text] {
        @apply rounded-md;
        width: 100%;
        padding: 15px;
        margin-bottom: 7px;
        border: none;
        background: #f1f1f1;
    }

    input[type=text]:focus {
        background-color: #ddd;
        outline: none;
    }

    
    hr {
        border: 1px solid #f1f1f1;
        margin-bottom: 10px;
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


</style>