<script setup>
import ModeToggle from "@/components/ui/mode-toggle";
import Navitem from "./NavbarItem.vue";
</script>

<template>
    <nav
        class="flex items-center flex-row h-22 px-[5%] box-border gap-10 border-[--border] border-b-[0.1px] w-full clip overflow-hidden sticky top-0 z-10 bg-[var(--background)]"
    >
        <span class="text-xl font-bold">
            <RouterLink to="/">PiEEG-16 Visualiser</RouterLink>
        </span>
        <ul class="mr-auto flex flex-row items-center gap-10">
            <Navitem to="/about">About</Navitem>
            <Navitem to="/record">Record EEGs</Navitem>
            <Navitem to="/visualiser">Visualiser</Navitem>
        </ul>
        <ModeToggle />
    </nav>
</template>
