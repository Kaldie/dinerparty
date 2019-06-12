<template>
    <!--Create a slide with an image if it is available-->
    <!-- <b-carousel-slide v-if=party.image :img-src=imageSrc()>
      <PartyContent v-bind:party="party"/>
    </b-carousel-slide> -->

    <!--fall back if it has not-->
    <b-carousel-slide  img-blank img-alt="Blank image" >
      <form @submit.prevent="handleSubmit">
      <PartyContent  v-bind:initialParty="party" v-bind="partyContent"/>
      </form>
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
import PartyContent from './PartyContent'
export default {
  name:"Party",
  data() {
    return {
      partyContent : {
        disabled:true,
        showButton:true,
        cancelShowButton:true,
        submitText:"Request Invite",
        cancelText: "Decline",
        onClickCancel: () => {
          console.log("declineing the party")
        }
      }
    }
  },
  components: {
    PartyContent
  },
  props: {
    "party" : Object
  },
  methods: {
    imageSrc: function() {
      return this.party.image
    },
    handleSubmit: () => {
      console.warn("handle submit!")
    } 
  }
}
</script>