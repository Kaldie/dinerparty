<template>
  <form role="form"> 
    <div class="form-group has-feedback">
        <input class="form-control input-party-name" type=text :value=party.name />
    </div>

    <div class="form-group has-feedback">
      <div class="input-group mb-3">
        <input :id="'datetimepicker-' + party.id" type="text" class="form-control" placeholder="Date"/>
        <span class="input-group-text" id="basic-addon2" v-on:click="showDateTime">
          <font-awesome-icon icon="calendar" />
        </span>
      </div>   
    </div> 

    <div class="form-check">
      <input type="checkbox" class=form-check-input id="has-guidance" aria-label="Checkbox" :checked=party.tutorial>
      <label class="form-check-label" for="has-guidance">Will teach</label>
    </div>


    <div class="form-group">
      <div class="input-group mb-3">
      <textarea class="form-control " v-model=description id="description-text-area" rows="3"/>
      </div>
    </div>

  </form>
</template>

<style>
input[id^=datetimepicker] {
  text-align: center;
  padding-left: 40px
}
#description-text-area {
  text-align: center;
}
</style>


<script>
  export default {
  name:"PartyContent",
  props: {
    "party" : Object
  },
  mounted: function() {
    $(`#datetimepicker-${this.party.id}`).datetimepicker({
      value:this.party.date
    });
  },
  methods: {
    showDateTime: function() {
      $(`#datetimepicker-${this.party.id}`).datetimepicker('show');
    }
  },
  computed: {
    description: function() {
      return`cousin: ${this.party.cousin} \n${this.party.description}`
    }
  }
}
</script>
