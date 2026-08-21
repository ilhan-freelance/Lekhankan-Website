<!-- CONTACT & LEAD GENERATION SECTION -->
<section id="contact" class="py-10 sm:py-16 bg-indigo-900 text-ivory-100 relative overflow-hidden border-t border-gold-500/20 ledger-grid">
  
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 space-y-6 sm:space-y-8">
    
    <!-- Section Header -->
    <div class="text-center max-w-3xl mx-auto space-y-3 reveal">
      <h2 class="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-white uppercase tracking-tight">
        Let's Build Your <span class="bg-gradient-to-r from-saffron-500 via-gold-500 to-amber-200 bg-clip-text text-transparent italic">Offshore Finance Team</span>
      </h2>
      <p class="text-slate-300 text-sm sm:text-base font-normal leading-relaxed">
        Complete the assessment details below. Our accounting specialists will evaluate your requirements and send a customized proposal within 24 hours.
      </p>
    </div>

    <!-- 12-FIELD QUALIFYING FORM -->
    <div class="max-w-4xl mx-auto bg-white/5 backdrop-blur-xl border border-gold-500/30 rounded-3xl p-8 sm:p-12 shadow-2xl reveal">
      
      <form onsubmit="handleLeadSubmit(event)" class="space-y-6">
        
        <!-- ROW 1: Name & Company -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">1. Full Name *</label>
            <input type="text" required placeholder="John Smith" class="f-input" />
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">2. Company / Firm Name *</label>
            <input type="text" required placeholder="Smith &amp; Associates CPA / Acme Inc" class="f-input" />
          </div>
        </div>

        <!-- ROW 2: Country & Industry -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">3. Country *</label>
            <select required class="f-select">
              <option value="United States">United States</option>
              <option value="Canada">Canada</option>
              <option value="Other">Other</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">4. Industry *</label>
            <select required class="f-select">
              <option value="CPA / Accounting Firm">CPA &amp; Accounting Firm</option>
              <option value="E-Commerce & Retail">E-Commerce &amp; Retail</option>
              <option value="Healthcare & Medical">Healthcare &amp; Medical Clinics</option>
              <option value="Real Estate & Housing">Real Estate &amp; Property Management</option>
              <option value="Construction & Build">Construction &amp; Contracting</option>
              <option value="Professional Services">Professional Services / Agency</option>
              <option value="Technology & SaaS">Technology &amp; SaaS</option>
              <option value="Other">Other Industry</option>
            </select>
          </div>
        </div>

        <!-- ROW 3: Revenue Range & Primary Software -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">5. Annual Revenue Range</label>
            <select class="f-select">
              <option value="Under $500k">Under $500k</option>
              <option value="$500k - $2M">$500k - $2M</option>
              <option value="$2M - $5M">$2M - $5M</option>
              <option value="$5M - $10M">$5M - $10M</option>
              <option value="$10M+">$10M+</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">6. Accounting Software</label>
            <select class="f-select">
              <option value="QuickBooks Online">QuickBooks Online (QBO)</option>
              <option value="Xero">Xero</option>
              <option value="NetSuite">NetSuite</option>
              <option value="SAP Business One">SAP Business One</option>
              <option value="Bill.com">Bill.com</option>
              <option value="Other">Other Software</option>
            </select>
          </div>
        </div>

        <!-- ROW 4: Bank Accounts & Monthly Transactions -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">7. Number of Bank / CC Accounts</label>
            <select class="f-select">
              <option value="1 - 3 Accounts">1 - 3 Accounts</option>
              <option value="4 - 7 Accounts">4 - 7 Accounts</option>
              <option value="8+ Accounts">8+ Accounts</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">8. Approx. Monthly Transactions</label>
            <select class="f-select">
              <option value="Under 250">Under 250 transactions/mo</option>
              <option value="250 - 750">250 - 750 transactions/mo</option>
              <option value="750 - 2,000">750 - 2,000 transactions/mo</option>
              <option value="2,000+">2,000+ transactions/mo</option>
            </select>
          </div>
        </div>

        <!-- ROW 5: Current Arrangement & Help Needed -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">9. Current Bookkeeping Arrangement</label>
            <select class="f-select">
              <option value="In-house Bookkeeper">In-House Staff</option>
              <option value="Local CPA / Accounting Firm">Local CPA Firm</option>
              <option value="Freelance Bookkeeper">Freelance Bookkeeper</option>
              <option value="Outdated / Need Cleanup">Behind on Books / Need Cleanup</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">10. Primary Goal / Help Needed</label>
            <select class="f-select">
              <option value="White-Label CPA Support">White-Label CPA Support</option>
              <option value="Full Back-Office Bookkeeping">Full Back-Office Bookkeeping</option>
              <option value="AP / AR Management">AP / AR Management</option>
              <option value="Payroll Accounting">Payroll Accounting</option>
              <option value="Historical Bookkeeping Cleanup">Historical Cleanup</option>
              <option value="Dedicated Virtual CFO">Dedicated Virtual CFO</option>
            </select>
          </div>
        </div>

        <!-- ROW 6: Work Email & Phone Number -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">11. Business Email Address *</label>
            <input type="email" required placeholder="john@company.com" class="f-input" />
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-200 uppercase tracking-wider mb-2">12. Direct Phone Number *</label>
            <input type="tel" required placeholder="+1 (555) 000-0000" class="f-input" />
          </div>
        </div>

        <!-- SUBMIT BUTTON -->
        <div class="pt-4 text-center">
          <button type="submit" class="w-full sm:w-auto px-10 py-4 rounded-xl bg-gradient-to-r from-saffron-500 via-gold-500 to-amber-400 text-indigo-900 font-extrabold text-xs uppercase tracking-widest hover:scale-105 transition-all shadow-xl shadow-saffron-500/20">
            Submit Assessment &amp; Request Proposal →
          </button>
        </div>

      </form>

    </div>

  </div>
</section>

<script>
  function handleLeadSubmit(e) {
    e.preventDefault();
    alert('Thank you! Your assessment has been received. A senior Lekhankan accounting consultant will contact you within 24 hours with your customized proposal.');
  }
</script>
