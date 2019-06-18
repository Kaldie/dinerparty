<template>
  <div name=Host>
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm">
                <img id=right-food-image class=column-food-image src="../assets/food_images/food2.png"> 
                <form @submit.prevent="handleSubmit">
                    <PartyContent v-bind:initialParty="newParty" v-bind="partyContent"/>/>
                </form>
            </div>

        </div>
    </div> 
</div>
</template>

<style scoped>
.column-food-image {
  width: 100%;
  height: 100%;
}

#dinner-information {
    color:white;
    align-items: left;
}

.content {
    position: absolute; /* Position the background text */
    top: 25%; /* At the bottom. Use top:0 to append it to the top */
    left: 12.5%;
    background: rgba(58, 6, 6, 0.65) !important; /* Black background with 0.5 opacity */
    background: rgb(58, 6, 6); /* Fallback color */
    color: #000000; /* Grey text */
    width: 75%; /* Full width */
    padding: 20px; /* Some padding */
}

</style>


<script>
import PartyContent from './parties/party_carousel/PartyContent'

import { mapActions} from 'vuex'

export default {
    name:"Host",
    components: {
        PartyContent
    },
    data() {
        return {
            newParty :  {
                name : 'New Diner name',
                description : '',
                seats : 2,
                teaching : false,
                cousin : 'default',
                image : undefined,
                date: ""
            },
            partyContent : {
                disabled:true,
                showButton:true,
                cancelShowButton:true,
                submitText:"Register",
                formDisabled:false
                // onClickCancel: () => {console.warn("here!! cancel clicked")}
            }
        }   
    },
    methods: {
        ...mapActions('party',['registerParty']),
        handleSubmit: function() {
            this.newParty.date = $('#datetimepicker').datetimepicker('getValue');
            this.registerParty(this.newParty)
        }
    },
}
</script>