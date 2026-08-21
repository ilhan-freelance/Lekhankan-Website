<!-- OUR SERVICES - INTERACTIVE MASTER TABBED MATRIX (LIGHT THEME) -->
<section id="services" class="py-10 sm:py-16 bg-gradient-to-br from-white via-slate-50 to-ivory-100 text-slate-900 relative overflow-hidden border-t border-slate-200">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 space-y-6 sm:space-y-8">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto space-y-2 reveal">
      <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-indigo-900 uppercase tracking-tight">
        OUR <span class="bg-gradient-to-r from-saffron-500 via-gold-500 to-amber-600 bg-clip-text text-transparent italic">SERVICES</span>
      </h2>
      <p class="text-slate-600 text-sm sm:text-base font-normal leading-relaxed">
        Comprehensive offshore bookkeeping, accounting, accounts payable, accounts receivable, payroll, and virtual CFO solutions built for North American businesses and CPA firms.
      </p>
    </div>

    <!-- TAB NAVIGATION PILLS -->
    <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-2.5 border-b border-slate-200 pb-4 reveal">
      <button onclick="switchServiceTab('tab-bookkeeping', this)" class="svc-tab-btn active px-3.5 sm:px-5 py-2 rounded-xl text-xs sm:text-sm font-bold tracking-wider uppercase transition-all bg-indigo-900 text-white shadow-lg">
        Bookkeeping
      </button>
      <button onclick="switchServiceTab('tab-ap', this)" class="svc-tab-btn px-3.5 sm:px-5 py-2 rounded-xl text-xs sm:text-sm font-bold tracking-wider uppercase transition-all bg-slate-100 text-slate-600 hover:bg-slate-200 border border-slate-200">
        Accounts Payable
      </button>
      <button onclick="switchServiceTab('tab-ar', this)" class="svc-tab-btn px-3.5 sm:px-5 py-2 rounded-xl text-xs sm:text-sm font-bold tracking-wider uppercase transition-all bg-slate-100 text-slate-600 hover:bg-slate-200 border border-slate-200">
        Accounts Receivable
      </button>
      <button onclick="switchServiceTab('tab-payroll', this)" class="svc-tab-btn px-3.5 sm:px-5 py-2 rounded-xl text-xs sm:text-sm font-bold tracking-wider uppercase transition-all bg-slate-100 text-slate-600 hover:bg-slate-200 border border-slate-200">
        Payroll Accounting
      </button>
      <button onclick="switchServiceTab('tab-reporting', this)" class="svc-tab-btn px-3.5 sm:px-5 py-2 rounded-xl text-xs sm:text-sm font-bold tracking-wider uppercase transition-all bg-slate-100 text-slate-600 hover:bg-slate-200 border border-slate-200">
        Financial Reporting
      </button>
      <button onclick="switchServiceTab('tab-virtual', this)" class="svc-tab-btn px-3.5 sm:px-5 py-2 rounded-xl text-xs sm:text-sm font-bold tracking-wider uppercase transition-all bg-slate-100 text-slate-600 hover:bg-slate-200 border border-slate-200">
        Virtual Finance Team
      </button>
    </div>

    <!-- TAB CONTENTS -->
    <div class="relative min-h-0">
      
      <!-- TAB 1: BOOKKEEPING SERVICES -->
      <div id="tab-bookkeeping" class="svc-tab-pane grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5 reveal">
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">📝</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Daily Transaction Recording</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Categorize income, expenses, deposits, and payments accurately according to your Chart of Accounts.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">🏦</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Bank &amp; Credit Card Reconciliation</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Regular bank and credit card statement matching to catch discrepancies, bank fees, and timing differences.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">📊</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">General Ledger &amp; Journal Entries</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Clean GL maintenance, accruals, prepayments, depreciation schedules, and month-end journal posting.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">🧹</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Historical Bookkeeping Cleanup</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Fix outdated, messy, or unreconciled accounts, remove duplicates, and organize books for tax filings.</p>
        </div>
      </div>

      <!-- TAB 2: ACCOUNTS PAYABLE -->
      <div id="tab-ap" class="svc-tab-pane hidden grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">📑</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Invoice Processing &amp; Coding</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Review supplier bills, verify supporting receipts, code expenses, and enter bills into QBO or Bill.com.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">🔐</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Approval Workflow Support</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Manage structured multi-tier authorization workflows to prevent duplicate or unapproved vendor payouts.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">💳</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Bill.com Management</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Day-to-day Bill.com administration, payment queue preparation, and seamless accounting synchronization.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">📉</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">AP Aging &amp; Vendor Reconciliation</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Weekly AP aging schedules, vendor statement matching, and working-capital optimization.</p>
        </div>
      </div>

      <!-- TAB 3: ACCOUNTS RECEIVABLE -->
      <div id="tab-ar" class="svc-tab-pane hidden grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">🧾</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Customer Invoicing</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Timely contract and project billing, verifying pricing, applying sales tax, and posting client invoices.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">💵</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Payment Application</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Accurately apply bank deposits, Stripe/Shopify payouts, and check payments to open customer accounts.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">📞</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Collections Support</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Polite AR follow-ups, customer statements, monitoring overdue invoices, and cash flow predictability.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">📈</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">AR Aging &amp; Revenue Tracking</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Track revenue dimensions by customer, project, or location, alongside detailed aging reports.</p>
        </div>
      </div>

      <!-- TAB 4: PAYROLL ACCOUNTING -->
      <div id="tab-payroll" class="svc-tab-pane hidden grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">💰</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Payroll Journal Entries</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Record gross wages, employer taxes, benefit deductions, and payroll liabilities in your GL.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">⚙️</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Gusto &amp; ADP Integration</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Seamlessly connect payroll reports from Gusto or ADP with your cloud accounting system.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">📋</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Payroll Liability Reconciliation</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Verify payroll tax withholding, 401(k) contributions, health insurance payables, and wage accounts.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">📊</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Payroll Cost Analysis</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Detailed departmental labor cost summaries for monthly management reviews.</p>
        </div>
      </div>

      <!-- TAB 5: FINANCIAL REPORTING -->
      <div id="tab-reporting" class="svc-tab-pane hidden grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">📉</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">P&amp;L, Balance Sheet &amp; Cash Flow</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Monthly closing statement package reflecting true financial health and operating profitability.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">🎯</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Budget vs. Actual Variance</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Compare actual operational results against planned budgets to catch cost overruns early.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">📊</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Financial KPIs &amp; Analysis</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Track gross margins, operating cash conversion, AR turnover days, and unit economics.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-saffron-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-saffron-500/10 border border-saffron-500/30 text-saffron-600 flex items-center justify-center text-xl font-bold">🖥️</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Power BI Executive Dashboards</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Interactive executive dashboards transforming raw transaction data into visual executive intelligence.</p>
        </div>
      </div>

      <!-- TAB 6: VIRTUAL FINANCE TEAM -->
      <div id="tab-virtual" class="svc-tab-pane hidden grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">👤</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Dedicated Bookkeeper</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Full-time or part-time dedicated resource for routine daily bookkeeping and reconciliations.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">🎓</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Senior Staff Accountant</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Advanced accounting support for month-end closing, complex journal entries, and GL supervision.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">⚖️</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Controller Support</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Senior financial oversight, internal controls, accounting policy enforcement, and CPA coordination.</p>
        </div>
        <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 hover:border-gold-500/60 hover:shadow-xl transition-all space-y-2 shadow-sm">
          <div class="w-10 h-10 rounded-xl bg-gold-500/10 border border-gold-500/30 text-gold-600 flex items-center justify-center text-xl font-bold">💼</div>
          <h3 class="font-serif text-base font-bold text-indigo-900">Virtual CFO Services</h3>
          <p class="text-xs text-slate-600 leading-relaxed">Strategic financial planning, forecasting, cash flow modeling, and advisory for growing enterprises.</p>
        </div>
      </div>

    </div>

  </div>
</section>

<script>
  function switchServiceTab(tabId, btn) {
    document.querySelectorAll('.svc-tab-pane').forEach(p => p.classList.add('hidden'));
    document.getElementById(tabId).classList.remove('hidden');
    document.querySelectorAll('.svc-tab-btn').forEach(b => {
      b.classList.remove('bg-indigo-900', 'text-white', 'shadow-lg');
      b.classList.add('bg-slate-100', 'text-slate-600', 'border', 'border-slate-200');
    });
    btn.classList.remove('bg-slate-100', 'text-slate-600', 'border', 'border-slate-200');
    btn.classList.add('bg-indigo-900', 'text-white', 'shadow-lg');
  }
</script>

