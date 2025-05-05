import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/api',
});

// 创建拦截器，在请求头中添加token
api.interceptors.request.use((config) => {
    const token = sessionStorage.getItem('jwt_key');
    if(token){
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

api.interceptors.response.use((response) => {
    return response;
    }, 
    (error) => {
    if(error.response.status === 401){
        // jwt过期或未授权
        sessionStorage.removeItem('jwt_key');
        window.location.href = '/Register';
    }
    return Promise.reject(error);
});



export default api;