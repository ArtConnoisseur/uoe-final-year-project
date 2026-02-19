<script setup>
import "@/App.css";
import { Navbar } from "@/components/navbar";
import { Button } from "@/components/ui/button";
import router from "@/router";
import { RouterView } from "vue-router";
</script>

<template>
    <div class="flex flex-col">
        <Navbar />
        <RouterView />
    </div>
</template>

<style scoped></style>
