<script setup>
import { Input } from "@/components/ui/input";
import { Button } from "../ui/button";
import { Field, FieldLabel } from "@/components/ui/field";
import { defineProps } from "vue";
import { usePinConfig } from "@/stores/pin-config";
import { ref } from "vue";

const props = defineProps(["pinNumber", "pinAnnotation"]);
const { pinNumber, pinAnnotation } = props;
const localAnnotationValue = ref(pinAnnotation);

const handleUpdateAnnotation = (event) => {
    const pinConfig = usePinConfig()
    pinConfig.pins[pinNumber] = localAnnotationValue.value; 
}
</script>

<template>
    <Field>
        <FieldLabel> Pin Number: {{ pinNumber }} </FieldLabel>
        <div class="flex gap-4">
            <Input placeholder="Enter the Pin Annotation" :model-value="localAnnotationValue" @update:model-value="localAnnotationValue = $event" />
            <Button @click="handleUpdateAnnotation" variant="outline">
                Update
            </Button>
        </div>
    </Field>
</template>
