<template>
    <!--Create a slide with an image if it is available-->
    <b-carousel-slide v-if=party.image :img-src=imageSrc()>
      <PartyContent v-bind:party="party"/>
    </b-carousel-slide>

    <!--fall back if it has not-->
    <b-carousel-slide v-else img-blank img-alt="Blank image" >
      <PartyContent v-bind:party="party"/>
    </b-carousel-slide>
</template>

<style>
input.input-party-name {
  text-align: center;
}
</style>

<script>

import '@/../imported-lib/lala/jquery.datetimepicker.full.js'
import '@/../imported-lib/lala/jquery.datetimepicker.min.css'
import icons from 'glyphicons'
import PartyContent from './PartyContent'
export default {
  name:"Party",
  components: {
    PartyContent
  },
  props: {
    "party" : Object
  },
  methods: {
    imageSrc: function() {
      return this.party.image
    } 
  }
}
</script>