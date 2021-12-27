<template>
    <div class="game">
        <b-container>
            <b-row align-v="center">
                <b-col>
                    <chessboard ref="chessboard" :fen="currentFen" @onMove="saveHistory"/>
                </b-col>
                <b-col class="chessboard-aside">
                    <stop-clock
                        class="chess-clock__half"
                        ref="clock1"
                        :minutes="clockMinutes" :seconds="clockSeconds"
                        :run="run1"
                        @end="endTime"
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
                        @end="endTime"
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

            clockMinutes: 5,
            clockSeconds: 0,
            isEnded: false,
            firstPlayerTurn: true,
            secondPlayerTurn: false,

            movesHistory: [],
            cnt: 0,
            currentTurn: 'white',
            currentFen: '',
            positionInfo: null,
            connection: null,
            currentOrientation: 'white',
            isWaiting: false,
            isViewer: false,

            pieces: {
                black: {
                    K: '♔',
                    Q: '♕',
                    R: '♖',
                    B: '♗',
                    N: '♘',
                    P: '♙'
                },
                white: {
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
            this.$refs.chessboard.board.set({orientation: this.currentOrientation, viewOnly: this.isWaiting})
            if (data.history.length === 0 || data.fen === this.currentFen) {
                return;
            }

            const obj = {
                fen: data.fen,
                isViewer: this.isViewer,
                messageType: 'Standart'
            };
            this.sendMessage(JSON.stringify(obj));

            this.movesHistory.push(
                {
                    id: this.cnt++,
                    move: this.transformToChessPiece(data.history[data.history.length - 1])
                }
            );
            
            this.checkGameOver();
            this.currentTurn = data.turn;
            this.nextTurn();
        },

        sendMessage(message) {
            try {
                this.connection.send(message);
            }
            catch(err) {
                console.log(err);
            }
        },

        connect() {
            console.log('Starting connection to WebSocket Server');
            this.connection = new WebSocket('ws://0.0.0.0:50051');
            let vm = this;

            this.connection.onmessage = function (event) {
                try {
                    var dic = JSON.parse(event.data);

                    vm.currentOrientation = dic.orientation;
                    vm.isViewer = dic.status === 'true'
                    vm.isWaiting = dic.status === 'true'
                    vm.$refs.chessboard.board.set({ viewOnly: true });
                    console.log(vm.$refs.chessboard.game.turn()[0]);
                    console.log(vm.currentOrientation[0]);
                }
                catch (e) {
                    vm.$refs.chessboard.game.load(event.data)
                    if (vm.isViewer !== true) {
                        if (vm.$refs.chessboard.game.turn()[0] !== vm.currentOrientation[0]) {
                            vm.$refs.chessboard.board.set({ viewOnly: true })
                            vm.isWaiting = true
                        }
                        else {
                            vm.$refs.chessboard.board.set({ viewOnly: false })
                            vm.isWaiting = false
                        }
                    }
                }

                vm.currentFen = event.data;
                vm.$refs.chessboard.board.set({ orientation: vm.currentOrientation })
            }

            this.connection.onopen = function(event) {
                console.log(event)
                console.log("Successfully connected to the echo websocket server...")
                vm.$refs.chessboard.board.set({ orientation: vm.currentOrientation })
                setTimeout(() => {
                    var myObj = new Object(); myObj.messageType = "Init"; myObj.user_id = localStorage.getItem('user_id');
                    vm.sendMessage(JSON.stringify(myObj))
                }, 10);
            }

            this.connection.onclose = function (event) {
                console.log(event)
                if (!event.wasClean) {
                    alert("Server is down... Reconnecting...")
                    setTimeout(function () {
                        vm.connect();
                    }, 5000);
                }
            }
        },

        async isOnline() {
            try {
                await fetch("https://google.com");
                return true;
            }
            catch (err) {
                console.log(err);
            }
            return false;
        },

        uuid() {
            var uuidValue = "", k, randomValue;
            for (k = 0; k < 32; k++) {
                randomValue = Math.random() * 16 | 0;

                if (k == 8 || k == 12 || k == 16 || k == 20) {
                    uuidValue += "-"
                }
                uuidValue += (k == 12 ? 4 : (k == 16 ? (randomValue & 3 | 8) : randomValue)).toString(16);
            }
            return uuidValue;
        },

        checkGameOver() {
            if (this.movesHistory[this.movesHistory.length - 1].move.slice(-1) === '#') {
                this.isEnded = true;
                if (this.firstPlayerTurn) {
                    this.firstPlayerName += " winnner!"
                } else {
                    this.secondPlayerName += " winnner!"
                }
            }
        },

        transformToChessPiece(item) {
            switch (item[0]) {
                case 'K':
                case 'Q':
                case 'R':
                case 'B':
                case 'N':
                    return this.pieces[this.currentTurn][item[0]] + item.slice(1);
                case 'O':
                    return item;
                default:
                    return this.pieces[this.currentTurn]['P'] + item;
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

        endTime() {
            this.isEnded = true;
            if (this.firstPlayerTurn) {
                this.secondPlayerName += " winnner!"
            } else {
                this.firstPlayerName += " winnner!"
            }
        }

    },

    created() {
        this.connect();
        if (localStorage.getItem('user_id') === null) {
            localStorage.setItem('user_id', this.uuid());
        }
        let userID = localStorage.getItem('user_id'); 
        this.firstPlayerName = 'Player_' + userID.slice(0, 8);
    },

    computed: {
        run1() {
            return !this.isEnded && this.firstPlayerTurn;
        },

        run2() {
            return !this.isEnded && this.secondPlayerTurn;
        },

    },

    watch: {
        isEnded() {
            if (this.isEnded) {
                this.$refs.chessboard.board.set({
                    viewOnly: true
                });
            }
        }
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