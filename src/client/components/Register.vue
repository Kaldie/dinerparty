<template>
    <div class="container">
        <h2>Register</h2>
        <form @submit.prevent="handleSubmit">

            <input id=user_name v-model="user.username" type="text" v-validate="{ required: true }" name="username" class="form-control" placeholder="User name (required)"/>
            <div v-show="submitted && !user.username" class="invalid-feedback">Username is required</div>

            <input id=password type="text" v-model="user.password" v-validate="{ required: true }" name="password" class="form-control" placeholder="Password (required)"/>
            <div v-show="submitted && !user.password" class="invalid-feedback">Password is required</div>

            <input id=email type="text" v-model="user.email" v-validate="{ required: true }" name="email" class="form-control" placeholder="Email (required)"/>
            <div v-show="submitted && !user.email" class="invalid-feedback">Username is required</div>

            <div class="input-group">
                <input type="text" v-model="user.address" placeholder="Street  number" v-validate="{ required: false }" name="user first name" class="form-control control-pair-left" :class="{ 'is-invalid': submitted && errors.has('firstName')  }" />
                <div v-show="submitted && !user.address" class="invalid-feedback">Username is required</div>

                <input type="text" placeholder='City' v-model="user.city" name="user first name" class="form-control control-pair-right" :class="{ 'is-invalid': submitted && errors.has('middleName')  }" />
                <div v-show="submitted && !user.city" class="invalid-feedback">Username is required</div>

            </div>

            <router-link to="/" class="btn btn-danger form-group-button float-left">Cancel</router-link> 
            <div class="form-group form-group-button float-right">
                <button class="btn btn-primary " :disabled="status.loggedIn">Register</button> 
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

.form-control {
    margin-top:0.5em;
    margin-bottom:0.5em
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

<script>
import {mapState, mapActions} from 'vuex'

export default {
    data() {
        return {
            user :  {
                email: '',
                username: '',
                password: '',
                address: '',
                city: ''
            },
            submitted : false
        }
    },
    computed: {
        ...mapState('account', ['status'])
    },
    methods: {
        ...mapActions('account', ['register']),
        handleSubmit(e) {
            this.submitted = true
            this.$validator.validate().then(valid => {
                console.warn("valid", valid)
                if (valid) {
                    console.warn("here", this.user)
                    this.register(this.user)
                }
            })
        }
    }
}

</script>