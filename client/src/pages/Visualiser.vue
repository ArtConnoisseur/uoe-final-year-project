<script setup>
import { EEGPlot } from "@/components/uplot";

const CHANNELS = 16;
</script>

<template>
    <main class="flex flex-1 px-[4%] gap-[4%] min-h-0 relative">
        <section class="flex flex-col w-[70%] divide-y-1 overflow-y-auto">
            <EEGPlot
                v-for="idx in Array.from(
                    { length: CHANNELS },
                    (_, idx) => idx + 1,
                )"
                :ch="idx"
                pn="P19"
            />
        </section>
        <section class="flex flex-col border-l-1 p-12 h-full sticky inset-0">
            <h3 class="text-2xl font-bold">Control Panel</h3>
        </section>
    </main>
</template>
