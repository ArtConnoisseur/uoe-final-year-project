<script setup>
import { RouterLink } from "vue-router";
import { useRoute } from "vue-router";

const { to } = defineProps(["to"]);
const route = useRoute();
</script>

<template>
    <RouterLink :to="to">
        <li
            :class="`${route.path === to ? 'bg-[var(--foreground)] text-[var(--background)]' : ''}
            ${!(route.path === to) ? 'hover:bg-[var(--accent)]' : ''} border-[var(--background)] box-border border-b-1 transition-2 transition-all
            px-8 py-2 rounded-full box-box-border`"
        >
            <slot />
        </li>
    </RouterLink>
</template>
