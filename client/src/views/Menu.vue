<template>
  <div class="menu">

  <b-container>

    <b-row class="justify-content-md-center">

      <b-col col lg="6">
        <b-list-group class="menu-list">

            <router-link to="/chess" class="router-link-exact-active">
              <b-list-group-item class="menu-list__item">
                Create game
              </b-list-group-item>
            </router-link>

            <router-link to="/">
              <b-list-group-item class="menu-list__item">
                Find game
              </b-list-group-item>
            </router-link>

        </b-list-group>
      </b-col>

      <b-col col lg="3">
        <rooms-list :roomsList="roomsList"></rooms-list>
      </b-col>

    </b-row>

  </b-container>
  </div>
</template>

<script>
import RoomsList from '@/components/RoomsList.vue'

  export default {
    components: {
      RoomsList
    },

    data() {
      return {
        roomsList: [
          'Room1',
          'Room2',
          'Room3',
          'Room4',
          'Room5',
          'Room6',
          'Room7',
          'Room8',
          'Room9'
        ]
      }
    }
  }
</script>

<style>
.menu {
  background-color: #161512;
}

a.router-link-exact-active {
  color: #42b983;
}

.menu-list__item {
  background-color: #383531;
  color: #bababa;
  font-size: 30px;
  font-weight: bold;
}

.menu-list__item:hover {
  background-color: #7a7979;
  color: white;
}

.menu-list__item:active {
  background-color: #b14607;
}

</style>
