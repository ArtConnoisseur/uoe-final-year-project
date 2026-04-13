<script setup>
import { usePinConfig } from "@/stores/pin-config";
import { CursorWorkspace } from "@/components/cursor";
import { MainWorkspace } from "@/components/recording";
import { Label } from "@/components/ui/label";
import { ref } from "vue";

const pinConfig = usePinConfig(); 

const activeSquare = ref([
    [0, 1, 0],
    [0, 0, 0], 
    [0, 0, 0]
]);
</script>

<template>
    <main class="h-[calc(100vh-100px)] flex w-full">
        <CursorWorkspace v-model:activity-square="activeSquare"/>
        <section class="w-[30%] border-l-2 flex flex-col gap-4 p-12">
            <Label>Classifier Output:</Label>
            <div class="w-full h-[40%] text-sm border">
                <MainWorkspace :activity="activeSquare"/>
            </div>
        </section>
    </main>
</template>
