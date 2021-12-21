<template>
    <div class="moves-container-parent">
        <div class="moves-container" ref="container">
            <b-container>
                <b-row>

                    <b-col class="first-player-moves">
                        <b-list-group class="player-list">
                            <b-list-group-item class="player-list__item" v-for="item in firstPlayerMoves" :key="item.id">
                                {{ `${item.id + 1}. ${item.move}` }}
                            </b-list-group-item>
                        </b-list-group>
                    </b-col>

                    <b-col class="second-player-moves">
                        <b-list-group class="player-list">
                            <b-list-group-item class="player-list__item" v-for="item in secondPlayerMoves" :key="item.id">
                                {{ `${item.id + 1}. ${item.move}` }}
                            </b-list-group-item>
                        </b-list-group>
                    </b-col>

                </b-row>
            </b-container>
        </div>
    </div>
</template>

<script>
export default {
    props: ['playerMoves'],

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

.player-list__item {
    font-size: 30px;
    background-color: #262421;
}

</style>
