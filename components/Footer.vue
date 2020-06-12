<template>
    <div class="flex justify-center">
        <div class="bottom-bar space-x-2">
            <button class="text-3xl font-thin text-blue-600" @click="toggleModal()">Help</button>
            <span class="border"></span>
            <a href="https://github.com/nhzaci/ClickClack" class="text-3xl font-thin" style="color:#a7ff83;">Github</a>
        </div>
        <ModalComponent @close="toggleModal()" v-if="showModal">
            <template v-slot:header>
                <h1 class="font-bold text-xl text-yellow-400" style="color: white;">Help</h1>
            </template>
            <template v-slot:body>
                <div class="p-5">
                    <ol class="list-disc space-y-2" style="color:white">
                        <li>The internal timer starts once you start typing in the input box</li>
                        <li>Space skips onto the next word</li>
                        <li>Pressing 'Esc' inside the input box allows you to restart</li>
                        <li>WPM and ACC is averaged over your runs on the top right and can be cleared by clearing your cookies</li>
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