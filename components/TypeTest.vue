<template>
    <div class="container">
        <div class="main-card space-y-5">
            <div class="word-box" v-html="textBox"/>
            <div class="space-y-5">
                <input type="text" class="text-input" :value="lastWord" @input="checkSpace($event.target.value)" placeholder="Type here">
                <div class="complete-box" v-if="isComplete">
                    <h1 class="align-middle">You have completed it!</h1>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            textBox: 'Random bunch of gibberish here to check accuracy compared to the other one',
            fullTextInput: '',
            isComplete: false,
            WPM: 0,
            ACC: 0,
        }
    },
    methods: {
        checkSpace(word) {
            if (this.textBox.split(' ').length === this.fullTextInput.split(' ').length) {
                //Completed test
                console.log('Test completed');
                this.isComplete = true;
            } else if (word.charAt(word.length - 1) == ' ') {
                this.fullTextInput += word;
                //console.log("space detected");
                console.log(this.fullTextInput);
            } else {
                //console.log('not detecting spaces');
            }
        }
    },
    computed: {
        lastWord() {
            let show = this.fullTextInput.split(" ");
            return show[show.length - 1];
        }
    }
}
</script>

<style scoped>
.container {
    @apply flex flex-col mx-auto p-5 bg-yellow-200 shadow-xl;
}

.main-card {
    @apply block flex flex-col p-5 bg-blue-800 font-serif shadow-lg;
}

.word-box {
    @apply w-full bg-orange-300 text-blue-800 p-5 text-2xl shadow-lg;
}

.text-input {
    @apply w-full h-16 text-2xl bg-blue-600 p-5 text-gray-900 shadow-lg;
}

.complete-box {
    @apply w-full p-2 text-3xl bg-yellow-200 text-blue-800 shadow-lg items-center text-center;
}
</style>