<script setup>
import { Button } from "@/components/ui/button";
import ModeToggle from "@/components/ui/mode-toggle";
import Navitem from "./NavbarItem.vue";
import { ref } from "vue";

const sentinel = ref(null);
</script>

<template>
    <nav
        class="flex items-center flex-row py-6 px-[5%] box-border gap-10 border-[--border] border-b-[0.1px] w-full clip overflow-hidden sticky top-0"
    >
        <span class="text-xl font-bold">
            <RouterLink to="/">PiEEG-16 Visualiser</RouterLink>
        </span>
        <ul class="mr-auto flex flex-row items-center gap-10">
            <Navitem to="/about">About</Navitem>
            <Navitem to="/guide">User Guidance</Navitem>
            <Navitem to="/visualiser">Visualiser</Navitem>
        </ul>
        <ModeToggle />
    </nav>
</template>
