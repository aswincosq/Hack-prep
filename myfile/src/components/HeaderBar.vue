<template>
    <div class="nav">
        <a href="#">MyHome</a>
        <a href="#">Add Restaurant</a>
        <a href="#">Update Restaurant</a>
        <a v-on:click="logout" href="#">Logout</a>
    </div>
</template>
<script>
export default{
    name:'HeaderBar',
    methods:{
    logout()
    {
        localStorage.clear();
        this.$router.push({name:'Login'})
    }
}
}
</script>
<style>
.nav{
    background-color: aquamarine;
    overflow: hidden
}

.nav a{
    float: left;
    color:black;
    padding: 14px 16px;
    text-align: center;
    font-size: 17px;
    text-decoration: none;
    margin-right: 5px;
}
    .nav a:hover{
        background: #ddd;
        color: #333

    }


</style>
