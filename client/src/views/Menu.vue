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

      <b-col col lg="4">
        <rooms-list
          class="rooms-list"
          :roomsList="roomsList"
          @connectPlayer="handleConnectPlayer"
          @connectViewer="handleConnectViewer"
        />
      </b-col>

    </b-row>

  </b-container>
  </div>
</template>

<script>
import RoomsList from '@/components/RoomsList.vue'
import { Client, createUser, createGame } from '@/api/grpc/client.js'

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
    },

    methods: {
      handleConnectPlayer(event) {
        this.client.joinPlayer();
      },

      handleConnectViewer(event) {
        console.log(event);
      },

      uuid() {
        var uuidValue = "", k, randomValue;
        for (k = 0; k < 32; k++) {
          randomValue = Math.random() * 16 | 0;

          if (k == 8 || k == 12 || k == 16 || k == 20) {
              uuidValue += "-"
          }
          uuidValue += (k == 12 ? 4 : (k == 16 ? (randomValue & 3 | 8) : randomValue)).toString(16);
        }
        return uuidValue;
      },
    },

    created() {
      if (localStorage.getItem('user_id') === null) {
        localStorage.setItem('user_id', this.uuid());
      }
      this.userID = localStorage.getItem('user_id');
      this.playerName = 'Player_' + this.userID.slice(0, 8);
      this.client = new Client(
        createUser(this.userID, this.playerName)
      );
    },

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

.rooms-list {
  max-height: 500px;
  margin-bottom: 10px;
  overflow-y:scroll;
  -webkit-overflow-scrolling: touch;
}

</style>
