import axios from "axios";

const apiUrl = "http://192.168.31.98:5000/api";


export const getGptResponse = async (user,problem,module,time) => {
    try{
        let userid = sessionStorage.getItem("userId") || "";
        let response;
        console.log(userid);
        if (!userid) {
            response = await axios.post(`${apiUrl}/getGPTResponse`, {
                text: problem,
                user: user,
                max_tokens: 100,
                model: module,
            });
        }
        else{
            response = await axios.post(`${apiUrl}/getGPTResponse`, {
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
        const response = await axios.get(`${apiUrl}/getCharHistory`);
        return response.data.history;
    } catch(error){
        console.log(error);
        return "Error getting character history";
    }
};