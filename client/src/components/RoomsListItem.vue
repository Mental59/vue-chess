<template>
    <div>
        <b-list-group-item class="rooms-list__item">
            <b-container>
                <b-row>
                    <b-col align-self="center">
                        <slot></slot>
                    </b-col>
                    <b-col align-self="center">
                        <b-button @click="$emit('connectGame')" variant="dark" class="connect-button">
                            Connect
                        </b-button>
                    </b-col>
                </b-row>
            </b-container>
        </b-list-group-item>
    </div>
</template>

<script setup>
export default {
    props: {
        roomID: {type: Number, required: true},
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