<template>
  <!-- AI Chatbot Widget Container -->
  <div class="fixed bottom-24 right-6 z-50 flex flex-col items-end font-sans selection:bg-[#22D3EE]/30 selection:text-white">
    
    <!-- Chat Window (Glassmorphism & Tech Aesthetic) -->
    <transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="transform scale-95 opacity-0 translate-y-4 origin-bottom-right"
      enter-to-class="transform scale-100 opacity-100 translate-y-0 origin-bottom-right"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="transform scale-100 opacity-100 translate-y-0 origin-bottom-right"
      leave-to-class="transform scale-95 opacity-0 translate-y-4 origin-bottom-right"
    >
      <div 
        v-if="isChatOpen" 
        class="w-[350px] sm:w-[400px] h-[520px] bg-[#0A192F]/90 backdrop-blur-xl border-2 border-[#233554] rounded-2xl shadow-[0_10px_50px_rgba(34,211,238,0.15)] flex flex-col overflow-hidden mb-4"
      >
        <!-- Header -->
        <div class="p-4 bg-[#0B1220] border-b border-[#233554] flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="relative flex h-2.5 w-2.5">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#22D3EE] opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-[#22D3EE] shadow-[0_0_8px_#22D3EE]"></span>
            </div>
            <div>
              <h4 class="text-sm font-bold text-white tracking-wide">Moaz's AI Assistant</h4>
              <p class="text-[10px] font-mono text-slate-400">Ask about tech stack, projects, or availability</p>
            </div>
          </div>
          <button @click="isChatOpen = false" class="text-slate-400 hover:text-white transition-colors p-1 rounded-lg hover:bg-[#112240]">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Messages Area -->
        <div ref="chatContainer" class="flex-1 p-4 overflow-y-auto space-y-4 scrollbar-thin scroll-smooth">
          <div v-for="(msg, index) in messages" :key="index" class="flex" :class="msg.sender === 'user' ? 'justify-end' : 'justify-start'">
            <div 
              class="max-w-[85%] rounded-xl px-4 py-2.5 text-sm leading-relaxed whitespace-pre-line"
              :class="msg.sender === 'user' ? 'bg-[#3B82F6] text-white rounded-br-none shadow-[0_4px_12px_rgba(59,130,246,0.2)]' : 'bg-[#112240] border border-[#233554] text-slate-300 rounded-bl-none'"
            >
              {{ msg.text }}
            </div>
          </div>
          
          <!-- Typing Indicator -->
          <div v-if="isTyping" class="flex justify-start">
            <div class="bg-[#112240] border border-[#233554] rounded-xl rounded-bl-none px-4 py-3.5 flex gap-1 items-center">
              <span class="w-1.5 h-1.5 bg-[#22D3EE] rounded-full animate-bounce [animation-duration:0.8s]"></span>
              <span class="w-1.5 h-1.5 bg-[#22D3EE] rounded-full animate-bounce [animation-duration:0.8s] [animation-delay:0.2s]"></span>
              <span class="w-1.5 h-1.5 bg-[#22D3EE] rounded-full animate-bounce [animation-duration:0.8s] [animation-delay:0.4s]"></span>
            </div>
          </div>
        </div>

        <!-- Input Area -->
        <form @submit.prevent="sendMessage" class="p-3 bg-[#0B1220] border-t border-[#233554] flex gap-2">
          <input 
            v-model="userMessage" 
            type="text" 
            placeholder="Type a message..." 
            :disabled="isTyping"
            class="flex-1 bg-[#070D19] border border-[#233554] rounded-xl px-4 py-2.5 text-sm text-slate-200 placeholder-slate-600 focus:outline-none focus:border-[#22D3EE] focus:ring-1 focus:ring-[#22D3EE] transition-all disabled:opacity-50"
          />
          <button 
            type="submit" 
            :disabled="!userMessage.trim() || isTyping"
            class="bg-[#22D3EE] text-[#0A192F] p-2.5 rounded-xl hover:bg-[#3B82F6] hover:text-white transition-colors duration-200 disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center"
          >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5">
              <path d="M3.478 2.404a.75.75 0 00-.926.941l2.432 7.905H13.5a.75.75 0 010 1.5H4.984l-2.432 7.905a.75.75 0 00.926.94 60.519 60.519 0 0018.445-8.986.75.75 0 000-1.218A60.517 60.517 0 003.478 2.404z" />
            </svg>
          </button>
        </form>
      </div>
    </transition>

    <!-- Chat Toggle Floating Action Button (FAB) -->
    <button 
      @click="isChatOpen = !isChatOpen" 
      class="w-14 h-14 bg-[#3B82F6] hover:bg-[#22D3EE] text-white hover:text-[#0A192F] rounded-full shadow-[0_4px_25px_rgba(59,130,246,0.3)] hover:shadow-[0_0_30px_rgba(34,211,238,0.4)] flex items-center justify-center transition-all duration-300 hover:scale-110 active:scale-95"
      :aria-label="isChatOpen ? 'Close chat' : 'Open AI Assistant'"
    >
      <svg v-if="!isChatOpen" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a.596.596 0 01-.548-.54 5.63 5.63 0 01.408-2.19C3.593 16.516 3 14.332 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z" />
      </svg>
      <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
      </svg>
    </button>
  </div>
</template>

<script setup>
import { ref, nextTick, watch } from 'vue'

const isChatOpen = ref(false)
const userMessage = ref('')
const isTyping = ref(false)
const chatContainer = ref(null)

const messages = ref([
  { sender: 'bot', text: "Hi! I'm Moaz's AI assistant. Ask me anything about his technical experience, software architecture expertise, or how to get in touch!" }
])

// Auto scroll to bottom helper
const scrollToBottom = async () => {
  await nextTick()
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}

// Watch chat state to scroll down when opened
watch(isChatOpen, (val) => {
  if (val) scrollToBottom()
})

const sendMessage = async () => {
  if (!userMessage.value.trim()) return

  const queryText = userMessage.value
  messages.value.push({ sender: 'user', text: queryText })
  userMessage.value = ''
  
  await scrollToBottom()
  isTyping.value = true

  try {
    // FIX: Starting clean forward slash lagayein taake base domain root standard mapping use ho
    // Production aur local dono environments par automatic domain setup handle karne ke liye absolute standard fallback lagayein:
    const baseUrl = window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')
      ? 'http://127.0.0.1:8000'
      : window.location.origin;

    const response = await fetch('/api/contact/chatbot/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)?.[1] || ''
      },
      body: JSON.stringify({ message: queryText })
    })

    const data = await response.json()

    if (response.ok && data.reply) {
      messages.value.push({ sender: 'bot', text: data.reply })
    } else {
      messages.value.push({ 
        sender: 'bot', 
        text: "I'm having trouble processing that right now. Please feel free to use the contact form or WhatsApp me directly!" 
      })
    }
  } catch (error) {
    console.error('Chatbot error:', error)
    messages.value.push({ 
      sender: 'bot', 
      text: "Unable to connect to the assistant server. Please check your connection or reach out via WhatsApp." 
    })
  } finally {
    isTyping.value = false
    await scrollToBottom()
  }
}
</script>

<style scoped>
.scrollbar-thin::-webkit-scrollbar {
  width: 4px;
}
.scrollbar-thin::-webkit-scrollbar-track {
  background: transparent;
}
.scrollbar-thin::-webkit-scrollbar-thumb {
  background: #233554;
  border-radius: 2px;
}
.scrollbar-thin::-webkit-scrollbar-thumb:hover {
  background: #22D3EE;
}
</style>