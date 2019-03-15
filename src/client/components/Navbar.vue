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

        <!-- <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form> -->

        <!-- <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown> -->

        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content">
            <em>User</em>
          </template>
          <b-dropdown-item to="/profile">Profile</b-dropdown-item>
          <b-dropdown-item to="/">Sign out</b-dropdown-item>
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