<template>
  <b-modal id="password-modal" ref="password_modal" @show="reset" @hidden="reset" @ok="handleOK" >
    
    <template slot=modal-title>
      Update your password
    </template>

    <form ref="form" @submit.stop.prevent="handleSubmit">
      <b-form-group label="Previous password" label-for="prev-password" invalid-feedback="Previous password is required">
          <b-form-input type=password id="prev-password" v-model="previousPassword" required autocomplete="current-password"> </b-form-input>
      </b-form-group>

      <b-form-group label="New password" label-for="new-password" invalid-feedback="Previous password is required">
          <b-form-input type=password id="new-password" v-model="newPassword" required autocomplete="new-password"> </b-form-input>
      </b-form-group>      
    </form>

  </b-modal>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  data() {
    return {
      previousPassword : "",
      newPassword : ""
    }
  },
  methods: {
    ...mapActions('account',['resetPassword']),
    reset() {
      this.prevPassword = ""
      this.newPassword = ""
    },
    handleOK(event) {
      event.preventDefault()
      this.handleSubmit()
    },
    handleSubmit() {
      this.resetPassword({
        previousPassword : this.previousPassword,
        newPassword : this.newPassword
        })
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.password_modal.hide()
      })
    }
  }
}
</script>
