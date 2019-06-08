<template>
  <div>
    <div class=container>
      <div class=row>
        <div class=col-sm>
            <b-carousel id="carousel2"
                style="text-shadow: 1px 1px 2px #333;"
                fade
                background="#ababab"
                :interval="10000"
                indicators
                controls>
              <Party v-for="party in foundParties" :key="party.id" v-bind:party="party" />

            </b-carousel>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import getCurrentPositionPromise from '@/client/utilities/GeoUtilties.js'
import Party from './Party'
import {mapState, mapActions} from 'vuex'
import { setTimeout } from 'timers';

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
            console.warn("fo und ", this.foundParties)
        })
  },
  methods: {
    ...mapActions('party',['findParties']),
    suitableParties: function() {
      if ( !this.refresh && this.position && this.position.coords) {
        1+1
      } else {
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