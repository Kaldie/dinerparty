<template>
<div>
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm">
                <img id=right-food-image class=column-food-image src="../../../assets/food_images/food2.png"> 
                <div class=content>

                    <b-carousel id="carousel2"
                        style="text-shadow: 1px 1px 2px #333;"
                        fade
                        :interval="10000"
                        indicators
                        img-width="6"
                        img-height="3"
                        controls>

                    <Party v-for="party in foundParties" :key="party.id" v-bind:party="party" />
                    
                    </b-carousel>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import getCurrentPositionPromise from '@/client/utilities/GeoUtilties.js'
import Party from './Party'
import {mapState, mapActions} from 'vuex'

export default {
  name: 'Find',
  props: {
    start_position: Object,
    refresh: Boolean(false),
    partyFilter: Object,
  },
  computed: {
    ...mapState("party",["status", "foundParties"])
  },
  components: {
    Party
  },
  mounted: function() {
    getCurrentPositionPromise().then( (position) => {
            const currentLocation = {
              lat : position.coords.latitude,
              long : position.coords.longitude
            }
            const range = 10000
            this.findParties({currentLocation, range})
        })
  },
  methods: {
    ...mapActions('party',['findParties']),
    suitableParties: function() {
      if ( this.refresh && this.position && this.position.coords) {
        getCurrentPositionPromise().then( (position) => {
          const currentLocation = {
            lat : position.coords.latitude,
            long : position.coords.longitude
          }
          const range = 10000
          this.findParties({currentLocation, range})
        }) 
      }
    }
  }
}
</script>

<style scoped>

.content {
    position: absolute; /* Position the background text */
    top: 2.5%; /* At the bottom. Use top:0 to append it to the top */
    left: 12.5%;
    background: rgb(255, 255, 255); /* Fallback color */
    background: hsla(0, 81%, 13%, 0.65) !important; /* Black background with 0.5 opacity */
    color: #000000; /* Grey text */
    width: 75%; /* Full width */
    padding: 20px; /* Some padding */
}

.column-food-image {
  width: 100%;
  height: 100%;
}

input {
  margin-top:0.25em;
  margin-bottom: 0.25em;
}

textarea {
  margin-top:0.25em;
  margin-bottom: 0.25em;
}

.control-pair-left {
  margin-right: 0.5em;
}

.control-pair-right {
  margin-left: 0.5em;
}

#datetimepicker {
    margin-top:0px
}

</style>