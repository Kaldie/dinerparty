<template>
  <div class="content" id=dinner-information>
    <h4 id=diner-info> Diner Information </h4>
    <input v-model="party.name" id=diner_name type="text" class="form-control" placeholder="Diner name" :disabled="formDisabled"/>
    <input v-model="party.seats" id=diner_number_of_seats type="number" class="form-control" placeholder=2 :disabled="formDisabled"/>

    <div class="input-group sm" id=date-picker-input>
      <input :id="'datetimepicker-' + party.id" type="text" class="form-control" placeholder="Date" :disabled="formDisabled"/>
      <b-input-group-append>
        <button class="input-group-text" id="basic-addon2" v-on:click="showDateTime">
          <font-awesome-icon icon="calendar"/>
        </button>
      </b-input-group-append>
    </div>   

    <textarea v-model="party.description" class="form-control" id="diner_description-text-area" rows="1" placeholder="Description of the diner" :disabled="formDisabled"/>

    <div class="input-group form-check" id=teach-check-input v-bind:class="{'disabled-check-form-box':formDisabled}" :disabled="formDisabled">
      <div id=inner-checkbox-group>
        <input v-model="party.teaching" type="checkbox" class=form-check-input id="has-guidance" aria-label="Checkbox" :disabled="formDisabled" >
        <label class="form-check-label" for="has-guidance">Will teach</label>
      </div>
    </div>

    <div v-if="showButton">
        <button v-if="cancelShowButton" type="button" v-on:click="formCancel" class="btn btn-danger float-left" >{{cancelText}}</button>
        <button v-if="submitShowButton" type="submit" class="btn btn-primary float-right">{{submitText}}</button>
    </div>
  </div>
</template>


<script> 
  export default {
  name:"PartyContent",
  props: {
    "initialParty" : Object,
    'showButton': {type:Boolean, default:false},

    'cancelText': {type:String, default:"Reset"},
    'cancelShowButton':{type:Boolean, default:true},
    'onClickCancel': {type: Function},

    'submitText': {type:String, default:"Submit"},
    'submitShowButton':{type:Boolean, default:true},
    
    'formDisabled': {type:Boolean, default: true}
  },
  data() {
      console.warn("this.initialParty", this.initialParty)
      return {
          party: this.initialParty
      }
  },
  mounted: function() {
    $(`#datetimepicker-${this.party.id}`).datetimepicker({
      value:this.party.date
    });
  },
  methods: {
    showDateTime: function() {
        console.warn("here")
      $(`#datetimepicker-${this.party.id}`).datetimepicker('show');
    },
    requestInvite: (event) => {
      event.preventDefault()
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
        $(`#datetimepicker-${this.party.id}`).datetimepicker('reset')
    },
    formCancel() {
        if( this.onClickCancel ) {
            this.onClickCancel()
        } else {
            this.resetForm()
        }    
    },
  },
  computed: {
    description: function() {
      return`cousin: ${this.party.cousin} \n${this.party.description}`
    }
  }
}
</script>


<style scoped>

#diner-info {
    text-align: left;
}

input[id^="datetimepicker"] {
    margin-top: 0px;
}

.disabled-check-form-box {
    background-color: #efe9ea !important;
}


.form-check-input:disabled ~ .form-check-label {
    color: #495057;
}

#teach-check-input {
    background-color:white;
    border: 1px solid #ced4da;
    border-radius: 0.25rem;
    height: calc(1.5em + 0.75rem + 2px);
    margin-top: 0.25em;
    margin-bottom: 0.25em;
    padding-top: 0.375rem;
    padding-bottom: 0.375rem; 
    color:rgb(73, 80, 87);
    text-shadow: none;
}

#inner-checkbox-group {
    margin-left: 0.6em;
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