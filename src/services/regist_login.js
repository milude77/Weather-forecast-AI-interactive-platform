import api from "@/services/interfaceApi";





export const registerUser = async (username,email, password) => {
    try {
      const response = await api.post(`/register`, {
        username: username,
        email: email,
        password: password,
      });
      if (response.status === 200){return response.data.message;}
      
    } catch (error) {
      if (error.response.status === 400){return "注册失败，用户名或邮箱已存在";}
    }
  };    


export const loginUser = async (email, password) => {
    try {
      const response = await api.post(`/login`, {
        email: email,
        password: password,
      });
      if (response.status === 200){return response.data;} 
      if (response.status === 401){return "登录失败，用户名或密码错误";}
    } catch (error) {
      console.error("请求失败:", error);
    }
  };