<template>
    <div>
        <b-list-group>
          <rooms-list-item
            v-for="(room, index) in roomsList"
            :key="index"
            :room="room"
            @connectPlayer="$emit('connectPlayer', { room })"
            @connectViewer="$emit('connectViewer', { room })"
          >
            {{ `Room_${room.owner.name}` }}
          </rooms-list-item>
        </b-list-group>
    </div>
</template>

<script>
    import RoomsListItem from '@/components/RoomsListItem.vue'

    export default {
        components: {
            RoomsListItem
        },
        
        props: {
            roomsList: { type: Array, required: true },
        }
    }
</script>

<style lang="scss" scoped>

</style>