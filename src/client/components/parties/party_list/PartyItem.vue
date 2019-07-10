<template>
<Collapsable v-bind:header="party.name">
    <PartyContent v-bind:initialParty="party" v-bind="partyContent"></PartyContent>
</Collapsable>

</template>

<script>
import PartyContent from '../party_carousel/PartyContent'
import Collapsable from '../../native_components/Collapsable'
import { PartyService } from '@/client/service/party';
export default {
    name:"PartyItem",
    components: {
        PartyContent,
        Collapsable
    },
    props: {
        "party":Object
    },
    data() {
      return {
        partyContent : {
          showButton:true,
          cancelShowButton:false,
          inventationShowButton:true,
          submitText:"Update",
          formDisabled:false,
          onClickCancel: () => {
            // TODO: fix it
          },
          onClickSubmit: (party) => {
            PartyService.updateParty(party)

          }
        }
      }
    },
    methods: {
      handleSubmit: function() {
        PartyService.updateParty(this.party)
      }
  },
}
</script>

