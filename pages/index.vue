<template>
  <div class="main-page space-y-10">
    <TypeTest />
  </div>
</template>

<script>
import TypeTest from '../components/TypeTest';
import Footer from '../components/Footer';

export default {
  components: {
    TypeTest,
    Footer
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
  @apply flex flex-col justify-center items-center mx-auto;
}
</style>
