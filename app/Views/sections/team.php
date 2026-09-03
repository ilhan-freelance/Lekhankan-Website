<!-- ═══ SECTION: OUR TEAM — Executive Department Filter Grid ═══ -->
<section class="team-sec" id="team">
  <div class="container-editorial">

    <!-- Section Header -->
    <div class="team-hdr-area">
      <h2 class="team-headline">OUR <em>TEAM</em></h2>
      <p class="team-subline">The experienced finance leaders, Chartered Accountants, and technology architects driving your back-office success.</p>
      
      <!-- Department Filter Pills -->
      <div class="team-filter-bar">
        <button class="team-filter-btn active" onclick="filterTeam('all', this)">All Members (11)</button>
        <button class="team-filter-btn" onclick="filterTeam('leadership', this)">Leadership &amp; Strategy</button>
        <button class="team-filter-btn" onclick="filterTeam('technology', this)">Technology</button>
        <button class="team-filter-btn" onclick="filterTeam('accounting', this)">Accounting Ops</button>
        <button class="team-filter-btn" onclick="filterTeam('people', this)">HR &amp; Marketing</button>
      </div>
    </div>

    <!-- Executive Team Grid -->
    <div class="team-grid" id="teamGrid">

      <!-- 1. Vipul Rajesh Modi -->
      <div class="team-card team-item leadership" data-dept="leadership">
        <div class="team-card-inner">
          <div class="team-avatar">VRM</div>
          <h3 class="team-name">Vipul Rajesh Modi</h3>
          <div class="team-role">Founder &bull; Strategy &amp; Process</div>
          <div class="team-tags">
            <span>Business Strategy</span>
            <span>Process Design</span>
            <span>Financial Consulting</span>
          </div>
        </div>
      </div>

      <!-- 2. Nazneen Akhtar -->
      <div class="team-card team-item leadership accounting" data-dept="leadership">
        <div class="team-card-inner">
          <div class="team-avatar">NA</div>
          <h3 class="team-name">Nazneen Akhtar</h3>
          <div class="team-role">Co-Founder &bull; Operations</div>
          <div class="team-tags">
            <span>Client Delivery</span>
            <span>Operations QA</span>
            <span>Accounting Ops</span>
          </div>
        </div>
      </div>

      <!-- 3. Amit Modi -->
      <div class="team-card team-item technology" data-dept="technology">
        <div class="team-card-inner">
          <div class="team-avatar">AM</div>
          <h3 class="team-name">Amit Modi</h3>
          <div class="team-role">Cloud Infrastructure Lead</div>
          <div class="team-tags">
            <span>Cloud Infra</span>
            <span>System Admin</span>
            <span>Tech Support</span>
          </div>
        </div>
      </div>

      <!-- 4. Akash Khodwal -->
      <div class="team-card team-item technology" data-dept="technology">
        <div class="team-card-inner">
          <div class="team-avatar">AK</div>
          <h3 class="team-name">Akash Khodwal <small>(IIT Kharagpur)</small></h3>
          <div class="team-role">Automation &amp; Architecture</div>
          <div class="team-tags">
            <span>Software Arch</span>
            <span>Tech Integration</span>
            <span>BI Analytics</span>
          </div>
        </div>
      </div>

      <!-- 5. Ritesh Vijay -->
      <div class="team-card team-item accounting" data-dept="accounting">
        <div class="team-card-inner">
          <div class="team-avatar">RV</div>
          <h3 class="team-name">Ritesh Vijay</h3>
          <div class="team-role">Senior Accounting Review</div>
          <div class="team-tags">
            <span>Accounting Review</span>
            <span>Financial Reporting</span>
            <span>Month-End Audit</span>
          </div>
        </div>
      </div>

      <!-- 6. Ayushi Agrawal -->
      <div class="team-card team-item accounting" data-dept="accounting">
        <div class="team-card-inner">
          <div class="team-avatar">AA</div>
          <h3 class="team-name">Ayushi Agrawal</h3>
          <div class="team-role">Bookkeeping Operations</div>
          <div class="team-tags">
            <span>Bookkeeping</span>
            <span>AP &amp; AR Ops</span>
            <span>GL Management</span>
          </div>
        </div>
      </div>

      <!-- 7. Harshita Maheshwari -->
      <div class="team-card team-item accounting" data-dept="accounting">
        <div class="team-card-inner">
          <div class="team-avatar">HM</div>
          <h3 class="team-name">Harshita Maheshwari</h3>
          <div class="team-role">Reconciliation &amp; Compliance</div>
          <div class="team-tags">
            <span>Bank Recon</span>
            <span>Compliance</span>
            <span>Financial Records</span>
          </div>
        </div>
      </div>

      <!-- 8. Vishal Agrawal -->
      <div class="team-card team-item accounting" data-dept="accounting">
        <div class="team-card-inner">
          <div class="team-avatar">VA</div>
          <h3 class="team-name">Vishal Agrawal</h3>
          <div class="team-role">Financial Analysis</div>
          <div class="team-tags">
            <span>Management Reporting</span>
            <span>FP&amp;A Analysis</span>
            <span>GL Review</span>
          </div>
        </div>
      </div>

      <!-- 9. ParthJeet Singh Hada -->
      <div class="team-card team-item accounting" data-dept="accounting">
        <div class="team-card-inner">
          <div class="team-avatar">PSH</div>
          <h3 class="team-name">ParthJeet Singh Hada</h3>
          <div class="team-role">Process Management</div>
          <div class="team-tags">
            <span>Accounting Ops</span>
            <span>Financial Statements</span>
            <span>Process Mgmt</span>
          </div>
        </div>
      </div>

      <!-- 10. Pallavi Modi -->
      <div class="team-card team-item people" data-dept="people">
        <div class="team-card-inner">
          <div class="team-avatar">PM</div>
          <h3 class="team-name">Pallavi Modi</h3>
          <div class="team-role">Human Resources</div>
          <div class="team-tags">
            <span>Talent Acquisition</span>
            <span>People Ops</span>
            <span>Client Admin</span>
          </div>
        </div>
      </div>

      <!-- 11. Muskan Khatri -->
      <div class="team-card team-item people" data-dept="people">
        <div class="team-card-inner">
          <div class="team-avatar">MK</div>
          <h3 class="team-name">Muskan Khatri</h3>
          <div class="team-role">Digital Marketing &amp; BD</div>
          <div class="team-tags">
            <span>Digital Marketing</span>
            <span>Brand Comm</span>
            <span>BD Support</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<script>
function filterTeam(dept, btn) {
  document.querySelectorAll('.team-filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  const items = document.querySelectorAll('.team-item');
  items.forEach(item => {
    if (dept === 'all' || item.classList.contains(dept)) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  });
}
</script>
