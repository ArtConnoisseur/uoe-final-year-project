// This file enables the store for the app state of pin configs
// it also provides the default pin mapping that can be loaded

// Definition of new pin mappings is handled by the server which is
// why you cannot see it here.

// Why is this file commented and not the others? 
// This is literally just a bunch of definitions, that needs context.
// Code is relatively self explanatory given the variable names. 
// I'm speedrunning this leave me alone. 

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

// Trial configuration 

export function createTrailObject( command, duration ) { 
    return { command, duration }
}

const leftRightTrial = [
    createTrailObject("none", 4),
    createTrailObject("left", 4),
    createTrailObject("none", 4),
    createTrailObject("right",4),
];

const upDownTrial = [
    createTrailObject("none", 4),
    createTrailObject("up", 4),
    createTrailObject("none", 4),
    createTrailObject("down", 4),
];

export function getLeftRightTrialsByDuration(duration) {
    const numberOfTrails = Math.ceil(duration * 60 / 16)
    return Array.from({ length: numberOfTrails }, () => [...leftRightTrial]).flat()
}

export function getUpDownTrialsByDuration( duration ) {
    // Duration is in minutes 
    const numberOfTrails = Math.ceil(duration * 60 / 16)
    return Array.from({ length: numberOfTrails }, () => [...upDownTrial]).flat()
}
