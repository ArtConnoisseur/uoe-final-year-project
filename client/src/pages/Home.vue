<script setup>
import { Button } from "@/components/ui/button";
</script>

<template>
    <main class="h-full w-full py-20 px-[20%]">
        <div class="flex flex-col gap-12">
            <span class="text-3xl"><strong>Welcome to the PiEEG visualiser</strong></span>
            <div>
                This app is built for a BCI navigation final year project. It aims to serve these purposes:
                <ul>
                    <li>Visualise EEGs</li>
                    <li>Record automatic EEGs</li>
                    <li>Show an example of the proposed BCI</li>
                </ul> 
            </div>
            <div>
                Navigate using the navbar to use the appropriate functions.
            </div>
        </div>
    </main>
</template>
