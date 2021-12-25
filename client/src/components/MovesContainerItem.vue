<template>
    <div>
        <b-list-group-item class="player-list__item">
            {{ `${move.id + 1}. ${move.move}` }}
        </b-list-group-item>
    </div>
</template>

<script>
    export default {
        props: {
            move: { type: Object, required: true },
        }
    }
</script>

<style lang="scss" scoped>
.player-list__item {
    font-size: 30px;
    background-color: #262421;
}
</style>