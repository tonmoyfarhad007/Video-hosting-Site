import { writable } from 'svelte/store';


function deleteSessionData(){
    
    const { subscribe, set, update } = writable("");

    return {
        subscribe,
        set: (val) => {set(val);},

        print: (msg) => {console.log(msg)},

        rmvSessionData: async ()=>{
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
                const res = await fetch('/removeEmaiFromSession', {
                    method: "GET",
                        headers: {
                            'Content-Type': 'application/json'
                        },
                }).then(checkStatus)
                .then(parseJSON);
                // debugger;
                let sessionData = res.session_data;
                console.log(sessionData);
                set(sessionData); 
                
            } catch (e) {
                console.log(e)
                
            }
        }       
    }
}


function storeSessionData(){
    
    const { subscribe, set, update } = writable("");

    return {
        subscribe,
        set: (val) => {set(val);},

        print: (msg) => {console.log(msg)},

        storeEmailInSession: async (email)=>{
            let surl = '/storeEmailInSession/'+email;
            console.log(surl);
            let response = await fetch(surl, {
                method: 'POST',
                body: ''
            });
            const sdata = await response.json();
            console.log(sdata);
        }

            
        
    }
}


export const removeSessionData   = deleteSessionData();
export const saveSessionData   = storeSessionData();

