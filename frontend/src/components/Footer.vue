<template>
  <!-- 13. MASTER FOOTER ARCHITECTURE (Full Width Background Shield) -->
  <footer class="relative z-10 w-full border-t border-[#233554]/40 bg-[#070D19]">
    
    <!-- Inner Centered Content Wrapper (Handles internal constraints) -->
    <div class="w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-20 pb-12">
      
      <!-- Top Layer: 3-Column Content Split Matrix -->
      <div class="grid grid-cols-1 md:grid-cols-12 gap-12 pb-16">
        
        <!-- COLUMN 1: BRAND IDENTITY & SOCIALS (5 Columns) -->
        <div class="md:col-span-5 space-y-6">
          <!-- Logo Mark with Custom Accent Split -->
          <div class="text-2xl font-black tracking-tight text-white">
            Moaz<span class="text-[#22D3EE]"> Ali</span>
          </div>
          <!-- Professional Narrative Statement -->
          <p class="text-slate-400 text-sm leading-relaxed max-w-sm">
            Backend & Full-Stack Software Developer specializing in scalable Python architectures, custom Generative AI execution nodes, and modern component-driven interfaces.
          </p>
          <!-- Raw Social Anchor Triggers -->
          <div class="flex items-center gap-6 font-mono text-xs font-bold text-slate-400">
            <a :href="githubUrl" target="_blank" class="hover:text-[#22D3EE] transition-colors duration-200">GitHub</a>
            <a :href="linkedinUrl" target="_blank" class="hover:text-[#22D3EE] transition-colors duration-200">LinkedIn</a>
          </div>
        </div>

        <!-- COLUMN 2: ARCHITECTURE DIRECTORY NAVIGATION (3 Columns) -->
        <div class="md:col-span-3 space-y-4">
          <div class="font-mono text-xs font-black text-white tracking-widest uppercase">
            Navigation
          </div>
          <ul class="space-y-2.5 text-sm text-slate-400 font-sans">
            <li v-for="item in navigationLinks" :key="item.text">
              <a :href="item.href" class="hover:text-[#22D3EE] transition-colors duration-150">
                {{ item.text }}
              </a>
            </li>
          </ul>
        </div>

        <!-- COLUMN 3: CONVERSION INQUIRY & RESUME DOWNLOAD (4 Columns) -->
        <div class="md:col-span-4 space-y-4">
          <div class="font-mono text-xs font-black text-white tracking-widest uppercase">
            Get In Touch
          </div>
          <div class="space-y-4">
            <a :href="`mailto:${emailAddress}`" class="block font-mono text-sm text-slate-300 hover:text-[#22D3EE] transition-colors duration-150">
              {{ emailAddress }}
            </a>
            <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
              Available for corporate freelance contracts, custom AI workflow automation, and long-term senior engineering positions.
            </p>
            
            <!-- EXPLICIT RIMMED RESUME DOWNLOAD BUTTON -->
            <div class="pt-2">
              <a :href="resumeLink" download class="inline-flex items-center gap-2 px-4 py-2.5 font-mono text-xs font-bold text-[#22D3EE] border border-[#22D3EE]/40 rounded-lg hover:border-[#22D3EE] hover:bg-[#22D3EE]/5 transition-all duration-200">
                Download Resume 
                <span class="text-xs">↓</span>
              </a>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom Layer: Technical Copyright Baseline Line Guide -->
      <div class="pt-8 border-t border-[#233554]/30 flex flex-col sm:flex-row justify-between items-center gap-4 font-mono text-[11px] text-slate-500 font-bold">
        <div>
          © {{ currentYear }} Moaz Ali. Built with Vue.js, Django & Tailwind CSS.
        </div>
        <div class="text-slate-600 sm:text-right">
          Crafted with precision — available for new projects.
        </div>
      </div>

    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'

const currentYear = ref(2026)
const emailAddress = ref('moaz55397@gmail.com')
const githubUrl = ref('https://github.com')
const linkedinUrl = ref('https://linkedin.com/in/moaz-ali10')
const resumeLink = ref('Moaz Ali Resume.pdf')

const navigationLinks = ref([
  { text: 'About', href: '#about' },
  { text: 'Projects', href: '#projects' },
  { text: 'Services', href: '#services' },
  { text: 'Experience', href: '#experience' },
  { text: 'Blog', href: '#blog' },
  { text: 'Contact', href: '#contact' }
])
</script>