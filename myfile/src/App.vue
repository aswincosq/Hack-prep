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
}
  body{
    padding:0;
    margin:0;

  }

.logo{
        width:100px
}
.register input,.login input{
    width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-right: auto;
    margin-left: auto;
    border: 1px solid skyblue;
}
.register button,.login button{
        width: 320px;
        height: 40px;
        border: 1px solid skyblue;
        background: skyblue;
        color: red;
        cursor: pointer;
}
</style>
