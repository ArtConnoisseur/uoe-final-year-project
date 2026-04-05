<script setup>
import {
    FieldGroup,
    FieldDescription,
} from "@/components/ui/field";
import { PinField } from ".";
import { usePinConfig } from "@/stores/pin-config";
import { Button } from "@/components/ui/button";
import { ButtonGroup } from "@/components/ui/button-group";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { Separator } from "@/components/ui/separator";

const pinConfig = usePinConfig();

const handleConfirmClick = (event) => { 
    pinConfig.flag = true
}

const handleRestoreClick = (event) => {
    localStorage.removeItem("pinConfig")
    pinConfig.reset()
    window.location.reload()
}
</script>

<template>
    <FieldGroup>
        <FieldDescription>
            Here you are setting names for the channels to which you have
            connected the pins. This automates naming in the creating of
            <code>.fif</code> files in this project.

            <Separator class="mt-4"/>
            
            <ul class="flex flex-col gap-1  mt-3">
                <li>Change each pin value to what you like and update them individually.</li>
                <li>When you are done, please press confirm before going to record.</li>
                <li>Your changes are saved to the browser when you make an update, maintaining session state. </li>
                <li>If you want to restore default, please press the button below. </li>
            </ul>
        </FieldDescription>
        <Separator/>    
        <ButtonGroup class="self-center">
            <Button 
                variant="outline" 
                :disabled="pinConfig.flag"
                @click="handleConfirmClick"
            >
                Confirm 
            </Button>
            <AlertDialog>
                <AlertDialogTrigger as-child>
                    <Button variant="outline">
                        Restore Default
                    </Button>
                </AlertDialogTrigger>
                <AlertDialogContent>
                    <AlertDialogHeader>
                        <AlertDialogDescription>
                            Are you sure you want to restore default values? The values you have saved will be lost. 
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                        <AlertDialogCancel>
                            Cancel
                        </AlertDialogCancel>
                        <AlertDialogAction @click="handleRestoreClick">
                            Continue
                        </AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>
            <Button variant="outline">
                <RouterLink to="/record">
                    Start Recording
                </RouterLink>
            </Button>
        </ButtonGroup>
        <PinField 
            v-for="(pinAnnotation, pinNumber) in pinConfig.pins" 
            :pinNumber="pinNumber" 
            :pinAnnotation="pinAnnotation"
            :key="pinNumber"
        />
    </FieldGroup>
</template>

<style scoped>
.upload-button {
    width: fit-content;
}
</style>
