<template>
<div class="w-full min-h-screen bg-[#0A192F] text-slate-300 font-sans selection:bg-[#22D3EE]/30 selection:text-white relative overflow-x-hidden">

    <div class="absolute inset-0 bg-[linear-gradient(to_right,#112240_1px,transparent_1px),linear-gradient(to_bottom,#112240_1px,transparent_1px)] bg-[size:5rem_5rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] opacity-40 pointer-events-none"></div>
    <main class="relative z-10 w-full max-w-[1440px] mx-auto px-10 pt-16 pb-32 grid grid-cols-1 lg:grid-cols-12 gap-16 items-center min-h-[calc(100vh-8rem)]">

        <div class="lg:col-span-7 w-full flex flex-col justify-center">
            <div class="flex items-center gap-3 mb-10">
                <span class="relative flex h-4 w-4">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#22D3EE] opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-4 w-4 bg-[#22D3EE]"></span>
                </span>
                <span class="text-sm font-bold tracking-widest text-[#22D3EE] uppercase font-mono">
                    Available For Opportunities
                </span>
            </div>

            <h1 class="text-6xl sm:text-7xl xl:text-8xl font-extrabold text-white tracking-tight leading-[1.0] mb-3">
                Backend Developer.
            </h1>
            <h2 class="text-6xl sm:text-7xl xl:text-8xl font-extrabold text-[#22D3EE] tracking-tight leading-[1.0] mb-10">
                Full-Stack Ready.
            </h2>

            <p class="text-slate-400 text-lg sm:text-2xl max-w-4xl mb-12 leading-relaxed">
                Hi, I'm <span class="text-white font-semibold">Moaz Ali</span>. I build <span class="text-[#22D3EE] font-medium">scalable web applications,</span> REST APIs, and business solutions using Python, Django, Vue.js, and PostgreSQL. I enjoy turning business requirements into reliable software that is easy to maintain and scale.
            </p>

            <div class="flex flex-wrap gap-3.5 mb-16 max-w-3xl">
                <span v-for="tech in techStack" :key="tech" class="px-5 py-3 rounded-xl text-sm font-mono bg-[#112240] border border-[#233554] text-slate-300 hover:border-[#3B82F6] transition-all duration-200">
                    {{ tech }}
                </span>
            </div>

            <div class="flex flex-wrap items-center gap-6">
                <a href="#projects" class="bg-[#3B82F6] hover:bg-blue-600 text-white text-xl font-medium px-10 py-5 rounded-3xl flex items-center gap-3 shadow-2xl shadow-blue-500/10 transition-all duration-200 group">
                    View Projects
                    <span class="group-hover:translate-x-1 transition-transform duration-200">→</span>
                </a>
                <a href="#contact" class="border border-slate-700 hover:border-slate-500 text-slate-300 text-xl font-medium px-10 py-5 rounded-3xl transition-all duration-200 bg-[#112240]/40 backdrop-blur-sm">
                    Contact Me
                </a>
            </div>
        </div>

        <div class="lg:col-span-5 w-full flex items-center justify-center relative mt-12 lg:mt-0">

            <div class="absolute -top-12 -right-4 z-20 bg-[#112240]/95 border border-[#233554] p-6 rounded-2xl shadow-3xl backdrop-blur-md min-w-[160px]">
                <div class="text-xs uppercase tracking-wider text-slate-400 font-mono">Test Coverage</div>
                <div class="text-3xl font-bold text-[#22D3EE] font-mono mt-1">99.4%</div>
            </div>

            <div class="w-full max-w-xl bg-[#0B1220] border border-[#233554] rounded-3xl shadow-3xl overflow-hidden font-mono text-sm sm:text-base relative z-10">

                <div class="bg-[#112240]/70 px-6 py-5 border-b border-[#233554] flex items-center justify-between">
                    <div class="flex items-center space-x-3">
                        <span class="w-4 h-4 rounded-full bg-red-500/80"></span>
                        <span class="w-4 h-4 rounded-full bg-yellow-500/80"></span>
                        <span class="w-4 h-4 rounded-full bg-green-500/80"></span>
                    </div>
                    <span class="text-xs text-slate-500 tracking-wide">moaz@dev:~</span>
                </div>

                <div class="p-10 space-y-7 min-h-[400px] leading-relaxed">
                    <div>
                        <div class="text-[#3B82F6] flex items-center gap-3"><span>&gt;</span> whoami</div>
                        <div class="text-slate-400 mt-2 pl-4">Moaz Ali — Backend Engineer & Founder</div>
                    </div>

                    <div>
                        <div class="text-[#3B82F6] flex items-center gap-3"><span>&gt;</span> python manage.py runserver</div>
                        <div class="text-emerald-400 mt-2 pl-4 flex items-center gap-2">
                            <span>✓</span> Django REST API active on port :8000
                        </div>
                    </div>

                    <div>
                        <div class="text-[#3B82F6] flex items-center gap-3"><span>&gt;</span> docker build -t techhyves-core .</div>
                        <div class="text-slate-500 mt-2 pl-4">↳ Multi-stage layer assembly initialized.</div>
                        <div class="text-emerald-400 pl-4 flex items-center gap-2">
                            <span>✓</span> Core images built successfully.
                        </div>
                    </div>

                    <div class="flex items-center gap-2">
                        <span class="text-[#22D3EE]">&gt;</span>
                        <span class="w-2.5 h-6 bg-[#22D3EE] animate-pulse"></span>
                    </div>
                </div>
            </div>

            <div class="absolute -bottom-12 -left-4 z-20 bg-[#112240]/95 border border-[#233554] p-6 rounded-2xl shadow-3xl backdrop-blur-md min-w-[160px]">
                <div class="text-xs uppercase tracking-wider text-slate-400 font-mono">Live Projects</div>
                <div class="text-3xl font-bold text-white font-mono mt-1">4+</div>
            </div>

        </div>
    </main>
</div>
<section class="relative z-10 w-full max-w-[1440px] mx-auto px-10 pt-8 pb-20">

    <div class="relative flex items-center justify-center my-12">
        <div class="w-full border-t border-slate-800/60"></div>
        <div class="absolute bg-[#0A192F] px-4 flex flex-col items-center gap-2">
            <span class="text-[10px] tracking-[0.3em] uppercase text-slate-500 font-mono font-bold">
                Scroll
            </span>
            <div class="w-[1px] h-12 bg-gradient-to-b from-[#22D3EE] to-transparent animate-pulse"></div>
        </div>
    </div>

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-12 pt-8">

        <div class="flex flex-col gap-1 group">
            <div class="text-5xl sm:text-6xl font-extrabold text-white font-mono tracking-tight group-hover:text-[#22D3EE] transition-colors duration-300">
                2+
            </div>
            <div class="text-sm sm:text-base tracking-wide text-slate-500 font-medium font-sans">
                Years Experience
            </div>
        </div>

        <div class="flex flex-col gap-1 group">
            <div class="text-5xl sm:text-6xl font-extrabold text-[#22D3EE] font-mono tracking-tight group-hover:text-white transition-colors duration-300">
                5+
            </div>
            <div class="text-sm sm:text-base tracking-wide text-slate-500 font-medium font-sans">
                Live Projects
            </div>
        </div>

        <div class="flex flex-col gap-1 group">
            <div class="text-5xl sm:text-6xl font-extrabold text-white font-mono tracking-tight group-hover:text-[#22D3EE] transition-colors duration-300">
                99%
            </div>
            <div class="text-sm sm:text-base tracking-wide text-slate-500 font-medium font-sans">
                Test Coverage
            </div>
        </div>

        <div class="hidden lg:flex flex-col gap-1 group">
            <div class="text-5xl sm:text-6xl font-extrabold text-[#3B82F6] font-mono tracking-tight group-hover:text-[#22D3EE] transition-colors duration-300">
                6+
            </div>
            <div class="text-sm sm:text-base tracking-wide text-slate-500 font-medium font-sans">
                Engineers Managed
            </div>
        </div>

    </div>
</section>
<section id="about" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32 flex flex-col lg:flex-row items-center justify-between gap-16">

    <div class="w-full lg:w-[55%] flex flex-col justify-center text-left">
        <div class="text-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono mb-4">
            01. About
        </div>

        <h2 class="text-4xl sm:text-5xl xl:text-6xl font-black text-white tracking-tight leading-tight mb-10">
            The Engineer Behind the Stack
        </h2>

        <div class="space-y-8 text-slate-400 text-lg sm:text-xl leading-relaxed font-normal">
            <p>
                I'm <span class="text-white font-semibold">Moaz Ali</span>, a Backend Developer with 2+ years of experience building scalable systems and full-stack web applications. Based in Pakistan, I work across <span class="text-white font-semibold">Python (Django, FastAPI)</span>, modern JavaScript solutions, and robust cloud data pipelines.
            </p>

            <p>
                My primary expertise is in Python and Django, where I develop secure <span class="text-white font-semibold">backend systems, database-driven applications, and API integrations.</span> Alongside backend development, I work with Vue.js and Tailwind CSS to create responsive and user-friendly interfaces.
            </p>

            <p>Over the past few years, I've <span class="text-white font-semibold">contributed to projects ranging </span> from school management systems and candidate testing platforms to company websites and service provider applications.</p>

            <p>
                I enjoy solving <span class="text-white font-semibold">real business problems through software</span> and continuously improving my skills in backend architecture, database design, and modern web development.
            </p>
        </div>
    </div>

    <div class="w-full lg:w-[45%] flex items-center justify-center relative mt-12 lg:mt-0">
        <div class="w-full max-w-[540px] bg-[#0B1220] border-2 border-[#233554] rounded-[24px] shadow-[0_25px_60px_-15px_rgba(0,0,0,0.8)] overflow-hidden font-mono text-xs sm:text-sm">

            <div class="bg-[#112240]/80 px-6 py-4 border-b border-[#233554] flex items-center justify-between">
                <div class="flex items-center space-x-2.5">
                    <span class="w-3.5 h-3.5 rounded-full bg-red-500/80"></span>
                    <span class="w-3.5 h-3.5 rounded-full bg-yellow-500/80"></span>
                    <span class="w-3.5 h-3.5 rounded-full bg-green-500/80"></span>
                </div>
                <span class="text-xs text-slate-500 font-bold tracking-wide">moaz.json</span>
            </div>

            <div class="p-8 text-slate-300 space-y-1.5 overflow-x-auto leading-relaxed">
                <div class="text-slate-400">{</div>

                <div class="pl-4">
                    <span class="text-[#3B82F6]">"name"</span>: <span class="text-[#22D3EE]">"Moaz Ali"</span>,
                </div>
                <div class="pl-4">
                    <span class="text-[#3B82F6]">"role"</span>: <span class="text-[#22D3EE]">"Backend Developer"</span>,
                </div>
                <div class="pl-4">
                    <span class="text-[#3B82F6]">"location"</span>: <span class="text-[#22D3EE]">"Pakistan (Remote-Ready)"</span>,
                </div>
                <div class="pl-4">
                    <span class="text-[#3B82F6]">"available"</span>: <span class="text-emerald-400">true</span>,
                </div>

                <div class="pl-4 text-slate-400">
                    <span class="text-[#3B82F6]">"experience"</span>: {
                </div>
                <div class="pl-8">
                    <span class="text-[#3B82F6]">"years"</span>: <span class="text-amber-500">2</span>,
                </div>
                <div class="pl-8">
                    <span class="text-[#3B82F6]">"liveProducts"</span>: <span class="text-amber-500">5+</span>,
                </div>
                <div class="pl-8">
                    <span class="text-[#3B82F6]">"testCoverage"</span>: <span class="text-[#22D3EE]">"99.4%"</span>
                </div>
                <div class="pl-4 text-slate-400">},</div>

                <div class="pl-4 text-slate-400">
                    <span class="text-[#3B82F6]">"stack"</span>: {
                </div>
                <div class="pl-8 text-slate-400">
                    <span class="text-[#3B82F6]">"backend"</span>: [
                </div>
                <div class="pl-12 text-[#22D3EE]">
                    "Python", "Django", "Django REST Framework"
                </div>
                <div class="pl-8 text-slate-400">],</div>
                <div class="pl-8 text-slate-400">
                    <span class="text-[#3B82F6]">"frontend"</span>: [
                </div>
                <div class="pl-12 text-[#22D3EE]">
                    "Vue.js", "React.js", "Tailwind CSS"
                </div>
                <div class="pl-8 text-slate-400">
                    <span class="text-[#3B82F6]">"database"</span>: [
                </div>
                <div class="pl-12 text-[#22D3EE]">
                    "PostgreSQL", "MySQL", "SQLite"
                </div>
                <div class="pl-8 text-slate-400">]</div>
                <div class="pl-4 text-slate-400">}</div>

                <div class="text-slate-400">}</div>
            </div>
        </div>
    </div>

</section>

<!-- 5. SKILLS SECTION (THE FULL TECHNICAL PICTURE) -->
<section id="services" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32">

    <!-- Top Heading Block -->
    <div class="w-full max-w-3xl text-left mb-16">
        <!-- Section Index Tag -->
        <div class="text-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono mb-4">
            02. Skills
        </div>
        <!-- Main Section Title -->
        <h2 class="text-4xl sm:text-5xl xl:text-6xl font-black text-white tracking-tight leading-tight mb-6">
            The Full Technical Picture
        </h2>
        <!-- Subtitle Narrative -->
        <p class="text-slate-400 text-lg sm:text-xl leading-relaxed">
            Backend-first with full-stack depth — structuring reliable server architectures, component-driven frontends, and production-optimized database layers.
        </p>
    </div>

    <!-- Skills Layout Grid Architecture (Perfectly balanced 6-card matrix) -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

        <!-- CARD 1: BACKEND & APIS -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#3B82F6]/50 transition-all duration-300 group shadow-xl">
            <div class="flex items-center gap-3.5 mb-8">
                <div class="p-2.5 bg-[#112240] rounded-xl text-[#22D3EE] group-hover:text-white transition-colors duration-300">
                    <!-- Settings / Gear Icon -->
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0" />
                    </svg>
                </div>
                <h3 class="text-xl font-bold text-white tracking-wide">Backend & APIs</h3>
            </div>

            <div class="space-y-6">
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">Python (Django / FastAPI)</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[95%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">RESTful API Design</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[90%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-400">Authentication & Authorization</span><span class="text-slate-500">Advanced</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] opacity-70 w-[85%]"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 2: FRONTEND -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#22D3EE]/50 transition-all duration-300 group shadow-xl">
            <div class="flex items-center gap-3.5 mb-8">
                <div class="p-2.5 bg-[#112240] rounded-xl text-[#22D3EE] group-hover:text-white transition-colors duration-300">
                    <!-- Monitor Desktop Icon -->
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                </div>
                <h3 class="text-xl font-bold text-white tracking-wide">Frontend</h3>
            </div>

            <div class="space-y-6">
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">Vue.js / React.js</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[88%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">Tailwind CSS Architecture</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[92%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-400">Responsive UI Development</span><span class="text-slate-500">Advanced</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] opacity-70 w-[80%]"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 3: DATABASES -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#3B82F6]/50 transition-all duration-300 group shadow-xl">
            <div class="flex items-center gap-3.5 mb-8">
                <div class="p-2.5 bg-[#112240] rounded-xl text-[#22D3EE] group-hover:text-white transition-colors duration-300">
                    <!-- Server / Database Icon -->
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" />
                    </svg>
                </div>
                <h3 class="text-xl font-bold text-white tracking-wide">Databases</h3>
            </div>

            <div class="space-y-6">
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">PostgreSQL / MySQL</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[90%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">MongoDB Database</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[85%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-400">Database Design</span><span class="text-slate-500">Advanced</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] opacity-70 w-[82%]"></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 4: Deployment -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#3B82F6]/50 transition-all duration-300 group shadow-xl">
            <div class="flex items-center gap-3.5 mb-8">
                <div class="p-2.5 bg-[#112240] rounded-xl text-[#22D3EE] group-hover:text-white transition-colors duration-300">
                    <!-- Cloud Infrastructure Icon -->
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
                    </svg>
                </div>
                <h3 class="text-xl font-bold text-white tracking-wide">Deployment</h3>
            </div>

            <div class="space-y-6">
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">AWS</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[88%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">Render</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[88%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-300 font-bold">Git & GitHub</span><span class="text-[#22D3EE]">Expert</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] w-[90%]"></div>
                    </div>
                </div>
                <div class="space-y-2">
                    <div class="flex justify-between items-center text-sm font-mono"><span class="text-slate-400">Production Deployment</span><span class="text-slate-500">Advanced</span></div>
                    <div class="h-1.5 w-full bg-[#112240] rounded-full overflow-hidden">
                        <div class="h-full bg-gradient-to-r from-[#3B82F6] to-[#22D3EE] opacity-70 w-[82%]"></div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</section>

<!-- 6. PROJECTS SECTION (PRODUCTION WORK & CASE STUDIES) -->
<section id="work" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32">

    <!-- Top Heading Block -->
    <div class="w-full max-w-3xl text-left mb-16">
        <!-- Section Index Tag -->
        <div class="text-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono mb-4">
            03. Projects
        </div>
        <!-- Main Section Title -->
        <h2 class="text-4xl sm:text-5xl xl:text-6xl font-black text-white tracking-tight leading-tight mb-6">
            Production Work & Case Studies
        </h2>
        <!-- Subtitle Narrative -->
        <p class="text-slate-400 text-lg sm:text-xl leading-relaxed">
            Real systems built for real traffic. Each case study covers architecture decisions, technical challenges, and measurable outcomes.
        </p>
    </div>

    <!-- Projects Cards Layout Grid Matrix -->
    <div id="projects" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

        <!-- CARD 1: Candidate Test Platform -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#3B82F6]/50 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div>
                <!-- Status Ribbon Block -->
                <div class="flex justify-between items-center mb-6 font-mono text-xs">
                    <div class="flex items-center gap-2 text-emerald-400 bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/20">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                        Live
                    </div>
                    <span class="text-slate-500 font-bold">2026</span>
                </div>

                <!-- Project Identity Header -->
                <h3 class="text-2xl font-black text-white tracking-wide mb-2 group-hover:text-[#22D3EE] transition-colors duration-300">
                    Candidate Test Platform
                </h3>
                <p class="text-sm font-semibold text-[#22D3EE] font-mono mb-6 leading-snug">
                    Online Exam & Candidate Management System
                </p>
                <p class="text-slate-400 text-sm sm:text-base leading-relaxed mb-8">
                    An online assessment platform that allows organizations to conduct tests, manage candidates, and evaluate results efficiently.

                    Built a full-stack system for online evaluations with role-based access, automated scoring logic, and structured candidate management.
                </p>
            </div>

            <!-- Metrics Analytics Grid Frame & Tags -->
            <div class="space-y-6 pt-6 border-t border-[#233554]">
                <div class="grid grid-cols-2 gap-4 font-mono">
                    <div>
                        <div class="text-lg font-bold text-white tracking-tight">3-Month</div>
                        <div class="text-[11px] text-slate-500 uppercase tracking-wider mt-0.5">Delivery Timeline</div>
                    </div>
                    <div>
                        <div class="text-lg font-bold text-[#22D3EE] tracking-tight">LoRA</div>
                        <div class="text-[11px] text-slate-500 uppercase tracking-wider mt-0.5">Custom Training</div>
                    </div>
                </div>

                <div class="flex flex-wrap gap-2 text-xs font-mono font-bold pt-2">
                    <span class="text-[#3B82F6] bg-[#3B82F6]/10 px-3 py-1 rounded-md">Django</span>
                    <span class="text-slate-400 bg-[#112240] px-3 py-1 rounded-md">Vue.js</span>
                    <span class="text-slate-400 bg-[#112240] px-3 py-1 rounded-md">PostgreSQL</span>
                </div>
            </div>
        </div>

        <!-- CARD 2: HIREHARRY.AI -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#22D3EE]/50 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div>
                <!-- Status Ribbon Block -->
                <div class="flex justify-between items-center mb-6 font-mono text-xs">
                    <div class="flex items-center gap-2 text-emerald-400 bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/20">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                        Live
                    </div>
                    <span class="text-slate-500 font-bold">2026</span>
                </div>

                <!-- Project Identity Header -->
                <h3 class="text-2xl font-black text-white tracking-wide mb-2 group-hover:text-[#22D3EE] transition-colors duration-300">
                    Tool Website
                </h3>
                <p class="text-sm font-semibold text-[#22D3EE] font-mono mb-6 leading-snug">
                    Utility-Based Web Application Platform
                </p>
                <p class="text-slate-400 text-sm sm:text-base leading-relaxed mb-8">
                    A web platform that provides simple online tools to help users perform common digital tasks efficiently.

                    Key Features:
                    Multiple utility tools in one platform,
                    Fast and responsive UI,
                    Clean and minimal user interface,
                    Modular tool-based architecture,
                    Easy navigation between tools.
                </p>
            </div>

            <!-- Metrics Analytics Grid Frame & Tags -->
            <div class="space-y-6 pt-6 border-t border-[#233554]">
                <div class="grid grid-cols-2 gap-4 font-mono">
                    <div>
                        <div class="text-lg font-bold text-white tracking-tight">FastAPI</div>
                        <div class="text-[11px] text-slate-500 uppercase tracking-wider mt-0.5">Core Backend</div>
                    </div>
                    <div>
                        <div class="text-lg font-bold text-[#22D3EE] tracking-tight">99.4%</div>
                        <div class="text-[11px] text-slate-500 uppercase tracking-wider mt-0.5">Test Coverage</div>
                    </div>
                </div>

                <div class="flex flex-wrap gap-2 text-xs font-mono font-bold pt-2">
                    <span class="text-[#3B82F6] bg-[#3B82F6]/10 px-3 py-1 rounded-md">Vue.js</span>
                    <span class="text-slate-400 bg-[#112240] px-3 py-1 rounded-md">Django</span>
                </div>
            </div>
        </div>

        <!-- CARD 3: AI INFLUENCER GENERATOR -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#3B82F6]/50 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div>
                <!-- Status Ribbon Block -->
                <div class="flex justify-between items-center mb-6 font-mono text-xs">

                    <span class="text-slate-500 font-bold">2025</span>
                </div>

                <!-- Project Identity Header -->
                <h3 class="text-2xl font-black text-white tracking-wide mb-2 group-hover:text-[#22D3EE] transition-colors duration-300">
                    School Management System
                </h3>
                <p class="text-sm font-semibold text-[#22D3EE] font-mono mb-6 leading-snug">
                    Educational Administration System
                </p>
                <p class="text-slate-400 text-sm sm:text-base leading-relaxed mb-8">
                    A web-based system designed to manage school operations including students, teachers, classes, and academic records in a structured way.

                    Key Features:
                    Student and teacher management system,
                    Class and subject organization,
                    Attendance tracking system,
                    Academic record management,
                    Role-based access control (Admin / Teacher / Student)
                </p>
            </div>

            <!-- Metrics Analytics Grid Frame & Tags -->
            <div class="space-y-6 pt-6 border-t border-[#233554]">
                <div class="grid grid-cols-2 gap-4 font-mono">
                    <div>
                        <div class="text-lg font-bold text-white tracking-tight">3-Months</div>
                        <div class="text-[11px] text-slate-500 uppercase tracking-wider mt-0.5">FYP</div>
                    </div>

                </div>

                <div class="flex flex-wrap gap-2 text-xs font-mono font-bold pt-2">
                    <span class="text-[#3B82F6] bg-[#3B82F6]/10 px-3 py-1 rounded-md">Django</span>
                    <span class="text-slate-400 bg-[#112240] px-3 py-1 rounded-md">Quasar</span>
                    <span class="text-slate-400 bg-[#112240] px-3 py-1 rounded-md">SQLite</span>
                </div>
            </div>
        </div>

    </div>
    <!-- 6.1 OTHER NOTABLE PROJECTS (TABLE LIST VIEW) -->
    <div class="mt-16 w-full bg-[#0B1220] border-2 border-[#233554] rounded-[24px] overflow-hidden shadow-2xl">

        <!-- Table Header Title Container -->
        <div class="bg-[#112240]/40 px-6 sm:px-8 py-5 border-b border-[#233554]">
            <h4 class="text-sm font-mono font-bold tracking-wider text-slate-300 uppercase">
                Other Notable Projects
            </h4>
        </div>

        <!-- Table Body Row Structure -->
        <div class="divide-y divide-[#233554]/60">

            <!-- ROW 1: FLATGIGS MODULE -->
            <div class="p-6 sm:p-8 flex flex-col sm:flex-row sm:items-center justify-between gap-6 hover:bg-[#112240]/20 transition-colors duration-200 group">
                <div class="space-y-2">
                    <div class="flex flex-wrap items-center gap-3">
                        <h5 class="text-lg font-bold text-white group-hover:text-[#22D3EE] transition-colors duration-200">
                            Flatgigs Portal Integration
                        </h5>
                        <span class="flex items-center gap-1.5 font-mono text-[11px] text-emerald-400 bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">
                            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                            Live
                        </span>
                    </div>
                    <p class="text-sm text-slate-400 max-w-2xl">
                        Custom remote infrastructure modules built utilizing Django frameworks to securely orchestrate multi-regional background pipelines.
                    </p>
                </div>
                <!-- Tech Badges Stack -->
                <div class="flex flex-wrap sm:justify-end gap-2 text-xs font-mono font-bold">
                    <span class="text-[#22D3EE] border border-[#233554] bg-[#112240]/50 px-3 py-1 rounded-full">Python</span>
                    <span class="text-[#22D3EE] border border-[#233554] bg-[#112240]/50 px-3 py-1 rounded-full">Django</span>
                    <span class="text-[#22D3EE] border border-[#233554] bg-[#112240]/50 px-3 py-1 rounded-full">PostgreSQL</span>
                </div>
            </div>

        </div>
    </div>

    <!-- BOTTOM CALL TO ACTION: VIEW ALL PROJECTS BUTTON -->
    <div class="mt-16 w-full flex justify-center">
        <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="group relative inline-flex items-center justify-center px-8 py-4 font-mono text-sm font-bold text-[#22D3EE] border border-[#22D3EE] rounded-xl overflow-hidden shadow-[0_0_20px_rgba(34,211,238,0.1)] hover:shadow-[0_0_35px_rgba(34,211,238,0.25)] transition-all duration-300">
            <span class="absolute inset-0 w-full h-full bg-[#22D3EE]/5 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"></span>
            <span class="relative flex items-center gap-2">
                View All Projects
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 transform group-hover:translate-x-1 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
            </span>
        </a>
    </div>
</section>

<section id="services" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32">

    <div class="w-full max-w-3xl text-center mx-auto mb-20">
        <div class="Servicetext-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono mb-4">
            04. s
        </div>
        <h2 class="text-4xl sm:text-5xl xl:text-6xl font-black text-white tracking-tight leading-tight mb-6">
            What I Build For You
        </h2>
        <p class="text-slate-400 text-lg sm:text-xl max-w-2xl mx-auto leading-relaxed">
            From MVP API to production microservices. Clear deliverables, documented code, and a smooth handoff.
        </p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">

        <div class="relative group rounded-[24px] p-[2px] bg-gradient-to-b from-[#22D3EE]/30 to-transparent shadow-[0_0_40px_rgba(34,211,238,0.05)] hover:shadow-[0_0_50px_rgba(34,211,238,0.15)] transition-all duration-300">
            <div class="absolute -top-3.5 left-8 z-20 bg-[#22D3EE] text-[#0A192F] font-mono text-[10px] font-black tracking-widest uppercase px-3 py-1 rounded-md shadow-lg">
                Most Requested
            </div>

            <div class="w-full h-full bg-[#0B1220] rounded-[22px] p-8 sm:p-10 border border-[#233554]">
                <div class="flex items-start gap-4 mb-6">
                    <div class="p-3 bg-[#112240] rounded-xl text-[#22D3EE]">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0" />
                        </svg>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold text-white tracking-wide">Backend API Development</h3>
                        <p class="text-slate-400 text-sm mt-2 leading-relaxed">
                            Production-ready RESTful APIs built with Python (Django/FastAPI). Secure, documented, and optimized for real-world scale.
                        </p>
                    </div>
                </div>

                <ul class="space-y-4 font-sans text-sm text-slate-300 pt-4 border-t border-[#233554]/60">
                    <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#22D3EE]/40 flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Python Django, FastAPI, or Custom Frameworks</li>
                    <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#22D3EE]/40 flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> REST API Design & OpenAPI / Swagger Documentation</li>
                    <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#22D3EE]/40 flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> JWT / OAuth 2.0 Secure Authentication Protocols</li>
                    <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#22D3EE]/40 flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Database Architecture Design (PostgreSQL, MongoDB, MySQL)</li>
                    <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#22D3EE]/40 flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Deep Unit Testing and Target Layer Validations with PyTest</li>
                </ul>
            </div>
        </div>

        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 sm:p-10 hover:border-[#3B82F6]/40 transition-all duration-300 shadow-xl group">
            <div class="flex items-start gap-4 mb-6">
                <div class="p-3 bg-[#112240] rounded-xl text-[#22D3EE] group-hover:text-white transition-colors duration-300">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-white tracking-wide">Full-Stack Web Development</h3>
                    <p class="text-slate-400 text-sm mt-2 leading-relaxed">
                        End-to-end web application development using high-performance frameworks — from responsive user interfaces to scalable backends.
                    </p>
                </div>
            </div>

            <ul class="space-y-4 font-sans text-sm text-slate-300 pt-4 border-t border-[#233554]/60">
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> React.js or Vue.js Component-Driven Frontends</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Tailwind CSS Utility-First Clean Responsive Layouts</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> State Management with Pinia / Redux Toolkit Depth</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Real-Time Full-Stack Integrations & Telemetry Control</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Semantic SEO Standard and High Loading Speed Execution</li>
            </ul>
        </div>

        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 sm:p-10 hover:border-[#22D3EE]/40 transition-all duration-300 shadow-xl group">
            <div class="flex items-start gap-4 mb-6">
                <div class="p-3 bg-[#112240] rounded-xl text-[#22D3EE] group-hover:text-white transition-colors duration-300">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
                    </svg>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-white tracking-wide">React Native Mobile Apps</h3>
                    <p class="text-slate-400 text-sm mt-2 leading-relaxed">
                        Cross-platform deployment running identical premium user-experiences across native Android and iOS environments.
                    </p>
                </div>
            </div>

            <ul class="space-y-4 font-sans text-sm text-slate-300 pt-4 border-t border-[#233554]/60">
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Native Thread Bridge Performance Tuning & Optimizations</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Local Data Schemas Caching Framework Configurations</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Native Biometrics & Hardware Push Notification Integrations</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Unified State Control Modules shared with Main Web Nodes</li>
            </ul>
        </div>

        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 sm:p-10 hover:border-[#3B82F6]/40 transition-all duration-300 shadow-xl group">
            <div class="flex items-start gap-4 mb-6">
                <div class="p-3 bg-[#112240] rounded-xl text-[#22D3EE] group-hover:text-white transition-colors duration-300">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                    </svg>
                </div>
                <div>
                    <h3 class="text-2xl font-bold text-white tracking-wide">DevOps & Cloud Deployment</h3>
                    <p class="text-slate-400 text-sm mt-2 leading-relaxed">
                        Automated infrastructure setup and high-availability systems scaling via modern cloud container orchestration solutions.
                    </p>
                </div>
            </div>

            <ul class="space-y-4 font-sans text-sm text-slate-300 pt-4 border-t border-[#233554]/60">
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> AWS Cloud Architecture Setup (EC2, S3, IAM Roles)</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Docker Containerization and Multi-Stage Build Configurations</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Automated GitHub Actions or Make.com Flow Pipelines</li>
                <li class="flex items-center gap-3"><span class="flex-shrink-0 w-5 h-5 rounded-full border border-[#233554] flex items-center justify-center text-[#22D3EE] font-black text-xs">✓</span> Dedicated AI Orchestration Deployments on RunPod Cluster Nodes</li>
            </ul>
        </div>

    </div>
    <!-- 7.1 SERVICES DISCOVERY CALL BANNER CARD -->
    <div class="mt-16 w-full bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 sm:p-12 lg:p-16 text-center relative overflow-hidden shadow-2xl hover:border-[#22D3EE]/30 transition-all duration-300">

        <!-- Premium Radial Subtle Gradient Glow Backing -->
        <div class="absolute inset-0 bg-gradient-to-b from-[#22D3EE]/5 to-transparent pointer-events-none"></div>

        <div class="relative z-10 max-w-2xl mx-auto flex flex-col items-center">
            <!-- Main Banner Heading -->
            <h4 class="text-2xl sm:text-3xl font-black text-white tracking-tight mb-4">
                Not sure what you need?
            </h4>

            <!-- Core Supporting Sub-text -->
            <p class="text-slate-400 text-base sm:text-lg leading-relaxed mb-8">
                Let's start with a free 30-minute discovery call. I'll ask the right questions and tell you honestly what your project needs and what it doesn't.
            </p>

            <!-- Premium High-Contrast Call To Action Button -->
            <a href="https://calendly.com/moazali-consulting" class="group relative inline-flex items-center justify-center px-8 py-4 font-mono text-sm font-black text-[#0A192F] bg-[#22D3EE] hover:bg-[#3B82F6] rounded-xl overflow-hidden shadow-[0_0_30px_rgba(34,211,238,0.2)] hover:shadow-[0_0_40px_rgba(59,130,246,0.4)] transition-all duration-300">
                <span class="relative flex items-center gap-2">
                    Get in Touch
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 transform group-hover:translate-x-1 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                    </svg>
                </span>
            </a>
        </div>

    </div>
</section>

<!-- 8. DEVOPS & CLOUD DEPLOYMENT SECTION -->
<section id="devops" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32">

    <!-- Layout Master Grid Structure -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">

        <!-- LEFT COLUMN: NARRATIVE & TECH ARCHITECTURE BLOCKS (7 Columns) -->
        <div class="lg:col-span-7 space-y-12">
            <!-- Heading Group -->
            <div class="space-y-4">
                <div class="text-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono">
                    05. DevOps & Deployment
                </div>
                <h2 class="text-4xl sm:text-5xl font-black text-white tracking-tight leading-none">
                    From Code to Production
                </h2>
                <p class="text-slate-400 text-lg leading-relaxed max-w-xl">
                    I don't just write the code I deploy it, monitor it, and make sure it stays running. Full ownership from git push to Grafana.
                </p>
            </div>

            <!-- Architecture Sub-Grid Framework -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">

                <!-- BLOCK 1: CONTAINERIZATION -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-2xl p-6 space-y-4 shadow-xl">
                    <div class="flex items-center gap-3 text-white font-bold text-base">
                        <span class="text-xl">🐳</span> Containerization
                    </div>
                    <div class="flex flex-wrap gap-2 font-mono text-xs font-bold">
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Docker</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Docker Compose</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Multi-stage builds</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Docker Hub</span>
                    </div>
                </div>

                <!-- BLOCK 2: ORCHESTRATION -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-2xl p-6 space-y-4 shadow-xl">
                    <div class="flex items-center gap-3 text-white font-bold text-base">
                        <span class="text-xl">☸️</span> Orchestration
                    </div>
                    <div class="flex flex-wrap gap-2 font-mono text-xs font-bold">
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Kubernetes (EKS)</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Helm Charts</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">HPA / VPA</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">RBAC</span>
                    </div>
                </div>

                <!-- BLOCK 3: CI/CD -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-2xl p-6 space-y-4 shadow-xl">
                    <div class="flex items-center gap-3 text-white font-bold text-base">
                        <span class="text-xl">🔄</span> CI/CD
                    </div>
                    <div class="flex flex-wrap gap-2 font-mono text-xs font-bold">
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">GitHub Actions</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">GitLab CI</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Jenkins</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">ArgoCD</span>
                    </div>
                </div>

                <!-- BLOCK 4: CLOUD PLATFORMS -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-2xl p-6 space-y-4 shadow-xl">
                    <div class="flex items-center gap-3 text-white font-bold text-base">
                        <span class="text-xl">☁️</span> Cloud Platforms
                    </div>
                    <div class="flex flex-wrap gap-2 font-mono text-xs font-bold">
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">AWS (EC2, S3, RDS)</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">RunPod Cluster</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Vercel</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Railway</span>
                    </div>
                </div>

                <!-- BLOCK 5: INFRASTRUCTURE AS CODE -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-2xl p-6 space-y-4 shadow-xl">
                    <div class="flex items-center gap-3 text-white font-bold text-base">
                        <span class="text-xl">📋</span> Infrastructure as Code
                    </div>
                    <div class="flex flex-wrap gap-2 font-mono text-xs font-bold">
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Terraform</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Ansible</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">AWS CDK</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Pulumi</span>
                    </div>
                </div>

                <!-- BLOCK 6: OBSERVABILITY -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-2xl p-6 space-y-4 shadow-xl">
                    <div class="flex items-center gap-3 text-white font-bold text-base">
                        <span class="text-xl">📊</span> Observability
                    </div>
                    <div class="flex flex-wrap gap-2 font-mono text-xs font-bold">
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Prometheus + Grafana</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Loki</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Jaeger</span>
                        <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-3 py-1.5 rounded-full">Datadog</span>
                    </div>
                </div>

            </div>
        </div>

        <!-- RIGHT COLUMN: HIGH-FI PREMIUM CODE TERMINAL CONTAINER (5 Columns) -->
        <div class="lg:col-span-5 w-full space-y-6">

            <!-- Terminal Base frame Box -->
            <div class="w-full bg-[#070D19] border-2 border-[#233554] rounded-2xl overflow-hidden shadow-2xl font-mono text-xs sm:text-sm">
                <!-- Window Decorative Header Bar -->
                <div class="bg-[#0B1220] px-4 py-3 border-b border-[#233554] flex items-center justify-between">
                    <div class="flex items-center gap-2">
                        <span class="w-3 h-3 rounded-full bg-[#EF4444]"></span>
                        <span class="w-3 h-3 rounded-full bg-[#F59E0B]"></span>
                        <span class="w-3 h-3 rounded-full bg-[#10B981]"></span>
                    </div>
                    <div class="text-slate-500 font-bold text-xs select-none">
                        .github/workflows/deploy.yml
                    </div>
                    <div class="w-10"></div> <!-- Layout spacer -->
                </div>

                <!-- Terminal Code Stream Content Area -->
                <div class="p-5 overflow-x-auto text-slate-300 space-y-2 leading-relaxed bg-[#070D19] max-h-[580px] overflow-y-auto custom-scrollbar">
                    <div><span class="text-pink-400">name</span>: Deploy to Production</div>
                    <div class="mt-2"><span class="text-pink-400">on</span>:</div>
                    <div class="pl-4"><span class="text-pink-400">push</span>:</div>
                    <div class="pl-8"><span class="text-pink-400">branches</span>: [main]</div>

                    <div class="mt-4"><span class="text-pink-400">jobs</span>:</div>
                    <div class="pl-4"><span class="text-pink-400">test</span>:</div>
                    <div class="pl-8"><span class="text-blue-400">runs-on</span>: ubuntu-latest</div>
                    <div class="pl-8"><span class="text-pink-400">steps</span>:</div>
                    <div class="pl-12">- <span class="text-blue-400">uses</span>: actions/checkout@v4</div>
                    <div class="pl-12">- <span class="text-blue-400">uses</span>: actions/setup-python@v5</div>
                    <div class="pl-14"><span class="text-pink-400">with</span>: { <span class="text-blue-400">python-version</span>: <span class="text-emerald-400">'3.11'</span> }</div>
                    <div class="pl-12">- <span class="text-blue-400">run</span>: pip install -r requirements.txt</div>
                    <div class="pl-12">- <span class="text-blue-400">run</span>: pytest --cov</div>

                    <div class="mt-4 pl-4"><span class="text-pink-400">build-and-push</span>:</div>
                    <div class="pl-8"><span class="text-blue-400">needs</span>: test</div>
                    <div class="pl-8"><span class="text-blue-400">runs-on</span>: ubuntu-latest</div>
                    <div class="pl-8"><span class="text-pink-400">steps</span>:</div>
                    <div class="pl-12">- <span class="text-blue-400">name</span>: Build Docker Image</div>
                    <div class="pl-12"><span class="text-blue-400">run</span>: |</div>
                    <div class="pl-16 text-slate-400">docker build -t $IMAGE:$SHA .</div>
                    <div class="pl-16 text-slate-400">docker push $IMAGE:$SHA</div>

                    <div class="mt-4 pl-4"><span class="text-pink-400">deploy</span>:</div>
                    <div class="pl-8"><span class="text-blue-400">needs</span>: build-and-push</div>
                    <div class="pl-8"><span class="text-blue-400">runs-on</span>: ubuntu-latest</div>
                    <div class="pl-8"><span class="text-pink-400">steps</span>:</div>
                    <div class="pl-12">- <span class="text-blue-400">name</span>: Rolling deploy to K8s</div>
                    <div class="pl-12"><span class="text-blue-400">run</span>: |</div>
                    <div class="pl-16 text-slate-400">kubectl set image deployment/api api=$IMAGE:$SHA</div>
                    <div class="pl-16 text-slate-400">kubectl rollout status deployment/api --timeout=120s</div>

                    <div class="mt-4 pl-12">- <span class="text-blue-400">name</span>: Notify Discord / Slack</div>
                    <div class="pl-12"><span class="text-pink-400">if</span>: always()</div>
                    <div class="pl-12"><span class="text-blue-400">run</span>: |</div>
                    <div class="pl-16 text-emerald-400">curl -X POST $SLACK_WEBHOOK -d '{"text":"✅ Deploy $SHA complete"}'</div>
                </div>
            </div>

            <!-- Bottom Metric Dashboard Row Array -->
            <div class="grid grid-cols-3 gap-4">
                <!-- Metric Card 1 -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-xl p-4 text-center shadow-md">
                    <div class="text-xl sm:text-2xl font-black text-emerald-400 font-mono">Daily</div>
                    <div class="text-[10px] sm:text-xs text-slate-500 uppercase font-mono tracking-wider mt-1">Deploy Frequency</div>
                </div>
                <!-- Metric Card 2 -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-xl p-4 text-center shadow-md">
                    <div class="text-xl sm:text-2xl font-black text-[#22D3EE] font-mono">&lt; 15min</div>
                    <div class="text-[10px] sm:text-xs text-slate-500 uppercase font-mono tracking-wider mt-1">MTTR Rate</div>
                </div>
                <!-- Metric Card 3 -->
                <div class="bg-[#0B1220] border border-[#233554] rounded-xl p-4 text-center shadow-md">
                    <div class="text-xl sm:text-2xl font-black text-emerald-400 font-mono">&lt; 2%</div>
                    <div class="text-[10px] sm:text-xs text-slate-500 uppercase font-mono tracking-wider mt-1">Change Fail</div>
                </div>
            </div>

        </div>

    </div>
</section>

<!-- 9. EXPERIENCE SECTION (PROFESSIONAL JOURNEY) -->
<section id="experience" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32">

    <!-- Top Heading Block -->
    <div class="w-full max-w-3xl text-left mb-16">
        <!-- Section Index Tag -->
        <div class="text-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono mb-4">
            06. Experience
        </div>
        <!-- Main Section Title -->
        <h2 class="text-4xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-6">
            Professional Journey
        </h2>
        <!-- Subtitle Narrative -->
        <p class="text-slate-400 text-lg sm:text-xl leading-relaxed">
            Building, shipping, and scaling production systems across founder roles, freelance contracts, and enterprise pipelines.
        </p>
    </div>

    <!-- Timeline Parent Container Layout -->
    <div class="relative max-w-5xl mx-auto space-y-12">
        <!-- Vertical Absolute Center-Left Line Guide -->
        <div class="absolute top-4 bottom-4 left-[15px] w-[2px] bg-[#233554]"></div>

        <!-- TIMELINE ITEM 1: TECHHYVES FOUNDER ROLE -->
        <div class="relative pl-12 group">
            <!-- Timeline Concentric Ring Indicator Pointer -->
            <div class="absolute left-0 top-2 z-20 w-[32px] h-[32px] rounded-full bg-[#0A192F] border-2 border-[#233554] group-hover:border-[#22D3EE] flex items-center justify-center transition-colors duration-300">
                <div class="w-2 h-2 rounded-full bg-[#233554] group-hover:bg-[#22D3EE] transition-colors duration-300"></div>
            </div>

            <!-- Main Content Card Box -->
            <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-6 sm:p-8 hover:border-[#3B82F6]/30 transition-all duration-300 shadow-xl">
                <!-- Card Adaptive Header Layer -->
                <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-4 mb-6">
                    <div>
                        <h3 class="text-xl sm:text-2xl font-black text-white group-hover:text-[#22D3EE] transition-colors duration-200">
                            Backend Developer
                        </h3>
                        <div class="flex flex-wrap items-center gap-2 mt-1.5 font-mono text-sm">
                            <a href="#" class="text-[#22D3EE] font-bold hover:underline inline-flex items-center gap-1">
                                TechHyves <span class="text-xs">↗</span>
                            </a>
                            <span class="text-slate-500">•</span>
                            <span class="text-slate-400">Pakistan (Full-Time)</span>
                        </div>
                    </div>

                    <!-- Timeline Duration Tag Frame -->
                    <div class="sm:text-right flex flex-row sm:flex-col items-center sm:items-end justify-between sm:justify-start gap-3 font-mono">
                        <span class="text-xs text-slate-400 font-bold">Oct 2025 — Present</span>
                        <span class="text-[11px] font-bold text-[#22D3EE] bg-[#22D3EE]/10 border border-[#22D3EE]/20 px-3 py-1 rounded-full uppercase tracking-wider">
                            Remote
                        </span>
                    </div>
                </div>

                <!-- Detailed Overview Text Paragraph -->
                <p class="text-slate-400 text-sm sm:text-base leading-relaxed mb-6">
                    Working on backend systems and web applications including internal tools, company websites, and utility-based platforms. Responsible for developing APIs, integrating frontend with backend systems, and maintaining production-ready applications.
                </p>

                <!-- Precision Metric Bullet Point Lists -->
                <ul class="space-y-3.5 text-sm text-slate-300 font-sans">
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Developed and maintained company websites and internal software solutions.</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Built backend APIs and database-driven applications using Django.</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Collaborated on software architecture and feature planning.</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Participated in deployment and maintenance of production applications.</span>
                    </li>
                </ul>
            </div>
        </div>

        <!-- TIMELINE ITEM 2: FREELANCE CONTRACTOR PIPELINES -->
        <div class="relative pl-12 group">
            <!-- Timeline Concentric Ring Indicator Pointer -->
            <div class="absolute left-0 top-2 z-20 w-[32px] h-[32px] rounded-full bg-[#0A192F] border-2 border-[#233554] group-hover:border-[#22D3EE] flex items-center justify-center transition-colors duration-300">
                <div class="w-2 h-2 rounded-full bg-[#233554] group-hover:bg-[#22D3EE] transition-colors duration-300"></div>
            </div>

            <!-- Main Content Card Box -->
            <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-6 sm:p-8 hover:border-[#22D3EE]/30 transition-all duration-300 shadow-xl">
                <!-- Card Adaptive Header Layer -->
                <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-4 mb-6">
                    <div>
                        <h3 class="text-xl sm:text-2xl font-black text-white group-hover:text-[#22D3EE] transition-colors duration-200">
                            Business Development Executive
                        </h3>
                        <div class="flex flex-wrap items-center gap-2 mt-1.5 font-mono text-sm">
                            <span class="text-[#22D3EE] font-bold">Digital Innovation</span>
                            <span class="text-slate-500">•</span>
                            <span class="text-slate-400">Full Time</span>
                        </div>
                    </div>

                    <!-- Timeline Duration Tag Frame -->
                    <div class="sm:text-right flex flex-row sm:flex-col items-center sm:items-end justify-between sm:justify-start gap-3 font-mono">
                        <span class="text-xs text-slate-400 font-bold">Apr 2025 – Sep 2025</span>
                        <span class="text-[11px] font-bold text-amber-400 bg-amber-500/10 border border-amber-500/20 px-3 py-1 rounded-full uppercase tracking-wider">
                            Hybrid
                        </span>
                    </div>
                </div>

                <!-- Detailed Overview Text Paragraph -->
                <p class="text-slate-400 text-sm sm:text-base leading-relaxed mb-6">
                    Worked closely with development and marketing teams to generate leads, manage client outreach, and support project planning. Also contributed to system planning and technical documentation for internal tools.
                </p>

                <!-- Precision Metric Bullet Point Lists -->
                <ul class="space-y-3.5 text-sm text-slate-300 font-sans">
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Managed LinkedIn, Fiverr, and Upwork outreach campaigns</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Wrote project proposals and optimized company profiles</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Worked with developers on lead management system design</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Assisted in software architecture discussions and requirements gathering</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Handled client communication and business coordination</span>
                    </li>
                </ul>
            </div>
        </div>

        <!-- TIMELINE ITEM 3: FREELANCE CONTRACTOR PIPELINES -->
        <div class="relative pl-12 group">
            <!-- Timeline Concentric Ring Indicator Pointer -->
            <div class="absolute left-0 top-2 z-20 w-[32px] h-[32px] rounded-full bg-[#0A192F] border-2 border-[#233554] group-hover:border-[#22D3EE] flex items-center justify-center transition-colors duration-300">
                <div class="w-2 h-2 rounded-full bg-[#233554] group-hover:bg-[#22D3EE] transition-colors duration-300"></div>
            </div>

            <!-- Main Content Card Box -->
            <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-6 sm:p-8 hover:border-[#22D3EE]/30 transition-all duration-300 shadow-xl">
                <!-- Card Adaptive Header Layer -->
                <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-4 mb-6">
                    <div>
                        <h3 class="text-xl sm:text-2xl font-black text-white group-hover:text-[#22D3EE] transition-colors duration-200">
                            Business Development Intern
                        </h3>
                        <div class="flex flex-wrap items-center gap-2 mt-1.5 font-mono text-sm">
                            <span class="text-[#22D3EE] font-bold">Digital Innovation</span>
                            <span class="text-slate-500">•</span>
                            <span class="text-slate-400">Full Time</span>
                        </div>
                    </div>

                    <!-- Timeline Duration Tag Frame -->
                    <div class="sm:text-right flex flex-row sm:flex-col items-center sm:items-end justify-between sm:justify-start gap-3 font-mono">
                        <span class="text-xs text-slate-400 font-bold">Jan 2025 – Mar 2025</span>
                        <span class="text-[11px] font-bold text-amber-400 bg-amber-500/10 border border-amber-500/20 px-3 py-1 rounded-full uppercase tracking-wider">
                            Hybrid
                        </span>
                    </div>
                </div>

                <!-- Detailed Overview Text Paragraph -->
                <p class="text-slate-400 text-sm sm:text-base leading-relaxed mb-6">
                    Learned and practiced business development strategies including client acquisition, proposal writing, and freelance platform optimization.
                </p>

                <!-- Precision Metric Bullet Point Lists -->
                <ul class="space-y-3.5 text-sm text-slate-300 font-sans">
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Created and submitted Upwork proposals</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Supported Fiverr gig optimization and outreach strategies</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Learned lead generation workflows and client handling basics</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Assisted senior team in daily business tasks</span>
                    </li>
                </ul>
            </div>
        </div>

        <!-- TIMELINE ITEM 3: FREELANCE CONTRACTOR PIPELINES -->
        <div class="relative pl-12 group">
            <!-- Timeline Concentric Ring Indicator Pointer -->
            <div class="absolute left-0 top-2 z-20 w-[32px] h-[32px] rounded-full bg-[#0A192F] border-2 border-[#233554] group-hover:border-[#22D3EE] flex items-center justify-center transition-colors duration-300">
                <div class="w-2 h-2 rounded-full bg-[#233554] group-hover:bg-[#22D3EE] transition-colors duration-300"></div>
            </div>

            <!-- Main Content Card Box -->
            <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-6 sm:p-8 hover:border-[#22D3EE]/30 transition-all duration-300 shadow-xl">
                <!-- Card Adaptive Header Layer -->
                <div class="flex flex-col sm:flex-row sm:items-start justify-between gap-4 mb-6">
                    <div>
                        <h3 class="text-xl sm:text-2xl font-black text-white group-hover:text-[#22D3EE] transition-colors duration-200">
                            Frontend Development Intern
                        </h3>
                        <div class="flex flex-wrap items-center gap-2 mt-1.5 font-mono text-sm">
                            <span class="text-[#22D3EE] font-bold">PKLogix</span>
                            <span class="text-slate-500">•</span>
                            <span class="text-slate-400">Full Time</span>
                        </div>
                    </div>

                    <!-- Timeline Duration Tag Frame -->
                    <div class="sm:text-right flex flex-row sm:flex-col items-center sm:items-end justify-between sm:justify-start gap-3 font-mono">
                        <span class="text-xs text-slate-400 font-bold">Oct 2022 – Dec 2022</span>
                        <span class="text-[11px] font-bold text-amber-400 bg-amber-500/10 border border-amber-500/20 px-3 py-1 rounded-full uppercase tracking-wider">
                            Hybrid
                        </span>
                    </div>
                </div>

                <!-- Detailed Overview Text Paragraph -->
                <p class="text-slate-400 text-sm sm:text-base leading-relaxed mb-6">
                    Started development journey by learning frontend fundamentals and working on Vue.js-based UI components.
                </p>

                <!-- Precision Metric Bullet Point Lists -->
                <ul class="space-y-3.5 text-sm text-slate-300 font-sans">
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Learned Vue.js fundamentals and component structure</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Built basic UI components and layouts</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Worked on responsive design implementation</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="text-[#22D3EE] font-mono mt-0.5 select-none">›</span>
                        <span>Collaborated with team for frontend integration tasks</span>
                    </li>
                </ul>
            </div>
        </div>

    </div>
</section>

<!-- 10. TESTIMONIALS SECTION -->
<section id="testimonials" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32">

    <!-- Top Heading Block -->
    <div class="w-full max-w-3xl text-center mx-auto mb-16">
        <!-- Section Index Tag -->
        <div class="text-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono mb-4">
            06. Testimonials
        </div>
        <!-- Main Section Title -->
        <h2 class="text-4xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-6">
            What Clients & Colleagues Say
        </h2>
    </div>

    <!-- Testimonials Grid Matrix Layout -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-6xl mx-auto">

        <!-- CARD 1: GLOBAL UPWORK CLIENT FEEDBACK -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#3B82F6]/30 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div class="space-y-6">
                <!-- 5-Star Rating Element Layer -->
                <div class="flex items-center gap-1 text-[#22D3EE] text-sm tracking-widest select-none">
                    ★★★★★
                </div>
                <!-- Testimonial Core Text Block -->
                <p class="text-slate-400 text-base sm:text-lg italic leading-relaxed font-sans">
                    "Moaz consistently delivered clean backend work and was reliable in handling API development tasks. He understands requirements quickly and executes with minimal supervision."
                </p>
            </div>

            <!-- User Identity Meta Profile Footer -->
            <div class="flex items-center gap-4 pt-6 mt-8 border-t border-[#233554]/60">
                <!-- Initial Badge Avatar -->
                <div class="w-12 h-12 rounded-full bg-[#112240] border border-[#3B82F6]/30 flex items-center justify-center font-mono font-bold text-sm text-[#22D3EE] select-none">
                    MB
                </div>
                <div>
                    <h4 class="text-base font-bold text-white tracking-wide">Muhammad Burhan</h4>
                    <p class="text-xs font-mono text-slate-500 mt-0.5">Backend Developer Colleague</p>
                </div>
            </div>
        </div>

        <!-- CARD 2: DASHBOARD BI SYSTEM DELIVERY FEEDBACK -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#22D3EE]/30 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div class="space-y-6">
                <!-- 5-Star Rating Element Layer -->
                <div class="flex items-center gap-1 text-[#22D3EE] text-sm tracking-widest select-none">
                    ★★★★★
                </div>
                <!-- Testimonial Core Text Block -->
                <p class="text-slate-400 text-base sm:text-lg italic leading-relaxed font-sans">
                    "His work on our internal systems improved stability and made data handling much more structured. Communication was clear throughout the project."
                </p>
            </div>

            <!-- User Identity Meta Profile Footer -->
            <div class="flex items-center gap-4 pt-6 mt-8 border-t border-[#233554]/60">
                <!-- Initial Badge Avatar -->
                <div class="w-12 h-12 rounded-full bg-[#112240] border border-[#22D3EE]/30 flex items-center justify-center font-mono font-bold text-sm text-[#22D3EE] select-none">
                    SK
                </div>
                <div>
                    <h4 class="text-base font-bold text-white tracking-wide">Sarah Khan</h4>
                    <p class="text-xs font-mono text-slate-500 mt-0.5">Project Coordinator</p>
                </div>
            </div>
        </div>

        <!-- CARD 3: DASHBOARD BI SYSTEM DELIVERY FEEDBACK -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#22D3EE]/30 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div class="space-y-6">
                <!-- 5-Star Rating Element Layer -->
                <div class="flex items-center gap-1 text-[#22D3EE] text-sm tracking-widest select-none">
                    ★★★★★
                </div>
                <!-- Testimonial Core Text Block -->
                <p class="text-slate-400 text-base sm:text-lg italic leading-relaxed font-sans">
                    "He handled both technical and coordination tasks well during our collaboration. Especially strong in backend logic and database structuring."
                </p>
            </div>

            <!-- User Identity Meta Profile Footer -->
            <div class="flex items-center gap-4 pt-6 mt-8 border-t border-[#233554]/60">
                <!-- Initial Badge Avatar -->
                <div class="w-12 h-12 rounded-full bg-[#112240] border border-[#22D3EE]/30 flex items-center justify-center font-mono font-bold text-sm text-[#22D3EE] select-none">
                    LE
                </div>
                <div>
                    <h4 class="text-base font-bold text-white tracking-wide">Lucia Elena</h4>
                    <p class="text-xs font-mono text-slate-500 mt-0.5">Client (Freelance Project)</p>
                </div>
            </div>
        </div>

        <!-- CARD 2: DASHBOARD BI SYSTEM DELIVERY FEEDBACK -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#22D3EE]/30 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div class="space-y-6">
                <!-- 5-Star Rating Element Layer -->
                <div class="flex items-center gap-1 text-[#22D3EE] text-sm tracking-widest select-none">
                    ★★★★★
                </div>
                <!-- Testimonial Core Text Block -->
                <p class="text-slate-400 text-base sm:text-lg italic leading-relaxed font-sans">
                    "Good understanding of full-stack flow. He was able to connect frontend and backend efficiently and fix issues quickly when needed"
                </p>
            </div>

            <!-- User Identity Meta Profile Footer -->
            <div class="flex items-center gap-4 pt-6 mt-8 border-t border-[#233554]/60">
                <!-- Initial Badge Avatar -->
                <div class="w-12 h-12 rounded-full bg-[#112240] border border-[#22D3EE]/30 flex items-center justify-center font-mono font-bold text-sm text-[#22D3EE] select-none">
                    AA
                </div>
                <div>
                    <h4 class="text-base font-bold text-white tracking-wide">Ahsan Ali</h4>
                    <p class="text-xs font-mono text-slate-500 mt-0.5">Team Member</p>
                </div>
            </div>
        </div>

    </div>
</section>

<!-- 11. BLOG / TECHNICAL WRITING SECTION -->
<section id="blog" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32">

    <!-- Top Heading Block -->
    <div class="w-full max-w-3xl text-left mb-16">
        <!-- Section Index Tag -->
        <div class="text-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono mb-4">
            09. Blog
        </div>
        <!-- Main Section Title -->
        <h2 class="text-4xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-6">
            Technical Writing
        </h2>
        <!-- Subtitle Narrative -->
        <p class="text-slate-400 text-lg sm:text-xl leading-relaxed">
            Deep dives into backend engineering, API design, and DevOps — written from real production experience.
        </p>
    </div>

    <!-- Blog Cards Layout Grid Matrix -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">

        <!-- CARD 1: DJANGO VS FASTAPI -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#3B82F6]/30 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div>
                <!-- Metadata Timeline Row -->
                <div class="flex justify-between items-center mb-6 font-mono text-xs text-slate-500 font-bold">
                    <span>May 14, 2026</span>
                    <span>8 min read</span>
                </div>

                <!-- Identity Header & Summary -->
                <h3 class="text-xl font-bold text-white tracking-wide mb-4 group-hover:text-[#22D3EE] transition-colors duration-200 leading-snug">
                    Django vs FastAPI: Choosing the Right Python Backend Framework
                </h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-8">
                    After building backends in both Django and FastAPI for production projects, here are the practical differences in developer experience, performance, and when each is the right tool.
                </p>
            </div>

            <!-- Tags Footer Matrix & Call to Action -->
            <div class="space-y-6 pt-6 border-t border-[#233554]/60">
                <div class="flex flex-wrap gap-2 text-[11px] font-mono font-bold">
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">Python</span>
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">Django</span>
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">FastAPI</span>
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">Backend</span>
                </div>

                <a href="#" class="inline-flex items-center gap-2 font-mono text-sm font-bold text-[#22D3EE] hover:text-white transition-colors duration-200">
                    Read Article <span>→</span>
                </a>
            </div>
        </div>

        <!-- CARD 2: COMFYUI PRODUCTION PIPELINES -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#22D3EE]/30 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div>
                <!-- Metadata Timeline Row -->
                <div class="flex justify-between items-center mb-6 font-mono text-xs text-slate-500 font-bold">
                    <span>April 22, 2026</span>
                    <span>10 min read</span>
                </div>

                <!-- Identity Header & Summary -->
                <h3 class="text-xl font-bold text-white tracking-wide mb-4 group-hover:text-[#22D3EE] transition-colors duration-200 leading-snug">
                    Scaling ComfyUI Node Matrices for High-Throughput Generative AI
                </h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-8">
                    A practical guide to orchestrating custom LoRA adjustments and automated image generation models through API clusters deployed natively across cloud GPU nodes.
                </p>
            </div>

            <!-- Tags Footer Matrix & Call to Action -->
            <div class="space-y-6 pt-6 border-t border-[#233554]/60">
                <div class="flex flex-wrap gap-2 text-[11px] font-mono font-bold">
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">ComfyUI</span>
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">GenAI</span>
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">RunPod</span>
                </div>

                <a href="#" class="inline-flex items-center gap-2 font-mono text-sm font-bold text-[#22D3EE] hover:text-white transition-colors duration-200">
                    Read Article <span>→</span>
                </a>
            </div>
        </div>

        <!-- CARD 3: POSTGRESQL VS MONGODB HYBRID STORAGE -->
        <div class="bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-8 hover:border-[#3B82F6]/30 transition-all duration-300 flex flex-col justify-between shadow-xl group">
            <div>
                <!-- Metadata Timeline Row -->
                <div class="flex justify-between items-center mb-6 font-mono text-xs text-slate-500 font-bold">
                    <span>March 05, 2026</span>
                    <span>9 min read</span>
                </div>

                <!-- Identity Header & Summary -->
                <h3 class="text-xl font-bold text-white tracking-wide mb-4 group-hover:text-[#22D3EE] transition-colors duration-200 leading-snug">
                    Using SQL and NoSQL Together in Modern Web Applications
                </h3>
                <p class="text-slate-400 text-sm leading-relaxed mb-8">
                    How and why we run both relational structures and document schemas in the same backend—which data layer handles consistency, cache strategies, and real-world infrastructure trade-offs.
                </p>
            </div>

            <!-- Tags Footer Matrix & Call to Action -->
            <div class="space-y-6 pt-6 border-t border-[#233554]/60">
                <div class="flex flex-wrap gap-2 text-[11px] font-mono font-bold">
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">PostgreSQL</span>
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">MongoDB</span>
                    <span class="text-[#22D3EE] bg-[#22D3EE]/5 border border-[#22D3EE]/20 px-2.5 py-1 rounded-full">Database</span>
                </div>

                <a href="#" class="inline-flex items-center gap-2 font-mono text-sm font-bold text-[#22D3EE] hover:text-white transition-colors duration-200">
                    Read Article <span>→</span>
                </a>
            </div>
        </div>

    </div>

</section>
<!-- 12. CONTACT / INQUIRY SECTION -->
<section id="contact" class="relative z-10 w-full max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16 pt-24 pb-32">

    <!-- Layout Master Grid Structure (Asymmetric Split Screen) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">

        <!-- LEFT COLUMN: NARRATIVE & CONTACT QUICK-CARDS (5 Columns) -->
        <div class="lg:col-span-5 space-y-8">
            <!-- Heading Group -->
            <div class="space-y-4">
                <div class="text-sm font-bold tracking-[0.2em] text-[#22D3EE] uppercase font-mono">
                    07. Contact
                </div>
                <h2 class="text-4xl sm:text-5xl font-black text-white tracking-tight leading-tight">
                    Let's Build Something Great
                </h2>
                <p class="text-slate-400 text-base sm:text-lg leading-relaxed">
                    I'm currently available for backend contracts, AI integration pipelines, and custom software architecture work. Whether you have a specific project in mind or want to explore options — reach out.
                </p>
            </div>

            <!-- Quick Information Metadata Cards Stack -->
            <div class="space-y-4 max-w-md">

                <!-- EMAIL CARD -->
                <a href="mailto:moaz55397@gmail.com" class="flex items-center gap-4 bg-[#0B1220] border border-[#233554] rounded-xl p-4 hover:border-[#22D3EE]/30 transition-all duration-300 shadow-md group">
                    <div class="w-10 h-10 rounded-lg bg-[#112240] border border-[#233554] flex items-center justify-center text-slate-400 group-hover:text-[#22D3EE] group-hover:border-[#22D3EE]/30 transition-colors">
                        <!-- SVG Mail Icon -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
                        </svg>
                    </div>
                    <div>
                        <div class="text-[11px] font-mono font-bold text-slate-500 uppercase tracking-wider">Email</div>
                        <div class="text-sm font-mono text-slate-300 group-hover:text-[#22D3EE] transition-colors mt-0.5">moaz55397@gmail.com</div>
                    </div>
                </a>

                <!-- LINKEDIN CARD -->
                <a href="https://linkedin.com/in/moaz-ali10/" target="_blank" class="flex items-center gap-4 bg-[#0B1220] border border-[#233554] rounded-xl p-4 hover:border-[#22D3EE]/30 transition-all duration-300 shadow-md group">
                    <div class="w-10 h-10 rounded-lg bg-[#112240] border border-[#233554] flex items-center justify-center text-slate-400 group-hover:text-[#22D3EE] group-hover:border-[#22D3EE]/30 transition-colors">
                        <!-- SVG LinkedIn Icon -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" class="w-5 h-5">
                            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
                        </svg>
                    </div>
                    <div>
                        <div class="text-[11px] font-mono font-bold text-slate-500 uppercase tracking-wider">LinkedIn</div>
                        <div class="text-sm font-mono text-slate-300 group-hover:text-[#22D3EE] transition-colors mt-0.5">linkedin.com/in/moaz-ali10</div>
                    </div>
                </a>
                <!-- LINKEDIN CARD -->
                <a href="tel:+923137929467" class="flex items-center gap-4 bg-[#0B1220] border border-[#233554] rounded-xl p-4 hover:border-[#22D3EE]/30 transition-all duration-300 shadow-md group">
                    <div class="w-10 h-10 rounded-lg bg-[#112240] border border-[#233554] flex items-center justify-center text-slate-400 group-hover:text-[#22D3EE] group-hover:border-[#22D3EE]/30 transition-colors">
                        <!-- SVG Phone Icon -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25z" />
                        </svg>
                    </div>
                    <div>
                        <div class="text-[11px] font-mono font-bold text-slate-500 uppercase tracking-wider">Phone Number</div>
                        <div class="text-sm font-mono text-slate-300 group-hover:text-[#22D3EE] transition-colors mt-0.5">+92 3137929467</div>
                    </div>
                </a>
                <!-- LINKEDIN CARD -->
                <a href="https://github.com/moazali06" target="_blank" class="flex items-center gap-4 bg-[#0B1220] border border-[#233554] rounded-xl p-4 hover:border-[#22D3EE]/30 transition-all duration-300 shadow-md group">
                    <div class="w-10 h-10 rounded-lg bg-[#112240] border border-[#233554] flex items-center justify-center text-slate-400 group-hover:text-[#22D3EE] group-hover:border-[#22D3EE]/30 transition-colors">
                        <!-- SVG GitHub Icon -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" class="w-5 h-5">
                            <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12" />
                        </svg>
                    </div>
                    <div>
                        <div class="text-[11px] font-mono font-bold text-slate-500 uppercase tracking-wider">GitHub</div>
                        <div class="text-sm font-mono text-slate-300 group-hover:text-[#22D3EE] transition-colors mt-0.5">github.com/moazali06</div>
                    </div>
                </a>

            </div>
        </div>

        <!-- RIGHT COLUMN: HIGH-FI CONVERSION INQUIRY FORM (7 Columns) -->
        <div class="lg:col-span-7 w-full">
            <div class="w-full bg-[#0B1220] border-2 border-[#233554] rounded-[24px] p-6 sm:p-10 shadow-2xl">

                <h3 class="text-xl font-bold text-white tracking-wide mb-8">
                    Start a Conversation
                </h3>

                <form @submit.prevent="handleContactSubmit" class="space-y-6">

    <div class="space-y-2">
        <label class="block font-mono text-[10px] font-black text-slate-400 uppercase tracking-widest">
            Your Name <span class="text-[#22D3EE]">*</span>
        </label>
        <input 
            v-model="nameField"
            type="text" 
            placeholder="Moaz Ali" 
            required 
            :disabled="isSubmitting"
            class="w-full bg-[#070D19] border border-[#233554] rounded-xl px-4 py-3.5 font-sans text-sm text-slate-200 placeholder-slate-600 focus:outline-none focus:border-[#22D3EE] focus:ring-1 focus:ring-[#22D3EE] transition-all duration-200 disabled:opacity-50" 
        />
    </div>

    <div class="space-y-2">
        <label class="block font-mono text-[10px] font-black text-slate-400 uppercase tracking-widest">
            Email Address <span class="text-[#22D3EE]">*</span>
        </label>
        <input 
            v-model="emailField"
            type="email" 
            placeholder="name@company.com" 
            required 
            :disabled="isSubmitting"
            class="w-full bg-[#070D19] border border-[#233554] rounded-xl px-4 py-3.5 font-sans text-sm text-slate-200 placeholder-slate-600 focus:outline-none focus:border-[#22D3EE] focus:ring-1 focus:ring-[#22D3EE] transition-all duration-200 disabled:opacity-50" 
        />
    </div>

    <div class="space-y-2">
    <label class="block font-mono text-[10px] font-black text-slate-400 uppercase tracking-widest">
        Project Budget
    </label>
    <div class="relative">
        <select 
            v-model="budgetField"
            :disabled="isSubmitting"
            class="w-full bg-[#070D19] border border-[#233554] rounded-xl px-4 py-3.5 font-sans text-sm text-slate-300 focus:outline-none focus:border-[#22D3EE] appearance-none cursor-pointer transition-all duration-200 disabled:opacity-50"
        >
            <option value="" disabled>Select a range</option>
            <option value="$1,000 — $3,000">$1,000 — $3,000</option>
            <option value="$3,000 — $5,000">$3,000 — $5,000</option>
            <option value="$5,000 — $10,000+">$5,000 — $10,000+</option>
        </select>
        <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-4 text-slate-500">
            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z" />
            </svg>
        </div>
    </div>
</div>

    <div class="space-y-2">
        <label class="block font-mono text-[10px] font-black text-slate-400 uppercase tracking-widest">
            Message <span class="text-[#22D3EE]">*</span>
        </label>
        <textarea 
            v-model="messageField"
            rows="4" 
            required 
            :disabled="isSubmitting"
            placeholder="Tell me about your project, tech stack, timeline, and what you need help with..." 
            class="w-full bg-[#070D19] border border-[#233554] rounded-xl px-4 py-3.5 font-sans text-sm text-slate-200 placeholder-slate-600 focus:outline-none focus:border-[#22D3EE] focus:ring-1 focus:ring-[#22D3EE] transition-all duration-200 resize-none disabled:opacity-50"
        ></textarea>
    </div>

    <div v-if="submitStatus" class="text-xs font-mono transition-all duration-200">
        <p :class="submitStatus.success ? 'text-emerald-400' : 'text-rose-400'">
            {{ submitStatus.success ? '✓' : '⚠' }} {{ submitStatus.message }}
        </p>
    </div>

    <div class="pt-2">
        <button 
            type="submit" 
            :disabled="isSubmitting"
            class="w-full group relative inline-flex items-center justify-center px-8 py-4 font-mono text-sm font-black rounded-xl overflow-hidden transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
            :class="isSubmitting ? 'bg-slate-700 text-slate-400 shadow-none' : 'text-[#0A192F] bg-[#22D3EE] hover:bg-[#3B82F6] shadow-[0_0_30px_rgba(34,211,238,0.2)] hover:shadow-[0_0_40px_rgba(59,130,246,0.4)]'"
        >
            <span class="relative flex items-center gap-2">
                {{ isSubmitting ? 'Sending...' : 'Send Message' }}
                <svg v-if="!isSubmitting" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 transform group-hover:translate-x-1 transition-transform duration-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
            </span>
        </button>
    </div>

</form>
            </div>
        </div>

    </div>
    <!-- GLOWING AVAILABILITY STATUS BOX -->
    <!-- Note: 'max-w-md' ko hata kar 'w-full' lagaya hai aur side ki padding ke liye 'mx-4' ya parent layout use karein -->
    <div class="w-full mt-4 bg-[#0B1220]/60 border border-[#233554] rounded-xl p-5 shadow-lg relative overflow-hidden">
        <div class="flex items-center gap-2.5 text-emerald-400 font-mono text-xs font-bold tracking-wider uppercase mb-2">
            <!-- Glowing Dot Indicator -->
            <span class="relative flex h-2.5 w-2.5">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-400 shadow-[0_0_10px_#10B981]"></span>
            </span>
            Currently Available
        </div>
        <p class="text-slate-400 text-xs sm:text-sm leading-relaxed font-sans">
            Open to full-time roles and freelance contracts. Typical response time: <strong class="text-slate-200 font-bold">within 24 hours</strong>.
        </p>
    </div>

</section>
</template>
<style scoped>
html {
  scroll-behavior: smooth;
  /* Agar navigation fixed hai aur section ka heading chhup raha hai, toh ye line help karegi */
  scroll-padding-top: 100px; 
}
</style>
<script setup>
import { ref } from 'vue'
import InteractiveBackground from '../components/InteractiveBackground.vue'

// 1. Form fields ko reactive refs banayein jo input tags ke sath v-model honge
const nameField = ref('')
const emailField = ref('')
const messageField = ref('')
const budgetField = ref('')

// Loading aur status alerts ke liye reactive state trackers
const isSubmitting = ref(false)
const submitStatus = ref(null)

const techStack = ref([
    'Python',
    'Django',
    'Vue.js',
    'React',
    'PostgreSQL',
    'SQL',
    'Tailwind CSS',
    'Bootstrap'
])

// 2. API Call ko function ke andar dalein jo submit event par chalega
const handleContactSubmit = async () => {
  isSubmitting.value = true
  submitStatus.value = null

  try {
    const response = await fetch('http://127.0.0.1:8000/api/contact/submit/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: nameField.value,
        email: emailField.value,
        message: messageField.value,
        budget:budgetField.value,
      })
    })

    const data = await response.json()

    if (response.ok) {
      submitStatus.value = { success: true, message: 'Message sent successfully!' }
      // Form fields ko khali kar dein submit hone ke baad
      nameField.value = ''
      emailField.value = ''
      messageField.value = ''
      budgetField.value = ''
    } else {
      submitStatus.value = { success: false, message: 'Something went wrong. Please check your fields.' }
    }
  } catch (error) {
    submitStatus.value = { success: false, message: 'Unable to connect to the backend server.' }
    console.error('Error submitting form:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script>