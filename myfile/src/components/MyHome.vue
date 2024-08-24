<template>
    
    <h1>Hello user, Welcome to the Home page</h1>
    <HeaderBar />
</template>
<script>
import HeaderBar from './HeaderBar.vue'
export default{

    name:'MyHome',
    components:{
        HeaderBar
    },
    mounted()
    {
        let user=localStorage.getItem('user-info');
        if (!user)
    {
        this.$router.push({name:'SignUp'})
    }
    }

}
</script>