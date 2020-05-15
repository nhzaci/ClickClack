<template>
  <div class="main-page space-y-10">
    <div class="title">
      Click<span class="text-yellow-400">Clack</span>
    </div>
    <TypeTest />
  </div>
</template>

<script>
import TypeTest from '../components/TypeTest';

export default {
  components: {
    TypeTest
  }
}
</script>

<style>
/* Sample `apply` at-rules with Tailwind CSS
.container {
  @apply min-h-screen flex justify-center items-center text-center mx-auto;
}
*/
.main-page {
  @apply h-full flex flex-col justify-center items-center mx-auto bg-blue-800;
}
.title {
  @apply text-4xl font-serif bg-blue-700 text-orange-300 p-5 shadow-xl;
}
</style>
