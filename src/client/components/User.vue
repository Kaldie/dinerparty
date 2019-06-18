 <template name="User">
 <div>
    <div class="form-group row">
        <label for=user_name class="col-sm-2 col-form-label" >User Name</label>
        <div class="col-sm-10">
            <input id=user_name v-model="user.username" type="text" v-validate="{ required: true }" name="username" class="form-control" placeholder="required"/>
        </div>
    </div>

    <div class="form-group row" v-if="showPassword">
        <label for=password class="col-sm-2 col-form-label" >Password</label>
        <div class="col-sm-10">
            <input id=password type="password" v-model="user.password" v-validate="{ required: true }" name="password" class="form-control" placeholder="required"/>
        </div>
    </div>

    <div class="form-group row" v-if="showEmail">
        <label for=user_name class="col-sm-2 col-form-label" >Email</label>
        <div class="col-sm-10">
            <input id=email type="text" v-model="user.email" v-validate="{ required: true }" name="email" class="form-control" placeholder="required"/>
        </div>
    </div>

    <div class="form-group row" v-if="showLocation">
        <label for=user_name class="col-sm-2 col-form-label" >Location</label>
        <div class="col-sm-10">
            <div class="input-group">
                <input type="text" v-model="user.address" placeholder="Address" v-validate="{ required: false }" name="address" class="form-control control-pair-left" />
                <input type="text" placeholder='City' v-model="user.city" name="City" class="form-control control-pair-right" />
            </div>
        </div>
    </div>
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


#button_container {
    padding-left: 0%;
    padding-right: 0%
}

#cancel_button_container {
    padding-left: 2.5em
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
      if (this.status.loggedIn) {
          this.get()
      }
    },
}
</script>