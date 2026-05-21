<script setup>
import { EEGPlot } from "@/components/uplot";
import { onMounted, reactive } from "vue";
import PinConfig from "@/components/pin-config/PinConfig.vue";

const CHANNELS = 16;
const SAMPLES = 50;

const channels = reactive({
    timestamps: [],
    samples: Array.from({ length: 16 }, (_, i) => []),
});

let startTime = document.timeline.currentTime; // represents the flow of time push

const updateValues = (timestep) => {
    console.log(timestep);  
    channels.timestamps.push(timestep - startTime);
    channels.samples.forEach((ele, idx) => {
        ele.push(Math.sin(idx * 180 * (timestep - startTime)/Math.PI))
    })

    if (channels.timestamps.length > SAMPLES) {
        channels.timestamps.shift();
        channels.samples.forEach((ch) => ch.shift());
    }

    requestAnimationFrame(updateValues);
}

onMounted(() => {
    // const socket = new WebSocket("ws://10.177.74.21:8000/eeg-ws");

    // socket.addEventListener("open", (event) => {
    //     socket.send("Hello Server");
    // });

    // socket.addEventListener("message", (event) => {
    //     const { timestamp, sample } = JSON.parse(event.data);
    //     channels.timestamps.push(timestamp);
    //     sample.forEach((val, i) => channels.samples[i].push(val));

    //     // Sliding window
    //     if (channels.timestamps.length > SAMPLES) {
    //         channels.timestamps.shift();
    //         channels.samples.forEach((ch) => ch.shift());
    //     }
    // });
    
    requestAnimationFrame(updateValues); 

    console.log("hello")
});
</script>

<template>
    <main class="flex flex-1 visualiser-container h-0 min-h-0">
        <section
            class="flex flex-col w-[70%] overflow-y-auto justify-center items-center"
        >
            <EEGPlot
                v-for="(sample, idx) in channels.samples"
                :ch="idx"
                :samples="sample"
                :timestamps="channels.timestamps"
            />
        </section>
        <section class="flex flex-col border-l w-[30%] overflow-y-auto">
            <div class="px-10 py-12 flex flex-col gap-10">
                <h3 class="text-2xl font-bold">Control Panel</h3>
                <PinConfig/>
            </div>
        </section>
    </main>
</template>
