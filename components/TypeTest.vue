<template>
    <div class="container">
        <div class="main-card space-y-5">
            <div class="word-sel">
                <div>
                    Word Selector: 
                    <button class="wordcount-button" @click="set_wordCount(10)">10</button>
                    <button class="wordcount-button" @click="set_wordCount(25)">25</button>
                    <button class="wordcount-button" @click="set_wordCount(50)">50</button>
                    <button class="wordcount-button" @click="set_wordCount(100)">100</button>
                    <button class="wordcount-button" @click="set_wordCount(250)">250</button>
                </div>
                <div>
                    <h1>{{ fullWPM }}</h1>
                </div>
            </div>
            <div class="word-box lg:text-2xl" v-html="currWordHTML"/>
            <div class="space-y-5">
                <div class="inline-flex justify-between w-full space-x-10">
                    <input 
                        type="text" 
                        class="text-input w-3/4" 
                        :value="lastWord" 
                        @keyup.esc="reloadPage()"
                        @input="checkSpace($event.target.value)" 
                        placeholder="Type here" 
                        v-if="!isComplete"
                    >
                    <button class="restart-button" v-if="!isComplete" @click="reloadPage()">Restart</button>
                    <input type="text" class="text-input w-full" placeholder="Type here" v-if="isComplete" />
                </div>
                <div class="complete-box space-y-2" v-if="isComplete">
                    <h1 class="align-middle" style="color:#071e3d;">Another one?</h1>
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
            wordsSel: 100,
            htmlTextBox: [],
            fullTextInput: '',
            isComplete: false,
            startTime: 0,
            timeCompl: 0,
            isCompleteOnce: false
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
                    this.isCompleteOnce = true;
                    //console.log(this.textBox);
                } else if (word.charAt(word.length - 1) == ' ') {
                    this.fullTextInput += word;
                    //console.log("space detected");
                }
            }
            //console.log(this.fullTextInput);
        },
        reloadPage() {
            window.location.reload(); //Refreshes page
        },
        set_wordCount(count) {
            this.wordCount = count;
            this.$cookies.set('word-count', count);
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
            if (!this.isCompleteOnce) {
                return "WPM: TBC ACC: TBC";
            }

            let correctChar = 0;
            let wrongChar = 0;
            let textInputSplit = this.fullTextInput.split(" ");
            let textBoxSplit = this.textBox.split(" ");
            for (let i = 0; i < textInputSplit.length; i++) {
                if (textInputSplit[i] === textBoxSplit[i]) {
                    correctChar += textInputSplit[i].length + 1;
                    if (i !== textInputSplit.length - 1) {
                        correctChar += 1;
                    }
                } else {
                    wrongChar += textInputSplit[i].length;
                    if (i !== textInputSplit.length - 1) {
                        wrongChar += 1;
                    }
                }
            }
            //console.log(correctChar);
            //console.log(wrongChar);
            console.log(this.timeCompl - this.startTime);
            let wpm = Math.round((correctChar / 5) / ((this.timeCompl - this.startTime) / 1000 / 60));
            let acc = Math.round(correctChar / (correctChar + wrongChar) * 100);
            return `WPM: ${wpm} ACC: ${acc}%`;
        },
        textBox() {
            let wordString = ''
            for(let i = 0; i < this.wordCount; i++) {
                wordString += this.wordsJson[Math.floor(Math.random() * 1000)];
                if (i !== this.wordCount - 1) {
                    wordString += ' ';
                }
            }
            return wordString;
        },
        wordCount: {
            get: function () {
                if (this.$cookies.get('word-count') !== undefined) {
                    this.wordsSel = this.$cookies.get('word-count');
                }
                return this.wordsSel;
            },
            set: function (count) {
                this.wordsSel = count;
                return this.wordsSel;
            }
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
    @apply w-full p-5 text-lg text-blue-800 shadow-lg;
    background-color: #086972;
    color: #a7ff83;
}

.text-input {
    @apply h-16 text-2xl p-5 shadow-lg;
    color: #071a52;
    background-color: #17b978;
}

.word-sel {
    @apply text-xl bg-blue-500 flex justify-between px-2 items-center;
    color: #a7ff83;
}

.wordcount-button {
    @apply pt-1 border-b border-transparent font-thin;
}

.wordcount-button:hover {
    @apply border-b border-yellow-200;
}

.restart-button {
    @apply w-1/4 h-16 text-2xl shadow-lg font-thin bg-blue-500;
    color: #a7ff83;
}

.restart-button:hover {
    @apply bg-blue-600 shadow-inner shadow-none;
}

.complete-box {
    @apply w-full p-5 text-3xl shadow-lg items-center text-center bg-orange-200;
}

::placeholder {
    color: white;
    opacity: 0.8;
}
</style>