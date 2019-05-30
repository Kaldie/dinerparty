<template>
  <div name=Host>
    <h1>
    Host your own Diner Party
    </h1>
    <div class="container-fluid">
        <div class="row">
            <!-- <div class="col-sm">
                <img id=left-food-image class=column-food-image src="../assets/food_images/food.png">
            
                <div class="content" id=user-information>
                <h4> User information </h4>

                <div class="input-group">
                <input id=user_name type="text" class="form-control control-pair-left" placeholder="User name"/>
                <input id=email type="text" class="form-control control-pair-right" placeholder="Email"/>
                </div>

                <div class="input-group">
                <input id=street_name type="text" class="form-control control-pair-left" placeholder="Street name"/>
                <input id=street_number type="number" class="form-control control-pair-right" placeholder="Street number"/>
                </div>

                <input id=postal_code type="text" class="form-control control-pair" placeholder="Postal code"/>
                <input id=city_name type="text" class="form-control control-pair" placeholder="City"/>
                </div>
            </div> -->

            <div class="col-sm">
                <img id=right-food-image class=column-food-image src="../assets/food_images/food2.png"> 

                <div class="content" id=dinner-information>
                    <h4 id=user-information-card-title> Diner Information </h4>
                    <input id=diner_name type="text" class="form-control" placeholder="Diner name"/>
                    <input id=diner_number_of_seats type="number" class="form-control" placeholder=2 />

                    <div class="input-group sm">
                        <input id=datetimepicker type="text" class="form-control" placeholder="Date"/>
                        <b-input-group-append>
                            <button class="input-group-text" id="basic-addon2" v-on:click="showDateTime">
                                <font-awesome-icon icon="calendar"/>
                            </button>
                        </b-input-group-append>
                    </div>   

                    <textarea class="form-control" id="diner_description-text-area" rows="1" placeholder="Description of the diner"/>




                    <div class="pull-left">
                        <input type="checkbox" class=form-check-input id="has-guidance" aria-label="Checkbox">
                        <label class="form-check-label" for="has-guidance">Will teach</label>
                    </div>
                </div>
            </div>

        </div>
    </div> 
</div>
</template>

<script>
import '@/../imported-lib/lala/jquery.datetimepicker.full.js'
import '@/../imported-lib/lala/jquery.datetimepicker.min.css'
import icons from 'glyphicons'
export default {
    name:"Host",
    methods: {
        showDateTime: function() {
            $('#datetimepicker').datetimepicker('show');
        }
    },
    mounted: function() {
        $(`#datetimepicker`).datetimepicker({
            value: Date.now,
            theme:"light",
        });
    },
}
</script>


<style scoped>

.content {
    position: absolute; /* Position the background text */
    top: 25%; /* At the bottom. Use top:0 to append it to the top */
    left: 12.5%;
    background: rgb(255, 255, 255); /* Fallback color */
    background: rgba(255, 255, 255, 0.65) !important; /* Black background with 0.5 opacity */
    color: #000000; /* Grey text */
    width: 75%; /* Full width */
    padding: 20px; /* Some padding */
}

.column-food-image {
  width: 100%;
  height: 100%;
}

.form-row {
  margin-top:0.5em;
  margin-bottom:0.25em;
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

