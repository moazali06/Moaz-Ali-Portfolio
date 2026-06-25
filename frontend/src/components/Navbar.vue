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
        @click="scrollToSection($event, link.href)"
        class="hover:text-[#22D3EE] transition-colors duration-200"
      >
        {{ link.text }}
      </a>
    </nav>

    <div class="hidden sm:flex items-center space-x-6 relative z-40">
      <a 
        href="/Moaz Ali Resume.pdf" 
        download
        class="border border-[#3B82F6]/40 hover:border-[#22D3EE] px-7 py-3 rounded-2xl text-lg font-medium text-[#22D3EE] transition-all duration-200 backdrop-blur-sm flex items-center gap-2.5 group"
      >
        Resume
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 transform group-hover:translate-y-0.5 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 13l-7 7-7-7m14-6l-7 7-7-7" />
        </svg>
      </a>

      <!-- Hire Me Button - Desktop (Popup Open karega) -->
      <button 
        @click="isModalOpen = true"
        class="bg-[#22D3EE] hover:bg-[#22D3EE]/90 text-[#0A192F] px-7 py-3 rounded-2xl text-lg font-bold shadow-2xl shadow-[#22D3EE]/10 transition-all duration-200"
      >
        Hire Me
      </button>
    </div>

    <!-- Mobile Menu Button -->
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

    <!-- Mobile Drawer Menu -->
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
          @click="scrollToSection($event, link.href)"
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
          <!-- Hire Me Button - Mobile (Popup Open karega aur drawer band karega) -->
          <button 
            @click="isModalOpen = true; isMobileMenuOpen = false"
            class="bg-[#22D3EE] text-center text-[#0A192F] py-3.5 rounded-xl text-lg font-bold"
          >
            Hire Me
          </button>
        </div>
      </div>
    </transition>

    <!-- ========================================== -->
    <!-- HIRE ME POPUP MODAL SCREEN -->
    <!-- ========================================== -->
    <transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-md" @click.self="isModalOpen = false">
        
        <!-- Modal Content Container Box -->
        <div class="relative w-full max-w-md bg-[#0B1220] border border-[#233554] rounded-3xl p-6 sm:p-8 shadow-2xl overflow-hidden transform transition-all">
          
          <!-- Close Button -->
          <button @click="isModalOpen = false" class="absolute top-4 right-4 text-slate-400 hover:text-white p-2 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>

          <!-- Headings -->
          <div class="text-center mb-8">
            <h3 class="text-2xl font-black text-white tracking-tight">Choose Platform</h3>
            <p class="text-slate-400 text-sm mt-2">Where would you prefer to initiate our contract?</p>
          </div>

          <!-- Options Stack -->
          <div class="space-y-4">
            
            <!-- FIVERR BUTTON -->
            <a 
              href="https://www.fiverr.com/moaz_seller" 
              target="_blank" 
              class="flex items-center justify-between bg-[#112240]/40 border border-[#233554] hover:border-[#1DBF73]/50 p-4 rounded-2xl group transition-all duration-300"
            >
              <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-xl bg-[#1DBF73]/10 text-[#1DBF73] flex items-center justify-center text-xl font-bold font-mono">
                  fi
                </div>
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
                <div class="w-12 h-12 rounded-xl bg-[#14A800]/10 text-[#14A800] flex items-center justify-center text-xl font-bold font-mono">
                  up
                </div>
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

          <!-- Light Neon Bottom Decorator Line -->
          <div class="absolute bottom-0 left-0 right-0 h-[2px] bg-gradient-to-r from-transparent via-[#22D3EE]/40 to-transparent"></div>

        </div>
      </div>
    </transition>

  </header>
</template>

<script setup>
import { ref } from 'vue'

const isMobileMenuOpen = ref(false)
const isModalOpen = ref(false) // Modal open state control flag

const navLinks = ref([
  { text: 'About', href: '#about' },
  { text: 'Projects', href: '#projects' },
  { text: 'Services', href: '#services' },
  { text: 'Experience', href: '#experience' },
  { text: 'Contact', href: '#contact' }
])

const scrollToSection = (e, href) => {
  e.preventDefault()
  isMobileMenuOpen.value = false
  
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