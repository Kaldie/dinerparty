<template>
  <div id="app">
    <div class=nav-container>
      <NavBar/>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './Navbar'
import 'vue-router'
export default {
  name: 'app',
  components: {
    NavBar
  }
}
</script>

<style lang="scss">
body {
  background-color:green;
  margin:0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.container {
    display:flex;
    margin-top : 0.1em;
    margin-bottom: 0.1em;
}

.column {
    flex-direction: column;
    justify-content: space-around
}

a.btn {
  padding: 0.15em;
  border-radius: 3px;
  text-decoration: none;
  color: rgb(0, 0, 0);
  margin:0.5em;
  cursor: pointer;
  i {
    padding-right: 0.3em;
  }
  &:hover {
    color:rgb(48, 1, 255);
  }
}
</style>
