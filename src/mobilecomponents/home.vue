<template>
  <van-nav-bar title="天气查询" />
  <van-search v-model="city" placeholder="请输入城市名称" />
  <van-cell-group>
    <van-cell title="当前城市" :value="weather.city" />
    <van-cell title="温度" :value="weather.temperature + '°C'" />
    <van-cell title="天气状况" :value="weather.condition" />
  </van-cell-group>
</template>

<script>
export default {
  name: 'HomeNavigation',
  data() {
    return {
      city: '',
      weather: {
        city: '北京',
        temperature: 25,
        condition: '晴',
      },
    };
  },
};
</script>

<style>
/* 移动端专属样式 */
</style>