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
                    <h1 class="wpm-counter">{{ fullWPM[1] }}</h1>
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
                        autofocus
                    >
                    <button class="restart-button" v-if="!isComplete" @click="reloadPage()">Restart</button>
                    <input type="text" class="text-input w-full" placeholder="Type here" @keyup.esc="reloadPage()" v-if="isComplete" />
                </div>
                <div class="complete-box space-y-3" v-if="isComplete">
                    <h1 class="complete-box-text align-middle">Another one? Current Run: {{ fullWPM[0] }}</h1>
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
            wordsSel: 25,
            htmlTextBox: [],
            fullTextInput: '',
            isComplete: false,
            startTime: 0,
            timeCompl: 0
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
        reloadPage() {
            window.location.reload(); //Refreshes page
        },
        set_wordCount(count) {
            this.wordCount = count;
            this.$cookies.set('word-count', count);
            if (this.isComplete) {
                this.reloadPage();
            } else {
                this.$forceUpdate();
            }
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
            let cookieCorrChar = 0;
            let cookieWrongChar = 0;
            let cookieTimeTaken = 0;

            if (this.$cookies.get("wpm-data") === undefined && !this.isComplete) {
                return ["", "WPM: TBC ACC: TBC"];
            } else if (this.$cookies.get("wpm-data") !== undefined) {
                //Check if cookies exist from previous attempts
                cookieCorrChar += Number(this.$cookies.get("wpm-data").correctChar);
                cookieWrongChar += Number(this.$cookies.get("wpm-data").wrongChar);
                cookieTimeTaken += Number(this.$cookies.get("wpm-data").totalTime);
                if (!this.isComplete) {
                    //if current session not complete, just history
                    let wpm = Math.round((cookieCorrChar / 5) / cookieTimeTaken);
                    let acc = Math.round(cookieCorrChar / (cookieCorrChar + cookieWrongChar) * 100);
                    return ["", `WPM: ${wpm} ACC: ${acc}%`];
                }
            }

            let correctChar = 0;
            let wrongChar = 0;
            let timeTakenInMins = (this.timeCompl - this.startTime) / 1000 / 60;
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

            //Add both cookie and normal values to make total
            let totalCorrChar = correctChar + cookieCorrChar;
            let totalWrongChar = wrongChar + cookieWrongChar;
            let totalTimeTaken = timeTakenInMins + cookieTimeTaken;

            //json object as cookie value
            let cookie_json = {
                "correctChar": totalCorrChar,
                "wrongChar": totalWrongChar,
                "totalTime": totalTimeTaken 
            }
            //Cookie set to expire in a week
            this.$cookies.set("wpm-data", cookie_json, {
                maxAge: 60 * 60 * 24 * 7
            });
            //console.log("Should have set cookie data already");

            let currWPM = Math.round((correctChar / 5) / timeTakenInMins);
            let currACC = Math.round(correctChar / (correctChar + wrongChar) * 100);
            

            let wpm = Math.round((totalCorrChar / 5) / totalTimeTaken);
            let acc = Math.round(totalCorrChar / (totalCorrChar + totalWrongChar) * 100);
            return [`WPM: ${currWPM} ACC: ${currACC}%`, `WPM: ${wpm} ACC: ${acc}%`];
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
@import url("@/assets/css/typetest.css");
</style>