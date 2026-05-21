<script setup>
import { Cursor } from "@/components/cursor";
import { ref, onMounted, onUnmounted } from "vue";

const activitySquare = defineModel("activitySquare");
const activitySquareConfigs = {
    left:   Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number(i === 1 && j === 0))), 
    right:  Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number(i === 1 && j === 2))), 
    up:     Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number(i === 0 && j === 1))), 
    down:   Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number(i === 2 && j === 1))),
    none:   Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number((i + j) % 2 === 0))), 
};

const cursorContainer = ref(null); 

const positon = ref({
    x: 400, 
    y: 30,
    rotation: 0
}); 

const boundaryCondition = () => positon.value.y > 0 && positon.value.x > 0 && positon.value.y < cursorContainer.value.offsetHeight && positon.value.x < cursorContainer.value.offsetWidth; 

const moveUp = () => {
    activitySquare.value = activitySquareConfigs.up;
    const dx = 3 * Math.cos((positon.value.rotation + 90) * Math.PI / 180);
    const dy = 3 * Math.sin((positon.value.rotation + 90) * Math.PI / 180);
    if (boundaryCondition()) {
        positon.value.y -= dy;
        positon.value.x -= dx;
    } else {
        if (positon.value.y <= 0) positon.value.y = 1;
        if (positon.value.x <= 0) positon.value.x = 1;
        if (positon.value.y >= cursorContainer.value.offsetHeight) positon.value.y = cursorContainer.value.offsetHeight - 1;
        if (positon.value.x >= cursorContainer.value.offsetWidth) positon.value.x = cursorContainer.value.offsetWidth - 1;
    }
}

const moveDown = () => {
    activitySquare.value = activitySquareConfigs.down;
    const dx = 3 * Math.cos((positon.value.rotation + 90) * Math.PI / 180);
    const dy = 3 * Math.sin((positon.value.rotation + 90) * Math.PI / 180);
    if (boundaryCondition()) {
        positon.value.y += dy;
        positon.value.x += dx;
    } else {
        if (positon.value.y <= 0) positon.value.y = 1;
        if (positon.value.x <= 0) positon.value.x = 1;
        if (positon.value.y >= cursorContainer.value.offsetHeight) positon.value.y = cursorContainer.value.offsetHeight - 1;
        if (positon.value.x >= cursorContainer.value.offsetWidth) positon.value.x = cursorContainer.value.offsetWidth - 1;
    }
}

const moveLeft = () => {
    activitySquare.value = activitySquareConfigs.left;
    positon.value.rotation -= 5;
}

const moveRight = () => {
    activitySquare.value = activitySquareConfigs.right;
    positon.value.rotation += 5;
}

const handleMovement = (event) => {
    switch(event.code) {
        case "ArrowUp": case "KeyW": moveUp(); break
        case "ArrowDown": case "KeyS": moveDown(); break
        case "ArrowLeft": case "KeyA": moveLeft(); break
        case "ArrowRight": case "KeyD": moveRight(); break
    }
};

const handleKeyUp = () => activitySquare.value = activitySquareConfigs.none;

const handleKeydown = (event) => {
    requestAnimationFrame(() => handleMovement(event))
}

onMounted(() => {
    window.addEventListener("keydown", handleKeydown);
    window.addEventListener("keyup", handleKeyUp)
})

onUnmounted(() => {
    window.removeEventListener("keydown", handleKeydown);
    window.removeEventListener("keyup", handleKeyUp);
})
</script>

<template>
    <section class="w-[70%] p-[2%] h-full">
        <div class="border-2 h-full rounded-xl dotted relative" ref="cursorContainer">
            <Cursor :position="positon"/>
        </div>
    </section>
</template>

<style scoped>
.dotted {
    background-color: transparent;
    background-image: radial-gradient(circle, #aaaaaa34 1px, transparent 1px);
    background-size: 24px 24px;
    overflow: hidden;
}
</style>