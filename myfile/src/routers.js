import Home from "./components/Home.vue";
import SignUp from "./components/SignUp.vue";
import { createRouter, createWebHistory } from "core-js/core/object";

const routes = [
    {
        name: "Home",
        path: "/",
    },
    {
        name: "SignUp",
        component: SignUp,
        path: "/sign-up",

    },
];
const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
