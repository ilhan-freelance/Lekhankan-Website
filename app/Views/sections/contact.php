<!-- ═══ SECTION 16: MULTI-STEP LEAD FORM (SPLIT SCREEN) ═══ -->
<section class="lead-form-sec" id="lead-form">
  <div class="container-editorial">
    <div class="split-form-grid">
      
      <!-- Left Visual & Messaging Column -->
      <div class="form-visual-side">
        <div class="eyebrow-tag gold">GET STARTED TODAY</div>
        <h2>LET'S BUILD YOUR OFFSHORE ACCOUNTING TEAM.</h2>
        <p>
          Fill out this brief assessment form to receive a tailored offshore accounting proposal, team structure, and cost reduction breakdown.
        </p>
        
        <div style="margin-top:3rem;padding:2rem;background:rgba(255,255,255,0.04);border-radius:var(--radius-md);border:1px solid var(--border-dark);">
          <div style="font-family:var(--font-serif);font-size:1.5rem;color:var(--saffron);margin-bottom:0.5rem;">Direct Response Guarantee</div>
          <p style="font-size:0.875rem;color:var(--ivory-3);">
            Our Chartered Accountants review all inquiries and respond within 12 business hours with a custom consultation plan.
          </p>
        </div>
      </div>
      
      <!-- Right 4-Step Interactive Form Box -->
      <div class="form-box-card">
        
        <div class="form-step-nav">
          <div class="eyebrow-tag" style="margin:0;">STEP ASSESSMENT</div>
          <div class="form-step-num" id="formStepIndicator">STAGE 01 / 04</div>
        </div>
        
        <form id="lekhankanLeadForm" onsubmit="handleFormSubmit(event)">
          
          <!-- STEP 1: Basic Details -->
          <div id="step1" class="form-step-panel">
            <div class="form-input-group">
              <label class="form-label">FULL NAME *</label>
              <input type="text" id="inpName" class="form-control" placeholder="e.g. Robert Smith" required/>
            </div>
            <div class="form-input-group">
              <label class="form-label">COMPANY NAME *</label>
              <input type="text" id="inpCompany" class="form-control" placeholder="e.g. Acme Financial Group" required/>
            </div>
            <div class="form-input-group">
              <label class="form-label">COUNTRY / LOCATION *</label>
              <select id="inpCountry" class="form-control">
                <option value="USA">United States</option>
                <option value="Canada">Canada</option>
                <option value="Other">Other International</option>
              </select>
            </div>
            <button type="button" class="btn-editorial btn-saffron" style="width:100%;margin-top:1rem;" onclick="goToStep(2)">Continue to Step 2 ➔</button>
          </div>
          
          <!-- STEP 2: Business Profile -->
          <div id="step2" class="form-step-panel" style="display:none;">
            <div class="form-input-group">
              <label class="form-label">INDUSTRY CATEGORY *</label>
              <select id="inpIndustry" class="form-control">
                <option value="CPA Firm">CPA / Accounting Firm</option>
                <option value="E-Commerce">E-Commerce / Retail</option>
                <option value="Healthcare">Healthcare / Medical</option>
                <option value="Real Estate">Real Estate / Property Management</option>
                <option value="Construction">Construction / Contracting</option>
                <option value="Professional Services">Professional Services</option>
              </select>
            </div>
            <div class="form-input-group">
              <label class="form-label">ANNUAL REVENUE RANGE</label>
              <select id="inpRevenue" class="form-control">
                <option value="Under $1M">Under $1 Million</option>
                <option value="$1M - $5M">$1 Million – $5 Million</option>
                <option value="$5M - $20M">$5 Million – $20 Million</option>
                <option value="$20M+">$20 Million+</option>
              </select>
            </div>
            <div class="form-input-group">
              <label class="form-label">PRIMARY ACCOUNTING SOFTWARE</label>
              <select id="inpSoftware" class="form-control">
                <option value="QuickBooks Online">QuickBooks Online</option>
                <option value="Xero">Xero</option>
                <option value="NetSuite">Oracle NetSuite</option>
                <option value="Other">Other / Spreadsheets</option>
              </select>
            </div>
            <div style="display:flex;gap:1rem;margin-top:1rem;">
              <button type="button" class="btn-editorial btn-outline-white" style="flex:1;" onclick="goToStep(1)">← Back</button>
              <button type="button" class="btn-editorial btn-saffron" style="flex:2;" onclick="goToStep(3)">Continue to Step 3 ➔</button>
            </div>
          </div>
          
          <!-- STEP 3: Bookkeeping Scope -->
          <div id="step3" class="form-step-panel" style="display:none;">
            <div class="form-input-group">
              <label class="form-label">NUMBER OF BANK ACCOUNTS</label>
              <input type="text" id="inpBankCount" class="form-control" placeholder="e.g. 3 checking accounts, 2 credit cards"/>
            </div>
            <div class="form-input-group">
              <label class="form-label">APPROX. MONTHLY TRANSACTIONS</label>
              <select id="inpTxnVolume" class="form-control">
                <option value="<100">Under 100 transactions/mo</option>
                <option value="100-500">100 – 500 transactions/mo</option>
                <option value="500-2000">500 – 2,000 transactions/mo</option>
                <option value="2000+">2,000+ transactions/mo</option>
              </select>
            </div>
            <div class="form-input-group">
              <label class="form-label">CURRENT BOOKKEEPING ARRANGEMENT</label>
              <select id="inpCurrentSetup" class="form-control">
                <option value="In-House Staff">In-House Staff</option>
                <option value="Local CPA Firm">Local CPA Firm</option>
                <option value="Owner Managed">Owner Managed</option>
                <option value="Behind / Cleanup Needed">Behind / Cleanup Needed</option>
              </select>
            </div>
            <div style="display:flex;gap:1rem;margin-top:1rem;">
              <button type="button" class="btn-editorial btn-outline-white" style="flex:1;" onclick="goToStep(2)">← Back</button>
              <button type="button" class="btn-editorial btn-saffron" style="flex:2;" onclick="goToStep(4)">Final Step ➔</button>
            </div>
          </div>
          
          <!-- STEP 4: Contact & Submission -->
          <div id="step4" class="form-step-panel" style="display:none;">
            <div class="form-input-group">
              <label class="form-label">WORK EMAIL ADDRESS *</label>
              <input type="email" id="inpEmail" class="form-control" placeholder="r.smith@company.com" required/>
            </div>
            <div class="form-input-group">
              <label class="form-label">PHONE / WHATSAPP NUMBER *</label>
              <input type="tel" id="inpPhone" class="form-control" placeholder="+1 (555) 000-0000" required/>
            </div>
            <div class="form-input-group">
              <label class="form-label">WHAT SPECIFIC HELP DO YOU NEED?</label>
              <textarea id="inpNotes" class="form-control" rows="3" placeholder="Describe your current accounting requirements..."></textarea>
            </div>
            <div style="display:flex;gap:1rem;margin-top:1rem;">
              <button type="button" class="btn-editorial btn-outline-white" style="flex:1;" onclick="goToStep(3)">← Back</button>
              <button type="submit" class="btn-editorial btn-saffron" style="flex:2;">Request Free Assessment ➔</button>
            </div>
          </div>

        </form>
        
      </div>
      
    </div>
  </div>
</section>

<script>
function goToStep(stepNum) {
  for (let i = 1; i <= 4; i++) {
    const el = document.getElementById('step' + i);
    if (el) el.style.display = (i === stepNum) ? 'block' : 'none';
  }
  document.getElementById('formStepIndicator').innerText = `STAGE 0${stepNum} / 04`;
}

function handleFormSubmit(e) {
  e.preventDefault();
  alert('Thank you! Your bookkeeping assessment request has been submitted to Lekhankan. A Chartered Accountant will contact you shortly.');
}
</script>
