<template>
  <header class="relative z-30 w-full max-w-[1440px] mx-auto px-6 sm:px-10 h-32 flex items-center justify-between">
    
    <div class="text-3xl font-bold tracking-tight text-white select-none relative z-40">
      Moaz<span class="text-[#22D3EE]"> Ali</span>
    </div>

    <nav class="hidden lg:flex items-center space-x-12 text-lg font-medium text-slate-400">
      <a 
        v-for="link in navLinks" 
        :key="link.text" 
        :href="link.href" 
        class="hover:text-[#22D3EE] transition-colors duration-200"
      >
        {{ link.text }}
      </a>
    </nav>

    <div class="hidden sm:flex items-center space-x-6 relative z-40">
      <a 
        href="/resume.pdf" 
        download
        class="border border-[#3B82F6]/40 hover:border-[#22D3EE] px-7 py-3 rounded-2xl text-lg font-medium text-[#22D3EE] transition-all duration-200 backdrop-blur-sm flex items-center gap-2.5 group"
      >
        Resume
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 transform group-hover:translate-y-0.5 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 13l-7 7-7-7m14-6l-7 7-7-7" />
        </svg>
      </a>

      <a 
        href="#contact" 
        class="bg-[#22D3EE] hover:bg-[#22D3EE]/90 text-[#0A192F] px-7 py-3 rounded-2xl text-lg font-bold shadow-2xl shadow-[#22D3EE]/10 transition-all duration-200"
      >
        Hire Me
      </a>
    </div>

    <button 
      @click="isMobileMenuOpen = !isMobileMenuOpen"
      class="block lg:hidden text-slate-400 hover:text-[#22D3EE] focus:outline-none relative z-40 p-2 transition-colors duration-200"
      aria-label="Toggle Menu"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
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

    <transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-8"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-8"
    >
      <div 
        v-if="isMobileMenuOpen"
        class="absolute top-0 left-0 w-full bg-[#0A192F]/95 backdrop-blur-xl border-b border-[#233554] pt-32 pb-10 px-8 shadow-2xl z-30 flex flex-col space-y-6 lg:hidden"
      >
        <a 
          v-for="link in navLinks" 
          :key="link.text" 
          :href="link.href" 
          @click="isMobileMenuOpen = false"
          class="text-xl font-medium text-slate-300 hover:text-[#22D3EE] transition-colors duration-200 border-b border-[#112240] pb-2"
        >
          {{ link.text }}
        </a>

        <div class="flex flex-col gap-4 pt-4 sm:hidden">
          <a 
            href="/resume.pdf" 
            download
            class="border border-[#3B82F6]/40 text-center py-3.5 rounded-xl text-lg font-medium text-[#22D3EE]"
          >
            Resume
          </a>
          <a 
            href="#contact" 
            @click="isMobileMenuOpen = false"
            class="bg-[#22D3EE] text-center text-[#0A192F] py-3.5 rounded-xl text-lg font-bold"
          >
            Hire Me
          </a>
        </div>
      </div>
    </transition>

  </header>
</template>

<script setup>
import { ref } from 'vue'

// Reactive state tracker for tracking Mobile Sidebar visibility bounds
const isMobileMenuOpen = ref(false)

// Array Matrix for Navigation Links Management
const navLinks = ref([
  { text: 'About', href: '#about' },
  { text: 'Projects', href: '#projects' },
  { text: 'Services', href: '#services' },
  { text: 'Experience', href: '#experience' },
  { text: 'Contact', href: '#contact' }
])
</script>