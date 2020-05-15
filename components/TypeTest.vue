<template>
    <div class="container">
        <div class="main-card space-y-5">
            <div class="word-box" v-html="currWordHTML"/>
            <div class="space-y-5">
                <input type="text" class="text-input" :value="lastWord" @input="checkSpace($event.target.value)" placeholder="Type here">
                <div class="complete-box" v-if="isComplete">
                    <h1 class="align-middle">You have completed it! WPM:{{ fullWPM }} ACC: {{ fullACC }}</h1>
                    <button>Restart</button>
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
            htmlTextBox: [],
            fullTextInput: '',
            isComplete: false,
            startTime: 0,
            timeCompl: 0,
        }
    },
    methods: {
        checkSpace(word) {
            if (this.startTime == 0) {
                this.startTime = Date.now();
            }
            if (!this.isComplete) {
                if (this.textBox.split(' ').length === this.fullTextInput.split(' ').length) {
                    //Completed test
                    this.fullTextInput += word;
                    console.log('Test completed');
                    this.timeCompl = Date.now();
                    this.isComplete = true;
                } else if (word.charAt(word.length - 1) == ' ') {
                    this.fullTextInput += word;
                    //console.log("space detected");
                }
            }
            console.log(this.fullTextInput);
        }
    },
    computed: {
        lastWord() {
            let show = this.fullTextInput.split(" ");
            return show[show.length - 1];
        },
        currWordHTML() {
            let textBoxSplit = this.textBox.split(" ");
            let currIndex = this.fullTextInput.split(" ").length - 1;
            let currWord = textBoxSplit[currIndex];
            if (currWord !== undefined) {
                let currWordHTML = '<span style="text-decoration:underline; color:#2a4365; font-weight:bold;">' + currWord + '</span>';
                textBoxSplit[currIndex] = currWordHTML
                this.
            }
            return textBoxSplit.join(" ");
        },
        fullWPM() {
            let correctChar = 0;
            let wrongChar = 0;
            console.log("Start time is: " + Date.parse(this.startTime) + " and the endTime is " + this.timeCompl);
            return (this.timeCompl - this.startTime)/1000
        },
        fullACC() {
            return 0;
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