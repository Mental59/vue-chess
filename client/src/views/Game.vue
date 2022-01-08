<template>
    <div class="game">
        <b-container>
            <b-row align-v="center">
                <b-col>
                    <chessboard ref="chessboard" :fen="currentFen" :orientation="currentOrientation" @onMove="onMove"/>
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
            firstPlayerName: "UNKNOWN",
            secondPlayerName: "UNKNOWN",
            firstPlayerTurn: true,
            secondPlayerTurn: false,
            playerType: '',

            clockMinutes: 5,
            clockSeconds: 0,

            movesHistory: [],

            currentFen: '',
            currentOrientation: 'white',
            currentTimeout: null,

            isEnded: false,
            isWaiting: null,
            isViewer: false,
            isGameStarted: false,

            connection: null,

            pieces: {
                K: '♔',
                Q: '♕',
                R: '♖',
                B: '♗',
                N: '♘',
                P: '♙'
            }
        }
    },

    methods: {
        onMove(data) {
            this.$refs.chessboard.board.set({
                viewOnly: this.isWaiting
            });
            if (data.history.length === 0 || data.fen === this.currentFen) {
                return;
            }
            console.log('onMove emitted!');
            console.log(data);

            this.movesHistory.push(
                {
                    move: this.transformToChessPiece(data.history[data.history.length - 1])
                }
            );
            
            this.checkGameOver();
            this.nextTurn(data);

            this.sendMessage({
                type: "Move",
                user: this.user,
                isEnded: this.isEnded,
                currentFen: this.currentFen,
                movesHistory: this.movesHistory
            });
        },

        sendMessage(message) {
            try {
                this.connection.send(JSON.stringify(message));
            }
            catch(err) {
                console.log(err);
            }
        },

        setClocktime(firstClockTime, secondClockTime) {
            if (this.playerType === "first" || this.playerType === "viewer") {
                this.$refs.clock1.setTime(firstClockTime);
                this.$refs.clock2.setTime(secondClockTime);
            } else {
                this.$refs.clock2.setTime(firstClockTime);
                this.$refs.clock1.setTime(secondClockTime);
            }
        },

        connect() {
            console.log('Starting connection to WebSocket Server');

            const address = this.$route.params.address;
            const port = this.$route.params.port;
            this.connection = new WebSocket(`ws://localhost:5001`);

            this.connection.onmessage = this.handleMessage;
            this.connection.onopen = this.handleOpenConnection;
            this.connection.onclose = this.handleCloseConnection;
        },

        handleMessage(event) {
            const response = JSON.parse(event.data);
            console.log(response);

            switch(response.type) {
                case "Init":
                    this.firstPlayerName = response.firstPlayerName;
                    this.currentFen = response.currentFen;
                    this.isWaiting = true;
                    this.playerType = response.playerType;

                    switch (response.playerType) {
                        case "first":
                            this.currentOrientation = "white";
                            this.firstPlayerTurn = true;
                            this.secondPlayerTurn = false;
                            break;
                        case "second":
                            this.currentOrientation = "black";
                            this.firstPlayerTurn = false;
                            this.secondPlayerTurn = true;
                            break;
                        case "viewer":
                            this.currentOrientation = "white";
                            break;
                    }

                    break;
                case "PlayerIn":
                    if (this.playerType === "viewer") {
                        this.firstPlayerName = response.firstPlayerName;
                        this.secondPlayerName = response.secondPlayerName;
                    } else {
                        if (this.playerType === "first")
                            this.secondPlayerName = response.secondPlayerName;
                        else
                            this.secondPlayerName=response.firstPlayerName;
                    }
                    if (this.playerType === "first") {
                        this.isWaiting = false;
                    }
                    this.isGameStarted = true;
                    break;
                case "Move":
                    this.currentFen = response.currentFen;
                    this.isEnded = response.isEnded;
                    this.movesHistory = response.movesHistory;
                    this.firstPlayerTurn=true;
                    this.secondPlayerTurn=false;
                    this.isWaiting = false;
                    break;
                case "Time":
                    this.setClocktime(response.firstClockTime, response.secondClockTime);
                    break;
                case "Leave":
                    console.log('Player has left the game');
                    break;
                case "Reconnect":
                    this.firstPlayerName = response.firstPlayerName;
                    this.secondPlayerName = response.secondPlayerName;
                    this.firstPlayerTurn = response.firstPlayerTurn;
                    this.secondPlayerTurn = response.secondPlayerTurn;
                    this.currentFen = response.currentFen;
                    this.movesHistory = response.movesHistory;
                    this.setClocktime(response.firstClockTime, response.secondClockTime);
                    this.isWaiting = response.isWaiting;
                    this.currentOrientation = response.currentOrientation;
                    this.isGameStarted = response.gameStarted;
                    break;
                case "Timeout":
                    this.isEnded = true;
                    this.firstPlayerName += " Winner";
                    break;
                default:
                    console.log(`Bad message type, got ${response.type}`);
                    return;
            }
        },

        handleOpenConnection(event) {
            this.sendMessage({
                type: "Init",
                user: this.user,
            });
        },

        handleCloseConnection(event) {
            if (!event.wasClean && !this.isEnded) {
                console.log('Server is down, reconnecting');
                this.currentTimeout = setTimeout(() => {
                    this.connect();
                }, 5000);
                return;
            }

            this.sendMessage({
                type: "Leave",
                user: this.user,
            });
        },

        closeConnectionAfterGame() {
            console.log("Game is over");
            setTimeout(() => {               
                this.sendMessage({
                    type: "GameOver",
                    user: this.user,
                });
                this.$router.push({path: "/"});
            }, 5000);
        },

        checkGameOver() {
            if (this.movesHistory[this.movesHistory.length - 1].move.slice(-1) === '#') {
                this.isEnded = true;
                if (this.firstPlayerTurn) {
                    this.firstPlayerName += " winnner!";
                } else {
                    this.secondPlayerName += " winnner!";
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
                    return this.pieces[item[0]] + item.slice(1);
                case 'O':
                    return item;
                default:
                    return this.pieces['P'] + item;
            }
        },

        nextTurn(data) {
            this.isWaiting = true;
            this.currentFen = data.fen;
            this.firstPlayerTurn = !this.firstPlayerTurn;
            this.secondPlayerTurn = !this.secondPlayerTurn;
        },

        endTime() {
            this.isEnded = true;
            if (this.firstPlayerTurn) {
                this.secondPlayerName += " winnner!";
            } else {
                this.firstPlayerName += " winnner!";
            }
            this.sendMessage({
                type: "Timeout",
                user: this.user,
            });
        },

    },

    created() {
        this.connect();
        this.user = localStorage.getItem("user_id");
    },

    destroyed() {
        clearTimeout(this.currentTimeout);
        this.connection.close();
    },

    computed: {
        run1() {
            return !this.isEnded && this.firstPlayerTurn && this.isGameStarted;
        },
        run2() {
            return !this.isEnded && this.secondPlayerTurn && this.isGameStarted;
        },
    },

    watch: {
        isEnded() {
            if (this.isEnded) {
                this.$refs.chessboard.board.set({
                    viewOnly: true
                });
                this.closeConnectionAfterGame();
            }
        },

        isWaiting() {
            this.$refs.chessboard.board.set({
                viewOnly: this.isWaiting
            });
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