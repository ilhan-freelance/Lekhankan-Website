# Build new index.html - Complete ground-up light theme rebuild
# Run: python build_new.py

import os

output_path = r"c:\Users\asus\Documents\LEKHANKAN Websitee\index.html"

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lekhankan by VRM Vrindam (P) Limited | Offshore Bookkeeping &amp; Accounting KPO &mdash; USA &amp; Canada</title>
  <meta name="description" content="Lekhankan provides offshore bookkeeping, accounting KPO, and virtual accounting services for CPA firms across USA &amp; Canada. Reduce costs by up to 60% with dedicated CA-supervised accounting teams." />
  <meta name="keywords" content="offshore bookkeeping services, bookkeeping services USA, bookkeeping services Canada, accounting outsourcing, accounting KPO, virtual bookkeeping, CPA firm support, QuickBooks bookkeeping" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&display=swap" rel="stylesheet" />
  <style>
    /* ============================================================
       LEKHANKAN MASTER DESIGN SYSTEM
       LIGHT THEME: 70% ivory/white | 20% slate | 10% saffron/gold
       Hero: Dark #17233C | Rest: Light ivory/white backgrounds
    ============================================================ */
    :root {
      --midnight: #17233C;
      --midnight-2: #1e2d4a;
      --saffron: #C98A32;
      --saffron-h: #b07528;
      --gold: #B79A5B;
      --ivory: #FFFFE3;
      --ivory-2: #FFFFE3;
      --white: #FFFFFF;
      --slate: #687080;
      --slate-2: #8A93A4;
      --slate-3: #4A5568;
      --dark: #1A202C;
      --border: #E2DDD4;
      --border-2: #D4CFBE;
      --r-sm: 0.5rem; --r-md: 0.875rem; --r-lg: 1.25rem;
      --r-xl: 1.75rem; --r-pill: 9999px;
      --sh-sm: 0 2px 8px rgba(23,35,60,0.08);
      --sh-md: 0 8px 24px rgba(23,35,60,0.12);
      --sh-lg: 0 16px 48px rgba(23,35,60,0.16);
    }
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    html{scroll-behavior:smooth}
    body{font-family:'Manrope','Plus Jakarta Sans',sans-serif;font-size:16px;line-height:1.65;color:var(--dark);background:var(--ivory);overflow-x:hidden;-webkit-font-smoothing:antialiased}
    ::selection{background:var(--saffron);color:#fff}
    ::-webkit-scrollbar{width:6px}
    ::-webkit-scrollbar-track{background:var(--ivory)}
    ::-webkit-scrollbar-thumb{background:var(--saffron);border-radius:3px}
    a{text-decoration:none;color:inherit}
    img{max-width:100%;display:block}
    button{cursor:pointer;font-family:inherit;border:none;background:none}
    .container{max-width:1260px;margin:0 auto;padding:0 2rem}
    .section{padding:5.5rem 0}
    .bg-white{background:#fff}
    .bg-ivory{background:#FFFFE3}
    .bg-ivory2{background:#FFFFE3}
    .bg-dark{background:var(--midnight)}

    /* Typography */
    .f-serif{font-family:'Cormorant Garamond',Georgia,serif}
    .f-display{font-family:'Plus Jakarta Sans',sans-serif}
    .label{font-family:'Plus Jakarta Sans',sans-serif;font-size:.6875rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--saffron)}
    .label-row{display:flex;align-items:center;gap:.75rem;margin-bottom:1rem}
    .label-row::before{content:'';width:2.5rem;height:2px;background:var(--saffron);border-radius:1px;flex-shrink:0}
    h1,h2,h3,h4{line-height:1.2;letter-spacing:-.01em}
    .h-xl{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(2.5rem,5vw,3.75rem);font-weight:800;color:#fff;line-height:1.1}
    .h-hero-sub{font-family:'Cormorant Garamond',serif;font-size:clamp(1.2rem,2.5vw,1.75rem);font-style:italic;font-weight:600;color:var(--saffron);line-height:1.4}
    .h-lg{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(1.9rem,3.5vw,2.75rem);font-weight:800;color:var(--midnight);line-height:1.15}
    .h-md{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(1.4rem,2.5vw,2rem);font-weight:700;color:var(--midnight);line-height:1.2}
    .h-sm{font-family:'Plus Jakarta Sans',sans-serif;font-size:1.0625rem;font-weight:700;color:var(--midnight);line-height:1.3}
    .t-saffron{color:var(--saffron)}
    .t-gold{color:var(--gold)}
    .t-white{color:#fff}
    .t-slate{color:var(--slate);font-size:.9375rem;line-height:1.75}
    .t-body{color:var(--slate-3);line-height:1.75}

    /* Buttons */
    .btn{display:inline-flex;align-items:center;gap:.5rem;padding:.875rem 2rem;border-radius:var(--r-pill);font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:.8125rem;letter-spacing:.06em;text-transform:uppercase;transition:all .25s ease;cursor:pointer}
    .btn-primary{background:var(--saffron);color:var(--midnight);border:2px solid var(--saffron);box-shadow:0 4px 16px rgba(201,138,50,.3)}
    .btn-primary:hover{background:var(--saffron-h);border-color:var(--saffron-h);transform:translateY(-2px)}
    .btn-white{background:transparent;color:#fff;border:2px solid rgba(255,255,255,.5)}
    .btn-white:hover{border-color:#fff;background:rgba(255,255,255,.1);transform:translateY(-2px)}
    .btn-dark{background:transparent;color:var(--midnight);border:2px solid var(--midnight)}
    .btn-dark:hover{background:var(--midnight);color:#fff;transform:translateY(-2px)}
    .btn-saffron-out{background:transparent;color:var(--saffron);border:2px solid var(--saffron)}
    .btn-saffron-out:hover{background:var(--saffron);color:#fff;transform:translateY(-2px)}

    /* Cards */
    .card{background:#fff;border:1.5px solid var(--border);border-radius:var(--r-lg);padding:1.75rem;transition:all .25s ease;box-shadow:var(--sh-sm)}
    .card:hover{border-color:var(--saffron);box-shadow:var(--sh-md);transform:translateY(-4px)}
    .card-dark{background:var(--midnight);border:1px solid rgba(201,138,50,.2);border-radius:var(--r-lg);padding:2rem;transition:all .25s}
    .card-dark:hover{border-color:rgba(201,138,50,.6)}
    .card-featured{background:var(--midnight);border:1.5px solid var(--saffron);border-radius:var(--r-xl);padding:2.5rem}

    /* Icon box */
    .icon-box{width:3rem;height:3rem;border-radius:var(--r-md);background:rgba(201,138,50,.1);border:1px solid rgba(201,138,50,.2);display:flex;align-items:center;justify-content:center;color:var(--saffron);flex-shrink:0}
    .icon-box-dark{width:3rem;height:3rem;border-radius:var(--r-md);background:rgba(201,138,50,.15);border:1px solid rgba(201,138,50,.3);display:flex;align-items:center;justify-content:center;color:var(--saffron);flex-shrink:0}
    .step-num{width:3rem;height:3rem;border-radius:50%;background:var(--saffron);color:var(--midnight);font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:.875rem;display:flex;align-items:center;justify-content:center;flex-shrink:0}
    .checkmark{width:1.5rem;height:1.5rem;border-radius:50%;background:rgba(201,138,50,.12);display:flex;align-items:center;justify-content:center;color:var(--saffron);flex-shrink:0;font-size:.75rem;font-weight:800;margin-top:.1rem}
    .check-dark{width:1.5rem;height:1.5rem;border-radius:50%;background:rgba(201,138,50,.2);display:flex;align-items:center;justify-content:center;color:var(--saffron);flex-shrink:0;font-size:.75rem;font-weight:800;margin-top:.15rem}

    /* Decorators */
    .gold-bar{width:3.5rem;height:3px;background:linear-gradient(90deg,var(--saffron),var(--gold));border-radius:2px;margin:.75rem auto 0}
    .gold-bar-left{width:3.5rem;height:3px;background:linear-gradient(90deg,var(--saffron),var(--gold));border-radius:2px;margin:.75rem 0 0}

    /* Section header */
    .sec-hdr{text-align:center;max-width:700px;margin:0 auto 4rem}
    .sec-hdr .label-row{justify-content:center}
    .sec-hdr .label-row::before{display:none}

    /* Utils */
    .grid-2{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
    .mb1{margin-bottom:.5rem}.mb2{margin-bottom:1rem}.mb3{margin-bottom:1.5rem}.mb4{margin-bottom:2rem}
    .mt1{margin-top:.5rem}.mt2{margin-top:1rem}.mt3{margin-top:1.5rem}.mt4{margin-top:2rem}
    .tc{text-align:center}.w-full{width:100%}

    /* Scroll reveal */
    .rev{opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s ease}
    .rev.on{opacity:1;transform:translateY(0)}
    .d1{transition-delay:.1s}.d2{transition-delay:.2s}.d3{transition-delay:.3s}.d4{transition-delay:.4s}

    /* ══ NAVBAR ══ */
    .nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(255,255,255,.97);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);transition:all .3s}
    .nav.scrolled{box-shadow:0 4px 20px rgba(23,35,60,.1)}
    .nav-in{display:flex;align-items:center;justify-content:space-between;height:72px}
    .nav-logo{display:flex;align-items:center;gap:.75rem}
    .logo-badge{width:2.25rem;height:2.25rem;border-radius:var(--r-sm);background:var(--midnight);display:flex;align-items:center;justify-content:center;color:var(--saffron);font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:700}
    .logo-name{font-family:'Plus Jakarta Sans',sans-serif;font-size:1.1rem;font-weight:800;color:var(--midnight);letter-spacing:-.02em;line-height:1}
    .logo-sub{font-size:.625rem;font-weight:600;color:var(--slate-2);letter-spacing:.08em;text-transform:uppercase;line-height:1.2}
    .nav-links{display:flex;align-items:center;gap:.25rem;list-style:none}
    .nav-links a{padding:.5rem .875rem;border-radius:var(--r-sm);font-family:'Plus Jakarta Sans',sans-serif;font-size:.8125rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--slate-3);transition:all .2s}
    .nav-links a:hover,.nav-links a.on{color:var(--midnight);background:var(--ivory)}

    /* ══ HERO ══ */
    .hero{background:var(--midnight);background-image:linear-gradient(135deg, rgba(23,35,60,0.95) 0%, rgba(23,35,60,0.85) 50%, rgba(23,35,60,0.92) 100%), url('industries_background.png');background-size:cover;background-position:center;position:relative;overflow:hidden;padding-top:85px;padding-bottom:2.25rem;min-height:auto;display:flex;flex-direction:column}
    .hero::before{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(201,138,50,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(201,138,50,.05) 1px,transparent 1px);background-size:60px 60px;pointer-events:none}
    .hero-heritage-txt{position:absolute;bottom:10%;left:2%;font-family:'Cormorant Garamond',serif;font-size:11rem;font-weight:700;color:rgba(201,138,50,.035);pointer-events:none;white-space:nowrap;user-select:none;line-height:1;z-index:1}
    .hero-chart{position:absolute;right:0;top:0;bottom:0;width:50%;pointer-events:none;opacity:.35;z-index:1}
    .hero-in{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;justify-content:center}
    .hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:2.5rem;align-items:center;padding:1rem 0}
    .hero-content{max-width:100%}
    .hero-tag{display:inline-flex;align-items:center;gap:.625rem;padding:.3rem .875rem;border-radius:var(--r-pill);background:rgba(201,138,50,.12);border:1px solid rgba(201,138,50,.3);margin-bottom:1.25rem}
    .tag-dot{width:.5rem;height:.5rem;border-radius:50%;background:var(--saffron);box-shadow:0 0 8px var(--saffron)}
    .tag-txt{font-family:'Plus Jakarta Sans',sans-serif;font-size:.6875rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--saffron)}
    .hero-btns{display:flex;gap:1rem;flex-wrap:wrap;margin-top:1.5rem}
    .hero-metrics{display:flex;gap:2.5rem;padding-top:1.5rem;margin-top:1.75rem;border-top:1px solid rgba(255,255,255,.1)}
    .m-num{font-family:'Cormorant Garamond',serif;font-size:2.25rem;font-weight:700;color:var(--saffron);line-height:1}
    .m-lbl{font-size:.75rem;color:rgba(255,255,255,.55);font-weight:500;letter-spacing:.04em;margin-top:.2rem}
    .hero-img-box{position:relative;border-radius:var(--r-xl);overflow:hidden;border:1.5px solid rgba(201,138,50,.35);box-shadow:0 20px 50px rgba(0,0,0,.4)}
    .hero-img-box img{width:100%;height:380px;object-fit:cover;display:block}
    .hero-img-overlay{position:absolute;bottom:1rem;left:1rem;right:1rem;background:rgba(23,35,60,.9);backdrop-filter:blur(12px);border:1px solid rgba(201,138,50,.3);border-radius:var(--r-md);padding:.75rem 1.25rem;display:flex;align-items:center;gap:.875rem}

    /* ══ TICKER ══ */
    .ticker{background:var(--midnight-2);overflow:hidden;padding:.875rem 0;border-bottom:1px solid rgba(201,138,50,.15)}
    .ticker-track{display:flex;gap:4rem;animation:tick 35s linear infinite;white-space:nowrap}
    @keyframes tick{from{transform:translateX(0)}to{transform:translateX(-50%)}}
    .tick-item{font-family:'Plus Jakarta Sans',sans-serif;font-size:.6875rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:rgba(201,138,50,.7);flex-shrink:0}

    /* ══ PILLARS STRIP ══ */
    .pillars-strip{background:#fff;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
    .pillars-grid{display:grid;grid-template-columns:repeat(4,1fr)}
    .pillar{padding:1.875rem 2rem;display:flex;align-items:flex-start;gap:1rem;border-right:1px solid var(--border);transition:background .2s}
    .pillar:last-child{border-right:none}
    .pillar:hover{background:var(--ivory-2)}
    .pillar.feat{background:var(--midnight)}
    .pillar.feat:hover{background:var(--midnight-2)}
    .p-icon{width:2.5rem;height:2.5rem;border-radius:var(--r-sm);background:rgba(201,138,50,.1);border:1px solid rgba(201,138,50,.2);display:flex;align-items:center;justify-content:center;color:var(--saffron);flex-shrink:0}
    .p-icon.feat{background:var(--saffron);border-color:var(--saffron);color:var(--midnight)}
    .p-title{font-size:.9375rem;font-weight:700;color:var(--midnight);margin-bottom:.25rem}
    .pillar.feat .p-title{color:var(--saffron)}
    .p-desc{font-size:.8125rem;color:var(--slate);line-height:1.55}
    .pillar.feat .p-desc{color:rgba(255,255,255,.6)}

    /* ══ ABOUT / BRAND STORY ══ */
    .about-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}
    .heritage-card{background:var(--midnight);border-radius:var(--r-xl);padding:2.5rem;position:relative;overflow:hidden}
    .heritage-card::before{content:'\\u0932\\u0947\\u0916\\u0928';position:absolute;top:-1rem;right:-.5rem;font-family:'Cormorant Garamond',serif;font-size:8rem;font-weight:800;color:rgba(201,138,50,.06);pointer-events:none;line-height:1}
    .ledger-viz{font-family:monospace;font-size:.6875rem;color:rgba(201,138,50,.4);letter-spacing:.03em;border:1px solid rgba(201,138,50,.15);border-radius:var(--r-md);padding:1rem;margin-top:1.5rem;line-height:1.8}
    .phase-strip{display:flex;margin-top:1.25rem;border-radius:var(--r-lg);overflow:hidden;border:1.5px solid var(--border-2)}
    .phase-item{flex:1;padding:1.25rem}
    .phase-lbl{font-size:.6875rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--saffron);margin-bottom:.375rem}
    .phase-name{font-size:.875rem;font-weight:700;color:var(--midnight)}
    .phase-sub{font-size:.75rem;color:var(--slate)}
    .why-list{background:#fff;border:1px solid var(--border);border-radius:var(--r-xl);padding:2.5rem;box-shadow:var(--sh-md)}
    .why-item{display:flex;align-items:flex-start;gap:1rem;padding:1.25rem 0;border-bottom:1px solid var(--border)}
    .why-item:last-child{border-bottom:none;padding-bottom:0}
    .why-item:first-child{padding-top:0}
    .tech-logos{display:flex;align-items:center;gap:2rem;margin-top:2.5rem;flex-wrap:wrap}
    .tech-logo{font-family:'Plus Jakarta Sans',sans-serif;font-size:.75rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--slate-2);opacity:.7;transition:opacity .2s}
    .tech-logo:hover{opacity:1}

    /* ══ SERVICES ══ */
    .tab-nav{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:3rem;justify-content:center}
    .tab-btn{padding:.625rem 1.375rem;border-radius:var(--r-pill);font-family:'Plus Jakarta Sans',sans-serif;font-size:.8125rem;font-weight:600;color:var(--slate-3);background:var(--ivory-2);border:1.5px solid var(--border);transition:all .2s;cursor:pointer}
    .tab-btn:hover{border-color:var(--saffron);color:var(--saffron)}
    .tab-btn.on{background:var(--midnight);color:#fff;border-color:var(--midnight)}
    .tab-pane{display:none}
    .tab-pane.on{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem}
    .svc-card{background:#fff;border:1.5px solid var(--border);border-radius:var(--r-lg);padding:1.75rem;transition:all .25s;box-shadow:var(--sh-sm)}
    .svc-card:hover{border-color:var(--saffron);box-shadow:var(--sh-md);transform:translateY(-4px)}
    .svc-icon{width:3rem;height:3rem;border-radius:var(--r-md);background:rgba(201,138,50,.1);border:1px solid rgba(201,138,50,.2);display:flex;align-items:center;justify-content:center;color:var(--saffron);margin-bottom:1.25rem}

    /* ══ WHY US ══ */
    .why-grid{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}
    .roi-card{background:rgba(255,255,255,.06);border:1.5px solid rgba(201,138,50,.3);border-radius:var(--r-xl);padding:2.5rem}
    .roi-amount{font-family:'Cormorant Garamond',serif;font-size:3rem;font-weight:700;color:var(--saffron);line-height:1}
    .roi-tabs{display:flex;gap:.5rem;margin-top:1.25rem;flex-wrap:wrap}
    .roi-tab{padding:.4rem 1rem;border-radius:var(--r-pill);font-size:.75rem;font-weight:600;color:rgba(255,255,255,.5);border:1px solid rgba(255,255,255,.15);cursor:pointer;transition:all .2s}
    .roi-tab.on{background:var(--saffron);color:var(--midnight);border-color:var(--saffron)}
    .roi-bar-row{margin-top:1.75rem}
    .roi-bar-lbl{display:flex;justify-content:space-between;font-size:.8125rem;color:rgba(255,255,255,.65);margin-bottom:.5rem}
    .roi-track{height:6px;border-radius:3px;background:rgba(255,255,255,.1);overflow:hidden}
    .roi-fill{height:100%;border-radius:3px;background:var(--saffron)}
    .cl-item{display:flex;align-items:flex-start;gap:1rem;padding:1rem 0;border-bottom:1px solid rgba(255,255,255,.06)}
    .cl-item:last-child{border-bottom:none}

    /* ══ INDUSTRIES ══ */
    .ind-grid{display:grid;grid-template-columns:260px 1fr;gap:2.5rem}
    .ind-sidebar{display:flex;flex-direction:column;gap:.5rem}
    .ind-btn{display:flex;align-items:center;gap:1rem;padding:1rem 1.25rem;border-radius:var(--r-md);border:1.5px solid var(--border);background:#fff;cursor:pointer;transition:all .2s;text-align:left}
    .ind-btn:hover{border-color:var(--saffron)}
    .ind-btn.on{background:var(--midnight);border-color:var(--midnight)}
    .ind-icon{width:2.5rem;height:2.5rem;border-radius:var(--r-sm);background:rgba(201,138,50,.1);display:flex;align-items:center;justify-content:center;color:var(--saffron);flex-shrink:0}
    .ind-btn.on .ind-icon{background:rgba(201,138,50,.2)}
    .ind-name{font-size:.875rem;font-weight:700;color:var(--midnight)}
    .ind-btn.on .ind-name{color:#fff}
    .ind-count{font-size:.6875rem;color:var(--slate);margin-top:.1rem}
    .ind-btn.on .ind-count{color:rgba(255,255,255,.55)}
    .ind-content{display:none}
    .ind-content.on{display:block}
    .ind-svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
    .ind-svc{background:#fff;border:1px solid var(--border);border-radius:var(--r-md);padding:1.25rem;transition:all .2s}
    .ind-svc:hover{border-color:var(--saffron)}

    /* ══ CPA PARTNER ══ */
    .cpa-grid{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
    .cpa-feat{display:flex;align-items:flex-start;gap:1.25rem;padding:1.25rem 0;border-bottom:1px solid rgba(255,255,255,.06)}
    .cpa-feat:last-child{border-bottom:none}
    .cpa-stats{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
    .cpa-stat{padding:1.25rem;background:rgba(201,138,50,.06);border:1px solid rgba(201,138,50,.15);border-radius:var(--r-md)}
    .cpa-stat-num{font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:700;color:var(--saffron);line-height:1}
    .cpa-stat-lbl{font-size:.75rem;color:rgba(255,255,255,.55);margin-top:.25rem}

    /* ══ PROCESS ══ */
    .proc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem}
    .proc-card{background:#fff;border:1.5px solid var(--border);border-radius:var(--r-lg);padding:1.75rem;transition:all .25s;position:relative}
    .proc-card::after{content:'\\2192';position:absolute;right:-1.5rem;top:50%;transform:translateY(-50%);color:var(--border-2);font-size:1.25rem;z-index:2}
    .proc-card:last-child::after{display:none}
    .proc-card:hover{border-color:var(--saffron);box-shadow:var(--sh-md)}
    .proc-card.active{border-color:var(--saffron);background:var(--midnight)}
    .proc-card.active .h-sm{color:var(--saffron)}
    .proc-card.active .t-slate{color:rgba(255,255,255,.6)}

    /* ══ TESTIMONIALS ══ */
    .test-grid{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
    .stars{display:flex;gap:.25rem}
    .star{color:var(--saffron);font-size:1.1rem}
    .test-card{background:var(--midnight);border:1px solid rgba(201,138,50,.25);border-radius:var(--r-xl);padding:2.5rem;margin-bottom:1.25rem}
    .test-card:last-child{margin-bottom:0}
    .test-q{font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-style:italic;color:rgba(255,255,255,.9);line-height:1.7;margin:1.25rem 0}
    .stat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem;margin-top:2.5rem}
    .s-num{font-family:'Cormorant Garamond',serif;font-size:2.5rem;font-weight:700;color:var(--midnight);line-height:1}
    .s-lbl{font-size:.8125rem;color:var(--slate);margin-top:.25rem}

    /* ══ LEAD MAGNETS ══ */
    .res-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem}
    .res-card{background:var(--ivory-2);border:1.5px solid var(--border);border-radius:var(--r-lg);padding:1.75rem;transition:all .25s;display:flex;flex-direction:column}
    .res-card:hover{border-color:var(--saffron);box-shadow:var(--sh-md);transform:translateY(-4px)}
    .res-icon{width:3rem;height:3rem;border-radius:var(--r-md);background:var(--midnight);display:flex;align-items:center;justify-content:center;color:var(--saffron);margin-bottom:1.25rem}
    .res-tag{display:inline-block;padding:.25rem .75rem;border-radius:var(--r-pill);background:rgba(201,138,50,.1);color:var(--saffron);font-size:.6875rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:.875rem}

    /* ══ CONTACT ══ */
    .contact-grid{display:grid;grid-template-columns:1fr 1.4fr;gap:5rem;align-items:flex-start}
    .form-lbl{display:block;font-size:.75rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--slate-3);margin-bottom:.5rem}
    .form-input{width:100%;padding:.875rem 1.125rem;border-radius:var(--r-md);border:1.5px solid var(--border);background:#fff;font-family:'Manrope',sans-serif;font-size:.875rem;color:var(--dark);outline:none;transition:border-color .2s}
    .form-input:focus{border-color:var(--saffron);box-shadow:0 0 0 3px rgba(201,138,50,.1)}
    .form-input::placeholder{color:var(--slate-2)}
    select.form-input{appearance:none;cursor:pointer}
    textarea.form-input{resize:vertical;min-height:120px}

    /* ══ FOOTER ══ */
    .footer{background:var(--midnight);padding:5rem 0 2rem;border-top:1px solid rgba(201,138,50,.15)}
    .footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:3rem;padding-bottom:3.5rem;border-bottom:1px solid rgba(255,255,255,.06)}
    .f-link{display:block;font-size:.875rem;color:rgba(255,255,255,.5);margin-bottom:.625rem;transition:color .2s}
    .f-link:hover{color:var(--saffron)}
    .f-head{font-family:'Plus Jakarta Sans',sans-serif;font-size:.6875rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--saffron);margin-bottom:1.25rem}

    /* ══ MODAL ══ */
    .modal{position:fixed;inset:0;background:rgba(23,35,60,.75);backdrop-filter:blur(8px);z-index:9000;display:flex;align-items:center;justify-content:center;padding:1.5rem;opacity:0;pointer-events:none;transition:opacity .3s}
    .modal.open{opacity:1;pointer-events:auto}
    .modal-box{background:#fff;border-radius:var(--r-xl);padding:2.5rem;max-width:520px;width:100%;transform:translateY(20px);transition:transform .3s;position:relative}
    .modal.open .modal-box{transform:translateY(0)}

    /* ══ RESPONSIVE ══ */
    @media(max-width:1024px){
      .about-grid,.why-grid,.contact-grid,.cpa-grid{grid-template-columns:1fr;gap:3rem}
      .pillars-grid{grid-template-columns:repeat(2,1fr)}
      .proc-grid{grid-template-columns:repeat(2,1fr)}
      .proc-card::after{display:none}
      .footer-grid{grid-template-columns:1fr 1fr;gap:2rem}
      .test-grid{grid-template-columns:1fr}
      .ind-grid{grid-template-columns:1fr}
      .res-grid{grid-template-columns:repeat(2,1fr)}
      .tab-pane.on{grid-template-columns:repeat(2,1fr)}
    }
    @media(max-width:768px){
      .nav-links{display:none}
      .pillars-grid{grid-template-columns:1fr 1fr}
      .proc-grid{grid-template-columns:1fr 1fr}
      .res-grid{grid-template-columns:1fr 1fr}
      .tab-pane.on{grid-template-columns:1fr}
      .hero-metrics{gap:1.5rem;flex-wrap:wrap}
      .footer-grid{grid-template-columns:1fr}
      .stat-grid{grid-template-columns:1fr 1fr}
    }
  </style>
</head>
<body>

<!-- ═══ NAVBAR ═══ -->
<nav class="nav" id="nav">
  <div class="container">
    <div class="nav-in">
      <a href="#hero" class="nav-logo">
        <div class="logo-badge">L</div>
        <div>
          <div class="logo-name">LEKHANKAN</div>
          <div class="logo-sub">By VRM Vrindam (P) Limited</div>
        </div>
      </a>
      <ul class="nav-links">
        <li><a href="#hero">Home</a></li>
        <li><a href="#brand-story">Heritage</a></li>
        <li><a href="#why-us">Why Us</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#industries">Industries</a></li>
        <li><a href="#process">Process</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <a href="#contact" class="btn btn-primary">Request Proposal &rarr;</a>
    </div>
  </div>
</nav>

<!-- ═══ HERO ═══ -->
<section id="hero" class="hero">
  <div class="hero-heritage-txt">&#x0932;&#x0947;&#x0916;&#x0928; BAHI KHATA</div>
  <svg class="hero-chart" viewBox="0 0 700 600" fill="none" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
    <circle cx="120" cy="430" r="5" fill="#C98A32" opacity="0.4"/>
    <circle cx="220" cy="370" r="5" fill="#C98A32" opacity="0.4"/>
    <circle cx="320" cy="310" r="5" fill="#C98A32" opacity="0.4"/>
    <circle cx="400" cy="200" r="5" fill="#C98A32" opacity="0.4"/>
    <circle cx="500" cy="250" r="5" fill="#C98A32" opacity="0.4"/>
    <circle cx="600" cy="140" r="5" fill="#C98A32" opacity="0.4"/>
    <polyline points="120,430 220,370 320,310 400,200 500,250 600,140" stroke="#C98A32" stroke-width="2" stroke-opacity="0.3" fill="none"/>
    <circle cx="160" cy="490" r="4" fill="#B79A5B" opacity="0.25"/>
    <circle cx="270" cy="450" r="4" fill="#B79A5B" opacity="0.25"/>
    <circle cx="380" cy="390" r="4" fill="#B79A5B" opacity="0.25"/>
    <circle cx="480" cy="340" r="4" fill="#B79A5B" opacity="0.25"/>
    <circle cx="570" cy="280" r="4" fill="#B79A5B" opacity="0.25"/>
    <circle cx="650" cy="200" r="4" fill="#B79A5B" opacity="0.25"/>
    <polyline points="160,490 270,450 380,390 480,340 570,280 650,200" stroke="#B79A5B" stroke-width="1.5" stroke-opacity="0.2" stroke-dasharray="6 4" fill="none"/>
    <!-- Second chart line (lower, dashed) -->
    <circle cx="100" cy="520" r="3" fill="#C98A32" opacity="0.2"/>
    <circle cx="200" cy="480" r="3" fill="#C98A32" opacity="0.2"/>
    <circle cx="340" cy="420" r="3" fill="#C98A32" opacity="0.2"/>
    <circle cx="460" cy="300" r="3" fill="#C98A32" opacity="0.2"/>
    <circle cx="560" cy="350" r="3" fill="#C98A32" opacity="0.2"/>
    <circle cx="670" cy="160" r="3" fill="#C98A32" opacity="0.2"/>
    <polyline points="100,520 200,480 340,420 460,300 560,350 670,160" stroke="#C98A32" stroke-width="1" stroke-opacity="0.15" fill="none"/>
  </svg>

  <div class="hero-in">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-content">
          <div class="hero-tag">
            <div class="tag-dot"></div>
            <span class="tag-txt">Accounting KPO &middot; USA &amp; Canada</span>
          </div>
          <h1 class="h-xl mb2" style="font-size:clamp(2.2rem, 3.8vw, 3.2rem);">
            Offshore Bookkeeping &amp;<br>Accounting Services for<br>
            <span class="t-saffron">USA &amp; Canada</span>
          </h1>
          <p class="h-hero-sub mt1" style="font-size:1.15rem;">Your Dedicated Accounting Team. Accurate Financials. Scalable Growth.</p>
          <p class="mt2" style="font-size:.875rem;line-height:1.7;color:rgba(255,255,255,.65)">
            Lekhankan provides professional bookkeeping, accounting, financial reporting, and back-office solutions for businesses and CPA firms across the United States and Canada.
          </p>
          <div class="hero-btns">
            <a href="#contact" class="btn btn-primary">Schedule Consultation</a>
            <a href="#contact" class="btn btn-white">Request Assessment</a>
          </div>
          <div class="hero-metrics">
            <div><div class="m-num">60%</div><div class="m-lbl">Cost Reduction</div></div>
            <div><div class="m-num">CA</div><div class="m-lbl">CA Supervised</div></div>
            <div><div class="m-num">24hr</div><div class="m-lbl">Timezone Overlap</div></div>
            <div><div class="m-num">100+</div><div class="m-lbl">Clients Served</div></div>
          </div>
        </div>

        <div class="hero-img-box rev d2">
          <img src="CPA Professional Services.png" alt="Lekhankan Financial Reporting &amp; Cloud Accounting Operations" />
          <div class="hero-img-overlay">
            <div class="icon-box-dark" style="width:2.25rem;height:2.25rem;"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div>
            <div>
              <div style="font-size:.8125rem;font-weight:700;color:#fff;">CA-Supervised Accounting Operations</div>
              <div style="font-size:.7rem;color:var(--saffron);font-weight:600;">US GAAP &amp; ASPE Compliant &middot; QBO &amp; Xero Certified</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Ticker -->
<div class="ticker">
  <div class="ticker-track">
    <span class="tick-item">&starf; Chartered Accountant Supervised</span>
    <span class="tick-item">&starf; QuickBooks &amp; Xero Certified</span>
    <span class="tick-item">&starf; Up to 60% Cost Reduction</span>
    <span class="tick-item">&starf; USA &amp; Canada Timezone Alignment</span>
    <span class="tick-item">&starf; Bank-Grade Confidentiality</span>
    <span class="tick-item">&starf; Dedicated Offshore Accounting Teams</span>
    <span class="tick-item">&starf; Chartered Accountant Supervised</span>
    <span class="tick-item">&starf; QuickBooks &amp; Xero Certified</span>
    <span class="tick-item">&starf; Up to 60% Cost Reduction</span>
    <span class="tick-item">&starf; USA &amp; Canada Timezone Alignment</span>
    <span class="tick-item">&starf; Bank-Grade Confidentiality</span>
    <span class="tick-item">&starf; Dedicated Offshore Accounting Teams</span>
  </div>
</div>

<!-- Pillars Strip — LIGHT white bg -->
<div class="pillars-strip">
  <div class="pillars-grid">
    <div class="pillar rev">
      <div class="p-icon"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5zm0 0v6"/></svg></div>
      <div><div class="p-title">Qualified CAs</div><div class="p-desc">Chartered Accountant supervision on all reconciliations &amp; reports</div></div>
    </div>
    <div class="pillar rev d1">
      <div class="p-icon"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg></div>
      <div><div class="p-title">Cloud Integrations</div><div class="p-desc">QuickBooks, Xero, Bill.com, Gusto, Dext &amp; Power BI stack</div></div>
    </div>
    <div class="pillar feat rev d2">
      <div class="p-icon feat"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div>
      <div><div class="p-title">Cost Optimization</div><div class="p-desc">Reduce accounting overhead by up to 60% with SLA delivery</div></div>
    </div>
    <div class="pillar rev d3">
      <div class="p-icon"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg></div>
      <div><div class="p-title">Bank-Grade Security</div><div class="p-desc">Role-based access, strict NDAs &amp; bank-grade encryption</div></div>
    </div>
  </div>
</div>

<!-- ═══ ABOUT / BRAND STORY — Warm Ivory bg ═══ -->
<section id="brand-story" class="section bg-ivory">
  <div class="container">
    <div class="sec-hdr rev">
      <div class="label-row"><span class="label">Sanskrit &amp; Hindi Heritage</span></div>
      <h2 class="h-lg mb2">Where Accounting Meets <span class="t-saffron f-serif" style="font-style:italic">Heritage</span></h2>
      <div class="gold-bar"></div>
    </div>
    <div class="about-grid">
      <!-- Left: Dark heritage card -->
      <div class="rev">
        <div class="heritage-card">
          <div class="label mb2">Traditional Philosophy</div>
          <h3 class="h-md t-white mb3">"Every Number Tells The Truth"</h3>
          <p style="font-size:.9375rem;color:rgba(255,255,255,.65);line-height:1.8;margin-bottom:1.5rem">
            <strong style="color:var(--saffron);font-style:italic">"Lekhankan"</strong> is derived from Sanskrit and Hindi, meaning systematic record-keeping and precise financial ledger writing.
          </p>
          <p style="font-size:.875rem;color:rgba(255,255,255,.55);line-height:1.8;margin-bottom:1.5rem">
            Long before cloud accounting and automated financial systems, merchants maintained detailed records through disciplined ledger practices. That spirit of precision, transparency, and organized financial thinking inspires Lekhankan today.
          </p>
          <blockquote style="border-left:2px solid var(--saffron);padding-left:1rem;font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1rem;color:rgba(255,255,255,.8);line-height:1.7">
            "From traditional ledgers to modern cloud accounting, the principle remains unchanged: <span style="color:var(--saffron)">every number should tell the truth.</span>"
          </blockquote>
          <div class="ledger-viz">
            DATE &nbsp;&nbsp;| ACCOUNT &nbsp;| DEBIT &nbsp;&nbsp;| CREDIT<br>
            &mdash;&mdash;&mdash;&mdash;+&mdash;&mdash;&mdash;&mdash;&mdash;+&mdash;&mdash;&mdash;&mdash;+&mdash;&mdash;&mdash;&mdash;<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Bahi Khata | Precise | True<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Cloud Acctg | Modern | Secure
          </div>
        </div>
        <div class="phase-strip">
          <div class="phase-item" style="background:#fff;border-right:1px solid var(--border-2)">
            <div class="phase-lbl">Phase 1</div>
            <div class="phase-name">Heritage</div>
            <div class="phase-sub">Bahi Khata Discipline</div>
          </div>
          <div class="phase-item" style="background:var(--ivory-2);border-right:1px solid var(--border-2)">
            <div class="phase-lbl" style="color:var(--gold)">Phase 2</div>
            <div class="phase-name">Cloud</div>
            <div class="phase-sub">QBO/Xero Workflows</div>
          </div>
          <div class="phase-item" style="background:var(--midnight)">
            <div class="phase-lbl">Phase 3</div>
            <div class="phase-name t-white">Intelligence</div>
            <div class="phase-sub" style="color:rgba(255,255,255,.5)">Power BI Insights</div>
          </div>
        </div>
        <div class="tech-logos">
          <span class="tech-logo">QuickBooks</span>
          <span class="tech-logo">Xero</span>
          <span class="tech-logo">Bill.com</span>
          <span class="tech-logo">Gusto</span>
          <span class="tech-logo">Dext</span>
          <span class="tech-logo">Power BI</span>
        </div>
      </div>
      <!-- Right: Why Choose Us — LIGHT card -->
      <div class="rev d2">
        <div class="label-row mb3"><span class="label">Our Core Pillars</span></div>
        <h2 class="h-lg mb2">Why Businesses Choose <span class="t-saffron">Lekhankan</span></h2>
        <p class="t-body mb4">We combine centuries of Indian accounting heritage with modern cloud technology, qualified finance professionals, and standardized processes to deliver reliable financial operations for North American businesses.</p>
        <div class="why-list">
          <div class="why-item">
            <div class="checkmark">&#10003;</div>
            <div><div class="h-sm mb1">Reduce Accounting Costs by up to 60%</div><div class="t-slate">Access dedicated accounting professionals without the overhead of hiring in-house finance staff in the US or Canada.</div></div>
          </div>
          <div class="why-item">
            <div class="checkmark">&#10003;</div>
            <div><div class="h-sm mb1">Dedicated Offshore Accounting Team</div><div class="t-slate">Work with dedicated bookkeepers, accountants, reviewers, and finance specialists aligned with your business processes.</div></div>
          </div>
          <div class="why-item">
            <div class="checkmark">&#10003;</div>
            <div><div class="h-sm mb1">Qualified Chartered Accountants</div><div class="t-slate">Our operations are supervised by Chartered Accountants, ensuring quality, consistency, and professional financial reporting.</div></div>
          </div>
          <div class="why-item">
            <div class="checkmark">&#10003;</div>
            <div><div class="h-sm mb1">Technology-Driven Accounting</div><div class="t-slate">We utilize QuickBooks Online, Xero, Bill.com, Gusto, Dext, Stripe, and Power BI for seamless operations.</div></div>
          </div>
          <div class="why-item">
            <div class="checkmark">&#10003;</div>
            <div><div class="h-sm mb1">Secure &amp; Confidential</div><div class="t-slate">Secure workflows, role-based access, confidentiality agreements, and standardized quality controls.</div></div>
          </div>
          <div class="why-item">
            <div class="checkmark">&#10003;</div>
            <div><div class="h-sm mb1">Scalable Accounting Solutions</div><div class="t-slate">Whether you need one bookkeeper or a complete offshore accounting department, our delivery model grows with you.</div></div>
          </div>
        </div>
        <div class="mt4" style="display:flex;gap:1rem;flex-wrap:wrap">
          <a href="#contact" class="btn btn-primary">Schedule a Consultation</a>
          <a href="#services" class="btn btn-dark">Our Services</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ SERVICES — White bg ═══ -->
<section id="services" class="section bg-white">
  <div class="container">
    <div class="sec-hdr rev">
      <div class="label-row"><span class="label">Comprehensive Solutions</span></div>
      <h2 class="h-lg mb2">We Provide The <span class="t-saffron">Best Services</span></h2>
      <div class="gold-bar"></div>
      <p class="t-body mt3">End-to-end offshore accounting, AP, AR, payroll, and virtual CFO solutions tailored for North American businesses and CPA firms.</p>
    </div>
    <div class="tab-nav rev">
      <button class="tab-btn on" onclick="svcTab('bookkeeping',this)">Bookkeeping (8)</button>
      <button class="tab-btn" onclick="svcTab('accounting',this)">Accounting (6)</button>
      <button class="tab-btn" onclick="svcTab('ap',this)">Accounts Payable (7)</button>
      <button class="tab-btn" onclick="svcTab('ar',this)">Accounts Receivable (6)</button>
      <button class="tab-btn" onclick="svcTab('payroll',this)">Payroll (5)</button>
      <button class="tab-btn" onclick="svcTab('reporting',this)">Reporting &amp; CFO (6)</button>
    </div>

    <div id="tab-bookkeeping" class="tab-pane on">
      <div class="svc-card rev"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></div><h3 class="h-sm mb2">Daily Transaction Recording</h3><p class="t-slate">Accurate recording of income, expenses, deposits, and payments categorized according to your Chart of Accounts and accounting policies.</p></div>
      <div class="svc-card rev d1"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Bank Reconciliation</h3><p class="t-slate">Regular reconciliation comparing accounting records with bank statements to identify missing transactions, duplicates, and unexplained balances.</p></div>
      <div class="svc-card rev d2"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Credit Card Reconciliation</h3><p class="t-slate">Reconciliation of business credit card accounts against monthly statements, reviewing purchases, refunds, payments, and outstanding balances.</p></div>
      <div class="svc-card rev d3"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></div><h3 class="h-sm mb2">General Ledger Maintenance</h3><p class="t-slate">Maintaining a clean and organized General Ledger by accurately recording transactions, reviewing classifications, and identifying incorrect entries.</p></div>
      <div class="svc-card rev d1"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg></div><h3 class="h-sm mb2">Chart of Accounts Management</h3><p class="t-slate">Structured Chart of Accounts aligned with your business model, reporting requirements, and accounting policies with consistent classification.</p></div>
      <div class="svc-card rev d2"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg></div><h3 class="h-sm mb2">Journal Entries &amp; Adjustments</h3><p class="t-slate">Preparing accruals, prepayments, depreciation, reclassifications, payroll adjustments, and other journal entries with proper documentation.</p></div>
      <div class="svc-card rev d3"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Month-End Bookkeeping</h3><p class="t-slate">Complete month-end cycle including transaction review, reconciliations, adjustments, account analysis, and financial statement preparation.</p></div>
      <div class="svc-card rev d4"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg></div><h3 class="h-sm mb2">Historical Bookkeeping Cleanup</h3><p class="t-slate">Reviewing prior transactions, reconciling accounts, correcting classifications, removing duplicates, and organizing financial records to an accurate position.</p></div>
    </div>

    <div id="tab-accounting" class="tab-pane">
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg></div><h3 class="h-sm mb2">Dedicated Staff Accountants</h3><p class="t-slate">Full-time dedicated accounting professionals working exclusively as an extension of your in-house finance team.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><h3 class="h-sm mb2">Senior Accountants &amp; Reviewers</h3><p class="t-slate">Advanced accounting support handling complex month-end closings, financial statement analysis, and quality assurance review.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Month-End Closing Support</h3><p class="t-slate">Structured month-end close support including reconciliations, adjustments, journal entries, variance analysis, and financial statement preparation.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg></div><h3 class="h-sm mb2">Multi-Entity Accounting</h3><p class="t-slate">Consolidated multi-entity bookkeeping and accounting support with separate books per entity and consolidated reporting.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg></div><h3 class="h-sm mb2">Financial Statement Preparation</h3><p class="t-slate">Preparation of P&amp;L, Balance Sheet, Cash Flow Statements, and management packages aligned with your reporting requirements.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><h3 class="h-sm mb2">Accounting Software Setup</h3><p class="t-slate">QuickBooks Online, Xero configuration, Chart of Accounts setup, opening balance migration, and workflow implementation.</p></div>
    </div>

    <div id="tab-ap" class="tab-pane">
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"/></svg></div><h3 class="h-sm mb2">Invoice Processing</h3><p class="t-slate">Accurate and timely recording of vendor invoices, verifying against purchase orders and managing approval workflows.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg></div><h3 class="h-sm mb2">Vendor Management</h3><p class="t-slate">Maintaining vendor records, contact information, payment terms, and W-9 documentation to support 1099 reporting.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2"/></svg></div><h3 class="h-sm mb2">Payment Processing Support</h3><p class="t-slate">Preparing payment runs, ACH batches, and check requests aligned with AP aging and cash flow priorities.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z"/></svg></div><h3 class="h-sm mb2">AP Aging Management</h3><p class="t-slate">Maintaining current AP aging reports, monitoring overdue balances, and providing management visibility into outstanding obligations.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><h3 class="h-sm mb2">AP Reconciliation</h3><p class="t-slate">Reconciling accounts payable balances against vendor statements, identifying discrepancies and unrecorded invoices.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zm0 8a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zm12 0a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/></svg></div><h3 class="h-sm mb2">Expense Report Processing</h3><p class="t-slate">Processing employee expense reports, verifying receipts, coding to appropriate accounts, and managing reimbursement workflows.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/></svg></div><h3 class="h-sm mb2">AP Automation Setup</h3><p class="t-slate">Implementing AP automation workflows using Bill.com, Dext, and QuickBooks to streamline invoice capture and approvals.</p></div>
    </div>

    <div id="tab-ar" class="tab-pane">
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/></svg></div><h3 class="h-sm mb2">Invoice Generation</h3><p class="t-slate">Creating and sending professional customer invoices accurately reflecting services rendered, payment terms, and billing schedules.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"/></svg></div><h3 class="h-sm mb2">Collections &amp; Follow-Up</h3><p class="t-slate">Managing customer communication for overdue invoices, sending payment reminders, and escalating per your collections policy.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg></div><h3 class="h-sm mb2">AR Aging Reports</h3><p class="t-slate">Maintaining current AR aging analysis, tracking outstanding customer balances by age to support collections and cash flow management.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Cash Application</h3><p class="t-slate">Accurately applying customer payments to open invoices, managing partial payments, credits, and adjustments within the accounting system.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg></div><h3 class="h-sm mb2">Customer Account Management</h3><p class="t-slate">Maintaining complete customer master data, payment history, credit terms, and account status to support billing accuracy.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><h3 class="h-sm mb2">Stripe &amp; Payment Reconciliation</h3><p class="t-slate">Reconciling Stripe and payment processor transactions with accounting records and bank deposits, accounting for fees and refunds.</p></div>
    </div>

    <div id="tab-payroll" class="tab-pane">
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"/></svg></div><h3 class="h-sm mb2">Payroll Journal Entries</h3><p class="t-slate">Recording payroll journal entries for wages, salaries, employer taxes, benefits, deductions, and payroll liabilities.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Payroll Reconciliation</h3><p class="t-slate">Reconciling payroll records against bank transactions, tax liabilities, and general ledger balances for accuracy.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg></div><h3 class="h-sm mb2">Gusto &amp; ADP Integration</h3><p class="t-slate">Integrating Gusto and ADP payroll data with QuickBooks Online and Xero, ensuring accurate sync of payroll entries.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><h3 class="h-sm mb2">Payroll Tax Accounting</h3><p class="t-slate">Recording and reconciling payroll tax deposits, employer FICA, state withholding, and unemployment tax liabilities.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Year-End Payroll Support</h3><p class="t-slate">Reconciling annual payroll records against W-2 and 1099 totals and organizing payroll documentation for tax filing.</p></div>
    </div>

    <div id="tab-reporting" class="tab-pane">
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg></div><h3 class="h-sm mb2">Monthly Financial Reporting</h3><p class="t-slate">Preparing P&amp;L statements, Balance Sheets, Cash Flow Statements, and management packages aligned with your reporting requirements.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 3.055A9.001 9.001 0 1020.945 13H11V3.055z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.488 9H15V3.512A9.025 9.025 0 0120.488 9z"/></svg></div><h3 class="h-sm mb2">Power BI Dashboards</h3><p class="t-slate">Creating and maintaining Power BI financial dashboards with real-time KPI visibility, trend analysis, and executive-level reporting.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg></div><h3 class="h-sm mb2">Budgeting &amp; Forecasting</h3><p class="t-slate">Preparing annual budgets, rolling forecasts, and variance analysis to support management decision-making and performance monitoring.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/></svg></div><h3 class="h-sm mb2">Cash Flow Management</h3><p class="t-slate">Monitoring cash inflows and outflows, preparing weekly and monthly cash flow projections, and analyzing working capital requirements.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Virtual CFO Services</h3><p class="t-slate">Fractional CFO-level financial strategy, KPI monitoring, financial modeling, investor reporting, and management advisory.</p></div>
      <div class="svc-card"><div class="svc-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></div><h3 class="h-sm mb2">KPI &amp; Performance Reporting</h3><p class="t-slate">Developing and maintaining KPI scorecards, operational metrics, and performance dashboards that connect financial data to business objectives.</p></div>
    </div>
  </div>
</section>

<!-- ═══ WHY US — Dark Midnight band ═══ -->
<section id="why-us" class="section bg-dark">
  <div class="container">
    <div class="why-grid">
      <div class="rev">
        <div class="label-row mb3"><span class="label">Cost Optimization &amp; ROI</span></div>
        <h2 class="h-lg t-white mb3">Reduce Accounting Overhead By Up To <span class="t-saffron">60%</span></h2>
        <p style="color:rgba(255,255,255,.65);font-size:.9375rem;line-height:1.8;margin-bottom:2.5rem">Get dedicated bookkeepers, staff accountants, and CA reviewers aligned with your timezone and accounting platforms without the cost of in-house hiring.</p>
        <div class="cl-item"><div class="check-dark">&#10003;</div><div><div style="font-size:.9375rem;font-weight:700;color:#fff;margin-bottom:.25rem">No Overhead Expenses</div><div style="font-size:.8125rem;color:rgba(255,255,255,.5)">Zero recruitment fees, employee benefits, healthcare, or office infrastructure costs.</div></div></div>
        <div class="cl-item"><div class="check-dark">&#10003;</div><div><div style="font-size:.9375rem;font-weight:700;color:#fff;margin-bottom:.25rem">Chartered Accountant Supervision</div><div style="font-size:.8125rem;color:rgba(255,255,255,.5)">Multi-tier quality assurance with qualified CAs reviewing all reconciliations.</div></div></div>
        <div class="cl-item"><div class="check-dark">&#10003;</div><div><div style="font-size:.9375rem;font-weight:700;color:#fff;margin-bottom:.25rem">Seamless Tech Stack</div><div style="font-size:.8125rem;color:rgba(255,255,255,.5)">Immediate operational setup in QBO, Xero, Bill.com, Gusto, and Power BI.</div></div></div>
        <div class="cl-item"><div class="check-dark">&#10003;</div><div><div style="font-size:.9375rem;font-weight:700;color:#fff;margin-bottom:.25rem">USA &amp; Canada Timezone Alignment</div><div style="font-size:.8125rem;color:rgba(255,255,255,.5)">Active during your business hours with real-time communication and daily updates.</div></div></div>
        <div class="mt4"><a href="#contact" class="btn btn-primary">Build Your Team Proposal</a></div>
      </div>
      <div class="roi-card rev d2">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;margin-bottom:.5rem">
          <div class="label">Annual ROI Calculator</div>
          <div style="display:flex;gap:.5rem">
            <button onclick="setROICur('USD')" id="btn-usd" class="roi-tab on" style="padding:.3rem .875rem;font-size:.6875rem">USD ($)</button>
            <button onclick="setROICur('CAD')" id="btn-cad" class="roi-tab" style="padding:.3rem .875rem;font-size:.6875rem">CAD ($)</button>
          </div>
        </div>
        <div id="roi-amount" class="roi-amount">$64,800 / year</div>
        <div style="font-size:.75rem;color:rgba(255,255,255,.5);margin-top:.375rem">Estimated annual savings</div>
        <div class="roi-tabs">
          <button class="roi-tab on" onclick="setROIRole('bookkeeper',this)">Bookkeeper</button>
          <button class="roi-tab" onclick="setROIRole('cpa',this)">CPA / Lead CA</button>
          <button class="roi-tab" onclick="setROIRole('tax',this)">Tax &amp; Payroll</button>
        </div>
        <div class="roi-bar-row" style="margin-top:2rem">
          <div class="roi-bar-lbl"><span>In-House Hire Cost</span><span id="inhouseLbl" style="color:rgba(255,255,255,.9)">$140,000/yr</span></div>
          <div class="roi-track"><div class="roi-fill" id="inhouseBar" style="width:100%"></div></div>
        </div>
        <div class="roi-bar-row">
          <div class="roi-bar-lbl"><span>Lekhankan Dedicated Team</span><span id="lekLbl" style="color:var(--saffron)">$75,200/yr</span></div>
          <div class="roi-track"><div class="roi-fill" id="lekBar" style="width:54%;background:rgba(201,138,50,.6)"></div></div>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:1.75rem;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,.08)">
          <div><div style="font-size:.75rem;color:rgba(255,255,255,.5)">You save approximately</div><div id="savePct" style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1.5rem;font-weight:800;color:var(--saffron)">~54%</div></div>
          <a href="#contact" class="btn btn-primary" style="padding:.75rem 1.5rem;font-size:.75rem">Get My Proposal &rarr;</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ INDUSTRIES — Ivory bg ═══ -->
<section id="industries" class="section bg-ivory2">
  <div class="container">
    <div class="sec-hdr rev">
      <div class="label-row"><span class="label">Industries We Serve</span></div>
      <h2 class="h-lg mb2">Specialized Accounting for <span class="t-saffron">Every Industry</span></h2>
      <div class="gold-bar"></div>
      <p class="t-body mt3">Deep expertise across CPA firms, e-commerce, healthcare, real estate, hospitality, and professional services businesses across North America.</p>
    </div>
    <div class="ind-grid rev">
      <div class="ind-sidebar">
        <button class="ind-btn on" onclick="indTab('cpa',this)"><div class="ind-icon"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><div><div class="ind-name">CPA &amp; Accounting Firms</div><div class="ind-count">6 service areas</div></div></button>
        <button class="ind-btn" onclick="indTab('ecomm',this)"><div class="ind-icon"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg></div><div><div class="ind-name">E-Commerce Businesses</div><div class="ind-count">6 service areas</div></div></button>
        <button class="ind-btn" onclick="indTab('health',this)"><div class="ind-icon"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg></div><div><div class="ind-name">Healthcare</div><div class="ind-count">5 service areas</div></div></button>
        <button class="ind-btn" onclick="indTab('realty',this)"><div class="ind-icon"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg></div><div><div class="ind-name">Real Estate</div><div class="ind-count">5 service areas</div></div></button>
        <button class="ind-btn" onclick="indTab('prof',this)"><div class="ind-icon"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></div><div><div class="ind-name">Professional Services</div><div class="ind-count">4 service areas</div></div></button>
        <button class="ind-btn" onclick="indTab('hosp',this)"><div class="ind-icon"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg></div><div><div class="ind-name">Hospitality &amp; Retail</div><div class="ind-count">4 service areas</div></div></button>
      </div>
      <div>
        <div id="ind-cpa" class="ind-content on"><h3 class="h-md mb2">CPA &amp; Accounting Firms</h3><p class="t-body mb4">We operate as a white-label accounting back-office for CPA and accounting firms, providing capacity and specialized skills without the overhead of internal hiring.</p><img src="cpa_firms_portrait.png" alt="CPA Professional Services" style="width:100%;max-height:200px;object-fit:cover;border-radius:var(--r-md);margin-bottom:1.5rem;border:1px solid var(--border);" /><div class="ind-svc-grid"><div class="ind-svc"><div class="h-sm mb1">White-Label Bookkeeping</div><p class="t-slate" style="font-size:.8125rem">Back-office support under your firm's brand and processes.</p></div><div class="ind-svc"><div class="h-sm mb1">Bookkeeping Cleanup</div><p class="t-slate" style="font-size:.8125rem">Historical cleanup of unreconciled, duplicate client books.</p></div><div class="ind-svc"><div class="h-sm mb1">Monthly Bookkeeping</div><p class="t-slate" style="font-size:.8125rem">Recurring monthly bookkeeping for your firm's client base.</p></div><div class="ind-svc"><div class="h-sm mb1">Year-End Support</div><p class="t-slate" style="font-size:.8125rem">Final reconciliations and schedules supporting tax preparation.</p></div><div class="ind-svc"><div class="h-sm mb1">Staff Augmentation</div><p class="t-slate" style="font-size:.8125rem">Flexible resources for seasonal or capacity-driven demands.</p></div><div class="ind-svc"><div class="h-sm mb1">Accounting Review</div><p class="t-slate" style="font-size:.8125rem">Independent QA review of reconciliations and financial records.</p></div></div></div>
        <div id="ind-ecomm" class="ind-content"><h3 class="h-md mb2">E-Commerce Businesses</h3><p class="t-body mb4">Specialized bookkeeping for Amazon, Shopify, WooCommerce, and direct-to-consumer brands, reconciling marketplace transactions with accounting accuracy.</p><img src="ecommerce_business_portrait.png" alt="E-Commerce Accounting" style="width:100%;max-height:200px;object-fit:cover;border-radius:var(--r-md);margin-bottom:1.5rem;border:1px solid var(--border);" /><div class="ind-svc-grid"><div class="ind-svc"><div class="h-sm mb1">Amazon Seller Accounting</div><p class="t-slate" style="font-size:.8125rem">Reconciliation of marketplace sales, fees, refunds, and settlements.</p></div><div class="ind-svc"><div class="h-sm mb1">Shopify Bookkeeping</div><p class="t-slate" style="font-size:.8125rem">Online sales, refunds, processing fees, and payout reconciliation.</p></div><div class="ind-svc"><div class="h-sm mb1">Stripe Reconciliation</div><p class="t-slate" style="font-size:.8125rem">Reconciling Stripe transactions with bank deposits and records.</p></div><div class="ind-svc"><div class="h-sm mb1">Inventory Accounting</div><p class="t-slate" style="font-size:.8125rem">Purchase, sales, and COGS accounting for product businesses.</p></div><div class="ind-svc"><div class="h-sm mb1">WooCommerce Support</div><p class="t-slate" style="font-size:.8125rem">Organizing WooCommerce transactions for accurate reporting.</p></div><div class="ind-svc"><div class="h-sm mb1">Sales Tax Support</div><p class="t-slate" style="font-size:.8125rem">Organizing data to support sales tax compliance workflows.</p></div></div></div>
        <div id="ind-health" class="ind-content"><h3 class="h-md mb2">Healthcare</h3><p class="t-body mb4">Bookkeeping and accounting tailored to medical practices, dental offices, and healthcare organizations with structured financial reporting and revenue visibility.</p><img src="healthcare_accounting_portrait.png" alt="Healthcare Accounting" style="width:100%;max-height:200px;object-fit:cover;border-radius:var(--r-md);margin-bottom:1.5rem;border:1px solid var(--border);" /><div class="ind-svc-grid"><div class="ind-svc"><div class="h-sm mb1">Medical Clinics</div><p class="t-slate" style="font-size:.8125rem">Revenue tracking, expense management, and financial reporting.</p></div><div class="ind-svc"><div class="h-sm mb1">Dental Practices</div><p class="t-slate" style="font-size:.8125rem">Bank reconciliation, AP/AR, and organized financial records.</p></div><div class="ind-svc"><div class="h-sm mb1">Physician Practices</div><p class="t-slate" style="font-size:.8125rem">Bookkeeping, reconciliations, and management reporting.</p></div><div class="ind-svc"><div class="h-sm mb1">Insurance Reconciliation</div><p class="t-slate" style="font-size:.8125rem">Reconciling insurance revenue and payment data against records.</p></div><div class="ind-svc"><div class="h-sm mb1">Revenue Reporting</div><p class="t-slate" style="font-size:.8125rem">Organized revenue and receivables reporting for management.</p></div></div></div>
        <div id="ind-realty" class="ind-content"><h3 class="h-md mb2">Real Estate</h3><p class="t-body mb4">Property-level bookkeeping, rent collection tracking, maintenance expense allocation, and investor-ready financial reporting.</p><img src="real_estate_portrait.png" alt="Real Estate Accounting" style="width:100%;max-height:200px;object-fit:cover;border-radius:var(--r-md);margin-bottom:1.5rem;border:1px solid var(--border);" /><div class="ind-svc-grid"><div class="ind-svc"><div class="h-sm mb1">Property Accounting</div><p class="t-slate" style="font-size:.8125rem">Income and expense accounting by property unit and portfolio.</p></div><div class="ind-svc"><div class="h-sm mb1">Rental Income Tracking</div><p class="t-slate" style="font-size:.8125rem">Rent collection recording, tenant ledgers, and cash flow visibility.</p></div><div class="ind-svc"><div class="h-sm mb1">CAM Reconciliation</div><p class="t-slate" style="font-size:.8125rem">Common area maintenance reconciliation for commercial properties.</p></div><div class="ind-svc"><div class="h-sm mb1">Investor Reporting</div><p class="t-slate" style="font-size:.8125rem">Monthly financial packages for real estate investors and funds.</p></div><div class="ind-svc"><div class="h-sm mb1">Mortgage Reconciliation</div><p class="t-slate" style="font-size:.8125rem">Recording and reconciling loan payments and principal balances.</p></div></div></div>
        <div id="ind-prof" class="ind-content"><h3 class="h-md mb2">Professional Services</h3><p class="t-body mb4">Bookkeeping and financial reporting for law firms, consulting firms, marketing agencies, and other service-based businesses.</p><img src="professional_services_portrait.png" alt="Professional Services Accounting" style="width:100%;max-height:200px;object-fit:cover;border-radius:var(--r-md);margin-bottom:1.5rem;border:1px solid var(--border);" /><div class="ind-svc-grid"><div class="ind-svc"><div class="h-sm mb1">Law Firm Bookkeeping</div><p class="t-slate" style="font-size:.8125rem">IOLTA trust account management and billing reconciliation.</p></div><div class="ind-svc"><div class="h-sm mb1">Consulting Firm Accounting</div><p class="t-slate" style="font-size:.8125rem">Project-level revenue tracking and expense allocation.</p></div><div class="ind-svc"><div class="h-sm mb1">Agency Bookkeeping</div><p class="t-slate" style="font-size:.8125rem">Client billing, retainer tracking, and financial reporting.</p></div><div class="ind-svc"><div class="h-sm mb1">Financial Reporting</div><p class="t-slate" style="font-size:.8125rem">Monthly P&amp;L, balance sheet, and management reporting packages.</p></div></div></div>
        <div id="ind-hosp" class="ind-content"><h3 class="h-md mb2">Hospitality &amp; Retail</h3><p class="t-body mb4">Daily revenue reporting, cost of goods sold tracking, and inventory accounting for hotels, restaurants, and retail businesses.</p><div class="ind-svc-grid"><div class="ind-svc"><div class="h-sm mb1">Restaurant Accounting</div><p class="t-slate" style="font-size:.8125rem">Daily sales recording, COGS tracking, and cash management.</p></div><div class="ind-svc"><div class="h-sm mb1">Hotel Bookkeeping</div><p class="t-slate" style="font-size:.8125rem">Revenue reconciliation, department expense allocation.</p></div><div class="ind-svc"><div class="h-sm mb1">Retail Inventory Accounting</div><p class="t-slate" style="font-size:.8125rem">Inventory cost tracking, shrinkage recording, and margin reporting.</p></div><div class="ind-svc"><div class="h-sm mb1">POS Reconciliation</div><p class="t-slate" style="font-size:.8125rem">Reconciling Point-of-Sale data with bank deposits and accounting.</p></div></div></div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ CPA PARTNER — Dark band ═══ -->
<section id="cpa-partner" class="section bg-dark">
  <div class="container">
    <div class="cpa-grid">
      <div class="rev">
        <div class="label-row mb3"><span class="label">CPA Firm Partnership</span></div>
        <h2 class="h-lg t-white mb3">Build Your Dedicated <span class="t-saffron">Finance Team</span> Today</h2>
        <p style="color:rgba(255,255,255,.65);font-size:.9375rem;line-height:1.8;margin-bottom:2.5rem">Join CPA firms and businesses across the USA &amp; Canada that have partnered with Lekhankan to scale accounting operations, improve turnaround times, and reduce overhead without sacrificing quality.</p>
        <div class="cpa-feat"><div class="icon-box-dark"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><div><div style="font-size:.9375rem;font-weight:700;color:#fff;margin-bottom:.25rem">White-Label Operations</div><div style="font-size:.8125rem;color:rgba(255,255,255,.5)">We operate invisibly under your brand using your templates, formats, and client communication style.</div></div></div>
        <div class="cpa-feat"><div class="icon-box-dark"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg></div><div><div style="font-size:.9375rem;font-weight:700;color:#fff;margin-bottom:.25rem">Scalable Capacity</div><div style="font-size:.8125rem;color:rgba(255,255,255,.5)">Add bookkeepers and accountants quickly during tax season or client growth without permanent hiring.</div></div></div>
        <div class="cpa-feat"><div class="icon-box-dark"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><div><div style="font-size:.9375rem;font-weight:700;color:#fff;margin-bottom:.25rem">Faster Turnaround Times</div><div style="font-size:.8125rem;color:rgba(255,255,255,.5)">Overnight task completion with results ready for your team each morning during North American hours.</div></div></div>
        <div class="mt4" style="display:flex;gap:1rem;flex-wrap:wrap"><a href="#contact" class="btn btn-primary">Partner With Lekhankan</a><a href="#contact" class="btn btn-white">Discuss Outsourcing</a></div>
      </div>
      <div class="rev d2">
        <div style="background:rgba(255,255,255,.05);border:1px solid rgba(201,138,50,.2);border-radius:var(--r-xl);padding:2.5rem">
          <div class="label mb4">Our Partnership Benefits</div>
          <div class="cpa-stats">
            <div class="cpa-stat"><div class="cpa-stat-num">24hr</div><div class="cpa-stat-lbl">SLA Turnaround</div></div>
            <div class="cpa-stat"><div class="cpa-stat-num">100%</div><div class="cpa-stat-lbl">CA Quality Review</div></div>
            <div class="cpa-stat"><div class="cpa-stat-num">NDA</div><div class="cpa-stat-lbl">Strict Confidentiality</div></div>
            <div class="cpa-stat"><div class="cpa-stat-num">60%</div><div class="cpa-stat-lbl">Avg. Cost Savings</div></div>
          </div>
          <p style="font-size:.8125rem;color:rgba(255,255,255,.45);line-height:1.7;margin-top:1.75rem;font-style:italic;font-family:'Cormorant Garamond',serif">"Lekhankan has allowed our firm to scale from 50 to 120 clients without adding a single internal hire. Their CA-supervised process quality is exceptional."</p>
          <div style="margin-top:1rem;font-size:.75rem;color:rgba(255,255,255,.35)">&mdash; Managing Partner, CPA Firm, Texas, USA</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ PROCESS — Ivory bg ═══ -->
<section id="process" class="section bg-ivory">
  <div class="container">
    <div class="sec-hdr rev">
      <div class="label-row"><span class="label">Standardized Execution Model</span></div>
      <h2 class="h-lg mb2">Our <span class="f-serif t-saffron" style="font-style:italic">Working Process</span></h2>
      <div class="gold-bar"></div>
      <p class="t-body mt3">An 8-step structured onboarding and daily delivery workflow designed for seamless accounting integration without operational friction.</p>
    </div>
    <div class="proc-grid rev">
      <div class="proc-card"><div class="step-num mb3">01</div><h3 class="h-sm mb2">Discovery &amp; Scope</h3><p class="t-slate">Evaluating software stack, transaction volumes, Chart of Accounts, SLAs, and reporting expectations.</p></div>
      <div class="proc-card active"><div class="step-num mb3">02</div><h3 class="h-sm mb2">SLA Agreement &amp; Security</h3><p class="t-slate">Establishing NDAs, role-based cloud access, data security protocols, and turn-around time SLAs.</p></div>
      <div class="proc-card"><div class="step-num mb3">03</div><h3 class="h-sm mb2">Software Configuration</h3><p class="t-slate">Connecting QBO, Xero, Bill.com, Gusto, Dext, and building standardized Chart of Accounts.</p></div>
      <div class="proc-card"><div class="step-num mb3">04</div><h3 class="h-sm mb2">Dedicated Team Assignment</h3><p class="t-slate">Assigning staff accountants, senior reviewers, and CA supervisors matching your US/Canada timezone.</p></div>
      <div class="proc-card"><div class="step-num mb3">05</div><h3 class="h-sm mb2">Daily Operations &amp; Coding</h3><p class="t-slate">Daily transaction categorization, bank reconciliations, vendor invoice coding, and payment processing.</p></div>
      <div class="proc-card"><div class="step-num mb3">06</div><h3 class="h-sm mb2">CA Review &amp; Audit Control</h3><p class="t-slate">Independent QA review by Chartered Accountants ensuring 100% accuracy before delivery.</p></div>
      <div class="proc-card"><div class="step-num mb3">07</div><h3 class="h-sm mb2">Month-End Reporting</h3><p class="t-slate">Dispatching P&amp;L, Balance Sheet, Cash Flow &amp; Power BI dashboards as closing packages.</p></div>
      <div class="proc-card"><div class="step-num mb3">08</div><h3 class="h-sm mb2">Review &amp; Scalability</h3><p class="t-slate">Monthly alignment meetings to refine workflows, review KPIs, and scale capacity as needed.</p></div>
    </div>
  </div>
</section>

<!-- ═══ TESTIMONIALS — White bg ═══ -->
<section id="testimonials" class="section bg-white">
  <div class="container">
    <div class="test-grid">
      <div class="rev">
        <div class="label-row mb3"><span class="label">Client Testimonials</span></div>
        <h2 class="h-lg mb3">Nothing Secures You <span class="t-saffron">Better Than Us</span></h2>
        <div class="gold-bar-left"></div>
        <p class="t-body mt3 mb4">Our clients trust us with their most sensitive financial operations. From CPA firms to multi-state businesses, we deliver consistent quality and accuracy every month.</p>
        <div class="stat-grid">
          <div><div class="s-num">100+</div><div class="s-lbl">Active Clients</div></div>
          <div><div class="s-num">60%</div><div class="s-lbl">Avg. Cost Savings</div></div>
          <div><div class="s-num">24hr</div><div class="s-lbl">SLA Turnaround</div></div>
        </div>
      </div>
      <div class="rev d2">
        <div class="test-card">
          <div class="stars"><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span></div>
          <p class="test-q">"Lekhankan's team integrated seamlessly with our QBO environment. Month-end closes that used to take two weeks now complete in 3 days. Their CA review process is outstanding."</p>
          <div style="display:flex;align-items:center;gap:.875rem;padding-top:1.25rem;border-top:1px solid rgba(255,255,255,.08)">
            <div style="width:2.25rem;height:2.25rem;border-radius:50%;background:rgba(201,138,50,.2);display:flex;align-items:center;justify-content:center;color:var(--saffron);font-weight:800;font-size:.875rem">MR</div>
            <div><div style="font-size:.875rem;font-weight:700;color:#fff">Michael R.</div><div style="font-size:.75rem;color:rgba(255,255,255,.45)">Managing Partner, CPA Firm &mdash; California</div></div>
          </div>
        </div>
        <div class="test-card">
          <div class="stars"><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span><span class="star">&#9733;</span></div>
          <p class="test-q">"We reduced our bookkeeping costs by 58% within the first quarter. The team knows QuickBooks Online exceptionally well and our financial reports are cleaner than ever."</p>
          <div style="display:flex;align-items:center;gap:.875rem;padding-top:1.25rem;border-top:1px solid rgba(255,255,255,.08)">
            <div style="width:2.25rem;height:2.25rem;border-radius:50%;background:rgba(201,138,50,.2);display:flex;align-items:center;justify-content:center;color:var(--saffron);font-weight:800;font-size:.875rem">ST</div>
            <div><div style="font-size:.875rem;font-weight:700;color:#fff">Sarah T.</div><div style="font-size:.75rem;color:rgba(255,255,255,.45)">CFO, E-Commerce Business &mdash; Ontario, Canada</div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ LEAD MAGNETS — Ivory bg ═══ -->
<section id="lead-magnets" class="section bg-ivory2">
  <div class="container">
    <div class="sec-hdr rev">
      <div class="label-row"><span class="label">Free Resources</span></div>
      <h2 class="h-lg mb2">Downloadable <span class="t-saffron">Accounting Guides</span></h2>
      <div class="gold-bar"></div>
      <p class="t-body mt3">Professional resources to help businesses and CPA firms improve bookkeeping processes, reduce overhead, and make informed outsourcing decisions.</p>
    </div>
    <div class="res-grid">
      <div class="res-card rev"><div class="res-tag">Checklist</div><div class="res-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg></div><h3 class="h-sm mb2">2026 US Small Business Bookkeeping Checklist</h3><p class="t-slate" style="font-size:.8125rem;flex:1;margin-bottom:1.5rem">Complete monthly bookkeeping checklist covering bank reconciliations, expense coding, AP/AR management, and month-end close.</p><button class="btn btn-saffron-out w-full" style="justify-content:center" onclick="openModal('2026 US Small Business Bookkeeping Checklist')">Download Free &rarr;</button></div>
      <div class="res-card rev d1"><div class="res-tag">Template</div><div class="res-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg></div><h3 class="h-sm mb2">Month-End Close Checklist</h3><p class="t-slate" style="font-size:.8125rem;flex:1;margin-bottom:1.5rem">Structured month-end closing checklist used by Lekhankan's CA-supervised teams, adapted for QuickBooks and Xero environments.</p><button class="btn btn-saffron-out w-full" style="justify-content:center" onclick="openModal('Month-End Close Checklist')">Download Free &rarr;</button></div>
      <div class="res-card rev d2"><div class="res-tag">Calculator</div><div class="res-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><h3 class="h-sm mb2">Bookkeeping Outsourcing Cost Calculator</h3><p class="t-slate" style="font-size:.8125rem;flex:1;margin-bottom:1.5rem">Compare the true cost of in-house bookkeeping vs. offshore outsourcing with salary benchmarks and overhead data for US and Canada.</p><button class="btn btn-saffron-out w-full" style="justify-content:center" onclick="openModal('Bookkeeping Outsourcing Cost Calculator')">Download Free &rarr;</button></div>
      <div class="res-card rev d3"><div class="res-tag">Guide</div><div class="res-icon"><svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><h3 class="h-sm mb2">CPA Firm Outsourcing Readiness Checklist</h3><p class="t-slate" style="font-size:.8125rem;flex:1;margin-bottom:1.5rem">Assessment guide to help CPA firms evaluate readiness for offshore bookkeeping outsourcing across process, security, and communication.</p><button class="btn btn-saffron-out w-full" style="justify-content:center" onclick="openModal('CPA Firm Outsourcing Readiness Checklist')">Download Free &rarr;</button></div>
    </div>
  </div>
</section>

<!-- ═══ CONTACT — Ivory bg ═══ -->
<section id="contact" class="section bg-ivory">
  <div class="container">
    <div class="contact-grid">
      <div class="rev">
        <div class="label-row mb3"><span class="label">Free Accounting Assessment</span></div>
        <h2 class="h-lg mb3">Build Your Dedicated Offshore <span class="t-saffron">Accounting Team</span></h2>
        <p class="t-body mb4">Schedule a consultation with our Chartered Accountants to review your accounting workflow, software stack, volume, and exact cost optimization model. No commitment required.</p>
        <div style="display:flex;flex-direction:column;gap:1.25rem;margin-bottom:2.5rem">
          <div style="display:flex;align-items:flex-start;gap:1rem"><div class="icon-box"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><div><div class="h-sm mb1">No Commitment Consultation</div><div class="t-slate">Custom proposal with transparent pricing and zero long-term lock-in.</div></div></div>
          <div style="display:flex;align-items:flex-start;gap:1rem"><div class="icon-box"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><div><div class="h-sm mb1">Same-Day Response</div><div class="t-slate">Our North American engagement managers respond within 4 business hours.</div></div></div>
          <div style="display:flex;align-items:flex-start;gap:1rem"><div class="icon-box"><svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg></div><div><div class="h-sm mb1">100% Confidential</div><div class="t-slate">All information is protected by strict NDA and data security protocols.</div></div></div>
        </div>
        <div style="background:var(--midnight);border-radius:var(--r-lg);padding:2rem">
          <div class="label mb3">Contact Information</div>
          <div style="display:flex;flex-direction:column;gap:1rem">
            <div style="display:flex;align-items:center;gap:.875rem;font-size:.875rem;color:rgba(255,255,255,.7)"><div class="icon-box-dark" style="width:2rem;height:2rem;border-radius:var(--r-sm);font-size:.75rem">&#9993;</div><span>info@lekhankan.com</span></div>
            <div style="display:flex;align-items:center;gap:.875rem;font-size:.875rem;color:rgba(255,255,255,.7)"><div class="icon-box-dark" style="width:2rem;height:2rem;border-radius:var(--r-sm);font-size:.75rem">&#9742;</div><span>Schedule via the form</span></div>
            <div style="display:flex;align-items:center;gap:.875rem;font-size:.875rem;color:rgba(255,255,255,.7)"><div class="icon-box-dark" style="width:2rem;height:2rem;border-radius:var(--r-sm);font-size:.75rem">&#9200;</div><span>Mon&ndash;Fri, 8AM&ndash;8PM EST</span></div>
          </div>
        </div>
      </div>
      <div class="rev d2">
        <div style="background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);padding:2.5rem;box-shadow:var(--sh-md)">
          <h3 class="h-md mb1">Request a Free Assessment</h3>
          <p class="t-slate mb4">Complete the form and our team will reach out within 4 business hours.</p>
          <form id="aform" onsubmit="formSubmit(event)" style="display:flex;flex-direction:column;gap:1.25rem">
            <div class="grid-2">
              <div><label class="form-lbl">First Name *</label><input type="text" required class="form-input" placeholder="John"/></div>
              <div><label class="form-lbl">Last Name *</label><input type="text" required class="form-input" placeholder="Smith"/></div>
            </div>
            <div class="grid-2">
              <div><label class="form-lbl">Work Email *</label><input type="email" required class="form-input" placeholder="john@firm.com"/></div>
              <div><label class="form-lbl">Phone *</label><input type="tel" required class="form-input" placeholder="+1 (555) 000-0000"/></div>
            </div>
            <div class="grid-2">
              <div><label class="form-lbl">Company / CPA Firm *</label><input type="text" required class="form-input" placeholder="Smith &amp; Associates CPA"/></div>
              <div><label class="form-lbl">Country *</label><select required class="form-input"><option>United States</option><option>Canada</option><option>Other</option></select></div>
            </div>
            <div class="grid-2">
              <div><label class="form-lbl">Industry</label><select class="form-input"><option>CPA / Accounting Firm</option><option>E-Commerce</option><option>Healthcare</option><option>Real Estate</option><option>Professional Services</option><option>Hospitality / Retail</option><option>Other</option></select></div>
              <div><label class="form-lbl">Accounting Software</label><select class="form-input"><option>QuickBooks Online</option><option>Xero</option><option>Bill.com</option><option>NetSuite / Other</option></select></div>
            </div>
            <div class="grid-2">
              <div><label class="form-lbl">Revenue Range</label><select class="form-input"><option>Under $500K</option><option>$500K &ndash; $2M</option><option>$2M &ndash; $10M</option><option>$10M+</option></select></div>
              <div><label class="form-lbl">Service Needed</label><select class="form-input"><option>Offshore Bookkeeping</option><option>AP &amp; AR Management</option><option>Payroll Accounting</option><option>Reporting / Virtual CFO</option><option>CPA Staff Augmentation</option></select></div>
            </div>
            <div><label class="form-lbl">Tell Us About Your Needs</label><textarea class="form-input" placeholder="Transaction volume, current setup, team requirements..."></textarea></div>
            <button type="submit" class="btn btn-primary w-full" style="justify-content:center">Submit Request &amp; Get Proposal &rarr;</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══ FOOTER ═══ -->
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div style="display:flex;align-items:center;gap:.75rem;margin-bottom:1.25rem">
          <div class="logo-badge">L</div>
          <div><div class="logo-name" style="color:#fff">LEKHANKAN</div><div class="logo-sub">By VRM Vrindam (P) Limited</div></div>
        </div>
        <p style="font-size:.875rem;color:rgba(255,255,255,.5);line-height:1.75;max-width:280px;margin-bottom:1.5rem">Where accounting tradition meets cloud precision. Offshore bookkeeping &amp; accounting KPO for USA &amp; Canada.</p>
        <div style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:.875rem;color:var(--saffron);opacity:.7;line-height:1.5">"Every number should tell the truth."</div>
      </div>
      <div>
        <div class="f-head">Services</div>
        <a href="#services" class="f-link">Offshore Bookkeeping</a>
        <a href="#services" class="f-link">Accounting Outsourcing</a>
        <a href="#services" class="f-link">Accounts Payable</a>
        <a href="#services" class="f-link">Accounts Receivable</a>
        <a href="#services" class="f-link">Payroll Accounting</a>
        <a href="#services" class="f-link">Reporting &amp; Virtual CFO</a>
      </div>
      <div>
        <div class="f-head">Industries</div>
        <a href="#industries" class="f-link">CPA &amp; Accounting Firms</a>
        <a href="#industries" class="f-link">E-Commerce</a>
        <a href="#industries" class="f-link">Healthcare</a>
        <a href="#industries" class="f-link">Real Estate</a>
        <a href="#industries" class="f-link">Professional Services</a>
        <a href="#industries" class="f-link">Hospitality &amp; Retail</a>
      </div>
      <div>
        <div class="f-head">Company</div>
        <a href="#brand-story" class="f-link">Our Heritage</a>
        <a href="#why-us" class="f-link">Why Lekhankan</a>
        <a href="#process" class="f-link">Our Process</a>
        <a href="#cpa-partner" class="f-link">CPA Partnership</a>
        <a href="#contact" class="f-link">Contact Us</a>
      </div>
      <div>
        <div class="f-head">Free Resources</div>
        <a href="#lead-magnets" class="f-link">Bookkeeping Checklist</a>
        <a href="#lead-magnets" class="f-link">Month-End Close Guide</a>
        <a href="#lead-magnets" class="f-link">Cost Calculator</a>
        <a href="#lead-magnets" class="f-link">CPA Readiness Guide</a>
        <div class="f-head" style="margin-top:1.5rem">Regions</div>
        <a href="#contact" class="f-link">United States</a>
        <a href="#contact" class="f-link">Canada</a>
      </div>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding-top:2rem;flex-wrap:wrap;gap:1rem">
      <p style="font-size:.8125rem;color:rgba(255,255,255,.3)">&copy; 2026 Lekhankan by VRM Vrindam (P) Limited. All rights reserved.</p>
      <div style="display:flex;gap:2rem">
        <a href="#" class="f-link" style="margin-bottom:0">Privacy Policy</a>
        <a href="#" class="f-link" style="margin-bottom:0">Terms of Service</a>
        <a href="#" class="f-link" style="margin-bottom:0">NDA Policy</a>
      </div>
    </div>
  </div>
</footer>

<!-- Resource Modal -->
<div class="modal" id="resModal" onclick="closeModal(event)">
  <div class="modal-box">
    <h3 class="h-md mb2" id="modalTitle">Download Resource</h3>
    <p class="t-body mb4">Enter your work email to receive the free resource instantly.</p>
    <form onsubmit="modalSubmit(event)" style="display:flex;flex-direction:column;gap:1rem">
      <div><label class="form-lbl">Your Name *</label><input type="text" required class="form-input" placeholder="John Smith"/></div>
      <div><label class="form-lbl">Work Email *</label><input type="email" required class="form-input" placeholder="john@firm.com"/></div>
      <div><label class="form-lbl">Company Name</label><input type="text" class="form-input" placeholder="Smith &amp; Associates"/></div>
      <button type="submit" class="btn btn-primary w-full" style="justify-content:center">Send Me The Resource &rarr;</button>
    </form>
    <button onclick="document.getElementById('resModal').classList.remove('open')" style="position:absolute;top:1.25rem;right:1.25rem;color:var(--slate);font-size:1.25rem;line-height:1">&#x2715;</button>
  </div>
</div>

<script>
// Navbar scroll
window.addEventListener('scroll',()=>{
  document.getElementById('nav').classList.toggle('scrolled',window.scrollY>60);
});

// Scroll reveal
const revEls=document.querySelectorAll('.rev');
const revObs=new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');revObs.unobserve(e.target)}});
},{threshold:0.1});
revEls.forEach(el=>revObs.observe(el));

// Service tabs
function svcTab(id,btn){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('on'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('on'));
  document.getElementById('tab-'+id).classList.add('on');
  btn.classList.add('on');
}

// Industry tabs
function indTab(id,btn){
  document.querySelectorAll('.ind-content').forEach(c=>c.classList.remove('on'));
  document.querySelectorAll('.ind-btn').forEach(b=>b.classList.remove('on'));
  document.getElementById('ind-'+id).classList.add('on');
  btn.classList.add('on');
}

// ROI Calculator
const roles={
  bookkeeper:{usd:{h:140000,l:75200},cad:{h:180000,l:96000}},
  cpa:{usd:{h:220000,l:112000},cad:{h:285000,l:145000}},
  tax:{usd:{h:175000,l:88000},cad:{h:225000,l:115000}}
};
let curRole='bookkeeper',curCur='USD';
function updateROI(){
  const d=roles[curRole][curCur.toLowerCase()];
  const save=d.h-d.l,pct=Math.round((save/d.h)*100);
  const sym=curCur==='USD'?'$':'CA$';
  document.getElementById('roi-amount').textContent=sym+save.toLocaleString()+' / year';
  document.getElementById('inhouseLbl').textContent=sym+d.h.toLocaleString()+'/yr';
  document.getElementById('lekLbl').textContent=sym+d.l.toLocaleString()+'/yr';
  document.getElementById('savePct').textContent='~'+pct+'%';
  document.getElementById('lekBar').style.width=Math.round((d.l/d.h)*100)+'%';
}
function setROIRole(role,btn){
  curRole=role;
  document.querySelectorAll('.roi-tab').forEach(t=>t.classList.remove('on'));
  btn.classList.add('on');
  updateROI();
}
function setROICur(cur){
  curCur=cur;
  document.getElementById('btn-usd').classList.toggle('on',cur==='USD');
  document.getElementById('btn-cad').classList.toggle('on',cur==='CAD');
  updateROI();
}

// Form
function formSubmit(e){
  e.preventDefault();
  alert('Thank you! Your assessment request has been submitted. Our team will contact you within 4 business hours.');
  document.getElementById('aform').reset();
}

// Modal
function openModal(name){
  document.getElementById('modalTitle').textContent='Download: '+name;
  document.getElementById('resModal').classList.add('open');
  document.body.style.overflow='hidden';
}
function closeModal(e){
  if(e.target.id==='resModal'){
    document.getElementById('resModal').classList.remove('open');
    document.body.style.overflow='';
  }
}
function modalSubmit(e){
  e.preventDefault();
  document.getElementById('resModal').classList.remove('open');
  document.body.style.overflow='';
  alert('Your resource is on its way! Check your email within a few minutes.');
}

// Nav active links
const secs=document.querySelectorAll('section[id]');
window.addEventListener('scroll',()=>{
  let cur='';
  secs.forEach(s=>{if(window.scrollY>=s.offsetTop-100)cur=s.id});
  document.querySelectorAll('.nav-links a').forEach(a=>{
    a.classList.toggle('on',a.getAttribute('href')==='#'+cur);
  });
});
</script>
</body>
</html>"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

size = len(html)
lines = html.count('\\n')
print(f"Successfully written index.html: {size:,} bytes, ~{lines} lines")
print("Done!")
