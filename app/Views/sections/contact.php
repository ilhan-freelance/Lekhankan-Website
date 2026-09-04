<!-- ═══ SECTION: CONTACT US (FORMAL LIGHT EDITORIAL DESIGN — 3-COLUMN COMPACT WIDESCREEN) ═══ -->
<section class="lead-form-sec" id="lead-form" style="padding:4rem 0 4.5rem;background:#FFFFFF;color:var(--midnight);position:relative;">
  <div class="container-editorial" style="max-width:1240px;margin:0 auto;position:relative;z-index:2;">
    
    <!-- Section Title & Subheading -->
    <div style="text-align:center;max-width:860px;margin:0 auto 2.5rem;">
      <h2 class="serif-heading" style="font-size:clamp(2.5rem, 4vw, 3.5rem);color:var(--midnight);margin:0 0 0.75rem;line-height:1.1;">
        CONTACT <span style="color:var(--saffron);">US</span>
      </h2>
      <div style="width:64px;height:3px;background:linear-gradient(90deg, var(--saffron), var(--gold));margin:0.75rem auto 0;border-radius:2px;"></div>
      <h3 style="font-family:var(--font-serif);font-size:1.25rem;color:var(--midnight);margin:1.1rem 0 0;font-weight:600;">
        Let's Build Your Offshore Accounting Team &bull; Book a Free Consultation
      </h3>
    </div>
    
    <!-- Single Window Formal Form Box (Light Widescreen 3-Column Grid) -->
    <div class="contact-form-card">
      
      <form id="lekhankanLeadForm" onsubmit="handleFormSubmit(event)">
        
        <div class="contact-3col-grid">
          
          <!-- Row 1: Basics -->
          <!-- 1. Full Name -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">1. FULL NAME *</label>
            <input type="text" id="inpName" class="form-control" placeholder="e.g. Robert Smith" required style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;"/>
          </div>

          <!-- 2. Work Email -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">2. WORK EMAIL ADDRESS *</label>
            <input type="email" id="inpEmail" class="form-control" placeholder="r.smith@company.com" required style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;"/>
          </div>

          <!-- 3. Phone / WhatsApp -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">3. PHONE / WHATSAPP NUMBER *</label>
            <input type="tel" id="inpPhone" class="form-control" placeholder="+1 (555) 000-0000" required style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;"/>
          </div>

          <!-- Row 2: Company Details -->
          <!-- 4. Company Name -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">4. COMPANY NAME *</label>
            <input type="text" id="inpCompany" class="form-control" placeholder="e.g. Acme Financial Group" required style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;"/>
          </div>

          <!-- 5. Country / Location -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">5. COUNTRY / LOCATION *</label>
            <select id="inpCountry" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;">
              <option value="USA">United States</option>
              <option value="Canada">Canada</option>
              <option value="UK">United Kingdom</option>
              <option value="Australia">Australia</option>
              <option value="Other">Other International</option>
            </select>
          </div>

          <!-- 6. Industry Category -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">6. INDUSTRY CATEGORY *</label>
            <select id="inpIndustry" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;">
              <option value="CPA Firm">CPA / Accounting Firm</option>
              <option value="E-Commerce">E-Commerce / Retail</option>
              <option value="Healthcare">Healthcare / Medical</option>
              <option value="Real Estate">Real Estate / Property Management</option>
              <option value="Construction">Construction / Contracting</option>
              <option value="Professional Services">Professional Services</option>
            </select>
          </div>

          <!-- Row 3: Financial Specs -->
          <!-- 7. Revenue Range -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">7. ANNUAL REVENUE RANGE</label>
            <select id="inpRevenue" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;">
              <option value="Under $1M">Under $1 Million</option>
              <option value="$1M - $5M">$1 Million &ndash; $5 Million</option>
              <option value="$5M - $20M">$5 Million &ndash; $20 Million</option>
              <option value="$20M+">$20 Million+</option>
            </select>
          </div>

          <!-- 8. Primary Accounting Software -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">8. PRIMARY ACCOUNTING SOFTWARE</label>
            <select id="inpSoftware" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;">
              <option value="QuickBooks Online">QuickBooks Online</option>
              <option value="Xero">Xero</option>
              <option value="NetSuite">Oracle NetSuite</option>
              <option value="Other">Other / Spreadsheets</option>
            </select>
          </div>

          <!-- 9. Approx Monthly Transactions -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">9. APPROX. MONTHLY TRANSACTIONS</label>
            <select id="inpTxnVolume" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;">
              <option value="<100">Under 100 transactions/mo</option>
              <option value="100-500">100 &ndash; 500 transactions/mo</option>
              <option value="500-1500">500 &ndash; 1,500 transactions/mo</option>
              <option value="1500+">1,500+ transactions/mo</option>
            </select>
          </div>

          <!-- Row 4: Setup Specs -->
          <!-- 10. Number of Bank Accounts -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">10. NUMBER OF BANK ACCOUNTS</label>
            <input type="text" id="inpBankCount" class="form-control" placeholder="e.g. 3 checking, 2 credit cards" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;"/>
          </div>

          <!-- 11. Current Bookkeeping Arrangement -->
          <div class="form-input-group" style="grid-column: span 2; margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">11. CURRENT BOOKKEEPING ARRANGEMENT</label>
            <select id="inpCurrentSetup" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;">
              <option value="In-House Staff">In-House Staff</option>
              <option value="Local CPA Firm">Local CPA Firm</option>
              <option value="Owner Managed">Owner Managed</option>
              <option value="Behind / Cleanup Needed">Behind / Cleanup Needed</option>
            </select>
          </div>

          <!-- Row 5: Notes (Full Width 3 Columns) -->
          <div class="form-input-group" style="grid-column: 1 / -1;margin-bottom:0;">
            <label class="form-label" style="font-size:0.75rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.35rem;display:block;font-weight:700;">12. WHAT HELP DO YOU NEED?</label>
            <textarea id="inpNotes" class="form-control" rows="2" placeholder="Describe your specific accounting requirements or goals..." style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.75rem 0.9rem;border-radius:8px;width:100%;font-size:0.92rem;resize:vertical;"></textarea>
          </div>

          <!-- Submit Button -->
          <div style="grid-column: 1 / -1;margin-top:0.5rem;text-align:center;">
            <button type="submit" class="btn-editorial btn-saffron" style="padding:0.95rem 3.5rem;font-size:0.95rem;font-weight:700;letter-spacing:0.05em;border-radius:8px;box-shadow:0 8px 24px rgba(201,138,50,0.25);">
              Submit
            </button>
          </div>

        </div>

      </form>

    </div>

  </div>
</section>

