<template name="Profile">
<div>
    <PasswordModal v-show="isModalVisible" @close="closeModal"></PasswordModal>

    <div class="container">
        <div class="row">
            <div class="col-sm-10"> 
             <h1 id=header >{{header}}</h1>
            </div>
        </div>       
        
        <div class="row">
            <div class="col-sm-10"> 
                <form @submit.prevent="handleSubmit">
                    <User v-bind:showPassword="false" v-bind:showEmail="true" v-bind:showLocation="true"></User>
                    
                    <div class="container-fluid" id=button_container>
                        <div class="col-sm-2 float-left" id=cancel_button_container >
                            <router-link to="/" class="btn btn-danger form-group-button ">Cancel</router-link> 
                        </div>

                        <div class="float-right" >
                            <div class="form-group form-group-button">
                                <button v-show="!showPassword" class="btn btn-primary control-pair-left" type=button v-b-modal="'password-modal'">reset password</button>
                                <button class="btn btn-primary" type=submit :enabled="status.loggedIn">{{submitButtonText}}</button> 
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div> 


        <div class="row">
            <div class="col-sm-10"> 
                <h1>Hosted Diners</h1>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-10"> 
            <PartyList v-bind:parties='parties()'></PartyList> 
            </div>
        </div>
    </div>
</div>
</template>


<script>

import {mapState, mapActions} from 'vuex'
import PasswordModal from './PasswordModal';
import User from './User'
import PartyList from './parties/party_list/PartyList'

export default {
    name:"Profile",
    components: { 
        PasswordModal, 
        User,
        PartyList
        },
    props: {
        'header': {
            type: String, 
            default: "Profile"
        },
        "submitButtonText": {
            type: String,
            default: "Update"
        },
        "dispatchMethod": {
            type: String,
            default: 'account/update'
        },
        'showPassword': {
            type: Boolean,
            default: false,
        }
    },
    data() {
        return {
            submitted : false,
            isModalVisible: false
        }
    },
    computed: {
        ...mapState('account', ['status', 'user'])
    },
    mounted () {
        if (this.status.loggedIn) {
            this.get()
        }
    },
    methods: {
        ...mapActions('account', ['get']),
        handleSubmit() {
            this.submitted = true
            this.$validator.validate().then(valid => {
                if (valid) {
                    this.$store.dispatch(this.dispatchMethod, this.user).then(() => {
                        this.get()
                    })
                    
                }
            })
        },
        resetPassword() {
            this.isModalVisible = true;
        },
        showModal() {
            this.isModalVisible = true;
        },
        closeModal() {
            this.isModalVisible = false;
        },
        parties() {
            return [{name:"alal", id:1}, {name:"bala", id:2}]
        }
    }
}
</script>

<style>
.container {
    position: absolute;
    top: 25%;
}

.col-form-label{
    text-align: right;
}

#button_container {
    padding-left: 0%;
    padding-right: 0%
}

#cancel_button_container {
    padding-left: 2.5em
}

.control-pair-left {
    margin-right: 0.5em;
}
.control-pair-right {
    margin-left: 0.5em
}
.control-pair-middle {
    margin-left: 0.5em;
    margin-right: 0.5em;
}

.form-group-button {
    margin-top:1em;
}
</style>
