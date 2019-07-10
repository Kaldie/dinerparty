<template>

<Modal :header="'lalal'" :id="'inventations-modal'">
    <div class="d-flex justify-content-center">
        <div class="flex-column justify-content-between"> 
            <div>Host:</div>
            <div>Client:</div>
        </div>

        <div class="container column">
            <div class="d-flex">
                    <a @click="host=1" id="host-accept">Accepts</a>  
                    <a @click="host=2" id="host-declines">Declines</a>  
            </div>

            <div class="d-flex">
                <a :variant="clientAccepedVariant()" @click="client=1">Accepts</a>  
                <a :variant="clientDeclinesVariant()" @click="client=2">Declines</a>  
            </div>

        </div>
        <a class=btn href="#">Cancel</a>
    </div>
</Modal>    
</template>

<style scoped>

.no-bullets {
    list-style-type: none;
}
</style>


<script>

import Modal from '../native_components/Modal'
import Inventations from '@/client/components/parties/Inventations.vue';

export default {

    name:'Inventations',
    components: {Modal},
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
