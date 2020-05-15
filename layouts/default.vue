<template>
  <div class="flex flex-col justify-between h-screen bg-gray-700">
    <Header />
    <nuxt/>
    <Footer/>
  </div>
</template>

<script>
import Footer from '../components/Footer';
import Header from '../components/Header';

export default {
  components: {
    Footer,
    Header
  }
}
</script>

<style>
</style>
