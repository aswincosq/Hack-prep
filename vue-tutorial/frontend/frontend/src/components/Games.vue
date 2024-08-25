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

        <!--Alert Message-->
        <b-alert variant="success" v-if="showMessage" show>{{ message }}</b-alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.game-modal> 
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
                <tr v-for="game in games" :key="game.id">
                    <td>{{ game.title }}</td>
                    <td>{{ game.genre }}</td>
                    <td>
                        <span v-if="game.played"> YES </span>
                        <span v-else> NO </span>
                    </td>
                    <td>
                        <div class="btn-group" role="group">
                            <button type="button" class="btn btn-info btn-sm" v-b-modal.game-update-modal
                                    @click="editGame(game)">Update</button>
                            <button type="button" class="btn btn-danger btn-sm">Delete</button>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
        <footer class="text-center bg-primary text-white" style="border-radius: 5px;">Copyright &copy; All Rights Reserved</footer>
        </div>
        </div>

        <!--first modal for adding-->

        <b-modal ref="addGameModal"
                 id="game-modal"
                 title="Add a new game" hide-backdrop hide-footer>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
            <b-form-group id="form-title-group" 
                          label="Title:"
                          label-for="form-title-input">
                <b-form-input id="form-title-input"
                              type="text"
                              v-model="addGameForm.title"
                              required
                              placeholder="Enter Game">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-genre-group" 
                          label="Genre:"
                          label-for="form-genre-input">
                <b-form-input id="form-genre-input"
                              type="text"
                              v-model="addGameForm.genre"
                              required
                              placeholder="Enter Genre">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-played-group">
                <b-form-checkbox-group v-model="addGameForm.played" id="form-checks">
                    <b-form-checkbox value="true"> Played </b-form-checkbox>
                </b-form-checkbox-group>
            </b-form-group>

            <b-button type="submit" variant="outline-info"> Submit</b-button>
            <b-button type="reset" variant="outline-danger"> Reset</b-button>
        
        </b-form>
        </b-modal>

        <!--second modal for updatng-->

        <b-modal ref="updateGameModal"
                 id="game-update-modal"
                 title="Update game" hide-backdrop hide-footer>
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
            <b-form-group id="form-title-edit-group" 
                          label="Title:"
                          label-for="form-title-edit-input">
                <b-form-input id="form-title-edit-input"
                              type="text"
                              v-model.trim="editForm.title"
                              required
                              placeholder="Enter Game">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-genre-edit-group" 
                          label="Genre:"
                          label-for="form-genre-edit-input">
                <b-form-input id="form-genre-edit-input"
                              type="text"
                              v-model="editForm.genre"
                              required
                              placeholder="Enter Genre">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-played-edit-group">
                <b-form-checkbox-group v-model="editForm.played" id="form-checks">
                    <b-form-checkbox value="true"> Played </b-form-checkbox>
                </b-form-checkbox-group>
            </b-form-group>

            <b-button type="submit" variant="outline-info"> Update </b-button>
            <b-button type="reset" variant="outline-danger"> Cancel</b-button>
        
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
            addGameForm: {
                title: "",
                genre: "",
                played: [],
            },
            editForm: {
                id: null,
                title: "",
                genre: "",
                played: [],
            },
            message: "",
            showMessage: false,
        };
    },
    message : "",
    methods:{
        
        getGames(){
            const path = 'http://127.0.0.1:5000/games'
            axios.get(path)
            .then((res)=>{
                this.$set(this, 'games', res.data.games);
            })
            .catch((err)=>{
                console.error(err);
            });
        },

        addGames(payload){
            const path = `http://127.0.0.1:5000/games`
            axios.post(path,payload)
            .then(()=>{
                this.getGames();
                this.message = " Game Added !";
                this.showMessage = true;
                setTimeout(() => {
                this.showMessage = false;
            }, 3000);
            })
            .catch((err)=>{
                console.error(err);
            });
        },
        initForm(){
            this.addGameForm.title = "";
            this.addGameForm.genre = "";
            this.addGameForm.played = [];
        },
        onSubmit(e) {
            e.preventDefault();
            this.$refs.addGameModal.hide();
            let played = false;
            if(this.addGameForm.played[0]) played = true;
            const payload = {
                title : this.addGameForm.title,
                genre : this.addGameForm.genre,
                played,
            }
            this.addGames(payload);
            this.initForm();
        },
        onReset(e) {
            e.preventDefault();
            this.$refs.addGameModal.hide();
            this.initForm();
        },
        updateGame(payload, gameID) {
            console.log('Updating game:', gameID, payload);
            const path = `http://127.0.0.1:5000/games/${gameID}`;
            axios.put(path, payload)
                .then((response) => {
                    console.log('Update response:', response);
                    // Fetch all games again to ensure state is consistent
                    this.getGames();
                    this.message = "Game Updated!";
                    this.showMessage = true;
                    setTimeout(() => {
                        this.showMessage = false;
                    }, 3000);
                    this.resetEditForm();
                })
                .catch((err) => {
                    console.error('Update error:', err);
                });
        },
        editGame(game) {
            this.editForm = {
                id: game.id,
                title: game.title,
                genre: game.genre,
                played: game.played ? [true] : []
            };
            console.log('Editing game:', this.editForm);
        },
        onSubmitUpdate(e) {
            e.preventDefault();
            this.$refs.updateGameModal.hide();
            let played = false;
            if(this.editForm.played[0]) played = true;
            const payload = {
                title: this.editForm.title,
                genre: this.editForm.genre,
                played,
            };
            console.log('Submitting update:', this.editForm.id, payload);
            this.updateGame(payload, this.editForm.id);
        },
        resetEditForm() {
            this.editForm = {
                id: null,
                title: '',
                genre: '',
                played: []
            };
        },
        onResetUpdate(e) {
            e.preventDefault();
            this.$refs.updateGameModal.hide();
            this.resetEditForm();
        },


    },
    created(){
        this.getGames();
    }
}
</script>
