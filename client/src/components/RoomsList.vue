<template>
    <div>
        <b-list-group>
          <rooms-list-item
            v-for="(roomName, index) in roomsList"
            :key="index"
            :roomID="index"
            @connectGame="$emit('connectGame', { index })"
          >
            {{ roomName }}
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