<!-- WHY BUSINESSES CHOOSE LEKHANKAN -->
<section id="why-us" class="py-10 sm:py-16 bg-gradient-to-br from-white via-slate-50 to-ivory-100 text-slate-900 relative overflow-hidden border-t border-slate-200">
  
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 space-y-6 sm:space-y-8">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto space-y-3 reveal">
      <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-indigo-900 uppercase tracking-tight">
        Why Businesses Choose <span class="bg-gradient-to-r from-saffron-500 via-gold-500 to-amber-600 bg-clip-text text-transparent italic">Lekhankan</span>
      </h2>
      <p class="text-slate-600 text-sm sm:text-base font-normal leading-relaxed">
        Empowering CPA firms, accounting practices, and growing enterprises across USA &amp; Canada with dedicated offshore accounting teams and cost optimization.
      </p>
    </div>

    <!-- 6 Core Feature Grid -->
    <div class="grid md:grid-cols-3 gap-6">

      <!-- 1. Reduce Accounting Costs by up to 60% -->
      <div class="md:col-span-2 bg-white border border-slate-200 rounded-3xl p-6 sm:p-8 shadow-sm hover:shadow-xl hover:border-saffron-500/50 transition-all reveal-l">
        <div class="flex flex-col h-full space-y-4">
          <div class="inline-flex items-center gap-2 text-xs font-bold tracking-widest uppercase text-saffron-600">
            <span class="w-2 h-2 rounded-full bg-saffron-500"></span> Cost Optimization
          </div>
          <h3 class="font-serif text-2xl sm:text-3xl font-bold text-indigo-900 leading-tight">
            Reduce Accounting Costs by up to <span class="bg-gradient-to-r from-saffron-500 via-gold-500 to-amber-600 bg-clip-text text-transparent italic">60%</span>
          </h3>
          <p class="text-xs sm:text-sm leading-relaxed text-slate-600">
            Access highly qualified accounting professionals without the overhead of hiring an in-house finance department.
          </p>

          <!-- Interactive Savings Calculator -->
          <div class="bg-indigo-900 text-white border border-indigo-800 rounded-2xl p-5 sm:p-6 mt-auto shadow-xl relative space-y-3">
            <div class="flex justify-between items-center">
              <div class="text-[0.68rem] font-bold uppercase tracking-wider text-slate-400">Estimated Annual Cost Savings</div>
              <div class="flex items-center gap-1 bg-white/10 p-0.5 rounded-lg border border-white/15 text-[0.65rem] font-bold">
                <button type="button" id="curr-usd" onclick="setCurrency('USD')" class="px-2 py-0.5 rounded-md bg-saffron-500 text-indigo-900 shadow-sm transition-all">USD ($)</button>
                <button type="button" id="curr-cad" onclick="setCurrency('CAD')" class="px-2 py-0.5 rounded-md text-slate-300 hover:text-white transition-all">CAD ($)</button>
              </div>
            </div>
            <div class="flex items-baseline justify-between">
              <div class="font-serif text-3xl sm:text-4xl font-bold text-saffron-500 tracking-tight" id="roi-val">$64,800 / year</div>
              <span class="text-[0.68rem] font-bold text-saffron-500 bg-saffron-500/20 px-2 py-0.5 rounded-md border border-saffron-500/40" id="roi-pct">Save ~54%</span>
            </div>
            <div class="flex flex-wrap items-center gap-1.5 pt-2">
              <span class="text-[0.65rem] font-bold text-slate-400 uppercase tracking-wider mr-1">Role:</span>
              <button type="button" class="role-btn px-2.5 py-0.5 rounded-full text-[0.68rem] font-bold bg-saffron-500 text-indigo-900 transition-all" data-role="bookkeeper" onclick="setRole('bookkeeper', this)">Bookkeeper</button>
              <button type="button" class="role-btn px-2.5 py-0.5 rounded-full text-[0.68rem] font-bold bg-white/10 text-slate-300 hover:bg-white/20 transition-all" data-role="cpa" onclick="setRole('cpa', this)">CPA / Lead CA</button>
              <button type="button" class="role-btn px-2.5 py-0.5 rounded-full text-[0.68rem] font-bold bg-white/10 text-slate-300 hover:bg-white/20 transition-all" data-role="tax" onclick="setRole('tax', this)">Tax &amp; Payroll</button>
            </div>
            <div class="pt-2">
              <div class="flex justify-between text-xs mb-1"><span class="text-slate-400 font-medium">In-House Overhead</span><span class="text-slate-200 font-bold" id="us-cost">$140,000/yr</span></div>
              <div class="h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full rounded-full bg-slate-500 w-full"></div></div>
            </div>
            <div>
              <div class="flex justify-between text-xs mb-1"><span class="text-saffron-500 font-bold">Lekhankan Dedicated Team</span><span class="text-saffron-500 font-extrabold" id="lk-cost">$75,200/yr</span></div>
              <div class="h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full rounded-full bg-gradient-to-r from-saffron-500 to-gold-500 transition-all duration-500" id="lk-bar" style="width:54%"></div></div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. Dedicated Offshore Accounting Team -->
      <div class="bg-white border border-slate-200 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl hover:border-saffron-500/50 transition-all flex flex-col reveal-r">
        <div class="h-44 overflow-hidden relative">
          <img src="<?= base_url('images/lekhankan_accounting_team.png') ?>" alt="Dedicated Offshore Accounting Team" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500"/>
          <div class="absolute inset-0 bg-gradient-to-t from-indigo-900/70 via-transparent to-transparent"></div>
          <span class="absolute bottom-3 left-4 py-1 px-3 rounded-full bg-saffron-500 text-[0.62rem] font-bold uppercase tracking-wider text-white shadow-md">Dedicated Team</span>
        </div>
        <div class="p-6 flex flex-col flex-1 space-y-3">
          <h3 class="font-serif text-xl font-bold text-indigo-900">Dedicated Offshore Team</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Work with dedicated bookkeepers, accountants, reviewers, and finance specialists aligned specifically with your business.
          </p>
          <a href="<?= base_url('#contact') ?>" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-saffron-600 hover:gap-3 transition-all pt-3 border-t border-slate-100 mt-auto">Learn Team Model →</a>
        </div>
      </div>

      <!-- 3. Qualified Chartered Accountants -->
      <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm hover:shadow-xl hover:border-saffron-500/50 transition-all flex flex-col space-y-3 reveal-l">
        <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">🎓</div>
        <h3 class="font-serif text-xl font-bold text-indigo-900">Qualified Chartered Accountants</h3>
        <p class="text-xs text-slate-600 leading-relaxed">
          Our accounting operations are supervised by Chartered Accountants, ensuring quality, consistency, and professional financial reporting.
        </p>
        <a href="<?= base_url('#contact') ?>" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-saffron-600 hover:gap-3 transition-all pt-3 border-t border-slate-100 mt-auto">Supervision Standard →</a>
      </div>

      <!-- 4. Technology-Driven Accounting -->
      <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm hover:shadow-xl hover:border-saffron-500/50 transition-all flex flex-col space-y-3 reveal-d2">
        <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">⚡</div>
        <h3 class="font-serif text-xl font-bold text-indigo-900">Technology-Driven Accounting</h3>
        <p class="text-xs text-slate-600 leading-relaxed">
          We utilize leading accounting platforms including QuickBooks Online, Xero, Bill.com, Gusto, Dext, Stripe, Hubdoc, and Power BI.
        </p>
        <a href="<?= base_url('#contact') ?>" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-saffron-600 hover:gap-3 transition-all pt-3 border-t border-slate-100 mt-auto">Integrations List →</a>
      </div>

      <!-- 5. Secure & Confidential -->
      <div class="bg-white border border-slate-200 rounded-3xl overflow-hidden shadow-sm hover:shadow-xl hover:border-saffron-500/50 transition-all flex flex-col reveal-r">
        <div class="h-44 overflow-hidden relative">
          <img src="<?= base_url('images/lekhankan_security_analytics.png') ?>" alt="Secure & Confidential Financial Data" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500"/>
          <div class="absolute inset-0 bg-gradient-to-t from-indigo-900/70 via-transparent to-transparent"></div>
          <span class="absolute bottom-3 left-4 py-1 px-3 rounded-full bg-gold-500 text-[0.62rem] font-bold uppercase tracking-wider text-white shadow-md">Bank-Grade Security</span>
        </div>
        <div class="p-6 flex flex-col flex-1 space-y-3">
          <h3 class="font-serif text-xl font-bold text-indigo-900">Secure &amp; Confidential</h3>
          <p class="text-xs text-slate-600 leading-relaxed">
            Your financial information is handled using secure workflows, role-based access, confidentiality agreements, and standardized controls.
          </p>
          <a href="<?= base_url('#contact') ?>" class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-saffron-600 hover:gap-3 transition-all pt-3 border-t border-slate-100 mt-auto">Security Protocols →</a>
        </div>
      </div>

      <!-- 6. Scalable Accounting Solutions -->
      <div class="md:col-span-3 bg-indigo-900 border border-indigo-800 rounded-3xl p-8 text-white relative overflow-hidden shadow-2xl reveal">
        <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="space-y-2 text-center md:text-left">
            <h3 class="font-serif text-2xl sm:text-3xl font-bold text-white">Scalable Accounting Solutions</h3>
            <p class="text-xs sm:text-sm leading-relaxed text-slate-300 max-w-2xl">
              Whether you need one bookkeeper or a complete offshore accounting department, our delivery model grows seamlessly with your business.
            </p>
          </div>
          <a href="<?= base_url('#contact') ?>" class="py-3.5 px-8 rounded-xl bg-saffron-500 text-indigo-900 font-extrabold text-xs tracking-widest uppercase shadow-xl hover:bg-gold-500 hover:scale-105 transition-all whitespace-nowrap">Build Your Team →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  let currentCurr = 'USD';
  let currentRoleMult = 1.0;
  function setCurrency(curr) {
    currentCurr = curr;
    document.getElementById('curr-usd').className = curr === 'USD' ? 'px-2 py-0.5 rounded-md bg-saffron-500 text-indigo-900 shadow-sm transition-all' : 'px-2 py-0.5 rounded-md text-slate-300 hover:text-white transition-all';
    document.getElementById('curr-cad').className = curr === 'CAD' ? 'px-2 py-0.5 rounded-md bg-saffron-500 text-indigo-900 shadow-sm transition-all' : 'px-2 py-0.5 rounded-md text-slate-300 hover:text-white transition-all';
    updateROI(2);
  }
  function setRole(role, btn) {
    document.querySelectorAll('.role-btn').forEach(b => { b.className = 'role-btn px-2.5 py-0.5 rounded-full text-[0.68rem] font-bold bg-white/10 text-slate-300 hover:bg-white/20 transition-all'; });
    btn.className = 'role-btn px-2.5 py-0.5 rounded-full text-[0.68rem] font-bold bg-saffron-500 text-indigo-900 transition-all';
    currentRoleMult = role === 'cpa' ? 1.4 : (role === 'tax' ? 1.2 : 1.0);
    updateROI(2);
  }
  function updateROI(val) {
    const symbol = currentCurr === 'CAD' ? 'C$' : '$';
    const rate = currentCurr === 'CAD' ? 1.35 : 1.0;
    const baseUS = 70000 * val * currentRoleMult * rate;
    const baseLK = 37600 * val * currentRoleMult * rate;
    const savings = baseUS - baseLK;
    const pct = Math.round((savings / baseUS) * 100);
    const valEl = document.getElementById('roi-val');
    const usEl = document.getElementById('us-cost');
    const lkEl = document.getElementById('lk-cost');
    const pctEl = document.getElementById('roi-pct');
    const barEl = document.getElementById('lk-bar');
    if (valEl) valEl.innerText = `${symbol}${Math.round(savings).toLocaleString()} / yr`;
    if (usEl) usEl.innerText = `${symbol}${Math.round(baseUS).toLocaleString()}/yr`;
    if (lkEl) lkEl.innerText = `${symbol}${Math.round(baseLK).toLocaleString()}/yr`;
    if (pctEl) pctEl.innerText = `Save ~${pct}%`;
    if (barEl) barEl.style.width = `${100 - pct}%`;
  }
</script>
