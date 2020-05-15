<template>
    <div class="container">
        <div class="main-card space-y-5">
            <div class="word-sel">
                Word Selector: 
                <button @click="set_wordCount(10)">10</button>
                <button @click="set_wordCount(25)">25</button>
                <button @click="set_wordCount(50)">50</button>
                <button @click="set_wordCount(100)">100</button>
                <button @click="set_wordCount(250)">250</button>
            </div>
            <div class="word-box" v-html="currWordHTML"/>
            <div class="space-y-5">
                <div class="inline-flex justify-between w-full space-x-10">
                    <input type="text" class="text-input w-3/4" :value="lastWord" @input="checkSpace($event.target.value)" placeholder="Type here" v-if="!isComplete">
                    <button class="restart-button" v-if="!isComplete" @click="reloadPage">Restart</button>
                    <input type="text" class="text-input w-full" placeholder="Type here" v-if="isComplete" />
                </div>
                <div class="complete-box space-y-2" v-if="isComplete">
                    <h1 class="align-middle" style="color:#071a52;">You have completed it! WPM:{{ fullWPM }} ACC: {{ fullACC }}</h1>
                    <button class="restart-button" @click="reloadPage">Restart</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import wordList from '../assets/words.json';

export default {
    data() {
        return {
            wordsJson: wordList,
            wordCount: 100,
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
                if (this.textBox.split(' ').length === this.fullTextInput.split(' ').length && word.charAt(word.length - 1) == ' ') {
                    //Completed test
                    this.fullTextInput += word;
                    //console.log('Test completed');
                    this.timeCompl = Date.now();
                    this.isComplete = true;
                    //console.log(this.textBox);
                } else if (word.charAt(word.length - 1) == ' ') {
                    this.fullTextInput += word;
                    //console.log("space detected");
                }
            }
            //console.log(this.fullTextInput);
        },
        reloadPage(count = 100) {
            window.location.reload();
            this.wordCount = count;
        },
        set_wordCount(count) {
            this.wordCount = count;
            this.$forceUpdate();
        }
    },
    computed: {
        lastWord() {
            let show = this.fullTextInput.split(" ");
            return show[show.length - 1];
        },
        currWordHTML() {
            let textBoxSplit = this.textBox.split(" ");
            let textInputSplit = this.fullTextInput.split(" ")
            let currIndex = textInputSplit.length - 1;
            let currWord = textBoxSplit[currIndex];
            if (currWord !== undefined) {
                let currWordHTML = '<span style="text-decoration:underline; font-weight:bold;">' + currWord + '</span>';
                textBoxSplit[currIndex] = currWordHTML
            }
            if (currIndex >= 1) {
                let isCorrect = textBoxSplit[currIndex - 1] === textInputSplit[currIndex - 1];
                let prevWord = textBoxSplit[currIndex - 1]
                if (isCorrect) {
                    this.htmlTextBox[currIndex - 1] = '<span style="color:greenyellow;">' + prevWord + '</span>';
                } else {
                    this.htmlTextBox[currIndex - 1] = '<span style="color:red;">' + prevWord + '</span>';
                }
                return this.htmlTextBox.join(" ") + ' ' + textBoxSplit.slice(currIndex, textBoxSplit.length + 1).join(" ");
            }
            return textBoxSplit.join(" ");
        },
        fullWPM() {
            let correctChar = 0;
            let wrongChar = 0;
            let textInputSplit = this.fullTextInput.split(" ");
            let textBoxSplit = this.textBox.split(" ");
            for (let i = 0; i < textInputSplit.length; i++) {
                if (textInputSplit[i] === textBoxSplit[i]) {
                    correctChar += textInputSplit.length;
                } else {
                    wrongChar += textInputSplit.length;
                }
            }
            //console.log(correctChar);
            //console.log(wrongChar);
            //console.log(this.timeCompl - this.startTime);
            return Math.round((correctChar / 5) / (this.timeCompl - this.startTime) * 1000 * 60);
        },
        fullACC() {
            return 0;
        },
        textBox() {
            let wordString = ''
            for(let i = 0; i < this.wordCount; i++) {
                wordString += this.wordsJson[Math.floor(Math.random() * 1000)]
                if (i !== this.wordCount - 1) {
                    wordString += ' '
                }
            }
            return wordString;
        }
    }
}
</script>

<style scoped>
.container {
    @apply flex flex-col mx-auto p-5;
}

.main-card {
    @apply block flex flex-col p-5 font-thin shadow-xl mx-auto;
    background-color: #1f4287;
}

.word-box {
    @apply w-full p-5 text-2xl text-blue-800 shadow-lg;
    background-color: #086972;
    color: #a7ff83;
}

.text-input {
    @apply h-16 text-2xl p-5 shadow-lg;
    color: #071a52;
    background-color: #17b978;
}

.word-sel {
    @apply text-xl bg-blue-500 p-2;
    color: #a7ff83;
}

.restart-button {
    @apply w-1/4 h-16 text-2xl shadow-lg font-thin bg-blue-500;
    color: #a7ff83;
}

.complete-box {
    @apply w-full p-5 text-3xl shadow-lg items-center text-center bg-orange-200;
    color: #17b978;
}

::placeholder {
    color: white;
    opacity: 0.8;
}
</style>