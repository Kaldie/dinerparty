<template>
<div class=nav-container>
  <b-navbar toggleable="md" type="dark" variant="info">

    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand to="/">Diner Party</b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav>
        <b-nav-item to="/find">Find</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav>
        <b-nav-item to="/host">Host</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav>
        <b-nav-item to="/profile">Profile</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content">
            <em>User</em>
          </template>
          <b-dropdown-item v-show="notLogged()" to="/login">Sign in</b-dropdown-item>
          <b-dropdown-item v-show="status.loggedIn" to="/profile">Profile</b-dropdown-item>
          <b-dropdown-item v-show="status.loggedIn" v-on:click="logout" to="/">Sign out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<style scoped>
nav {
  background-color: #304051 !important;
}
.dropdown-item, .dropdown-item a, .dropdown-item.active {
  color: black !important;
  background-color:white;
  outline: none;
}
</style>

<script>
import {mapState, mapActions} from 'vuex'

export default {
  methods: {
    ...mapActions('account', ['logout']),
    notLogged() {
      return this.status.loggedIn ? !this.status.loggedIn: true 
    }
  },
  computed: {
    ...mapState('account', ['status'])
  },
} 
</script>
