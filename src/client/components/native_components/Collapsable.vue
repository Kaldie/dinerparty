<template>
    <div>
        <button class="collapsible" v-bind:class="{ active: isActive }" @click="isActive=!isActive">{{header}}</button>
        <div class="container">
            <div class="content">
                <slot v-if="isActive"></slot>   
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name:"Collapsable",
    data() {
        return  {
            isActive: false
        }
    },
    props: {
        header:{type:String, default:"magic"}
    }
}
</script>



<style lang="scss" scoped>
/* Style the button that is used to open and close the collapsible content */
.collapsible {
  background-color: #eee;
  color: #444;
  cursor: pointer;
  border: none;
  text-align: left;
  outline: none;
  margin: auto;
}

.container {
    justify-content: center;
}

/* Style the collapsible content. Note: hidden by default */
.content {
  padding: 0 18px;
  overflow: hidden;
  background-color: rgba(255, 255, 255, 0.5);
}
</style>
