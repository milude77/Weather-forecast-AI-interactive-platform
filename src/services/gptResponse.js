import axios from "axios";



export const getGptResponse = async (user,problem,module) => {
    try{
        const response = await axios.post("http://192.168.2.64:5000/api/getGPTResponse", {
            text: problem,
            user: 'user',
            max_tokens: 100,
            model: module
        });
        console.log(response.data);
        return response.data;
    } catch(error){
        console.log(error);
        return "Error getting GPT-3 response";
    }
};


export const getCharHistory = async () => {
    try{
        const response = await axios.get("http://192.168.2.64:5000/api/getCharHistory");
        return response.data.history;
    } catch(error){
        console.log(error);
        return "Error getting character history";
    }
};