<template>
<TheNavbar />
  <HeroSection />
  <Footer />
  
  </template>

<script setup>
// HeroSection component ko import kar rahe hain
import HeroSection from './components/HeroSection.vue'
import TheNavbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

</script>

<style>
/* Global styles agar chahiye hon, warna Tailwind handle kar lega */
body {
  margin: 0;
  padding: 0;
  background-color: #0A192F; /* Dark background default */
}
</style>