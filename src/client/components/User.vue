 <template name="User">
  <div>
    <div class="container" >
            <label for=user_name class="col-sm-2 col-form-label" >User Name</label>
            <input id=user_name v-model="user.username" type="text" v-validate="{ required: true }" name="username"  placeholder="required"/>
            <label for=email class="col-sm-2 col-form-label" >Email</label>
            <input id=email type="text" v-model="user.email" v-validate="{ required: true }" name="email" placeholder="required"/>

            <label for=password v-if="showPassword"  class="col-sm-2 col-form-label" >Password</label>
            <input v-if="showPassword" id=password type="password" v-model="user.password" v-validate="{ required: true }" name="password"  placeholder="required"/>


            <label for=location>Location</label>
            <input type="text" v-model="user.address" placeholder="Address" v-validate="{ required: false }" name="address" />
            <input type="text" placeholder='City' v-model="user.city" name="City" />

    </div>
  </div>
</template>

<style scoped>



.container {
  display:grid;
  grid-template-columns: 1fr 1fr;
  grid-column-gap: 1em;
}

input {
  justify-self: start;
}

label {
  padding-top:3px;
  padding-bottom: 3px;
  justify-self: end;
}

label[for=location] {
  grid-row: 3/5;
  align-self: center;
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