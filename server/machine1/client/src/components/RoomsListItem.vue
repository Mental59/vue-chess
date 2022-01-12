<template>
    <div>
        <b-list-group-item class="rooms-list__item">
            <b-container>
                <b-row>
                    <b-col align-self="center">
                        <slot></slot>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col align-self="center">
                        <b-button
                            @click="$emit('connectPlayer')"
                            variant="dark"
                            class="connect-button"
                            :disabled="gameStatus === 1 || gameStatus === 2"
                        >
                            Connect as player
                        </b-button>
                    </b-col>
                    <b-col align-self="center">
                        <b-button
                            @click="$emit('connectViewer')"
                            variant="dark"
                            class="connect-button"
                            :disabled="gameStatus === 0 || gameStatus === 2"
                        >
                            Connect as viewer
                        </b-button>
                    </b-col>
                </b-row>
            </b-container>
        </b-list-group-item>
    </div>
</template>

<script>
export default {
    props: {
        room: {type: Object, required: true},
    },

    computed: {
        gameStatus() {
            return this.room.state;
        }
    }
}
</script>

<style lang="scss" scoped>
.rooms-list__item {
  background-color: #312e2b;
  color: #bababa;
  font-weight: bold;
}

.connect-button {
    font-weight: bold;
    color: #bababa;
}
</style>