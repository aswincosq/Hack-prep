<template>
  <router-view />
</template>
<script>
/* eslint-disable vue/multi-word-component-names, vue/no-unused-components */
import SignUp from './components/SignUp.vue'


export default {
  name: 'App',
  components: {
    SignUp
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
