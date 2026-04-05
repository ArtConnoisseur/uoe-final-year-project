// This file enables the store for the app state of pin configs
// it also provides the default pin mapping that can be loaded

// Definition of new pin mappings is handled by the server which is
// why you cannot see it here.

import { defineStore } from "pinia";

// Default pin labels. ToDo: Complete

let eegElectrode = ["O1", "O2", "T5", "T6", "P3", "P4", "T3", "T4"];

// Initilise config object
const config = Object.fromEntries(
    Array.from({ length: 17 }, (_, i) => [`E${i}`, eegElectrode[i]]),
);

export const usePinConfig = defineStore("pinConfig", {
    state: () => ({ pins: {...config}, flag: false }),
    persist: true,
    actions: {
        reset() {
            this.pins = { ...config };
            this.flag = false;
        }
    }
});

