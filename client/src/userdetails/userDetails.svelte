<script>

   
   import {fetchSingleData, isLoggedIn, hasCOntent, isUpdate,isUpload} from "../store/profileStore.js";
   import {removeSessionData} from "../store/sessionStore.js";
   import ContentUpload from "./contentUpload.svelte";
   import UpdateContent from './update.svelte';
   import Admin from './admin.svelte';



   document.getElementById("profile-col").style.backgroundColor = "green";
   document.getElementById("profile-col").style.color = "white";

   let singlePersonsContent = fetchSingleData;
   
   function handleLogout(){
        removeSessionData.rmvSessionData();
        isLoggedIn.set(false)
        window.location.href = "#/login";
   }

   let showUpdate = false;
   let upload = false;

   let sessionData=[];
   async function getSessionData(){
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
            sessionData = res.session_data;
            
            let email = sessionData[0].email;
            fetchSingleData.featchSingleUserData(email);
            if(sessionData.length>0){
                isLoggedIn.set(true);
            } 
            
        } catch (e) {
            console.log(e)
            
        }
    }

   if(!$isLoggedIn) {

        getSessionData();
   }

   async function deleteUserContent(email){
        let url = "/deleteUserContent/"+email
        let response = await fetch(url, {
            method: 'POST',
            body: ''
        });

        const data = await response.json();
        console.log(data);
        if(data['success']){
            singlePersonsContent.featchSingleUserData(email);
        }
        
   }

   
</script>

<div>

{#if $isLoggedIn}
    <div class="m-6">
        <div class="text-center mb-7">
            <p class="text-blue-800 text-2xl">welcome to your profile!!!</p>
        </div>
        {#each $singlePersonsContent as content}
            <div class="flex justify-around border-2 rounded-md bg-green-300">
                <div>Name:{content.username}</div>
                <div>Role: {content.role}</div>
                <button on:click={()=> handleLogout()}>
                    <div class="flex justify-center">
                        <div class="mr-1">log out</div>
                        <div class="pt-1"><i class="mi mi-log-out"></i></div>
                        
                    </div>
                     
                </button>
            </div>
            {#if $hasCOntent}
            <div class="text-center">
                <p class="text-xl font-bold mt-3 mb-2">{content.title}</p>
                <div class="video-container rounded-md border-2">
                    <video class="w-full h-full rounded-md" controls poster={"http://127.0.0.1:5000"+content.th_url}>
                        <source src={"http://127.0.0.1:5000"+content.url} type="video/mp4"> 
                    </video>
                </div>
                <div class="flex justify-center mb-3">
                    <div class="btn-update mr-3" on:click={()=> isUpdate.set(showUpdate=!showUpdate)}>Update</div>
                    <div class="btn-delete" on:click={()=> deleteUserContent(content.email)}>Delete</div>
                </div>
                {#if $isUpdate}
                    <div class="update-content border-2 rounded-md">
                        <UpdateContent email={content.email}></UpdateContent>
                    </div>
                    
                    
                {/if}
            </div>
                
            {:else}

                {#if content.role=="admin"}
                    <div class="flex justify-center mt-3 mb-3">
                        <div class="mr-3 p-1"><p>Hello Mr. Admin if you want to upload a content please click the upload button</p></div>
                        <div class="btn-upload" on:click={()=> isUpload.set(upload=!upload)}>Upload </div>
                    </div>
                    
                    
                    {#if $isUpload}
                    <div class="border-2 rounded-md mt-3">
                        <ContentUpload email={content.email}></ContentUpload>
                    </div>
                    
                        
                    {/if}
                {:else}
                <div class="border-2 rounded-md mt-3">
                    <ContentUpload email={content.email}></ContentUpload>
                </div>
                    
                {/if}
            
                
            {/if}

            {#if content.role=="admin"}
                <Admin></Admin>
            {/if}
        {/each}
    </div>
    

{/if}

    
    
</div>

<style>
    .btn-update {
        @apply flex w-20 justify-center cursor-pointer rounded-md bg-blue-600 text-white p-1;
    }
    .btn-upload {
        @apply flex w-20 justify-center cursor-pointer rounded-md bg-green-600 text-white p-1;
    }
    .btn-delete {
        @apply flex w-20 justify-center cursor-pointer rounded-md bg-red-600 text-white p-1;
    }
    .update-content {
        display: inline-block;
        vertical-align: top;
        width: 650px;
        
    }
    .video-container {
        display: inline-block;
        vertical-align: top;
        width: 650px;
        
    }
</style>