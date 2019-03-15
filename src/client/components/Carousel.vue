<template>
  <div class="Home">
    <b-carousel id="carousel1"
                style="text-shadow: 1px 1px 2px #333;"
                fade
                background="#ababab"
    >
      <!-- Slides with custom text -->
      <b-carousel-slide img-src="https://picsum.photos/512/240/?random">
        <h1>{{msg.title}}</h1>
        <h2>{{msg.msg}}</h2>
      </b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
export default {
  name: 'Carousel',
  props: ["msg"]
}
</script>


<style lang="less">
  .Home .carousel-caption {
    bottom:50%; 
    h1 {
      font-size:150px;
    }
    h2 {
      font-size:75px;
    }
  }
</style>