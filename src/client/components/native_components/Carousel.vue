<template>
  <!-- Slideshow container -->
  
    <div class="slideshow-container">
      <transition name="fade">
        <img id=image :src="imgSource" :key="imgSource">
      </transition>
        <div id="previous" @click='prev()'><span>&#60;&#60;</span></div>
        <div id="next" @click='next()'><span>&#62;&#62;</span></div>
      <transition name="fade">
        <div id=text :key="text">{{text}} </div>
      </transition>
      <div id=slide_control>
        <div class=dot v-for='n in numberOfSlides' :key=n></div>
      </div>
    </div>

</template>


<style lang="scss" scoped>
$padding:0.2em;

@mixin item {
  align-self: center;
  background:rgba(255, 255, 255, 0.336);
  transition: all 0.3s;
  padding:$padding;
  &:hover {
      background-color: rgba(255, 255, 255,1)
  }

}

.fade-enter {
      opacity: 0;
  }
  .fade-enter-active {
      transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }
  .fade-leave-active, .welcome-leave-to {
      opacity: 0;
  }

/* Slideshow container */
.slideshow-container {
  display:grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 25vh 25vh;

  grid-template-areas: 
  "1-1  2-1"
  "1-2  2-2"
  "3-3  3-3";

  img {
    grid-area: 1/1/3/3;
    z-index: -1;
    width: 100%;
    height: 100%;
    display: block;
    object-fit: cover;
    
  }

  #previous {
    grid-area: 1/1/3/1;
    justify-self: left;
    font-size:40px;
    padding:$padding;
    border-radius: 0px 10px 10px 0px;
    @include item();
  }

  #text {
    grid-area: 2/1/3/3;
    margin:3%;
    color:black;
    @include item();
    background:rgba(255, 255, 255, 0.75);
  }

  #next {
    grid-area: 1/2/3/3;
    background:rgba(255, 255, 255, 0.336);
    justify-self: right;
    
    font-size:40px;
    border-radius: 10px 0px 0px 10px;
    @include item();
  }
  #slide_control {
    grid-area: 2/1/3/3;
    align-self: flex-end;
    font-size:30px;
    display:flex;
    justify-content: center;
    .dot {
      @include item();
      height: 15px;
      width: 15px;
      border-radius: 50%;
      margin:5px;
      background:rgba(255, 255, 255, 0.60)
    } 
  }
}
</style>

<script>
import CarouselSlide from "./CarouselSlide"
import Inventations from '@/client/components/parties/Inventations.vue';
export default {
  name:"Carousel",
  components: {},
  props: {
    slides: {type: Array[Object], default: () => 
      [
        {
        text:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, dolorem cumque ullam repellat labore aliquid error, quam necessitatibus et magni ea voluptatum nostrum veritatis porro modi id. Sed vel mollitia necessitatibus minima iste suscipit repudiandae officiis autem similique aliquid. Labore tempore esse molestiae quidem neque. Iure fuga nisi perspiciatis dolor quibusdam ut odio molestias cumque, eveniet neque aut nobis veritatis. Ab sed voluptatum odit assumenda omnis nobis modi vel ipsum in! Asperiores nemo, voluptatum odit tempore ad corrupti in reprehenderit et esse iure accusamus recusandae delectus sit porro blanditiis eligendi voluptatibus dolorum quod odio facilis. Magnam numquam doloribus exercitationem voluptas?",
        imgSource: "food2.png"
        }, {
        text:"Much shorter!!!",
        imgSource: "food.png"
        }
      ]
  }},
  data() {
    return {
      slideIndex: 0 
    }
  },
  computed: {
    numberOfSlides() {
      if ( this.slides ) {
        return this.slides.length
      }
      return 0
    },
    text() {
      if ( this.slides ) {
        if (this.slides.length > this.slideIndex) {
          return this.slides[this.slideIndex].text
        }
      }
      return ""
    },
    imgSource() {
      if ( this.slides ) {
        if (this.slides.length > this.slideIndex && this.slideIndex >= 0) {
          console.warn("here!")
          console.warn("require('../../assets/food_images/' + this.slides[this.slideIndex].imgSource)", require('../../assets/food_images/' + this.slides[this.slideIndex].imgSource))
          return require('../../assets/food_images/' + this.slides[this.slideIndex].imgSource)
        }
      }
    }
  },
  methods: {
    next() {
      this.slideIndex += 1
      if (this.slideIndex >= this.slides.length) {
        this.slideIndex = 0
      }
    },
    prev() {
      this.slideIndex -= 1
      if (this.slideIndex < 0 ) {
        this.slideIndex = this.slides.length - 1
      }
    }
  }
}
</script>



