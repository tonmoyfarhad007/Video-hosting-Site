<script>
    import {fetchAllUsersData} from '../store/registrationStore.js';
    
    let users = fetchAllUsersData;

    async function deleteUser(email){
        let url = "/deleteUser/"+email
        let response = await fetch(url, {
            method: 'POST',
            body: ''
        });

        const data = await response.json();
        console.log(data)

        url = "/deleteUserContent/"+email
        let response_1 = await fetch(url, {
            method: 'POST',
            body: ''
        });

        const data_1 = await response_1.json();
        console.log(data_1);
        users.getRegistrationData();
    }

</script>

<svelte:head>
	<link rel="stylesheet" href="https://unpkg.com/mono-icons@1.0.5/iconfont/icons.css" >
</svelte:head>

<p class="text-blue-700">List of all users:</p>
<div class="pt-3 grid grid-cols-3 gap-5">
    {#each $users as item}
        <div class="card">
            <div class="container">
            <div class="flex justify-between">
                <h4><b>{item.username}</b></h4> 
                <button on:click={()=> deleteUser(item.email)}><i class="text-red-500 mi mi-user-remove"/></button>
            </div>
            <p>{item.email}</p> 
            </div>
        </div>
    {/each}      
</div>

<style>
    .mi {
		font-size: 1.4rem;
	}
    .card {
      @apply rounded-md bg-cyan-100;
      box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
      transition: 0.3s;
      width: 90%;
    }
    
    .card:hover {
      box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    
    .container {
      padding: 2px 16px;
    }
</style>