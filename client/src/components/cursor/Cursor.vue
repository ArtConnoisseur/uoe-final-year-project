<script setup>
import { CircleArrowUp } from 'lucide-vue-next';
import { ref, watchEffect } from "vue"; 

const props = defineProps(["position"]);
const cursorRef = ref(null); 

watchEffect(() => {
    if (!cursorRef.value) return;
    const cursorElement = cursorRef.value 
    cursorElement.style.setProperty("--x", `${props.position.x}px`)
    cursorElement.style.setProperty("--y", `${props.position.y}px`)
    cursorElement.style.setProperty("--rotation-angle", `${props.position.rotation}deg`)
})
</script>

<template>
    <div class="cursor" ref="cursorRef">
        <CircleArrowUp class="h-20 w-20"/>
    </div>
</template>

<style scoped>
.cursor {
    --x: 20px;
    --y: 20px;
    --rotation-angle: 20deg;

    position: absolute;
    left: var(--x); 
    top: var(--y);
    transform: rotate(var(--rotation-angle));
}
</style>