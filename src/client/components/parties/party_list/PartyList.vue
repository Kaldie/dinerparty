<template>
    <div role="tablist">
        <PartyItem v-for="party in parties" v-bind:party="party" v-bind:key="party.id"></PartyItem>
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
