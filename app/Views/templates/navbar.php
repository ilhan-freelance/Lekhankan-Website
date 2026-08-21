<!-- NAVBAR -->
<header id="nav" class="fixed top-0 left-0 right-0 w-full z-50 transition-all duration-500">
  <div class="w-full px-6 sm:px-12 lg:px-16 py-5 flex items-center justify-between gap-6 bg-transparent border-b border-transparent transition-all duration-500" id="nav-inner">
    <a href="<?= base_url('#hero') ?>" class="flex items-center gap-3.5 text-decoration-none group">
      <div id="nav-badge" class="w-10 h-10 rounded-xl bg-saffron-500/25 border border-saffron-500/40 backdrop-blur-md flex items-center justify-center text-white font-serif font-bold text-xl shadow-sm group-hover:scale-105 group-hover:bg-saffron-500 group-hover:text-indigo-900 transition-all">L</div>
      <div class="flex flex-col leading-none">
        <span class="font-display text-xl font-black tracking-tight uppercase text-white transition-colors" id="nav-logo">Lekhankan</span>
        <span class="text-[.58rem] font-semibold text-white/70 transition-colors mt-0.5" id="nav-sub">By VRM Vrindam (P) Limited</span>
      </div>
    </a>
    <nav class="hidden xl:flex items-center gap-7" id="nav-links">
      <a href="<?= base_url('#hero') ?>" class="nav-link text-[.7rem] font-extrabold tracking-widest uppercase text-white/90 hover:text-saffron-500 transition-all relative py-1 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[2px] after:bg-saffron-500 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:rounded-full">Home</a>
      <a href="<?= base_url('#brand-story') ?>" class="nav-link text-[.7rem] font-extrabold tracking-widest uppercase text-white/90 hover:text-saffron-500 transition-all relative py-1 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[2px] after:bg-saffron-500 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:rounded-full">Heritage</a>
      <a href="<?= base_url('#services') ?>" class="nav-link text-[.7rem] font-extrabold tracking-widest uppercase text-white/90 hover:text-saffron-500 transition-all relative py-1 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[2px] after:bg-saffron-500 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:rounded-full">Services</a>
      <a href="<?= base_url('#industries') ?>" class="nav-link text-[.7rem] font-extrabold tracking-widest uppercase text-white/90 hover:text-saffron-500 transition-all relative py-1 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[2px] after:bg-saffron-500 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:rounded-full">Industries</a>
      <a href="<?= base_url('#process') ?>" class="nav-link text-[.7rem] font-extrabold tracking-widest uppercase text-white/90 hover:text-saffron-500 transition-all relative py-1 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[2px] after:bg-saffron-500 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:rounded-full">Process</a>
      <a href="<?= base_url('#team') ?>" class="nav-link text-[.7rem] font-extrabold tracking-widest uppercase text-white/90 hover:text-saffron-500 transition-all relative py-1 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[2px] after:bg-saffron-500 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:rounded-full">Team</a>
      <a href="<?= base_url('#lead-magnets') ?>" class="nav-link text-[.7rem] font-extrabold tracking-widest uppercase text-white/90 hover:text-saffron-500 transition-all relative py-1 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-[2px] after:bg-saffron-500 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:rounded-full">Checklists</a>
    </nav>
    <a href="<?= base_url('#contact') ?>" class="hidden md:inline-flex items-center gap-2 py-3 px-6 rounded-xl bg-gradient-to-r from-saffron-500 via-gold-500 to-amber-400 text-indigo-900 text-[.72rem] font-extrabold tracking-widest uppercase shadow-lg shadow-saffron-500/20 hover:scale-105 transition-all whitespace-nowrap">Request Proposal →</a>
    <button id="mob-btn" class="xl:hidden p-2 text-white hover:text-saffron-500 transition-colors" aria-label="Menu">
      <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 6h16M4 12h16M4 18h16"/></svg>
    </button>
  </div>
</header>

<!-- MOBILE MENU -->
<div id="mob-menu" class="hidden fixed inset-0 z-[999] bg-indigo-900/98 backdrop-blur-3xl flex-col items-center justify-center gap-6 text-white">
  <button id="mob-close" class="absolute top-6 right-6 text-white text-4xl leading-none hover:text-saffron-500 transition-colors">&times;</button>
  <a href="<?= base_url('#hero') ?>" class="mob-link font-serif text-2xl font-bold text-white hover:text-saffron-500 transition-colors">Home</a>
  <a href="<?= base_url('#brand-story') ?>" class="mob-link font-serif text-2xl font-bold text-white hover:text-saffron-500 transition-colors">Heritage</a>
  <a href="<?= base_url('#services') ?>" class="mob-link font-serif text-2xl font-bold text-white hover:text-saffron-500 transition-colors">Services</a>
  <a href="<?= base_url('#industries') ?>" class="mob-link font-serif text-2xl font-bold text-white hover:text-saffron-500 transition-colors">Industries</a>
  <a href="<?= base_url('#process') ?>" class="mob-link font-serif text-2xl font-bold text-white hover:text-saffron-500 transition-colors">Process</a>
  <a href="<?= base_url('#team') ?>" class="mob-link font-serif text-2xl font-bold text-white hover:text-saffron-500 transition-colors">Team</a>
  <a href="<?= base_url('#lead-magnets') ?>" class="mob-link font-serif text-2xl font-bold text-white hover:text-saffron-500 transition-colors">Checklists</a>
  <a href="<?= base_url('#contact') ?>" class="mob-link inline-flex items-center gap-2 py-3.5 px-8 rounded-xl bg-saffron-500 text-indigo-900 font-extrabold text-xs tracking-widest uppercase shadow-xl shadow-saffron-500/30 mt-4">Request Proposal</a>
</div>
