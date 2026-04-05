<script setup>
import { Proportions, ProportionsIcon } from 'lucide-vue-next';

const props = defineProps([
    "command",
    "icon"
]);

const Icon = props.icon; 
</script>

<template>
    <div class="h-full w-[33.33%] border-dashed flex flex-col gap-2 items-center justify-center hover:bg-green-400">
        <Icon class="w-10 h-10"/>
        <spand>{{ props.command }}</spand>
    </div>
</template>