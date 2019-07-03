<template>
    <div class="container">
        <h2>Login</h2>
        <form @submit.prevent="handleSubmit">

            <div class="row">
                <div class="column">
                    <label for=user_name>User Name</label>
                    <label for=password>Password</label>
                </div>

                <div class="column">
                    <input id=user_name v-model="user.username" type="text" v-validate="{ required: true }" name="username" class="form-control" placeholder="required"/>
                    <div v-show="submitted && !user.username" class="invalid-feedback">Username is required</div>
                
                    <input id=password type="password" v-model="user.password" v-validate="{ required: true }" name="password" class="form-control" placeholder="required"/>
                    <div v-show="submitted && !user.password" class="invalid-feedback">Password is required</div>
                </div>
            </div>

            <div id='button-row' class="row">
                <router-link to="/" class="btn btn-danger float-left">Cancel</router-link>

                    <router-link to="/register" class="btn btn-link">Register</router-link>
                    <button class="btn btn-primary" v-if='isLoggedIn() === false'>Login
                    </button>

            </div>
        </form>
    </div>
</template>

<style scoped>
.container {
    display:flex;
    flex-direction: column;
}

.row {
    display:flex;
    justify-content:center;
    margin: 1mm;
}

#button-row {
   justify-content: space-around; 
}

.column {
    display: flex;
    flex-direction: column;
    justify-content: space-around
}

label {
    text-align: left;
    margin-right: 2mm;
}

</style>

<script>
import {mapState, mapActions} from 'vuex'

export default {
    data() {
        return {
            user :  {
                username : '',
                password : ''
            },
            submitted : false
        }
    },
    computed: {
        ...mapState('account', ['status'])
    },
    methods: {
        ...mapActions('account', ['login']),
        handleSubmit() {
            this.submitted = true
            this.$validator.validate().then(valid => {
                if (valid) {
                    this.login({
                        username: this.user.username, 
                        password: this.user.password
                        })
                }
            })
        },
        isLoggedIn() {
            if (this.status && this.status.loggedIn)
                return  true
            return false
        }
    }
}

</script>
