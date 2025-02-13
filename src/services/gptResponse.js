import axios from "axios";



export const getGptResponse = async (user, problem) => {
    try{
        const response = await axios.post("http://127.0.0.1:5000/api/getGPT3.5", {
            text: problem,
            user: user,
            max_tokens: 100,
        });
        return response.data.choices[0].text;
    } catch(error){
        console.log(error);
        return "Error getting GPT-3 response";
    }
};


export const getCharHistory = async () => {
    try{
        const response = await axios.get("http://127.0.0.1:5000/api/getCharHistory");
        return response.data.history;
    } catch(error){
        console.log(error);
        return "Error getting character history";
    }
};