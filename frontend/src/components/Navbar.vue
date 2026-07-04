<template>
  <!-- FIXED HEADER CONTAINER (Handles global positioning over viewport) -->
  <header class="fixed top-0 left-0 right-0 z-50 w-full px-4 sm:px-6 lg:px-8 pt-6">
    
    <!-- MASTER FLOATING CAPSULE SHIELD (Inspired by image_8f1a8e.png with your theme colors) -->
    <div class="w-full max-w-[1440px] mx-auto bg-[#070D19]/80 backdrop-blur-md border border-[#233554]/60 rounded-full h-20 px-6 sm:px-10 flex items-center justify-between shadow-2xl shadow-black/40">
      
      <!-- BRAND LOGO & NAME WRAPPER -->
      <div class="flex items-center gap-3 select-none relative z-40">
        <!-- Logo Asset -->
        <img 
          src="../assets/logo.png" 
          alt="Moaz Ali Logo" 
          class="w-7 h-7 sm:w-8 sm:h-8 object-contain"
        />
        <!-- Custom Accent Text Split -->
        <div class="text-xl sm:text-2xl font-black tracking-tight text-white">
          Moaz<span class="text-[#22D3EE]"> Ali</span>
        </div>
      </div>

      <!-- CENTER DIRECTORY NAVIGATION (Capsule Pillar Links) -->
      <nav class="hidden lg:flex items-center bg-[#0B1220]/60 border border-[#233554]/40 px-3 py-1.5 rounded-full text-base font-medium text-slate-400 gap-1">
        <a 
          v-for="link in navLinks" 
          :key="link.text" 
          :href="link.href" 
          @click="scrollToSection($event, link.href)"
          :class="[
            link.active 
              ? 'bg-[#22D3EE] text-[#0A192F] font-bold' 
              : 'hover:text-white hover:bg-[#233554]/30'
          ]"
          class="px-5 py-2 rounded-full transition-all duration-300 whitespace-nowrap"
        >
          {{ link.text }}
        </a>
      </nav>

      <!-- RIGHT SIDE CONVERSION STACK -->
      <div class="hidden sm:flex items-center space-x-4 relative z-40">
        <!-- RIMMED RESUME DOWNLOAD BUTTON -->
        <a 
          href="/Moaz Ali Resume.pdf" 
          download
          class="border border-[#22D3EE]/30 hover:border-[#22D3EE] px-5 py-2.5 rounded-full text-sm font-bold text-[#22D3EE] transition-all duration-200 hover:bg-[#22D3EE]/5 flex items-center gap-2 group"
        >
          Resume
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 transform group-hover:translate-y-0.5 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 13l-7 7-7-7m14-6l-7 7-7-7" />
          </svg>
        </a>

        <!-- SOLID ACTION TRIGGER BUTTON -->
        <button 
          @click="isModalOpen = true"
          class="bg-[#22D3EE] hover:bg-[#22D3EE]/90 text-[#0A192F] px-6 py-2.5 rounded-full text-sm font-black shadow-lg shadow-[#22D3EE]/10 transition-all duration-200 transform hover:scale-[1.02]"
        >
          Hire Me
        </button>
      </div>

      <!-- MOBILE TRIGGER ANCHOR -->
      <button 
        @click="isMobileMenuOpen = !isMobileMenuOpen"
        class="block lg:hidden text-slate-400 hover:text-[#22D3EE] focus:outline-none relative z-40 p-2 transition-colors duration-200"
        aria-label="Toggle Menu"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path 
            v-if="!isMobileMenuOpen"
            stroke-linecap="round" 
            stroke-linejoin="round" 
            stroke-width="2" 
            d="M4 6h16M4 12h16M4 18h16"
          />
          <path 
            v-else
            stroke-linecap="round" 
            stroke-linejoin="round" 
            stroke-width="2" 
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </div>

    <!-- MOBILE EXPANDABLE PANEL (Matches floating geometry) -->
    <transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-4"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-4"
    >
      <div 
        v-if="isMobileMenuOpen"
        class="absolute top-full left-4 right-4 mt-3 bg-[#070D19]/95 backdrop-blur-xl border border-[#233554]/80 rounded-3xl p-6 shadow-2xl z-30 flex flex-col space-y-4 lg:hidden"
      >
        <a 
          v-for="link in navLinks" 
          :key="link.text" 
          :href="link.href" 
          @click="scrollToSection($event, link.href)"
          class="text-base font-medium text-slate-300 hover:text-[#22D3EE] transition-colors duration-200 px-4 py-2.5 rounded-xl hover:bg-[#233554]/20"
        >
          {{ link.text }}
        </a>

        <div class="flex flex-col gap-3 pt-4 border-t border-[#233554]/40 sm:hidden">
          <a 
            href="/Moaz Ali Resume.pdf" 
            download
            class="border border-[#22D3EE]/30 text-center py-3 rounded-xl text-base font-bold text-[#22D3EE]"
          >
            Resume
          </a>
          <button 
            @click="isModalOpen = true; isMobileMenuOpen = false"
            class="bg-[#22D3EE] text-center text-[#0A192F] py-3 rounded-xl text-base font-black"
          >
            Hire Me
          </button>
        </div>
      </div>
    </transition>

    <!-- HIRE ME POPUP MODAL SCREEN -->
    <transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-md" @click.self="isModalOpen = false">
        
        <div class="relative w-full max-w-md bg-[#0B1220] border border-[#233554] rounded-3xl p-6 sm:p-8 shadow-2xl overflow-hidden transform transition-all">
          <button @click="isModalOpen = false" class="absolute top-4 right-4 text-slate-400 hover:text-white p-2 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>

          <div class="text-center mb-8">
            <h3 class="text-2xl font-black text-white tracking-tight">Choose Platform</h3>
            <p class="text-slate-400 text-sm mt-2">Where would you prefer to initiate our contract?</p>
          </div>

          <div class="space-y-4">
            <!-- FIVERR BUTTON -->
            <a 
              href="https://www.fiverr.com/moaz_seller" 
              target="_blank" 
              class="flex items-center justify-between bg-[#112240]/40 border border-[#233554] hover:border-[#1DBF73]/50 p-4 rounded-2xl group transition-all duration-300"
            >
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-xl bg-[#1DBF73]/10 text-[#1DBF73] flex items-center justify-center text-xl font-bold font-mono">fi</div>
                <div>
                  <div class="text-base font-bold text-white group-hover:text-[#1DBF73] transition-colors">Fiverr Marketplace</div>
                  <div class="text-xs text-slate-400 mt-0.5">Order fixed-price custom service gigs</div>
                </div>
              </div>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-500 group-hover:text-[#1DBF73] group-hover:translate-x-1 transition-all" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </a>

            <!-- UPWORK BUTTON -->
            <a 
              href="https://www.upwork.com/freelancers/~018a591f2015343780" 
              target="_blank" 
              class="flex items-center justify-between bg-[#112240]/40 border border-[#233554] hover:border-[#14A800]/50 p-4 rounded-2xl group transition-all duration-300"
            >
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-xl bg-[#14A800]/10 text-[#14A800] flex items-center justify-center text-xl font-bold font-mono">up</div>
                <div>
                  <div class="text-base font-bold text-white group-hover:text-[#14A800] transition-colors">Upwork Profile</div>
                  <div class="text-xs text-slate-400 mt-0.5">Hourly contracts & enterprise scope systems</div>
                </div>
              </div>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-slate-500 group-hover:text-[#14A800] group-hover:translate-x-1 transition-all" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </a>
          </div>

          <div class="absolute bottom-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-[#22D3EE]/40 to-transparent"></div>
        </div>
      </div>
    </transition>

  </header>
</template>

<script setup>
import { ref } from 'vue'

const isMobileMenuOpen = ref(false)
const isModalOpen = ref(false)

// Added 'active' key to control image_8f1a8e.png style highlight capsule trigger
const navLinks = ref([
  { text: 'About', href: '#about', active: false },
  { text: 'Projects', href: '#projects', active: false },
  { text: 'Services', href: '#services', active: false },
  { text: 'Experience', href: '#experience', active: false },
  { text: 'Contact', href: '#contact', active: false }
])

const scrollToSection = (e, href) => {
  e.preventDefault()
  isMobileMenuOpen.value = false
  
  // Reset all active states and set current clicked item to true
  navLinks.value.forEach(link => link.active = link.href === href)
  
  const targetId = href.replace('#', '')
  const element = document.getElementById(targetId)
  
  if (element) {
    element.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  }
}
</script>