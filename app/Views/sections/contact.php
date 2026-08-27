<!-- ═══ SECTION: CONTACT US (FORMAL LIGHT EDITORIAL DESIGN) ═══ -->
<section class="lead-form-sec" id="lead-form" style="padding:5rem 0 5.5rem;background:var(--ivory);color:var(--midnight);position:relative;">
  <div class="container-editorial" style="max-width:1160px;margin:0 auto;position:relative;z-index:2;">
    
    <!-- Section Title & Subheading -->
    <div style="text-align:center;max-width:860px;margin:0 auto 3.5rem;">
      <h2 class="serif-heading" style="font-size:clamp(2.6rem, 4.5vw, 3.8rem);color:var(--midnight);margin:0 0 1rem;line-height:1.1;">
        CONTACT <span style="color:var(--saffron);">US</span>
      </h2>
      <h3 style="font-family:var(--font-serif);font-size:1.35rem;color:var(--midnight);margin:0 0 0.85rem;font-weight:600;">
        Let's Build Your Offshore Accounting Team &bull; Book a Free Consultation
      </h3>
      <p style="font-size:1.025rem;color:var(--slate);line-height:1.65;margin:0;">
        Email us to discuss your accounting requirements. Our specialists will evaluate your existing accounting process and recommend an efficient outsourcing model tailored to your business.
      </p>
    </div>
    
    <!-- Single Window Formal Form Box (Light Theme) -->
    <div style="background:var(--white);border:1px solid var(--border-ivory);border-top:4px solid var(--saffron);border-radius:20px;padding:3rem 2.8rem;box-shadow:0 12px 36px rgba(0,0,0,0.04);">
      
      <form id="lekhankanLeadForm" onsubmit="handleFormSubmit(event)">
        
        <div style="display:grid;grid-template-columns: repeat(2, 1fr);gap:1.4rem;">
          
          <!-- Field 1: Full Name -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">1. FULL NAME *</label>
            <input type="text" id="inpName" class="form-control" placeholder="e.g. Robert Smith" required style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;"/>
          </div>
          
          <!-- Field 2: Company Name -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">2. COMPANY NAME *</label>
            <input type="text" id="inpCompany" class="form-control" placeholder="e.g. Acme Financial Group" required style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;"/>
          </div>
          
          <!-- Field 3: Country / Location -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">3. COUNTRY / LOCATION *</label>
            <select id="inpCountry" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;">
              <option value="USA">United States</option>
              <option value="Canada">Canada</option>
              <option value="UK">United Kingdom</option>
              <option value="Australia">Australia</option>
              <option value="Other">Other International</option>
            </select>
          </div>
          
          <!-- Field 4: Industry Category -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">4. INDUSTRY CATEGORY *</label>
            <select id="inpIndustry" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;">
              <option value="CPA Firm">CPA / Accounting Firm</option>
              <option value="E-Commerce">E-Commerce / Retail</option>
              <option value="Healthcare">Healthcare / Medical</option>
              <option value="Real Estate">Real Estate / Property Management</option>
              <option value="Construction">Construction / Contracting</option>
              <option value="Professional Services">Professional Services</option>
            </select>
          </div>
          
          <!-- Field 5: Revenue Range -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">5. ANNUAL REVENUE RANGE</label>
            <select id="inpRevenue" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;">
              <option value="Under $1M">Under $1 Million</option>
              <option value="$1M - $5M">$1 Million – $5 Million</option>
              <option value="$5M - $20M">$5 Million – $20 Million</option>
              <option value="$20M+">$20 Million+</option>
            </select>
          </div>
          
          <!-- Field 6: Primary Accounting Software -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">6. PRIMARY ACCOUNTING SOFTWARE</label>
            <select id="inpSoftware" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;">
              <option value="QuickBooks Online">QuickBooks Online</option>
              <option value="Xero">Xero</option>
              <option value="NetSuite">Oracle NetSuite</option>
              <option value="Other">Other / Spreadsheets</option>
            </select>
          </div>
          
          <!-- Field 7: Number of Bank Accounts -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">7. NUMBER OF BANK ACCOUNTS</label>
            <input type="text" id="inpBankCount" class="form-control" placeholder="e.g. 3 checking accounts, 2 credit cards" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;"/>
          </div>
          
          <!-- Field 8: Approx Monthly Transactions -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">8. APPROX. MONTHLY TRANSACTIONS</label>
            <select id="inpTxnVolume" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;">
              <option value="<100">Under 100 transactions/mo</option>
              <option value="100-500">100 – 500 transactions/mo</option>
              <option value="500-1500">500 – 1,500 transactions/mo</option>
              <option value="1500+">1,500+ transactions/mo</option>
            </select>
          </div>
          
          <!-- Field 9: Current Bookkeeping Arrangement -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">9. CURRENT BOOKKEEPING ARRANGEMENT</label>
            <select id="inpCurrentSetup" class="form-control" style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;">
              <option value="In-House Staff">In-House Staff</option>
              <option value="Local CPA Firm">Local CPA Firm</option>
              <option value="Owner Managed">Owner Managed</option>
              <option value="Behind / Cleanup Needed">Behind / Cleanup Needed</option>
            </select>
          </div>
          
          <!-- Field 10: Phone Number -->
          <div class="form-input-group" style="margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">10. PHONE / WHATSAPP NUMBER *</label>
            <input type="tel" id="inpPhone" class="form-control" placeholder="+1 (555) 000-0000" required style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;"/>
          </div>
          
          <!-- Field 11: Work Email Address (Full Width Row) -->
          <div class="form-input-group" style="grid-column: 1 / -1;margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">11. WORK EMAIL ADDRESS *</label>
            <input type="email" id="inpEmail" class="form-control" placeholder="r.smith@company.com" required style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;"/>
          </div>
          
          <!-- Field 12: What Help Do You Need? (Full Width Row) -->
          <div class="form-input-group" style="grid-column: 1 / -1;margin-bottom:0;">
            <label class="form-label" style="font-size:0.775rem;letter-spacing:0.05em;color:var(--midnight);margin-bottom:0.4rem;display:block;font-weight:700;">12. WHAT HELP DO YOU NEED?</label>
            <textarea id="inpNotes" class="form-control" rows="3" placeholder="Describe your specific accounting requirements or goals..." style="background:var(--white);border:1px solid rgba(0,0,0,0.14);color:var(--midnight);padding:0.85rem 1rem;border-radius:8px;width:100%;font-size:0.95rem;resize:vertical;"></textarea>
          </div>
          
          <!-- Submit Button -->
          <div style="grid-column: 1 / -1;margin-top:1rem;text-align:center;">
            <button type="submit" class="btn-editorial btn-saffron" style="padding:1.1rem 3.5rem;font-size:0.95rem;font-weight:700;letter-spacing:0.05em;border-radius:8px;box-shadow:0 8px 24px rgba(201,138,50,0.25);">
              Submit
            </button>
          </div>
          
        </div>
        
      </form>
      
    </div>
    
  </div>
</section>
