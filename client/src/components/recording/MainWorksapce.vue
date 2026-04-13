<script setup>
import { Instructor } from '.';
import { 
    MoveUp, 
    MoveLeft, 
    MoveRight,
    MoveDown,
    Move,
    CircleDot
} from 'lucide-vue-next';
import { computed } from 'vue';

const props = defineProps(["activity"]);

const commandList = [
    [
        {
            command: "", 
            icon: CircleDot,
            isActive: computed(() => props.activity?.[0][0])   
        }, 
            {
            command: "Clench both fists", 
            icon: MoveUp,
            isActive: computed(() => props.activity?.[0][1])
        }, 
        {
            command: "", 
            icon: CircleDot,
            isActive: computed(() => props.activity?.[0][2])
        }, 
    ],
    [
        {
            command: "Clench Left Fist", 
            icon: MoveLeft,
            isActive: computed(() => props.activity?.[1][0])
        }, 
        {
            command: "Relax", 
            icon: Move,
            isActive: computed(() => props.activity?.[1][1])
        }, 
        {
            command: "Clench Right Fist", 
            icon: MoveRight,
            isActive: computed(() => props.activity?.[1][2])  
        }, 
    ],
    [
        {
            command: "", 
            icon: CircleDot,
            isActive: computed(() => props.activity?.[2][0])
        }, 
        {
            command: "Clench both feet", 
            icon: MoveDown,
            isActive: computed(() => props.activity?.[2][1])
        }, 
        {
            command: "", 
            icon: CircleDot,
            isActive: computed(() => props.activity?.[2][2])
        }, 
    ],

]
</script>

<template>
    <div class="flex flex-col w-full h-full divide-y-2">
        <div class="h-[33.33%] w-full flex divide-x-2 border-dashed" v-for="commands in commandList">
            <Instructor v-for="commandObject in commands" :command="commandObject.command" :icon="commandObject.icon" :is-active="commandObject.isActive.value"/>
        </div>
    </div>
</template>