<template>
  <div class="main-page space-y-10">
    <TypeTest />
  </div>
</template>

<script>
import Footer from '@/components/Footer';
import TypeTest from '@/components/TypeTest';

export default {
  head: {
      titleTemplate: "%s - Home", 
  },
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
