<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title><?= htmlspecialchars($pageTitle ?? 'Lekhankan by VRM Vrindam (P) Limited | Offshore Bookkeeping & Accounting KPO') ?></title>
  <meta name="description" content="<?= htmlspecialchars($metaDescription ?? 'Lekhankan by VRM Vrindam (P) Limited — Offshore Bookkeeping | Accounting KPO | Virtual Accounting Services for CPA firms across USA & Canada.') ?>" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            navy: { 800: "#0b192e", 900: "#061224", 950: "#030a16" },
            indigo: { 900: "#17233C" },
            saffron: { 500: "#C98A32", 600: "#B87A22" },
            gold: { 500: "#B79A5B", 600: "#A6894A" },
            ivory: { 100: "#F5F1E8", 200: "#EFEAE0" },
            emerald: { 300: "#6ee7b7", 400: "#34d399", 500: "#10b981", 600: "#059669", 700: "#047857" },
            cyan: { 300: "#67e8f9", 400: "#22d3ee", 500: "#06b6d4" }
          },
          fontFamily: {
            display: ["'Plus Jakarta Sans'","Inter","sans-serif"],
            serif: ["'Cormorant Garamond'","Georgia","serif"],
            body: ["Inter","system-ui","sans-serif"]
          }
        }
      }
    }
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    * { box-sizing: border-box; }
    :root { --ease-expo: cubic-bezier(0.16,1,0.3,1); }
    ::selection { background: #C98A32; color: white; }
    ::-webkit-scrollbar { width: 6px; } ::-webkit-scrollbar-track { background: #F5F1E8; } ::-webkit-scrollbar-thumb { background: #C98A32; border-radius: 3px; }
    .reveal { opacity: 0; transform: translateY(28px); transition: opacity .85s var(--ease-expo), transform .85s var(--ease-expo); }
    .reveal.visible { opacity: 1; transform: none; }
    .reveal-l { opacity: 0; transform: translateX(-36px); transition: opacity .85s var(--ease-expo), transform .85s var(--ease-expo); }
    .reveal-l.visible { opacity: 1; transform: none; }
    .reveal-r { opacity: 0; transform: translateX(36px); transition: opacity .85s var(--ease-expo), transform .85s var(--ease-expo); }
    .reveal-r.visible { opacity: 1; transform: none; }
    .d1 { transition-delay: .1s; } .d2 { transition-delay: .2s; } .d3 { transition-delay: .3s; } .d4 { transition-delay: .4s; }
    .reveal-d1 { opacity: 0; transform: translateY(28px); transition: opacity .85s var(--ease-expo) .15s, transform .85s var(--ease-expo) .15s; }
    .reveal-d1.visible { opacity: 1; transform: none; }
    .reveal-d2 { opacity: 0; transform: translateY(28px); transition: opacity .85s var(--ease-expo) .3s, transform .85s var(--ease-expo) .3s; }
    .reveal-d2.visible { opacity: 1; transform: none; }
    #hero { position: relative; min-height: 100svh; overflow: hidden; background: #030a16; display: flex; flex-direction: column; }
    .hero-vid { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transform: scale(1.04); filter: contrast(1.08) saturate(1.15) brightness(.82); will-change: transform; }
    .hero-o1 { position: absolute; inset: 0; background: linear-gradient(to right, rgba(3,10,22,.75) 0%, rgba(3,10,22,.45) 50%, rgba(3,10,22,.2) 100%); z-index: 1; }
    .hero-o2 { position: absolute; inset: 0; background: linear-gradient(to bottom, rgba(3,10,22,.5) 0%, transparent 40%, transparent 70%, rgba(3,10,22,.85) 100%); z-index: 2; }
    .hero-grid { position: absolute; inset: 0; z-index: 3; background-image: linear-gradient(rgba(201,138,50,.06) 1px, transparent 1px), linear-gradient(90deg, rgba(201,138,50,.06) 1px, transparent 1px); background-size: 64px 64px; animation: gp 10s ease-in-out infinite; }
    @keyframes gp { 0%,100% { opacity: .25; } 50% { opacity: .6; } }
    .gold-text { background: linear-gradient(135deg,#C98A32,#B79A5B,#10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    .ledger-grid { background-image: linear-gradient(rgba(183, 154, 91, 0.08) 1px, transparent 1px), linear-gradient(90deg, rgba(183, 154, 91, 0.08) 1px, transparent 1px); background-size: 32px 32px; }
    .marquee-track { display: flex; width: max-content; animation: mq 16s linear infinite; }
    .mq-wrap:hover .marquee-track { animation-play-state: paused; }
    @keyframes mq { from { transform: translateX(0); } to { transform: translateX(-50%); } }
    #nav-inner.nav-top {
      background: transparent !important;
      backdrop-filter: none !important;
      border-bottom-color: rgba(255, 255, 255, 0.15) !important;
      box-shadow: none !important;
      padding-top: 1.25rem !important;
      padding-bottom: 1.25rem !important;
    }
    #nav-inner.nav-top #nav-logo { color: #ffffff !important; }
    #nav-inner.nav-top #nav-sub { color: rgba(255, 255, 255, 0.7) !important; }
    #nav-inner.nav-top #nav-badge { background: rgba(201, 138, 50, 0.25) !important; border-color: rgba(201, 138, 50, 0.45) !important; color: #ffffff !important; }
    #nav-inner.nav-top .nav-link { color: rgba(255, 255, 255, 0.9) !important; }
    #nav-inner.nav-top #mob-btn { color: #ffffff !important; }

    #nav-inner.nav-scrolled {
      background: rgba(255, 255, 255, 0.97) !important;
      backdrop-filter: blur(20px) saturate(180%) !important;
      border-bottom: 1px solid rgba(201, 138, 50, 0.2) !important;
      box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06), 0 0 12px rgba(201, 138, 50, 0.08) !important;
      padding-top: 0.75rem !important;
      padding-bottom: 0.75rem !important;
    }
    #nav-inner.nav-scrolled #nav-logo { color: #17233C !important; font-weight: 900 !important; }
    #nav-inner.nav-scrolled #nav-sub { color: rgba(23, 35, 60, 0.6) !important; font-weight: 600 !important; }
    #nav-inner.nav-scrolled #nav-badge { background: rgba(201, 138, 50, 0.15) !important; border-color: rgba(201, 138, 50, 0.4) !important; color: #C98A32 !important; }
    #nav-inner.nav-scrolled .nav-link { color: #17233C !important; font-weight: 800 !important; }
    #nav-inner.nav-scrolled .nav-link:hover { color: #C98A32 !important; }
    #nav-inner.nav-scrolled #mob-btn { color: #17233C !important; }
    .f-input, .f-select, .f-textarea { width: 100%; padding: .75rem 1rem; border: 1.5px solid #e2e8f0; border-radius: .75rem; font-size: .9rem; font-family: inherit; color: #0f172a; background: #f8fafc; transition: all .25s; outline: none; }
    .f-input:focus, .f-select:focus, .f-textarea:focus { border-color: #C98A32; background: white; box-shadow: 0 0 0 3px rgba(201,138,50,.15); }
    .testi-card { background: white; border: 1px solid #e2e8f0; border-radius: 1.5rem; padding: 2rem; transition: all .4s var(--ease-expo); box-shadow: 0 4px 20px rgba(0,0,0,.03); }
    .testi-card:hover { border-color: rgba(201,138,50,.4); transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,.08); }
  </style>
</head>
<body class="font-body bg-slate-50 text-slate-900 overflow-x-hidden">
