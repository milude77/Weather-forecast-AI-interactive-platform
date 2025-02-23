import axios from 'axios';


const apiUrl = "http://192.168.31.98:5000/api";



export const registerUser = async (username,email, password) => {
    try {
      const response = await axios.post(`${apiUrl}/register`, {
        username: username,
        email: email,
        password: password,
      });
      if (response.status === 200){return response.data;}
      if (response.status === 400){return "注册邮箱已存在";}
    } catch (error) {
      console.error("请求失败:", error);
      alert("发生错误，请稍后再试");
    }
  };    


export const loginUser = async (email, password) => {
    try {
      const response = await axios.post(`${apiUrl}/login`, {
        email: email,
        password: password,
      });
      if (response.status === 200){return response.data;} 
      if (response.status === 401){return "登录失败，用户名或密码错误";}
    } catch (error) {
      console.error("请求失败:", error);
    }
  };