<template>
<div class="jumbotron vertical-center">
    <div class="container">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lumen/bootstrap.min.css" 
        integrity="sha384-GzaBcW6yPIfhF+6VpKMjxbTx6tvR/yRd/yJub90CqoIn2Tz4rRXlSpTFYMKHCifX" crossorigin="anonymous">
        <div class="row">
        <div class="col-sm-12">
        <p>
            Games Library 🎮      
        </p>
        <hr><br>

        <!--Alert Message-->
        <button type="button" class="btn btn-success btn-sm"> 
            Add Game
        </button>
        <br><br>
        <table class="table table-hover">
            <!--Table Head-->
            <thead>
                <tr>
                    <!--Table header cells-->
                    <th scope="col">Title</th>
                    <th scope="col">Genre</th>
                    <th scope="col">Played</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="game,index in games":key="index">
                    <td>{{ game.title }}</td>
                    <td>{{game.genre}}</td>
                    <td>{{game.played}}</td>
                    <td>
                        <div class="btn-group" role="group">
                            <button type="button" class="btn btn-info btn-sm">Update</button>
                            <button type="button" class="btn btn-danger btn-sm">Delete</button>
                        </div>
                    </td>
                </tr>
            </tbody>

        </table>
        </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
    name: "GamesLibrary",
    data() {
      return {
        games:[] ,
      };
    },
    methods:{
        getGames(){
            const path = 'http://127.0.0.1:5000/games'
            axios.get(path)
            .then((res)=>{
                this.games = res.data.games;
            })
            .catch((err)=>{
                console.error(err);
            });
        },
    },
    created(){
        this.getGames();
    }
}
</script>
