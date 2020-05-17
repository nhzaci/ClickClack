<template>
    <div class="flex justify-center">
        <div class="bottom-bar space-x-2">
            <button class="text-3xl font-thin text-blue-600" @click="toggleModal()">Help</button>
            <span class="border"></span>
            <a href="https://github.com/nhzaci/ClickClack" class="text-3xl font-thin" style="color:#a7ff83;">Github</a>
        </div>
        <ModalComponent @close="toggleModal()" v-if="showModal">
            <template v-slot:header>
                <h1 class="font-bold text-xl text-gray-200">Help</h1>
            </template>
            <template v-slot:body>
                <div class="p-5 text-gray-100">
                    <ol class="list-disc space-y-2">
                        <li>When you start typing in the input box, the time starts</li>
                        <li>Press space to move onto the next word</li>
                        <li>WPM and ACC is averaged over your runs</li>
                    </ol>
                </div>
            </template>
        </ModalComponent>
    </div>
</template>

<script>
import ModalComponent from "./ModalComponent";

export default {
    components: {
        ModalComponent
    },
    data() {
        return {
            showModal: false
        }
    },
    methods: {
        toggleModal() {
            this.showModal = !this.showModal;
        }
    }
}
</script>

<style scoped>
.bottom-bar {
    @apply p-5 inline-flex justify-center;
}
</style>