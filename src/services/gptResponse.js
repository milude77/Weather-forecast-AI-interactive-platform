import api from "@/services/interfaceApi";



export const getGptResponse = async (user,problem,module,time) => {
    try{
        let userid = sessionStorage.getItem("userId") || "";
        let response;
        if (!userid) {
            response = await api.post(`/getGPTResponse`, {
                text: problem,
                user: user,
                max_tokens: 100,
                model: module,
            });
        }
        else{
            response = await api.post(`/getGPTResponse`, {
                text: problem,
                user: user,
                max_tokens: 100,
                model: module,
                userid: userid,
                time:time
            });
        }
        console.log(response.data);
        return response.data;
    } catch(error){
        console.log(error);
        return "Error getting GPT-3 response";
    }
};


export const getCharHistory = async () => {
    try{
        const response = await api.get(`/getCharHistory`);
        return response.data.history;
    } catch(error){
        console.log(error);
        return "Error getting character history";
    }
};