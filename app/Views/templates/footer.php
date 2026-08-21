<!-- FOOTER -->
<footer class="bg-indigo-900 text-white pt-16 pb-12 border-t border-saffron-500/20">
  <div class="max-w-[1440px] mx-auto px-6 sm:px-12 lg:px-16">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12 border-b border-white/10">
      
      <div class="lg:col-span-2 space-y-4">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-saffron-500 to-gold-500 flex items-center justify-center text-indigo-900 font-serif font-bold text-xl shadow-lg">L</div>
          <div>
            <div class="font-display text-xl font-black tracking-tight uppercase text-white">Lekhankan</div>
            <div class="text-[.62rem] font-bold text-saffron-500">By VRM Vrindam (P) Limited</div>
          </div>
        </div>
        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-sm">
          Accounting Knowledge Process Outsourcing (KPO) delivering dedicated offshore bookkeeping and accounting solutions to CPA firms and growing enterprises across USA &amp; Canada.
        </p>
      </div>

      <div class="space-y-3">
        <h4 class="font-display text-xs font-black uppercase tracking-widest text-saffron-500">Services</h4>
        <ul class="space-y-2 text-xs text-slate-300">
          <li><a href="<?= base_url('#services') ?>" class="hover:text-saffron-500 transition-colors">Bookkeeping &amp; Accounting</a></li>
          <li><a href="<?= base_url('#services') ?>" class="hover:text-saffron-500 transition-colors">CPA Back-Office Support</a></li>
          <li><a href="<?= base_url('#services') ?>" class="hover:text-saffron-500 transition-colors">Payroll Processing</a></li>
          <li><a href="<?= base_url('#services') ?>" class="hover:text-saffron-500 transition-colors">Financial Reporting &amp; Analytics</a></li>
          <li><a href="<?= base_url('#services') ?>" class="hover:text-saffron-500 transition-colors">Tax Prep Support</a></li>
        </ul>
      </div>

      <div class="space-y-3">
        <h4 class="font-display text-xs font-black uppercase tracking-widest text-saffron-500">Company</h4>
        <ul class="space-y-2 text-xs text-slate-300">
          <li><a href="<?= base_url('#brand-story') ?>" class="hover:text-saffron-500 transition-colors">About Us</a></li>
          <li><a href="<?= base_url('#why-us') ?>" class="hover:text-saffron-500 transition-colors">Why Choose Us</a></li>
          <li><a href="<?= base_url('#industries') ?>" class="hover:text-saffron-500 transition-colors">Industries Served</a></li>
          <li><a href="<?= base_url('#process') ?>" class="hover:text-saffron-500 transition-colors">Our Process</a></li>
          <li><a href="<?= base_url('#contact') ?>" class="hover:text-saffron-500 transition-colors">Contact Us</a></li>
        </ul>
      </div>

      <div class="space-y-3">
        <h4 class="font-display text-xs font-black uppercase tracking-widest text-saffron-500">Contact &amp; Support</h4>
        <ul class="space-y-2 text-xs text-slate-300">
          <li><strong class="text-white">Email:</strong> contact@lekhankan.com</li>
          <li><strong class="text-white">Location:</strong> VRM Vrindam (P) Limited</li>
          <li><strong class="text-white">Coverage:</strong> USA &amp; Canada Timezones</li>
        </ul>
      </div>

    </div>

    <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-[.7rem] text-slate-400">
      <div>&copy; <?= date('Y') ?> Lekhankan by VRM Vrindam (P) Limited. All Rights Reserved.</div>
      <div class="flex items-center gap-6">
        <a href="#" class="hover:text-saffron-500 transition-colors">Privacy Policy</a>
        <a href="#" class="hover:text-saffron-500 transition-colors">Terms of Service</a>
        <a href="#" class="hover:text-saffron-500 transition-colors">Security Overview</a>
      </div>
    </div>
  </div>
</footer>

<!-- JS SCRIPTS & CALCULATOR HANDLER -->
<script>
  let currentCurrency = 'USD';
  const roleRates = {
    bookkeeper: { US: 70000, LK: 37600, pct: 46 },
    cpa: { US: 110000, LK: 52000, pct: 53 },
    tax: { US: 95000, LK: 44000, pct: 54 }
  };
  let currentRole = 'bookkeeper';

  // Scroll Reveal Observer
  document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal, .reveal-l, .reveal-r, .reveal-d1, .reveal-d2').forEach(el => observer.observe(el));

    // Navbar Scroll Handler
    const navInner = document.getElementById('nav-inner');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        navInner.classList.remove('nav-top');
        navInner.classList.add('nav-scrolled');
      } else {
        navInner.classList.remove('nav-scrolled');
        navInner.classList.add('nav-top');
      }
    });

    // Mobile Menu
    const mobBtn = document.getElementById('mob-btn');
    const mobMenu = document.getElementById('mob-menu');
    const mobClose = document.getElementById('mob-close');
    if (mobBtn && mobMenu) {
      mobBtn.addEventListener('click', () => mobMenu.classList.remove('hidden'));
      mobClose.addEventListener('click', () => mobMenu.classList.add('hidden'));
      document.querySelectorAll('.mob-link').forEach(l => l.addEventListener('click', () => mobMenu.classList.add('hidden')));
    }
  });
</script>
</body>
</html>
