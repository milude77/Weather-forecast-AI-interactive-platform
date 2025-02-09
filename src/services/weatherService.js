// weatherService.js
import axios from 'axios';


/**
 * 获取指定城市的天气数据
 * @param {String} city - 城市名
 * @returns {Promise} - 返回天气数据的 Promise
 */
export const fetchWeatherData = async (city) => {
  try {
    const response = await axios.get('http://192.168.2.57:5000/api/getDistrictweather', {
      params: { city: city }
    });
    return response.data;  // 返回天气数据
  } catch (error) {
    console.error("获取天气数据失败", error);
    throw new Error("获取天气数据失败");
  }
};

export const fetchWeatherAllCityData = async () => {
  try {
    const response = await axios.get('http://192.168.2.57:5000/api/getAllcityweather');
    return response.data;  // 返回天气数据
  } catch (error) {
    console.error("获取天气数据失败", error);
    throw new Error("获取天气数据失败");
  }
}

export const fetchCityData = async () => {
  try {
    const response = await axios.get('http://192.168.2.57:5000/api/city');
    return response.data;  // 返回城市数据
  } catch (error) {
    console.error("获取城市数据失败", error);
    throw new Error("获取城市数据失败");
  }
};


