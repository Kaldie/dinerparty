<template>
  <nav>  
    <ul class="container" >  
      <li>
        <router-link to="/">
          <font-awesome-icon icon="home"/>
          Home
        </router-link>
      </li>

      <li>
        <router-link to="/notifications">
          <font-awesome-icon icon="bell"/>
          Notifications
        </router-link>
      </li>

      <li id=parties>
        <router-link to="/find">
          <font-awesome-icon icon="utensils"/>
          Parties
        </router-link>
      </li>

      <li>
        <router-link to="/profile">
          <font-awesome-icon icon="id-badge"/>
          Profile
        </router-link>
      </li>

      <li>
        <router-link to="/login">
          <font-awesome-icon icon="sign-in-alt"/>
          Login
        </router-link>
      </li>

    </ul>  
  </nav>
</template>

<style scoped>

ul {
  padding: 0;
  margin: 0;
  list-style: none;
  background-color: black;
}

a {
  color:aliceblue;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container > li {  
 margin:1mm;  
}

.container > li:hover {
  background-color:darkslategrey;
}

.container {  
  display: flex;  
  justify-content: space-between
}

#parties {
  margin-left: auto;
  margin-right: auto
}

svg {
  margin-right: 1mm;
}
</style>