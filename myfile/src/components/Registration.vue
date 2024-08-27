<template>
<img class= "logo" src="../assets/fitness-gym.jpg" />
<h1>Sign Up</h1>
<div class="register">
    <input type="text" v-model="name" placeholder="Enter Full Name" />
    <input type="text" v-model="primary mobile Number" placeholder="Enter primary mobile number" />
    <input type="text" v-model="alternative mobile Number" placeholder="Enter alternative mobile number" />
    <button v-on:click="SignUp" >Sign Up</button>
    <p>
        <router-link to="/login" >LoginPage</router-link>
    </p>
    </div>
</template>
<script>
import axios from 'axios'
export default{
        name:'Registration',
        data()
        {
return{
        name:'',
        primary mobile Number:'',
        alternative mobile Number:''
}
        
        },
        methods:{
               async SignUp()
                {
                        let result = await axios.post("http://localhost:3000/users",{
                                name:this.name,
                                email:this.email,
                                password:this.password
                        });
                        console.warn(result);
                        if(result.status==201)
                        {
                                alert("Sign-Up done ")
                                localStorage.setItem("user-info",result,JSON.stringify(result.data))
                                this.$router.push({name:'MyHome'})
                        }
                }
        }

}
</script>
<style>

</style>