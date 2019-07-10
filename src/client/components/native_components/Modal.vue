<template>

  <div :id="modal_id" class="modal-window">
      <header>
          <h1>{{header}}</h1>
      </header>
    <div>
        <slot></slot>
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
</style>

<script>

export default {
    name:'Modal',
    props: {
        header : {type:String, default:"modal"},
        modal_id: {type:String, default:"open-modal"}
    }
}
</script>
