<template>
    <div>
      <transition name="modal">
        <div class="modal-mask">
          <div class="modal-wrapper">
            <div class="modal-container">
              <div class="modal-header">
                <slot name="header">
                </slot>
              </div>

              <div class="modal-body">
                <slot name="body">
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                </slot>
                <button class="modal-default-button" @click="$emit('close')">
                  Close
                </button>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
@import url("@/assets/css/modal.css");
</style>