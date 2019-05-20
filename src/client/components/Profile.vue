<template name="Profile">
    <div class="container">
        <div class="row">
            <div class="col-sm-2"> 
             <h1 id=header >{{header}}</h1>
            </div>
        </div>

        <form @submit.prevent="handleSubmit">
            <div class="form-group row">
                <label for=user_name class="col-sm-2 col-form-label" >User Name</label>
                <div class="col-sm-10">
                    <input id=user_name v-model="user.username" type="text" v-validate="{ required: true }" name="username" class="form-control" placeholder="required"/>
                    <div v-show="submitted && !user.username" class="invalid-feedback">Username is required</div>
                </div>
            </div>

            <div class="form-group row">
                <label for=password class="col-sm-2 col-form-label" >Password</label>
                <div class="col-sm-10">
                    <input id=password type="password" v-model="user.password" v-validate="{ required: true }" name="password" class="form-control" placeholder="required"/>
                    <div v-show="submitted && !user.password" class="invalid-feedback">Password is required</div>
                </div>
            </div>

            <div class="form-group row">
                <label for=user_name class="col-sm-2 col-form-label" >Email</label>
                <div class="col-sm-10">
                    <input id=email type="text" v-model="user.email" v-validate="{ required: true }" name="email" class="form-control" placeholder="required"/>
                    <div v-show="submitted && !user.email" class="invalid-feedback">Email is required</div>
                </div>
            </div>

            <div class="form-group row">
                <label for=user_name class="col-sm-2 col-form-label" >Location</label>
                <div class="col-sm-10">
                    <div class="input-group">
                        <input type="text" v-model="user.address" placeholder="Address" v-validate="{ required: false }" name="address" class="form-control control-pair-left" :class="{ 'is-invalid': submitted && errors.has('firstName')  }" />
                        <input type="text" placeholder='City' v-model="user.city" name="City" class="form-control control-pair-right" :class="{ 'is-invalid': submitted && errors.has('middleName')  }" />
                    </div>
                </div>
            </div>

            <div class="container-fluid" id=button_container>
                <div class="col-sm-2 float-left" id=cancel_button_container >
                    <router-link to="/" class="btn btn-danger form-group-button ">Cancel</router-link> 
                </div>

                <div class="float-right" >
                    <div class="form-group form-group-button">
                        <button class="btn btn-primary " :disabled="status.loggedIn">{{submitButtonText}}</button> 
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<style>
.container {
    position: absolute;
    top: 25%;
    left: 50%;
    -moz-transform: translateX(-50%) translateY(-25%);
    -webkit-transform: translateX(-50%) translateY(-25%);
    transform: translateX(-50%) translateY(-25%);
}

.col-form-label{
    text-align: right;
}

#header {
    text-align: right;
}

#button_container {
    padding-left: 0%;
    padding-right: 0%
}

#cancel_button_container {
    padding-left: 5em
}

/* .form-control {
    margin-top:0.5em;
    margin-bottom:0.5em
} */

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

<script>
import {mapState, mapActions} from 'vuex'
import { store } from '@/client/store'

export default {
    name:"Profile",
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
            default: 'account/register'
        },
    },
    data() {
        return {
            user :  {
                email: '',
                username: '',
                password: '',
                address: '',
                city: ''
            },
            submitted : false,
        }
    },
    computed: {
        ...mapState('account', ['status'])
    },
    methods: {
        handleSubmit(e) {
            this.submitted = true
            this.$validator.validate().then(valid => {
                if (valid) {
                    this.$store.dispatch(this.dispatchMethod, this.user)
                }
            })
        }
    }
}
</script>