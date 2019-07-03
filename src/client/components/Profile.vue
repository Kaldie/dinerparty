<template name="Profile">
<div>
    <PasswordModal></PasswordModal>

    <div class="container column">
        <h1 id=header >{{header}}</h1>
        <User v-bind:showPassword="false" v-bind:showEmail="true" v-bind:showLocation="true"></User>
        
        <div class="container column" id="button_container">
            <router-link to="/" class="btn">Cancel</router-link> 
            <a class="btn" href="#open-modal" v-show="!showPassword">Reset Password</a>
            <a class="btn" @click="handleSubmit" :enabled="status.loggedIn">{{submitButtonText}}</a> 
        </div>
    </div>
    <h2>Hosted Diners</h2>
    
    <PartyList v-bind:parties=parties></PartyList> 
</div>
</template>


<script>

import {mapState, mapActions} from 'vuex'
import PasswordModal from './PasswordModal';
import User from './User'
import PartyList from './parties/party_list/PartyList'
import { PartyService } from '@/client/service/party'

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
            isModalVisible: false,
            parties: []
        }
    },
    computed: {
        ...mapState('account', ['status', 'user'])
    },
    mounted() {
        if (this.status.loggedIn && this.user) {
            this.get(this.user.username)
        }
        PartyService.getHostedParties().then((result) => {
                this.parties = result.data || [] 
            })
    },
    methods: {
        ...mapActions('account', ['get']),
        handleSubmit() {
            this.submitted = true
            this.$validator.validate().then(valid => {
                if (valid) {
                    this.$store.dispatch(this.dispatchMethod, this.user).then(() => {
                        this.get(this.user.username)
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
        }
    }
}
</script>

<style lang=scss scoped>
#button_container {
    display: flex;
    flex-direction: row;
    justify-content: center;
}
</style>
