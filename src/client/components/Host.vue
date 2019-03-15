<template>
  <div name=Host>
    <h1>
    Host your own Diner Party
    </h1>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm">
          <img id=left-food-image class=column-food-image src="../assets/food_images/food.png">
        </div>
        <div class="col-sm">
          <img id=right-food-image class=column-food-image src="../assets/food_images/food2.png">
        </div>
      </div>
      <div class="row form-row">
        
        <div class="col-sm">
          <div class="card"> 
            <div class=card-title id=user-information-card>
              <h4 id=user-information-card-title> User information </h4>
            </div>
            
            <div class="card-body" id=user-information-card-body>
                <div class="input-group">
                  <input id=user_name type="text" class="form-control control-pair-left" placeholder="User name"/>
                  <input id=email type="text" class="form-control control-pair-right" placeholder="Email"/>
                </div>
                <div class="input-group">
                  <input id=street_name type="text" class="form-control control-pair-left" placeholder="Street name"/>
                  <input id=street_number type="number" class="form-control control-pair-right" placeholder="Street number"/>
                </div>
                <input id=postal_code type="text" class="form-control control-pair" placeholder="Postal code"/>
                <input id=city_name type="text" class="form-control control-pair" placeholder="City"/>
            </div>
          </div>
        </div>

         <div class="col-sm">
          <div class="card"> 
            <div class=card-title id=diner-information-card>
              <h4 id=user-information-card-title> Diner description </h4>
            </div>
            <div class="card-body" id=user-information-card-body>
              <input id=diner_name type="text" class="form-control" placeholder="Diner name"/>
              <input id=diner_number_of_seats type="number" class="form-control" placeholder=2 />
              <textarea class="form-control" id="diner_description-text-area" rows="1" placeholder="Description of the diner"/>

              <div class="form-check">
                <input type="checkbox" class=form-check-input id="has-guidance" aria-label="Checkbox">
                <label class="form-check-label" for="has-guidance">Will teach</label>
              </div>

            </div>
          </div>
         </div>


"name":"first",
      "location": {
        "latitude":50.1,
        "longtitude":24.123,
      },
      "description": "small party!",
      "seets" : 5,
      "tutorial": False,
      "cousine": "Greek",
      "date": str(datetime.date(2019, 12, 1)),
      "image": "http://127.0.0.1:5000/second.png",



      </div>
    </div>
  </div>
</template>

<style scoped>
.column-food-image {
  width: 100%;
  height: 100%;
}
.form-row {
  margin-top:0.5em;
  margin-bottom:0.25em;
}
input {
  margin-top:0.25em;
  margin-bottom: 0.25em;
}
.form-check {
  margin-top:0.25em;
  margin-bottom: 0.25em;
  border:1px solid #ced4da;
}

textarea {
  margin-top:0.25em;
  margin-bottom: 0.25em;
}

.control-pair-left {
  margin-right: 0.5rem;
}
.control-pair-right {
  margin-left: 0.5rem;
}

 .card-title  {
   padding:0em;
   margin-bottom:0em;
 }

 #user-information-card-body {
   padding-top:0em;
 }

 .card-body {
   padding:0em;
   padding-left:0.25em;
   padding-right:0.25rem;
   
 }
</style>

