<template>
  <div v-if="weatherData && cities[Province]" class="weatherForecast">
    <h1>天气预报</h1>
    <!-- 省市县选择框 -->
    <div id="selectCity">
    <select v-model="Province" @change="updateCities">
      <option v-for="(province, index) in Object.keys(this.cities)" :key="index" :value="province">{{ province }}</option>
    </select>
    <select v-model="City" @change="updateDistricts">
      <option v-for="(city, index) in Object.keys(this.cities[this.Province] || {})" :key="index" :value="city">{{ city }}</option>
    </select>
    <select v-model="District">
      <option  v-for="(district, index) in this.cities[Province]?.[City] || []" :key="index" :value="district">{{ district }}</option>
    </select>
    </div>
    <!-- 天气模块 -->
    <div class="weathermodule" v-if="cities && weatherData">
      <div class="weatherTable">   
        <table v-if="weatherData && City==''">
          <thead>
            <tr>
              <th>地区</th>
              <th>天气</th>
              <th>温度</th>
              <th>风力</th>
            </tr>
          </thead>
          <tbody v-if="Province">
            <tr v-for="(city, index) in Object.keys(this.cities[this.Province])" :key="index" :value="city">
              <td>{{ city }}</td>
              <td>{{ weatherData[city]?.[0]?.wea }}</td>
              <td>{{ weatherData[city]?.[0]?.tem }}</td>
              <td>{{ weatherData[city]?.[0]?.wind }}</td>
            </tr>
          </tbody>
        </table>
        <table v-if="weatherData && City!='' && District==''">
          <thead>
            <tr>
              <th>地区</th>
              <th>天气</th>
              <th>温度</th>
              <th>风力</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(city, index) in cities[Province][City]" :key="index">
              <td>{{ city }}</td>
              <td>{{ weatherData[city]?.[0]?.wea }}</td>
              <td>{{ weatherData[city]?.[0]?.tem }}</td>
              <td>{{ weatherData[city]?.[0]?.wind }}</td>
            </tr>
          </tbody>
        </table>
        <table v-if="weatherData && City!='' && District!=''">
          <thead>
            <tr>
              <th>日期</th>
              <th>天气</th>
              <th>温度</th>
              <th>风力</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(weather, index) in weatherData[District]" :key="index">
              <td>{{ weather?.day }}</td>
              <td>{{ weather?.wea }}</td>
              <td>{{ weather?.tem }}</td>
              <td>{{ weather?.wind }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="weatherChart">
        <WeatherChart v-if="weatherData && cities && Province!='' && City==''" :WeatherData="weatherData" :cities="cities" :Province="Province"  />
        <weatherChart v-if="weatherData && City!='' && District==''" :WeatherData="weatherData" :cities="cities" :Province="Province" :City="City" />
        <WeatherChart v-if="weatherData && District!=''" :WeatherData="weatherData" :cities="cities" :Province="Province" :City="City" :District="District"  />
      </div>
    </div>
  </div>
  
</template>

<script>
// 引入外部 CSS 和 JS 文件
import '@/assets/weather.css';
import { fetchCityData,fetchWeatherAllCityData} from '@/services/weatherService.js';
import WeatherChart  from './weatherChart.vue';

export default {
  name: "WeatherForecast", 
  data() {
    return {
      weatherData: {}, 
      cities: {}, 
      Province: "辽宁",
      City: '', 
      District: '', 
    };
  },
  methods: {
    async fetchWeather() {
      try {
        this.weatherData = await fetchWeatherAllCityData();
        this.cities = await fetchCityData();
      } catch (error) {
        console.error("获取天气数据失败", error);
      }
    },
    updateCities() {
      this.City = '';
      this.District = '';
    },
    updateDistricts() {
        this.District = '';
      }
  },
  created() {
      this.fetchWeather(); 
  },
  components: {
    WeatherChart,
  }
};


</script>

<style scoped>
/* 这里的样式会优先覆盖外部 CSS 文件中的相同样式 */
</style>
