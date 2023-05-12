import { writable } from 'svelte/store';


function singleUserData(){
    
    const { subscribe, set, update } = writable("");

    return {
        subscribe,
        set: (val) => {set(val);},

        print: (msg) => {console.log(msg)},

        featchSingleUserData: async (email) => {
            
            let url = "/getUserDetailsByEmail/"+email;
            console.log(url);

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
                const res = await fetch(url, {
                method: "GET",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                }).then(checkStatus)
                .then(parseJSON);

                let singleData = res.single_data;

                url = "/getSingleUserRegistrationData/"+email;
                const res_1 = await fetch(url, {
                    method: "GET",
                        headers: {
                            'Content-Type': 'application/json'
                        },
                }).then(checkStatus)
                .then(parseJSON);

                if(singleData.length > 0){
                    

                    singleData[0].username = res_1.single_data[0].username;
                    singleData[0].role = res_1.single_data[0].role;

                    console.log(singleData);
                    hasCOntent.set(true);
                    set(singleData);
                }else{
                    // let data = res_1.single_data;
                    // data[0].title = "";
                    hasCOntent.set(false);
                    set(res_1.single_data);
                }

                
                
            } catch (e) {
                console.log(e);
            }
            
        },

        featchSingleUserRegistrationData: async (email) => {
            // debugger;
            let url = "/getSingleUserRegistrationData/"+email;
            console.log(url);

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
                const res = await fetch(url, {
                method: "GET",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                }).then(checkStatus)
                .then(parseJSON);
                // debugger;

                let singleData = res.single_data;

                console.log(singleData);
                set(singleData);
                
            } catch (e) {
                error = e
            }
            
        }

        
    
        
    }
}


export const fetchSingleData   = singleUserData();

export let isLoggedIn = writable(false);
export let hasCOntent = writable(true);
export let isUpdate = writable(false);
export let isUpload = writable(false);

