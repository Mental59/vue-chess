<template>
    <div id="app" class="main-page">

        <div class="main-page__content-wrapper">

            <div class="main-page__chessboard">
                <chessboard @onMove="saveHistory"/>
            </div>
    
            <div class="main-page__aside">

                <h2 class="main-page__title">Ходы</h2>

                <div ref="container" class="scrollable-container">

                    <ul class="unstyled-list">
                        <li v-for="item in movesHistory">
                            {{ item.move }}
                        </li>
                    </ul>

                </div>

            </div>

        </div> 

    </div>
</template>

<script>
import {chessboard} from 'vue-chessboard'
import 'vue-chessboard/dist/vue-chessboard.css'
import './styles/index.css'

export default {
    name: 'app',

    components: {
        chessboard,
    },

    data() {
        return {
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
            },
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
            setTimeout(this.scrollToEnd);
        },

        transformToChessPiece(item) {
            switch (item[0]) {
                case 'K':
                case 'Q':
                case 'R':
                case 'B':
                case 'N':
                    item = this.pieces[this.turn][item[0]] + item.slice(1);
                    break;
                default:
                    item = this.pieces[this.turn]['P'] + item;
                    break;
            }
            return item;
        },

        scrollToEnd() {
            let container = this.$refs.container;
            container.scrollTop = container.scrollHeight;
        },
    },
}

</script>
