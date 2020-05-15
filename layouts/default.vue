<template>
  <div class="main-layout">
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
.main-layout {
  @apply flex flex-col justify-between h-screen;
  background-color: #071e3d;
}
</style>
