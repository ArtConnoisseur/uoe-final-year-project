<script setup>
import { MainWorkspace } from '@/components/recording';
import { usePinConfig } from '@/stores/pin-config';
import { RouterLink } from 'vue-router';

const { pins, flag } = usePinConfig(); 
</script>

<template>
    <main class="h-[calc(100vh-100px)] flex">
        <MainWorkspace/>
        <section class="w-[30%] border-l-2 h-full p-10">
            <h1 class="text-2xl"><strong>Control Panel</strong> </h1>
            <div class="flex flex-col grow-0 gap-2">
                <div v-if="flag">
                    Flag is Set
                </div>
                <div v-else>
                    You cannot access the controls for the recording as you have not confirmed pin annotations. Please go to <RouterLink to="/visualiser" class="hover:bg-accent p-2 rounded-xl"><u>Visualiser</u></RouterLink> to check the connection is established and confirm pin annotations.
                </div>
            </div>
        </section>
    </main>
</template>
