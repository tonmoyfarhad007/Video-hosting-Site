<script>

    import {hasCOntent,isUpload} from "../store/profileStore.js";
    import {fetchSingleData} from '../store/profileStore.js';
    export let email;
    async function onSubmit(e){
        // debugger;

        const formData = new FormData(e.target);

        let response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        console.log(data);
        if(data['success']){
            fetchSingleData.featchSingleUserData(email);
            hasCOntent.set(true);
            isUpload.set(false);
        }else{
            alert("This video is already uploaded by another user!!");
        }
    }

</script>

<div class="center">
    <form on:submit|preventDefault={onSubmit}>

        <div class="container">
            <h1>Upload Your Video</h1>
            <hr>
            
            <label for="fname"><b>Title</b></label>
            <input type="text" placeholder="Write the title of your video" name="title" id="username" value="" required>

            <label for="thumbnill"><b>Choose Thumbnill image</b></label>
            <input type="file" placeholder="select thumbnill image" id="thFile" name="thFile" value="" required>
            <br>

            <!-- <label for="email"><b>Email</b></label> -->
            <input class="hidden" type="text" placeholder="Enter Email" id="email" name="email" bind:value={email} required>
            
            <div class="pt-4">
                <label class="pt-3 vdo-lbl" for="video"><b>Choose Video</b></label>
                <input type="file" placeholder="Select video" id="file" name="file" value="" required>
            
            </div>
            
            
            <button type="submit" class="registerbtn">Upload</button>
          </div>
          
        
    </form>  
</div>

<style>
    .vdo-lbl{
        margin-right: 84px;
    }
    * {
    box-sizing: border-box;
    }

    /* Add padding to containers */
    .container {
        padding: 16px;
        background-color: white;
    }

    /* Full-width input fields */
    input[type=text] {
        @apply rounded-md;
        width: 100%;
        padding: 15px;
        margin: 5px 0 22px 0;
        /* display: inline-block; */
        border: none;
        background: #f1f1f1;
    }

    input[type=text]:focus {
        background-color: #ddd;
        outline: none;
    }

    /* Overwrite default styles of hr */
    hr {
        border: 1px solid #f1f1f1;
        margin-bottom: 4px;
    }

    /* Set a style for the submit button */
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

    
    
    .center{
        display: flex;
        justify-content: center;
    }
</style>
