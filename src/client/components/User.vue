 <template name="User">
 <div>
    <div class="container" >
        <div class="container column" id="user-container">
            <label for=user_name class="col-sm-2 col-form-label" >User Name</label>
            <label for=email class="col-sm-2 col-form-label" >Email</label>
            <label v-if="showPassword" for=password class="col-sm-2 col-form-label" >Password</label>
        </div>

        <div class="container column">
            <input id=user_name v-model="user.username" type="text" v-validate="{ required: true }" name="username"  placeholder="required"/>
            <input id=email type="text" v-model="user.email" v-validate="{ required: true }" name="email" placeholder="required"/>
            <input v-if="showPassword" id=password type="password" v-model="user.password" v-validate="{ required: true }" name="password"  placeholder="required"/>
        </div>
    </div>

    <div class='container location-container'>
      <div class="container column location-container">
        <label for=location>Location</label>
    </div>

    <div class="container column location-container">
        <input type="text" v-model="user.address" placeholder="Address" v-validate="{ required: false }" name="address" />
        <input type="text" placeholder='City' v-model="user.city" name="City" />
    </div>
  </div>
 </div>
</template>

<style scoped>



.container {
  justify-content: center;
  margin-bottom: 0px;
}

.container.column {
  justify-content: space-between;
  margin-right: 0.3em;
}

input{
  margin: 0.1em;
}

label {
  margin-top:auto;
  margin-bottom: auto;
}

label[for='location'] {
  margin:auto;
  margin-right: 1.3em;
}

#user-container, #location-container {
  align-items: flex-start;
}

div.location-container {
  margin-top:0px;
}

</style>

<script>
import {mapState, mapActions} from 'vuex'

export default {
  computed: {
    ...mapState('account', ['status', 'user'])
    
    },
  props: {
    "showPassword": {
      type:Boolean,
      default: false
    },
    "showEmail": {
      type:Boolean,
      default: false
    },
    "showLocation": {
      type:Boolean,
      default: false
    }
  },
  methods: {
    ...mapActions('account', ['get']),
    },
  mounted () {
      if (this.status.loggedIn && this.user.userName) {
          this.get(this.user.userName)
      }
    },
}
</script>