<template>
    <b-card no-body class="mb-1">
        <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button block href="#" v-b-toggle="'party-' + party.id" variant="info">{{party.name}} </b-button>
        </b-card-header>
        <b-collapse :id="'party-' + party.id" visible accordion="my-accordion" role="tabpanel">
        <b-card-body>
            <PartyContent v-bind:initialParty="party" v-bind="partyContent"></PartyContent>
        </b-card-body>
        </b-collapse>
    </b-card>
</template>

<script>
import PartyContent from '../party_carousel/PartyContent'
export default {
    name:"PartyItem",
    components: {
        PartyContent
    },
    props: {
        "party":Object
    },
    data() {
    return {
      partyContent : {
        showButton:true,
        cancelShowButton:false,
        submitText:"Update",
        formDisabled:false,
        onClickCancel: () => {
          console.log("declineing the party")
        }
      }
    }
  },
}
</script>

