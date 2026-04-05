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

const commandList = [
    [
        {
            command: "", 
            icon: CircleDot,  
        }, 
            {
            command: "Clench both fists", 
            icon: MoveUp,  
        }, 
        {
            command: "", 
            icon: CircleDot,  
        }, 
    ],
    [
        {
            command: "Clench Left Fist", 
            icon: MoveLeft,  
        }, 
        {
            command: "Relax", 
            icon: Move,  
        }, 
        {
            command: "Clench Right Fist", 
            icon: MoveRight,  
        }, 
    ],
    [
        {
            command: "", 
            icon: CircleDot,  
        }, 
        {
            command: "Clench both feet", 
            icon: MoveDown,  
        }, 
        {
            command: "", 
            icon: CircleDot,  
        }, 
    ],

]
</script>

<template>
    <section class="flex flex-col w-[70%] h-full divide-y-2">
        <div class="h-[33.33%] w-full flex divide-x-2 border-dashed" v-for="commands in commandList">
            <Instructor v-for="commandObject in commands" :command="commandObject.command" :icon="commandObject.icon"/>
        </div>
    </section>
</template>