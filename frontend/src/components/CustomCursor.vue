<template>
  <div class="hidden md:block pointer-events-none fixed inset-0 z-[9999]">
    
    <div 
      class="fixed w-2.5 h-2.5 bg-[#22D3EE] rounded-full -translate-x-1/2 -translate-y-1/2 transition-transform duration-75 ease-out will-change-transform shadow-[0_0_10px_#22D3EE]"
      :style="{ left: `${dotX}px`, top: `${dotY}px` }"
    ></div>

    <div 
      class="fixed rounded-full -translate-x-1/2 -translate-y-1/2 border border-[#22D3EE]/40 bg-[#22D3EE]/5 transition-all duration-300 ease-out will-change-transform"
      :class="[isHovered ? 'w-16 h-16 bg-[#22D3EE]/10 border-[#22D3EE] scale-110 shadow-[0_0_25px_rgba(34,211,238,0.2)]' : 'w-8 h-8']"
      :style="{ left: `${trailingX}px`, top: `${trailingY}px` }"
    ></div>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Mouse coordinates positions
const dotX = ref(0)
const dotY = ref(0)
const trailingX = ref(0)
const trailingY = ref(0)
const isHovered = ref(false)

// Smooth Interpolation/Lerp Animation Core Engine
const updateTrailingCursor = () => {
  // Distance formula base tracking gap config
  const ease = 0.15 
  trailingX.value += (dotX.value - trailingX.value) * ease
  trailingY.value += (dotY.value - trailingY.value) * ease
  
  requestAnimationFrame(updateTrailingCursor)
}

const handleMouseMove = (e) => {
  dotX.value = e.clientX
  dotY.value = e.clientY
}

// Check if cursor is hovering over actionable items (links, buttons, etc.)
const handleMouseOver = (e) => {
  if (e.target.closest('a') || e.target.closest('button') || e.target.classList.contains('cursor-pointer')) {
    isHovered.value = true
  } else {
    isHovered.value = false
  }
}

onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove)
  window.addEventListener('mouseover', handleMouseOver)
  requestAnimationFrame(updateTrailingCursor)
  
  // Base structural CSS inject default cursor ko hide karne ke liye
  document.documentElement.style.cursor = 'none'
  const style = document.createElement('style')
  style.id = 'hide-default-cursor'
  style.innerHTML = 'a, button, input, select, textarea, [role="button"] { cursor: none !important; }'
  document.head.appendChild(style)
})

onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove)
  window.removeEventListener('mouseover', handleMouseOver)
  document.documentElement.style.cursor = 'auto'
  document.getElementById('hide-default-cursor')?.remove()
})
</script>