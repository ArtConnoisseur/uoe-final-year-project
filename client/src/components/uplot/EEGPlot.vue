<script setup>
import { onMounted, onBeforeUnmount, ref, watch } from "vue";
import { useTheme } from "@/composables/useTheme";
import { useColorMode } from "@vueuse/core";
import uPlot from "uplot";
import "uplot/dist/uPlot.min.css";

const props = defineProps(["ch", "pn", "timestamps", "samples"]);
const channelName = ref(props.ch);

const SAMPLE_RATE = 60; // Hz
const WINDOW_LENGTH = 5; // Seconds

// Calculate how many points there should at any given
// point in time
const DATA_POINTS = SAMPLE_RATE * WINDOW_LENGTH; // This is the effective window length

// Intialise the chart element to null
const chartElement = ref(null);
let uplot = null;
let time = null;
let animFrame = null;

function EEGValue(time) {
    time = time / SAMPLE_RATE;
    return (
        Math.sin(time * 5) +
        Math.sin(2 * time + Math.PI / 3) -
        Math.random() * 4 +
        Math.random()
    );
}

const data = [[], []];

watch(
    () => [props.timestamps, props.samples],
    ([newTimestamps, newSamples]) => {
        if (!uplot) {
            console.error("uplot is not initialised");
            return;
        }
        newTimestamps = Array.from(newTimestamps);
        newSamples = Array.from(newSamples);
        uplot.setData([newTimestamps, newSamples]);
    },
    { deep: true },
);

function buildChart() {
    const theme = useTheme();
    time = WINDOW_LENGTH;

    // Initialise options for the chart
    const opts = {
        width: chartElement.value.clientWidth,
        height: chartElement.value.clientHeight,
        padding: [10, 10, 0, 10],
        legend: { show: false },
        cursor: {
            show: true,
            stroke: theme.accent,
            width: 1,
        },
        select: {
            fill: theme.accent + "33", // 33 = 20% opacity in hex
        },
        axes: [
            {
                stroke: theme.mutedForeground,
                grid: { stroke: theme.border, width: 1 },
                ticks: { stroke: theme.border, width: 1 },
                font: `12px sans-serif`,
            },
            {
                stroke: theme.mutedForeground,
                grid: { stroke: theme.border, width: 1 },
                ticks: { stroke: theme.border, width: 1 },
                font: `12px sans-serif`,
            },
        ],
        scales: {
            x: { time: false },
            y: { auto: true },
        },
        series: [
            {},
            {
                label: props.ch,
                stroke: theme.foreground,
                width: 1.5,
            },
        ],
    };

    uplot = new uPlot(opts, data, chartElement.value);
}

onMounted(() => {
    buildChart(uplot);
});

onBeforeUnmount(() => {
    uplot?.destroy();
});
</script>

<template>
    <div class="py-8 flex flex-col gap-4 w-[80%]">
        <span>
            <span>Channel Name: {{ channelName }}</span>
            <span class="pl-3">Pin ID: {{ props.pn }}</span>
        </span>
        <div
            ref="chartElement"
            class="w-full h-[350px] border-[var(--border)] border-2 rounded-md"
        ></div>
    </div>
    <span class="w-full border-b-1"></span>
</template>
