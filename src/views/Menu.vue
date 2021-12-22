<template>
  <div class="menu">

  <b-container>

    <b-row class="justify-content-md-center">

      <b-col col lg="6">
        <b-list-group class="menu-list">

            <router-link to="/chess" class="router-link-exact-active">
              <b-list-group-item class="menu-list__item">
                Создать игру
              </b-list-group-item>
            </router-link>

            <router-link to="/">
              <b-list-group-item class="menu-list__item">
                Найти игру
              </b-list-group-item>
            </router-link>

        </b-list-group>
      </b-col>

      <b-col col lg="3">
        <b-list-group class="players-list">
          <router-link to="/" v-for="(playerName, index) in playersList" :key="index">
            <b-list-group-item class="players-list__item">
              {{ playerName }}
            </b-list-group-item>
          </router-link>
        </b-list-group>
      </b-col>

    </b-row>

  </b-container>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        playersList: [
          'Player1',
          'Player2',
          'Player3',
          'Player4',
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

.players-list__item {
  background-color: #312e2b;
  color: #bababa;
  font-weight: bold;
}

</style>
