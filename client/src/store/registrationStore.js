import { writable } from 'svelte/store';


function allUsersData(){
    
    const { subscribe, set, update } = writable("");

    return {
        subscribe,
        set: (val) => {set(val);},

        print: (msg) => {console.log(msg)},

        getRegistrationData: async ()=>{

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
                const res = await fetch("/getAllUsers", {
                method: "GET",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                }).then(checkStatus)
                .then(parseJSON);
                // debugger;
                let allData = [];
                res.all_data.forEach(e => {
                    if(e.role !== "admin"){
                        allData.push(e);
                    }
                });
                console.log(allData)
                set(allData);
                
            } catch (e) {
                console.log(e)
                
            }
        }

        
    
        
    }
}


export const fetchAllUsersData   = allUsersData();

