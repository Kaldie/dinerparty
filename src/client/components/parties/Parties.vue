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
              <Party v-for="party in parties" :key="party.id" v-bind:party="party" />
            </b-carousel>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import getCurrentPositionPromise from '@/client/utilities/GeoUtilties.js'
import axios from 'axios'
import Party from './Party'
import Settings from '@/client/settings.js'

export default {
  name: 'Find',
  props: {
    start_position: Object,
    refresh: Boolean(false),
    partyFilter: Object,
  },
  data: function() {
    return {
      parties: []
    }
  },
  components: {
    Party
  },
  mounted: function() {
    this.suitableParties()
  },
  methods: {
    suitableParties: function() {
      if ( !this.refresh && this.position && this.position.coords) {

      } else {
        getCurrentPositionPromise().then( (position) => {
          let config = {
            headers: {
              "Access-Control-Allow-Origin": "127.0.0.1:5000",
            },
            params: {
              lat : position.coords.latitude,
              lon : position.coords.longitude,
          }}
          axios.get(`http://${Settings.server}:${Settings.port}/parties`, config)
          .catch((error) => {
            console.warn(error)
          }).then((response) => {
            this.parties = response.data
            return response.data
          })
        })
      }
    }
  },
  computed: {

  }
}
</script>
