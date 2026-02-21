import { createRouter, createWebHistory } from "vue-router";
import { Home, About, Visualiser, Record } from "@/pages";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: "/", component: Home },
        { path: "/about", component: About },
        { path: "/visualiser", component: Visualiser },
        { path: "/record", component: Record },
    ],
});

export default router;
