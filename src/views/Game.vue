<template>
    <div class="game">
        <b-container>
            <b-row align-v="center">
                <b-col>
                    <chessboard @onMove="saveHistory"/>
                </b-col>
                <b-col>
                    <b-card title="Ходы" class="moves-history">
                        <moves-container :playerMoves="movesHistory"></moves-container>
                    </b-card>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import {chessboard} from 'vue-chessboard'
import 'vue-chessboard/dist/vue-chessboard.css'
import MovesContainer from '@/views/MovesContainer.vue'
import '@/styles/game.css'

export default {
    name: 'game',

    components: {
        chessboard,
        'moves-container': MovesContainer,
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

    },
}

</script>
