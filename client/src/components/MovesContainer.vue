<template>
    <div class="moves-container-parent">
        <div class="moves-container" ref="container">
            <b-container>
                <b-row>

                    <b-col class="first-player-moves">
                        <b-list-group class="player-list">
                            <moves-container-item v-for="(move, index) in firstPlayerMoves" :key="index" :id="index" :move="move"/>
                        </b-list-group>
                    </b-col>

                    <b-col class="second-player-moves">
                        <b-list-group class="player-list">
                            <moves-container-item v-for="(move, index) in secondPlayerMoves" :key="index" :id="index" :move="move"/>
                        </b-list-group>
                    </b-col>

                </b-row>
            </b-container>
        </div>
    </div>
</template>

<script>
import MovesContainerItem from '@/components/MovesContainerItem'

export default {
    components: {
        MovesContainerItem
    },

    props: {
        playerMoves: {type: Array, required: true}
    },

    computed: {
        firstPlayerMoves() {
            return this.playerMoves.filter((item, index) => index % 2 == 0)
        },
        secondPlayerMoves() {
            return this.playerMoves.filter((item, index) => index % 2 == 1)
        }
    },

    methods: {
        scrollToEnd() {
            let container = this.$refs.container;
            container.scrollTop = container.scrollHeight;
        }
    },

    updated() {
        this.scrollToEnd();
    }
}
</script>

<style>
.first-player-moves {
    padding: 0;
}

.second-player-moves {
    padding: 0;
}

.moves-container-parent {
    width: 100%;
    height: 100%;
    overflow: hidden;
}

.moves-container {
    width: 100%;
    height: 100%;
    overflow-y: scroll;
    padding-right: 17px;
    box-sizing: content-box;
}

.player-list {
    max-height: 300px;
    margin-bottom: 10px;
    border-radius: 0px;
}

</style>
