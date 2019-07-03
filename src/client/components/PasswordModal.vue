<template>

  <div id="open-modal" class="modal-window">
    <div>
      <h1>Reset Password</h1>

      <div class="container">

        <div class="container column" id=label-column>
            <label label="Previous password" label-for="prev-password" invalid-feedback="Previous password is required">Previous password</label>
            <label label="New password" label-for="new-password" invalid-feedback="Previous password is required">New password</label>
            <label label="Repeat password" label-for="new-password-2" invalid-feedback="Previous password is required">Repeat password</label>
        </div>

        <div class="container column">
            <input type=password id="prev-password" v-model="previousPassword" required autocomplete="current-password"/> 
            <input type=password id="new-password" v-model="newPassword" required autocomplete="new-password"/> 
            <input type=password id="new-password-2" v-model="repeatPassword" required autocomplete="new-password"/> 
        </div>

      </div>

      <div class=container id=button-container>
        <a class=btn href="#">Cancel</a>
        <a class=btn @click=handleSubmit>Accept</a>
      </div>

    </div>
  </div>
</template>

<style lang="scss" scoped>
.modal-window {
  position: fixed;
  background-color: rgba(0, 0, 0, 0.75);
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 999;
  opacity: 0;
  pointer-events: none;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
  transition: all 0.3s;
  
  &:target {
    opacity: 1;
    pointer-events: auto;
  }

  &>div {
    width: 400px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 2em;
    background: #ffffff;
    border-radius: 3px;
  }

  header {
    font-weight: bold;
  }

  h1 {
    font-size: 150%;
    margin: 0 0 1px;
  }

}

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

export default {
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
        console.warn("passwords are not the same!")
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
