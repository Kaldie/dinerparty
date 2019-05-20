<template>
  <div class=container>
        
    <div class=row id=map-row>
      <div class=col-sm>
        <h1>hi</h1>
      <div id="map"></div>
      </div>
    </div>

    <div class=row>
      <div class="col-sm" id="map-container">
        <h1>hey</h1>
      </div>
    </div> 

    <div class=row>
      <div class="col-sm">
        <h1>hey</h1>
      </div>
    </div> 
  </div>
</template>

<script>
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';

export default {
  name:"Map",
  props: {
    "position" : Object
  },
  date: function() {
    return {
      position : {
        latitude: 40,
        longitudinal: 40
      }
    }
  },
  mounted() {
    console.warn("here!!", this.props)
    mapboxgl.accessToken = 'pk.eyJ1Ijoia2FsZGllIiwiYSI6ImNqcTd5YTA2dDAxNjY0OXBqdTZ2Y2JvMjgifQ.SaROSQWHudNg3OtKu2Nz3A';
    const map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/dark-v9',
      center: [this.position.latitude, this.position.longitudinal],
      zoom: 5.0,
      trackResize: true
    });
  }
}
</script>

<style>

.mapboxgl-canvas {
  left: 0;
}
#map {
  /* left:22%; */
  height: 100%;
  width: 50%;
  position: absolute;
  z-index: 2;
  text-align: justify
}
#map-row {
  height: 400px;
  width: 100%;
  position: absolute;
  z-index: 2;
  text-align: justify
}
</style>