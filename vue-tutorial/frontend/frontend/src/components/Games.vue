<template>
<div class="jumbotron vertical-center">
    <div class="container">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lumen/bootstrap.min.css" 
        integrity="sha384-GzaBcW6yPIfhF+6VpKMjxbTx6tvR/yRd/yJub90CqoIn2Tz4rRXlSpTFYMKHCifX" crossorigin="anonymous">
        <div class="row">
        <div class="col-sm-12">
        <h1 class="text-center bg-primary text-white" style="border-radius: 10px;">
            Games Library 🎮      
        </h1>
        <hr><br>

        <!-- Alert Message -->
        <b-alert variant="success" v-if="showMessage" show>{{ message }}</b-alert>
        <button type="button" class="btn btn-success btn-sm" @click="showAddGameModal = true"> 
            Add Game
        </button>
        <br><br>
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Genre</th>
                    <th scope="col">Played</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="game in games" :key="game.id">
                    <td>{{ game.title }}</td>
                    <td>{{ game.genre }}</td>
                    <td>
                        <span v-if="game.played"> YES </span>
                        <span v-else> NO </span>
                    </td>
                    <td>
                        <div class="btn-group" role="group">
                            <button type="button" class="btn btn-info btn-sm" @click="editGame(game)">Update</button>
                            <button type="button" class="btn btn-danger btn-sm" @click="deleteGame(game.id)">Delete</button>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
        <footer class="text-center bg-primary text-white" style="border-radius: 5px;">Copyright &copy; All Rights Reserved</footer>
        </div>
        </div>

        <!-- Add Game Modal -->
        <b-modal v-model="showAddGameModal"
                    title="Add a new game" hide-footer>
        <b-form @submit="onSubmit" @reset="onReset">
            <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
                <b-form-input id="form-title-input" type="text" v-model="addGameForm.title" required placeholder="Enter Game"></b-form-input>
                <b-form-invalid-feedback v-if="!addGameForm.title">Please enter a title.</b-form-invalid-feedback>
            </b-form-group>
            <b-form-group id="form-genre-group" label="Genre:" label-for="form-genre-input">
                <b-form-input id="form-genre-input" type="text" v-model="addGameForm.genre" required placeholder="Enter Genre"></b-form-input>
                <b-form-invalid-feedback v-if="!addGameForm.genre">Please enter a genre.</b-form-invalid-feedback>
            </b-form-group>
            <b-form-group id="form-played-group">
                <b-form-checkbox v-model="addGameForm.played"> Played </b-form-checkbox>
            </b-form-group>
            <b-button type="submit" variant="outline-info">Submit</b-button>
            <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
        </b-modal>

        <!-- Update Game Modal -->
        <b-modal v-model="showUpdateGameModal" title="Update game" hide-footer>
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate">
            <b-form-group id="form-title-edit-group" label="Title:" label-for="form-title-edit-input">
                <b-form-input id="form-title-edit-input" type="text" v-model="editForm.title" required placeholder="Enter Game"></b-form-input>
            </b-form-group>
            <b-form-group id="form-genre-edit-group" label="Genre:" label-for="form-genre-edit-input">
                <b-form-input id="form-genre-edit-input" type="text" v-model="editForm.genre" required placeholder="Enter Genre"></b-form-input>
            </b-form-group>
            <b-form-group id="form-played-edit-group">
                <b-form-checkbox v-model="editForm.played"> Played </b-form-checkbox>
            </b-form-group>
            <b-button type="submit" variant="outline-info">Update</b-button>
            <b-button type="reset" variant="outline-danger">Cancel</b-button>
        </b-form>
        </b-modal>

    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
    name: "GamesLibrary",
    data() {
        return {
            games: [],
            addGameForm: { title: "", genre: "", played: false },
            editForm: { id: null, title: "", genre: "", played: false },
            message: "",
            showMessage: false,
            showAddGameModal: false,
            showUpdateGameModal: false,
        };
    },
    methods:{
        getGames(){
            axios.get('http://127.0.0.1:5000/games')
            .then((res)=>{
                this.games = res.data.games;
            })
            .catch((err)=>{
                console.error(err);
            });
        },
        addGames(payload){
            axios.post('http://127.0.0.1:5000/games', payload)
            .then(()=>{
                this.getGames();
                this.showSuccessMessage("Game Added!");
            })
            .catch((err)=>{
                console.error(err);
            });
        },
        updateGame(payload, gameID) {
            axios.put(`http://127.0.0.1:5000/games/${gameID}`, payload)
                .then(() => {
                    this.getGames();
                    this.showSuccessMessage("Game Updated!");
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        deleteGame(gameId) {
            axios.delete(`http://127.0.0.1:5000/games/${gameId}`)
                .then(() => {
                    this.getGames();
                    this.showSuccessMessage("Game Deleted!");
                })
                .catch((error) => {
                    console.error('Error deleting game:', error);
                });
        },
        onSubmit(e) {
            e.preventDefault();
            this.showAddGameModal = false;
            const payload = {
                title: this.addGameForm.title,
                genre: this.addGameForm.genre,
                played: this.addGameForm.played
            };
            this.addGames(payload);
            this.resetForm();
        },
        onReset(e) {
            e.preventDefault();
            this.showAddGameModal = false;
            this.resetForm();
        },
        onSubmitUpdate(e) {
            e.preventDefault();
            this.showUpdateGameModal = false;
            const payload = {
                title: this.editForm.title,
                genre: this.editForm.genre,
                played: this.editForm.played
            };
            this.updateGame(payload, this.editForm.id);
            this.resetEditForm();
        },
        onResetUpdate(e) {
            e.preventDefault();
            this.showUpdateGameModal = false;
            this.resetEditForm();
        },
        editGame(game) {
            this.editForm = { id: game.id, title: game.title, genre: game.genre, played: game.played };
            this.showUpdateGameModal = true;
        },
        showSuccessMessage(message) {
            this.message = message;
            this.showMessage = true;
            setTimeout(() => {
                this.showMessage = false;
            }, 3000);
        },
        resetForm() {
            this.addGameForm = { title: "", genre: "", played: false };
        },
        resetEditForm() {
            this.editForm = { id: null, title: "", genre: "", played: false };
        },
    },
    created(){
        this.getGames();
    }
}
</script>
