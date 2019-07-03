<template>
<b-modal :id="'inventations-' + party.id" :title="'Inventations of ' + party.name">
    <div class="d-flex justify-content-center">
        <div class="flex-column justify-content-between"> 
            <div>Host:</div>
            <div>Client:</div>
        </div>

        <div class="flex-column">
            <div class="d-flex">
                    <b-button :variant="hostAccepedVariant()" @click="host=1" id="host-accept">Accepts</b-button>  
                    <b-button :variant="hostDeclinesVariant()" @click="host=2" id="host-declines">Declines</b-button>  
            </div>

            <div class="d-flex">
                <b-button :variant="clientAccepedVariant()" @click="client=1">Accepts</b-button>  
                <b-button :variant="clientDeclinesVariant()" @click="client=2">Declines</b-button>  
            </div>

        </div>
    </div>
</b-modal>
    
</template>

<style scoped>

.no-bullets {
    list-style-type: none;
}
</style>


<script>



export default {

    name:'Inventations',
    data() {
        return {
            inventations : [],
            lala:true,
            host:0,
            client:0
        }
    },
    props: {
        party: {type: Object}
    },
    methods: {
        hostAccepedVariant:function() {
            if (this.host===1) {
                return "success"
            }
            return "outline-success"
        },
        hostDeclinesVariant: function() {
            if (this.host===2) {
                return "danger"
            }
            return "outline-danger"
        },
                clientAccepedVariant:function() {
            if (this.client===1) {
                return "success"
            }
            return "outline-success"
        },
        clientDeclinesVariant: function() {
            if (this.client===2) {
                return "danger"
            }
            return "outline-danger"
        }
    },
}

</script>
