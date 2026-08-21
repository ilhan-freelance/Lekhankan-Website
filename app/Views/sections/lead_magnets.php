<!-- FREE DOWNLOADABLE LEAD MAGNETS & CHECKLISTS SECTION (LIGHT THEME) -->
<section id="lead-magnets" class="py-10 sm:py-16 bg-gradient-to-br from-ivory-100 via-white to-amber-50/30 text-slate-900 relative overflow-hidden border-t border-slate-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 space-y-6 sm:space-y-8">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto space-y-3 reveal">
      <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-indigo-900 uppercase tracking-tight">
        FREE <span class="bg-gradient-to-r from-saffron-500 via-gold-500 to-amber-600 bg-clip-text text-transparent italic">BOOKKEEPING GUIDES</span> &amp; CHECKLISTS
      </h2>
      <p class="text-slate-600 text-sm sm:text-base font-normal leading-relaxed">
        Download our free standardized checklists, cost calculators, and month-end templates designed for US &amp; Canadian finance leaders.
      </p>
    </div>

    <!-- RESOURCE CARDS GRID -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 reveal">
      
      <!-- Card 01 -->
      <div class="bg-white border border-slate-200 hover:border-saffron-500/60 rounded-2xl p-6 transition-all flex flex-col justify-between space-y-4 group shadow-sm hover:shadow-xl">
        <div class="space-y-3">
          <span class="text-2xl">📋</span>
          <h3 class="font-serif text-base font-bold text-indigo-900 group-hover:text-saffron-600 transition-colors">2026 US Small Business Bookkeeping Checklist</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Step-by-step quarterly &amp; annual accounting tasks to keep your books audit-ready.</p>
        </div>
        <button onclick="openResourceModal('2026 US Small Business Bookkeeping Checklist')" class="w-full py-2.5 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 font-bold text-xs uppercase tracking-wider hover:bg-saffron-500 hover:text-white transition-all">
          Download Free PDF ↓
        </button>
      </div>

      <!-- Card 02 -->
      <div class="bg-white border border-slate-200 hover:border-saffron-500/60 rounded-2xl p-6 transition-all flex flex-col justify-between space-y-4 group shadow-sm hover:shadow-xl">
        <div class="space-y-3">
          <span class="text-2xl">🗓️</span>
          <h3 class="font-serif text-base font-bold text-indigo-900 group-hover:text-saffron-600 transition-colors">Month-End Close Checklist</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Standard closing procedures for accurate monthly financial statements without delays.</p>
        </div>
        <button onclick="openResourceModal('Month-End Close Checklist')" class="w-full py-2.5 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 font-bold text-xs uppercase tracking-wider hover:bg-saffron-500 hover:text-white transition-all">
          Download Free PDF ↓
        </button>
      </div>

      <!-- Card 03 -->
      <div class="bg-white border border-slate-200 hover:border-saffron-500/60 rounded-2xl p-6 transition-all flex flex-col justify-between space-y-4 group shadow-sm hover:shadow-xl">
        <div class="space-y-3">
          <span class="text-2xl">🧮</span>
          <h3 class="font-serif text-base font-bold text-indigo-900 group-hover:text-saffron-600 transition-colors">Bookkeeping Outsourcing Cost Calculator</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Calculate exact annual cost savings of an offshore accounting team vs. hiring in-house.</p>
        </div>
        <button onclick="openResourceModal('Bookkeeping Outsourcing Cost Calculator')" class="w-full py-2.5 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 font-bold text-xs uppercase tracking-wider hover:bg-saffron-500 hover:text-white transition-all">
          Download Calculator ↓
        </button>
      </div>

      <!-- Card 04 -->
      <div class="bg-white border border-slate-200 hover:border-saffron-500/60 rounded-2xl p-6 transition-all flex flex-col justify-between space-y-4 group shadow-sm hover:shadow-xl">
        <div class="space-y-3">
          <span class="text-2xl">🏬</span>
          <h3 class="font-serif text-base font-bold text-indigo-900 group-hover:text-saffron-600 transition-colors">CPA Firm Outsourcing Readiness Checklist</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Capacity planning guide for public accounting firms scaling white-label staff.</p>
        </div>
        <button onclick="openResourceModal('CPA Firm Outsourcing Readiness Checklist')" class="w-full py-2.5 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 font-bold text-xs uppercase tracking-wider hover:bg-saffron-500 hover:text-white transition-all">
          Download Free PDF ↓
        </button>
      </div>

    </div>

  </div>
</section>

<!-- DOWNLOAD RESOURCE MODAL -->
<div id="resource-modal" class="hidden fixed inset-0 z-[999] bg-indigo-900/90 backdrop-blur-xl flex items-center justify-center p-4">
  <div class="bg-white border border-slate-200 rounded-3xl p-8 max-w-md w-full relative space-y-6 shadow-2xl">
    <button onclick="closeResourceModal()" class="absolute top-6 right-6 text-slate-400 hover:text-slate-800 text-2xl font-bold">&times;</button>
    <div class="space-y-2">
      <div class="text-xs font-bold text-saffron-600 uppercase tracking-widest">FREE RESOURCE DOWNLOAD</div>
      <h3 id="modal-resource-title" class="font-serif text-xl font-bold text-indigo-900">Resource Title</h3>
      <p class="text-xs text-slate-600">Enter your business email to instantly receive your free downloadable checklist.</p>
    </div>

    <form onsubmit="handleResourceSubmit(event)" class="space-y-4">
      <div>
        <label class="block text-xs font-bold text-slate-700 mb-1">Work Email Address *</label>
        <input type="email" required placeholder="name@company.com" class="w-full p-3 rounded-xl bg-slate-50 border border-slate-300 text-slate-900 text-xs outline-none focus:border-saffron-500 focus:ring-2 focus:ring-saffron-500/20" />
      </div>
      <div>
        <label class="block text-xs font-bold text-slate-700 mb-1">Company Name</label>
        <input type="text" placeholder="Your Business / CPA Firm" class="w-full p-3 rounded-xl bg-slate-50 border border-slate-300 text-slate-900 text-xs outline-none focus:border-saffron-500 focus:ring-2 focus:ring-saffron-500/20" />
      </div>
      <button type="submit" class="w-full py-3.5 rounded-xl bg-saffron-500 text-white font-bold text-xs uppercase tracking-widest hover:bg-gold-500 transition-all shadow-lg">
        Send Me The Guide
      </button>
    </form>
  </div>
</div>

<script>
  function openResourceModal(title) {
    document.getElementById('modal-resource-title').innerText = title;
    document.getElementById('resource-modal').classList.remove('hidden');
  }
  function closeResourceModal() {
    document.getElementById('resource-modal').classList.add('hidden');
  }
  function handleResourceSubmit(e) {
    e.preventDefault();
    alert('Thank you! Your guide has been sent to your inbox.');
    closeResourceModal();
  }
</script>
