<template>
    <div role="tablist">
        <div role="tablist">
            <PartyItem v-for="party in parties" v-bind:party="party" v-bind:key="party.id"></PartyItem>
        </div>
    </div>
</template>


<script>
import PartyItem from './PartyItem'
export default {
    components: {
        PartyItem
    },
    props: {
        parties: Array[Object]
    }
}
</script>
