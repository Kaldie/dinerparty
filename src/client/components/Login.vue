<template>
    <div class="container">
        <h2>Login</h2>
        <form @submit.prevent="handleSubmit">
            <div class="form-group">
                <input type="text" v-model="user.userName" placeholder="user name" name="user name" class="form-control" :class="{ 'is-invalid': submitted && errors.has('userName')  }" />
                <div v-show="submitted && !user.userName" class="invalid-feedback">Username is required</div>

                <input type="password" placeholder="password" v-model="user.password" v-validate="{ required: true }" name="password" class="form-control" :class="{ 'is-invalid': submitted && !user.password }" />
                <div v-show="submitted && errors.has('password')" class="invalid-feedback">Password is required</div>
            </div>
            <router-link to="/" class="btn btn-danger float-left">Cancel</router-link>  
            <div class="form-group float-right">   
                <router-link to="/register" class="btn btn-link">Register</router-link>
                <button class="btn btn-primary" v-if='isLoggedIn() === false'>Login
                <img v-show="status.loggingIn" src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
                </button>
            </div>
        </form>
    </div>
</template>

<style>
.container {
    top: 25%;
    left: 50%;
    -moz-transform: translateX(-50%) translateY(-25%);
    -webkit-transform: translateX(-50%) translateY(-25%);
    transform: translateX(-50%) translateY(-25%);
}
</style>

<script>
import {mapState, mapActions} from 'vuex'

export default {
    data() {
        return {
            user :  {
                userName : '',
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
                    this.login(this.user, this.password)
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
