<template>
  <div>

    <Carousel v-bind:msg='{title:"Diner Party", msg:"Making hosting fun."}'/>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm">
          <h1>Locate diner party!</h1>
        </div>
        <div class="col-sm">
          <h1>Host a diner party!</h1>
          <br>
          <ul class="list-group">
            <li class="list-group-item">Meet people</li>
            <li class="list-group-item">Learn new skills</li>
            <li class="list-group-item">Share recepies</li>
          </ul>
        </div>
        <div class="col-sm">
          <h1>Join a party</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Carousel from './native_components/Carousel'
export default {
  name: 'Home',
  components: {
    Carousel
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.list-group-item {
  border-width: 0px;
  font-size: 30px;
}

</style>
