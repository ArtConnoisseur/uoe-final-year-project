<script setup>
const props = defineProps([
    "command",
    "icon",
    "isActive"
]);

const Icon = props.icon; 
</script>

<template>
    <div :class="`h-full w-[33.33%] border-dashed flex flex-col gap-2 items-center justify-center ${isActive == 1 && 'border-green-400 border-2  bg-green-400/20'}`">
        <Icon class="w-[20%] h-[20%]"/>
        <span>{{ props.command }}</span>
    </div>
</template>