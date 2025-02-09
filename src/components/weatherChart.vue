<template>
  <div class="LineChart" v-if="District && WeatherData[District]" >
    <strong> {{ this.District }} 未来七天气温变化</strong>
    <Line :data="chartData" :options="chartOptions" />
  </div>
  <div class="BarChart" v-if="(City && !District) || (Province && !City)">
    <Bar :data="barData" :options="barOptions" />
    <div class="no-data">
      <strong>无数据请尝试</strong>
      <button @click="City ? updateBarData(City):updateBarData_Province(Province)">刷新</button>
    </div> 
  </div>
  
</template>

<script>
import { Line, Bar }  from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement,BarElement, CategoryScale, LinearScale, PointElement } from 'chart.js';


ChartJS.register(Title, Tooltip, Legend, LineElement, BarElement , CategoryScale, LinearScale, PointElement);


export default {
  name: 'WeatherChart',
  props: {
    WeatherData: {
      type: Object,
      required: true
    },
    cities: {
      type: Object,
      required: true
    },
    Province: {
      type: String,
      default:''
    },
    City: {
      type: String,
      required: false
    },
    District: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      chartData: null,
      chartOptions: {
        responsive: true,
        plugins: {
          title: {
            display: false,
            text: '未来七天气温变化'
          }
        }
      },
      barData: null,
      barOptions: {
        responsive: true,
        plugins: {
          title: {
            display: true,
          }
        },
        scales: {
          x: {
            stacked: false,
          },
          y: {
            beginAtZero: true,
            grid: {
              color:(context)=> {
                if (context.tick.value === 0) {
                  return "black";
                }
                  return "#e0e0e0"
              },
              linewith: (context)=> {
                if (context.tick.value === 0) {
                  return 2;
                }
                  return 1;
              }
            }
        }
      },
        animation: {
          duration: 2000, // 动画时间，单位毫秒
          easing: 'easeInOutQuad', // 缓动函数，让动画效果更加平滑
        }
      }
    }
  },
  watch: {
    Province:{
      handler(newVal){
        this.updateBarData_Province(newVal);
      },
      immediate: true
    },
    District: {
      handler(newVal) {
        this.updateChartData(newVal);
      },
      immediate: true
    },
    City: {
      handler(newVal) {
        this.updateBarData(newVal);
      },
      immediate: true
    },
  },
  methods: {
    updateChartData(District) {
      if (!District || this.WeatherData[District] == undefined) return;

      const cityWeather = this.WeatherData[District]; 
      const regex = /(-?\d+)\/(-?\d+)℃/; 
      const temperatures = cityWeather.map(day => day.day); 
      const maxTemperatures = cityWeather.map(day => day.tem.match(regex)[1]);
      const minTemperatures = cityWeather.map(day => day.tem.match(regex)[2]);

      this.chartData = {
        labels: temperatures, // 日期
        datasets: [
          {
            label: '最高气温',
            data: maxTemperatures,
            borderColor: 'red',
            backgroundColor: 'transparent',
            fill: false
          },
          {
            label: '最低气温',
            data: minTemperatures,
            borderColor: 'blue',
            backgroundColor: 'transparent',
            fill: false
          }
        ]
      };
    },
    updateBarData(City) {
      if (!City || this.cities[this.Province][City] == undefined) return;

      const cityNameList = this.cities[this.Province][City];
      const regex = /(-?\d+)\/(-?\d+)℃/;
      const temperatures = cityNameList.map(city => this.WeatherData[city]?.[0]?.tem);
      const maxTemperatures = temperatures.map(tem => tem.match(regex)[1]);
      const minTemperatures = temperatures.map(tem => tem.match(regex)[2]);

      this.barData = {
        labels: cityNameList, // 城市名
        datasets: [
          {
            label:'最高气温',
            data: maxTemperatures,
            backgroundColor: 'red',
            borderColor: 'transparent',
            borderwidth: 1
            
          } ,
          {
            label:'最低气温',
            data: minTemperatures,
            backgroundColor: 'blue',
            borderColor: 'transparent',
            borderwidth: 1
          }
        ]
      };
    },
    updateBarData_Province(Province) {
      if (!Province || this.cities[this.Province] == undefined || !this.WeatherData) return;
      const cityNameList = Object.keys(this.cities[Province]);
      const regex = /(-?\d+)\/(-?\d+)℃/;
      const temperatures = cityNameList.map(city => this.WeatherData?.[city]?.[0].tem);
      const maxTemperatures = temperatures.map(tem => tem?.match(regex)?.[1]);
      const minTemperatures = temperatures.map(tem => tem?.match(regex)?.[2]);
      this.barData = {
        labels: cityNameList, // 城市名
        datasets: [
          {
            label:'最高气温',
            data: maxTemperatures,
            backgroundColor: 'red',
            borderColor: 'transparent',
            borderwidth: 1
            
          } ,
          {
            label:'最低气温',
            data: minTemperatures,
            backgroundColor: 'blue',
            borderColor: 'transparent',
            borderwidth: 1
          }
        ]
      };
    }
  },
  created(){
    this.City ? this.updateBarData(this.City):this.updateBarData_Province(this.Province);
  },
  components: {
    Line,
    Bar,
  }
}
</script>

<style>
.LineChart {
  height: 100%;
  width: 100%;
}

.BarChart {
  height: 100%;
  width: 100%;
} 

.LineChart strong {
  margin-left:40%;
}

.no-data {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.5rem;
  color: #646464;
}

.no-data button {
  border-radius: 10px;
  padding: 2px 20px;
  background-color: #85d0e5;
}
</style>
