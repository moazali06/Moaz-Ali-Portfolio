<template>
  <canvas 
    ref="canvasRef" 
    class="fixed inset-0 w-full h-full pointer-events-none z-0 bg-[#0A192F]"
  ></canvas>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const canvasRef = ref(null)
let ctx = null
let animationFrameId = null
const particles = []

// 👇 QUANTITY AUR DISTANCE CONFIGURATION (Sleek & Minimal Setup)
const PARTICLE_COUNT = 45 // 🚀 Quantity kam kar di (Pehle 80 thi, ab 45 hai for a cleaner look)
const CONNECTION_DISTANCE = 110 // Dots ke darmiyan lines banne ka distance range thora tight kiya
const mouse = { x: null, y: null, radius: 160 } // Mouse effect area

class Particle {
  constructor(width, height) {
    this.x = Math.random() * width
    this.y = Math.random() * height
    // Slow, elegant floating speed vector
    this.vx = (Math.random() - 0.5) * 0.4
    this.vy = (Math.random() - 0.5) * 0.4
    this.radius = Math.random() * 1.5 + 0.8 // Dots ka size bhi slightly subtle kiya
  }

  update(width, height) {
    this.x += this.vx
    this.y += this.vy

    // Boundary check logic
    if (this.x < 0 || this.x > width) this.vx *= -1
    if (this.y < 0 || this.y > height) this.vy *= -1

    // Mouse movement response math
    if (mouse.x !== null && mouse.y !== null) {
      const dx = mouse.x - this.x
      const dy = mouse.y - this.y
      const distance = Math.sqrt(dx * dx + dy * dy)
      
      if (distance < mouse.radius) {
        const force = (mouse.radius - distance) / mouse.radius
        this.x -= (dx / distance) * force * 1.0
        this.y -= (dy / distance) * force * 1.0
      }
    }
  }

  draw() {
    ctx.beginPath()
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2)
    ctx.fillStyle = 'rgba(34, 211, 238, 0.4)' // 🎨 Dots ki opacity kam kar ke 0.4 kar di
    ctx.fill()
  }
}

const resizeCanvas = () => {
  if (!canvasRef.value) return
  canvasRef.value.width = window.innerWidth
  canvasRef.value.height = window.innerHeight
}

const animate = () => {
  const w = canvasRef.value.width
  const h = canvasRef.value.height
  ctx.clearRect(0, 0, w, h)

  for (let i = 0; i < particles.length; i++) {
    particles[i].update(w, h)
    particles[i].draw()

    for (let j = i + 1; j < particles.length; j++) {
      const dx = particles[i].x - particles[j].x
      const dy = particles[i].y - particles[j].y
      const dist = Math.sqrt(dx * dx + dy * dy)

      if (dist < CONNECTION_DISTANCE) {
        // 👇 OPACITY TUNING ENGINE
        // Is multiplier ko 0.18 se kam kar ke 0.08 kar diya hai taake lines bohot faint aur premium lagein
        const alpha = (1 - dist / CONNECTION_DISTANCE) * 0.08 
        ctx.beginPath()
        ctx.moveTo(particles[i].x, particles[i].y)
        ctx.lineTo(particles[j].x, particles[j].y)
        ctx.strokeStyle = `rgba(59, 130, 246, ${alpha})` // Electric Blue lines with ultra-low opacity
        ctx.lineWidth = 0.6 // Lines ki width thori mazeed barik (thin) kar di
        ctx.stroke()
      }
    }
  }

  animationFrameId = requestAnimationFrame(animate)
}

const handleMouseMove = (e) => {
  mouse.x = e.clientX
  mouse.y = e.clientY
}

const handleMouseLeave = () => {
  mouse.x = null
  mouse.y = null
}

onMounted(() => {
  ctx = canvasRef.value.getContext('2d')
  resizeCanvas()

  for (let i = 0; i < PARTICLE_COUNT; i++) {
    particles.push(new Particle(canvasRef.value.width, canvasRef.value.height))
  }

  window.addEventListener('resize', resizeCanvas)
  window.addEventListener('mousemove', handleMouseMove)
  document.addEventListener('mouseleave', handleMouseLeave)

  animate()
})

onUnmounted(() => {
  window.removeEventListener('resize', resizeCanvas)
  window.removeEventListener('mousemove', handleMouseMove)
  document.removeEventListener('mouseleave', handleMouseLeave)
  cancelAnimationFrame(animationFrameId)
})
</script>