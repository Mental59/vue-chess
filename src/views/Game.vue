<template>
    <div class="game">
        <b-container>
            <b-row align-v="center">
                <b-col>
                    <chessboard @onMove="saveHistory"/>
                </b-col>
                <b-col class="chessboard-aside">
                    <stop-clock
                        class="chess-clock__half"
                        ref="clock1"
                        :minutes="clockMinutes" :seconds="clockSeconds"
                        :run="run1"
                        @end="end"
                    />

                    <b-card
                        class="moves-history"
                        :header="firstPlayerName"
                        :footer="secondPlayerName"
                    >
                        <moves-container :playerMoves="movesHistory"/>
                    </b-card>

                    <stop-clock
                        class="chess-clock__half"
                        ref="clock2"
                        :minutes="clockMinutes" :seconds="clockSeconds"
                        :run="run2"
                        @end="end"
                    />
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import {chessboard} from 'vue-chessboard'
import 'vue-chessboard/dist/vue-chessboard.css'
import MovesContainer from '@/components/MovesContainer.vue'
import StopClock from '@/components/StopClock.vue'

export default {
    name: 'game',

    components: {
        chessboard,
        MovesContainer,
        StopClock
    },

    data() {
        return {
            firstPlayerName: "Player1",
            secondPlayerName: "Player2",

            clockMinutes: 1,
            clockSeconds: 0,
            isEnded: false,
            firstPlayerTurn: true,
            secondPlayerTurn: false,

            movesHistory: [],
            cnt: 0,
            turn: 'white',

            pieces: {
                white: {
                    K: '♔',
                    Q: '♕',
                    R: '♖',
                    B: '♗',
                    N: '♘',
                    P: '♙'
                },
                black: {
                    K: '♚',
                    Q: '♛',
                    R: '♜',
                    B: '♝',
                    N: '♞',
                    P: '♟'
                },
            }
        }
    },

    methods: {
        saveHistory(data) {
            if (data.history.length === 0) {
                return;
            }

            this.movesHistory.push(
                {
                    id: this.cnt++,
                    move: this.transformToChessPiece(data.history[data.history.length - 1])
                }
            );
            
            this.turn = data.turn;
            this.nextTurn();
            console.log(data);
            // console.log(`Clock1=${this.$refs.clock1.countMinutes}:${this.$refs.clock1.countSeconds}`);
            // console.log(`Clock1=${this.$refs.clock2.countMinutes}:${this.$refs.clock2.countSeconds}`);
        },

        transformToChessPiece(item) {
            switch (item[0]) {
                case 'K':
                case 'Q':
                case 'R':
                case 'B':
                case 'N':
                    return this.pieces[this.turn][item[0]] + item.slice(1);
                case 'O':
                    return item;
                default:
                    return this.pieces[this.turn]['P'] + item;
            }
        },

        nextTurn() {
            if (this.isEnded) {
                return;
            }
            
            if (this.firstPlayerTurn) {
                this.$refs.clock1.increaseTime(5);
                this.start2();
            } else {
                this.$refs.clock2.increaseTime(5);
                this.start1();
            }
        },

        start1() {
            this.firstPlayerTurn = true;
            this.secondPlayerTurn = false;
        },

        start2() {
            this.firstPlayerTurn = false;
            this.secondPlayerTurn = true;
        },

        end() {
            this.isEnded = true;
        }

    },

    computed: {
        run1() {
            return !this.isEnded && this.firstPlayerTurn;
        },

        run2() {
            return !this.isEnded && this.secondPlayerTurn;
        },

    }

}
</script>

<style>
.game {
    color: #bababa;
}

.cg-board-wrap { 
    width: 600px;
    height: 600px;
}

.moves-history {
    height: 400px;
    text-align: left;
    background-color: #423c34;
    border-radius: 0px;
}

.card-header {
    font-size: 2rem;
}

.card-footer {
    font-size: 2rem;
}

.chessboard-aside {
    margin-bottom: 20px;
}
</style>