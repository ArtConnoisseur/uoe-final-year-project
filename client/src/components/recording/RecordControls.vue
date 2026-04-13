<script setup>
import { ButtonGroup } from '../ui/button-group';
import { Button } from '../ui/button';
import { Input } from "../ui/input";
import { Separator } from '../ui/separator';
import { ref } from "vue"; 
import { 
    getLeftRightTrialsByDuration, 
    getUpDownTrialsByDuration 
} from '@/stores/pin-config';
import { Pause, Play } from "lucide-vue-next";

const activitySquareConfigs = {
    left: Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number(i === 1 && j === 0))), 
    right: Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number(i === 1 && j === 2))), 
    up: Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number(i === 0 && j === 1))), 
    down: Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number(i === 2 && j === 1))),
    none: Array.from({length: 3}, (_, i) => Array.from({ length: 3 }, (_, j) => Number((i + j) % 2 === 0))), 
};

const activitySquare = defineModel("activitySquare"); 
const handleActivitySquareClick = (direction) => {
    activitySquare.value = activitySquareConfigs[direction]; 
}

const duration = ref(2);
const trialRunInProcess = ref(false); 
const paused = ref(false);
const currentCommandIndex = ref(0)
const commands = ref([])
const total = ref(0)

const timeoutId = ref(null)

const recordingDriverFunction = () => {
    if (currentCommandIndex.value >= commands.value.length) {
        trialRunInProcess.value = false
        currentCommandIndex.value = 0
        activitySquare.value = activitySquareConfigs['none']
        return
    }
    if (paused.value) {
        timeoutId.value = setTimeout(recordingDriverFunction, 200) // poll until unpaused
        return
    }
    const currentCommand = commands.value[currentCommandIndex.value]
    activitySquare.value = activitySquareConfigs[currentCommand.command]
    currentCommandIndex.value++
    timeoutId.value = setTimeout(recordingDriverFunction, Number(currentCommand.duration) * 1000)
}

const handleClickStartStopRecording = (trialType) => {
    if (trialRunInProcess.value) {
        // Stop
        clearTimeout(timeoutId.value)
        trialRunInProcess.value = false
        currentCommandIndex.value = 0
        activitySquare.value = activitySquareConfigs['none']
        return
    }
    // Start
    if (trialType.toUpperCase() === "LEFTRIGHT") {
        commands.value = getLeftRightTrialsByDuration(duration.value)
        total.value = commands.value.length
    }
    trialRunInProcess.value = true
    currentCommandIndex.value = 0
    recordingDriverFunction()
}

console.log(activitySquare.value)
</script>

<template> 
    <div class="flex flex-col gap-6 mt-4">
        <span class="text-sm">
            Test that the instruction panel is working as expected:
        </span>
        <ButtonGroup>
            <Button :disabled="trialRunInProcess"  v-for="direction in Object.keys(activitySquareConfigs)" @click="() => handleActivitySquareClick(direction)" variant="outline">
                {{ direction[0].toUpperCase() + direction.slice(1) }}
            </Button>
        </ButtonGroup>

        <Separator/>
        <span class="text-sm">
            Enter duration in minute and start trial
        </span>
        <Input placeholder="Enter duration of trial in minutes. Ex. 0" v-model="duration"/>

        <ButtonGroup>
            <Button :variant="!trialRunInProcess ? 'outline' : 'destructive'" @click="() => handleClickStartStopRecording('LEFTRIGHT')"> 
                <span v-if="!trialRunInProcess">
                    Start
                </span>
                <span v-else="trialRunInProcess">
                    Stop
                </span>
            </Button>
            <Button :disabled="!trialRunInProcess" variant="outline" @click="() => paused = !paused"> 
                <Play v-if="paused"/>
                <Pause v-else/>
            </Button>
        </ButtonGroup>

        <Separator/>

        <span>
            <span class="blinking-animation rounded bg-red-700 h-2 w-2"></span>
        </span> 
    </div>
</template>

<style>

</style>