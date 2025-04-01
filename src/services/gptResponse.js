import api from "@/services/interfaceApi";



export const getGptResponse = async (user,problem,module,time) => {
    try{
        let userid = sessionStorage.getItem("userId") || "";
        let response;
        if (!userid) {
            response = await api.post(`/getGPTResponse`, {
                text: problem,
                user: user,
                model: module,
            });
        }
        else{
            response = await api.post(`/getGPTResponse`, {
                text: problem,
                user: user,
                model: module,
                userid: userid,
                time:time
            });
        }
        return response.data;
    } catch(error){
        console.log(error);
        return "Error getting GPT model response";
    }
};


export const getCharHistory = async (userid) => {
    try{
        const response = await api.post(`/getGPTHistory`,{
            user_id: userid 
        });
        return response.data;
    } catch(error){
        console.log(error);
        return "Error getting character history";
    }
};


export const delMessages = async (userid) => {
    try{
        const response = await api.post(`/delMessage`,{
            user_id: userid 
        });
        return response.data.message;
    } catch(error){
        console.log(error);
        return "Error deleting messages";
    }
};