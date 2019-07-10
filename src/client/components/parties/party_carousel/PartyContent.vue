<template>
<div class="container">
  <div class="container column" id=dinner-information>
    
    <h4 id=diner-info> Diner Information </h4>
    
    <input v-model="party.name" type="text"  placeholder="Diner name" :disabled="formDisabled"/>
    <input v-model="party.seats" type="number" placeholder="Number available seats" :disabled="formDisabled"/>


    <div class="" id=date-picker-input>
      <input ref="datetimepicker" type="text" placeholder="Date" :disabled="formDisabled"/>
        <button class="input-group-text" v-on:click="showDateTime" :disabled="formDisabled">
          <font-awesome-icon icon="calendar"/>
        </button>
    </div>   

    <textarea v-model="party.description" rows="1" placeholder="Description of the diner" :disabled="formDisabled"/>

      <div class=container id='teach-button-container'>
        <label class="form-check-label" for="has-guidance">Will teach</label>
        <input v-model="party.teaching" type="checkbox" class=form-check-input id="has-guidance" aria-label="Checkbox" :disabled="formDisabled" >
      </div>  

    <div v-if="showButton">
      <a v-if="cancelShowButton" type="button" v-on:click="formCancel" class="btn btn-danger float-left" >{{cancelText}}</a>
      <a class="btn" href="#inventations-modal" v-show="inventationShowButton">Invitations</a>
      <!-- <a v-if="inventationShowButton" type="button" v-on:click="$bvModal.show('inventations-' + party.id)" class="btn">Invitations</a> -->
      <a v-if="submitShowButton" type="button" v-on:click="formSubmit" class="btn ">{{submitText}}</a>
    </div>

    <Inventations v-bind:party="party"></Inventations>


  </div>
</div>
</template>


<script> 
  import Inventations from '@/client/components/parties/Inventations.vue'
  export default {
  name:"PartyContent",
  components: {
    Inventations
    },
  props: {
    "initialParty" : Object,
    'showButton': {type:Boolean, default:false},
    "inventationShowButton": {type:Boolean, default: false},

    'cancelText': {type:String, default:"Reset"},
    'cancelShowButton':{type:Boolean, default:true},
    'onClickCancel': {type: Function},
    'onClickSubmit': {type: Function},

    'submitText': {type:String, default:"Submit"},
    'submitShowButton':{type:Boolean, default:true},
    
    'formDisabled': {type:Boolean, default: true},
    'resolveSeats': {type:Boolean, default:false}
  },
  data() {
      return {
          party: this.initialParty
      }
  },
  mounted: function() {
    console.warn("this", this)
    console.warn("$(this.$refs.datetimepicker)", $(this.$refs.datetimepicker))
    console.warn("this.$refs.datetimepicker", this.$refs.datetimepicker)
    
    $(this.$refs.datetimepicker).datetimepicker({
      value:this.party.date
    });
  },
  methods: {
    showDateTime: function() {
      $(this.$refs.datetimepicker).datetimepicker('show');
    },
    resetForm() {
        this.party = {
            name : '',
            description : '',
            seats : undefined,
            teaching : false,
            cousin : undefined,
            image : undefined,
            date: ""
            }
        $(this.$refs.datetimepicker).datetimepicker('reset')
    },
    formCancel() {
        if( this.onClickCancel ) {
            this.onClickCancel()
        } else {
            this.resetForm()
        }    
    },
    formSubmit() {
      this.party.date = $(this.$refs.datetimepicker).datetimepicker('getValue');
      if (this.onClickSubmit) {
          this.onClickSubmit(this.party)
      }
    }
  },
  computed: {
    description: function() {
      return`cousin: ${this.party.cousin} \n${this.party.description}`
    }
  }
}
</script>


<style scoped lang="less">
.container {
  justify-content: center;
}

#teach-button-container {
  justify-content: space-between;
  align-items: flex-start;
  background-color: white;
  margin:0%;

    border-width: 0.5px;
    border-style: inset;
    border-top-style: inset;
    border-right-style: inset;
    border-bottom-style: inset;
    border-left-style: inset;
    border-color: initial;
    border-image: initial;
  label {
    margin-left: 0.1em;
  }
}

h4 {
  margin:0px;
}
</style>