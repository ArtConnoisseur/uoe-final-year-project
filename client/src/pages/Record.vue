<script setup>
import { MainWorkspace } from '@/components/recording';
import { usePinConfig } from '@/stores/pin-config';
import { RouterLink } from 'vue-router';
import { RecordControls } from '@/components/recording';
import { ref } from 'vue';
const { flag } = usePinConfig(); 

const activeSquare = ref([
    [0, 1, 0],
    [0, 0, 0], 
    [0, 0, 0]
]);
</script>

<template>
    <main class="h-[calc(100vh-100px)] flex">
        <section class="h-full w-[70%]">
            <MainWorkspace :activity="activeSquare"/>
        </section>
        <section class="w-[30%] border-l-2 h-full p-10">
            <h1 class="text-2xl"><strong>Control Panel</strong> </h1>
            <div class="flex flex-col grow-0 gap-2">
                <div v-if="flag">
                    <RecordControls v-model:activitySquare="activeSquare"/>
                </div>
                <div v-else>
                    You cannot access the controls for the recording as you have not confirmed pin annotations. Please go to <RouterLink to="/visualiser" class="hover:bg-accent p-2 rounded-xl"><u>Visualiser</u></RouterLink> to check the connection is established and confirm pin annotations.
                </div>
            </div>
        </section>
    </main>
</template>
