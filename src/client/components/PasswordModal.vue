<template>
<Modal v-bind:header="'Reset Password'">
    <div class="container">

      <div class="container column" id=label-column>
          <!-- <input type=text id="username" hidden class=flex-hidden/> -->
          <label label="Previous password" label-for="prev-password" invalid-feedback="Previous password is required">Previous password</label>
          <label label="New password" label-for="new-password" invalid-feedback="Previous password is required">New password</label>
          <label label="Repeat password" label-for="new-password-2" invalid-feedback="Previous password is required">Repeat password</label>
      </div>

      <div class="container column">
        <form>
          <!-- <input type=text id="username" hidden/> -->
          <input type=password id="prev-password" v-model="previousPassword" required autocomplete="current-password"/> 
          <input type=password id="new-password" v-model="newPassword" required autocomplete="new-password"/> 
          <input type=password id="new-password-2" v-model="repeatPassword" required autocomplete="new-password"/> 
        </form>
      </div>

    </div>

    <div class=container id=button-container>
      <a class=btn href="#">Cancel</a>
      <a class=btn @click=handleSubmit>Accept</a>
    </div>

</Modal>
</template>

<style lang="scss" scoped>


.container {
  justify-content: space-around;
}

#label-column {
  align-items:flex-start;

}

#input-column {
  align-items: flex-end;
  margin: auto;
}

#button-container {
  justify-content: space-between;
}

input {
  margin: 0.3em;
}
</style>

<script>
import {mapActions} from 'vuex'
import Modal from './native_components/Modal'

export default {
  
  components: { Modal },
  data() {
    return {
      previousPassword : "",
      newPassword : "",
      repeatPassword:"",
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

      if (this.repeatPassword !== this.newPassword) {
        // console.warn("passwords are not the same!")
        return
      }

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
