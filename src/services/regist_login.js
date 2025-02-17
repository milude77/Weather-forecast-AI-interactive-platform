import axios from 'axios';

export const registerUser = async (username,email, password) => {
    try {
      const response = await axios.post('http://192.168.2.64:5000/api/register', {
        username: username,
        email: email,
        password: password,
      });
      if (response.status === 200){return "注册成功";}
      if (response.status === 400){return "注册邮箱已存在";}
    } catch (error) {
      console.error("请求失败:", error);
      alert("发生错误，请稍后再试");
    }
  };    


export const loginUser = async (email, password) => {
    try {
      const response = await axios.post('http://192.168.2.64:5000/api/login', {
        email: email,
        password: password,
      });
      if (response.status === 200){return "登录成功";}
      if (response.status === 401){return "登录失败，用户名或密码错误";}
    } catch (error) {
      console.error("请求失败:", error);
      alert("发生错误，请稍后再试");
    }
  };