<template>
  <div id="app">
    <div id="nav">
      <router-link to="/" :disabled="true" :event="''">Menu</router-link> |
      <router-link to="/chess" :disabled="true" :event="''">Chess</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

#nav {
    padding: 30px;
    background-color: #282520;
    margin-bottom: 10px;
}

#nav a {
    font-weight: bold;
    color: #2c3e50;
}

#nav a.router-link-exact-active {
    color: #42b983;
}

</style>
