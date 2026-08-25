<!-- ═══ SECTION 10: INDUSTRIES (PINNED IMAGE SWITCHER) ═══ -->
<section class="industry-sec" id="industries-switcher">
  <div class="container-editorial">
    
    <!-- Centered Section Title at Top -->
    <div style="text-align:center;max-width:800px;margin:0 auto 4.5rem;">
      <h2 class="serif-heading" style="font-size:clamp(2.5rem, 4vw, 3.75rem);color:var(--midnight);line-height:1.15;">
        Industries We Serve
      </h2>
      <div style="width:64px;height:3px;background:linear-gradient(90deg, var(--saffron), var(--gold));margin:1rem auto 0;border-radius:2px;"></div>
      <p style="font-size:1.0625rem;color:var(--slate);margin-top:1.25rem;">
        Select your industry domain to view our tailored accounting, reconciliation, and reporting processes.
      </p>
    </div>
    
    <div class="industry-switcher-grid">
      
      <!-- Left: Vertical Tab Menu -->
      <div class="industry-menu-list">
        <button class="industry-tab-btn active" onclick="switchIndustry('cpa', this)">
          <span>CPA &amp; Accounting Firms</span>
          <span class="tab-arrow">➔</span>
        </button>
        <button class="industry-tab-btn" onclick="switchIndustry('ecommerce', this)">
          <span>E-Commerce Businesses</span>
          <span class="tab-arrow">➔</span>
        </button>
        <button class="industry-tab-btn" onclick="switchIndustry('healthcare', this)">
          <span>Healthcare &amp; Medical</span>
          <span class="tab-arrow">➔</span>
        </button>
        <button class="industry-tab-btn" onclick="switchIndustry('realestate', this)">
          <span>Real Estate &amp; Property</span>
          <span class="tab-arrow">➔</span>
        </button>
        <button class="industry-tab-btn" onclick="switchIndustry('construction', this)">
          <span>Construction &amp; Job Costing</span>
          <span class="tab-arrow">➔</span>
        </button>
        <button class="industry-tab-btn" onclick="switchIndustry('proservices', this)">
          <span>Professional Services</span>
          <span class="tab-arrow">➔</span>
        </button>
      </div>
      
      <!-- Right: Display Card with Image & Details -->
      <div class="industry-display-card" id="indDisplayCard">
        <img id="indImg" src="images/cpa_firms_portrait.png" alt="CPA Industry Accounting" class="industry-card-img"/>
        <div class="industry-card-body">
          <h3 class="industry-card-title" id="indTitle">CPA &amp; Accounting Firms</h3>
          
          <div class="industry-tag-list" id="indTagList">
            <div class="industry-tag-item">White-Label Bookkeeping</div>
            <div class="industry-tag-item">Bookkeeping Cleanup</div>
            <div class="industry-tag-item">Monthly Bookkeeping</div>
            <div class="industry-tag-item">Year-End Support</div>
            <div class="industry-tag-item">Staff Augmentation</div>
            <div class="industry-tag-item">Accounting Review</div>
          </div>
          
          <div style="margin-top:2.25rem;">
            <a href="#lead-form" class="industry-cta-link">
              <span>Explore Solution</span>
              <span class="arrow-icon">➔</span>
            </a>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</section>

<script>
const indData = {
  cpa: {
    title: "CPA & Accounting Firms",
    img: "images/cpa_firms_portrait.png",
    tags: ["White-Label Bookkeeping", "Bookkeeping Cleanup", "Monthly Bookkeeping", "Year-End Support", "Staff Augmentation", "Accounting Review"]
  },
  ecommerce: {
    title: "E-Commerce Businesses",
    img: "images/ecommerce_business_portrait.png",
    tags: ["Amazon & Shopify Accounting", "WooCommerce Integration", "Stripe Reconciliation", "Inventory Accounting", "Sales Tax Support", "COGS Tracking"]
  },
  healthcare: {
    title: "Healthcare & Medical Clinics",
    img: "images/healthcare_accounting_portrait.png",
    tags: ["Medical Clinics & Dental Practices", "Physician Bookkeeping", "Insurance Reconciliation", "Revenue Cycle Reporting", "Patient Payment Allocation", "HIPAA-Compliant Workflows"]
  },
  realestate: {
    title: "Real Estate & Property Management",
    img: "images/real_estate_portrait.png",
    tags: ["Property Management Accounting", "Rental Bookkeeping", "Trust Accounting Support", "Property Reconciliations", "Investor Reporting", "CAM Reconciliations"]
  },
  construction: {
    title: "Construction & Contracting",
    img: "images/construction_job_costing_portrait.png",
    tags: ["Job Costing", "Project Accounting", "Subcontractor Payments", "Progress Billing", "Retention Accounting", "WIP Schedule Management"]
  },
  proservices: {
    title: "Professional Services",
    img: "images/professional_services_portrait.png",
    tags: ["Law Firms & Legal Trust", "Marketing Agencies", "Consulting Firms", "Architecture & Engineering", "IT Services Companies", "Time & Billing Reconciliations"]
  }
};

function switchIndustry(key, btnElem) {
  document.querySelectorAll('.industry-tab-btn').forEach(b => b.classList.remove('active'));
  btnElem.classList.add('active');
  const d = indData[key];
  document.getElementById('indTitle').innerText = d.title;
  document.getElementById('indImg').src = d.img;
  
  let html = '';
  d.tags.forEach(t => {
    html += `<div class="industry-tag-item">${t}</div>`;
  });
  document.getElementById('indTagList').innerHTML = html;
}
</script>
