<script>

    import SearchBar from './searchBar.svelte';
    import {fetchSingleData, isUpload,isLoggedIn} from '../store/profileStore.js';
    


    document.getElementById("home-col").style.backgroundColor = "green";
    document.getElementById("home-col").style.color = "white";


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


    async function getData(){
        // debugger
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
            const res = await fetch("/getAllUsersDetails", {
            method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                },
            }).then(checkStatus)
            .then(parseJSON);
            // debugger;getSingleUserRegistrationData
            let allData = res;
            console.log(allData.all_data);
            return allData.all_data;
        } catch (e) {
            console.log(e)
            return e
        }
            
    }

</script>

<div class="mt-6 text-center font-bold">
    <SearchBar></SearchBar>
    <div class="p-3"><hr class="border-2"></div>
</div>
<div class="flex justify-center">
    <div class="all">all</div>
    <div class="item">category 1</div>
    <div class="item">category 2</div>
    <div class="item">category 3</div>
    <div class="item">category 4</div>
    <div class="item">category 5</div>
    <div class="item">category 6</div>
</div>
{#await getData()}
    loding....
{:then items} 
<div class="pt-10 p-10 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5">

    {#each items as item}
    <div class="card-container rounded-md overflow-hidden shadow-lg bg-white w-full h-full">
        <video class="w-full" controls poster={"http://127.0.0.1:5000"+item.th_url}>
            <source src={"http://127.0.0.1:5000"+item.url} type="video/mp4"> 
        </video>
        <div class="flex flex-col gap-y-11 h-full w-full">
            <div class="px-6 py-4">
                <div class="font-bold md:text-lg lg:text-xl mb-2">{item.title}</div>
            </div>
            <div class="flex">
                <div>
                    <h4 class="px-1 pb-2 text-xs">Uploaded by: </h4>
                </div>
                <div>
                    <h4 class="font-medium pb-2 text-xs text-blue-600 italic">{item.username}</h4>
                </div>
                
            </div>
        </div>
        <!-- <div class="flex">
            <div>uploaded by:</div>
            <div>{item.username}</div>

        </div> -->
    </div>
    {/each}
    

</div>
    
{/await}


<style>
    .item {
        @apply flex justify-center w-24 cursor-pointer rounded-md bg-slate-400 text-white p-1 mr-2;
    }
    .all {
        @apply flex justify-center w-24 cursor-pointer rounded-md bg-stone-800 text-white p-1 mr-2;
    }
</style>
