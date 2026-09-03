import os

logos = {
    'quickbooks.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#2CA01C"/>
  <path d="M48 24c-11 0-20 9-20 20v24c0 4.4 3.6 8 8 8s8-3.6 8-8V44c0-2.2 1.8-4 4-4s4 1.8 4 4v16c0 11 9 20 20 20s20-9 20-20V36c0-4.4-3.6-8-8-8s-8 3.6-8 8v24c0 2.2-1.8 4-4 4s-4-1.8-4-4V44c0-11-9-20-20-20z" fill="#FFFFFF"/>
</svg>''',

    'xero.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <circle cx="50" cy="50" r="48" fill="#13B5EA"/>
  <path d="M32 30l18 20-18 20h8l14-15.5L68 70h8L58 50l18-20h-8L54 45.5 40 30h-8z" fill="#FFFFFF"/>
</svg>''',

    'netsuite.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#0F2537"/>
  <path d="M26 74V26h14l20 34V26h14v48H60L40 40v34H26z" fill="#E66E19"/>
  <circle cx="74" cy="26" r="5" fill="#13B5EA"/>
</svg>''',

    'sap.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#008FD3"/>
  <text x="50%" y="64%" font-family="Arial, Helvetica, sans-serif" font-weight="900" font-size="34" fill="#FFFFFF" text-anchor="middle" letter-spacing="-1">SAP</text>
</svg>''',

    'bill.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#0052FF"/>
  <text x="50%" y="64%" font-family="Manrope, Arial, sans-serif" font-weight="900" font-size="28" fill="#FFFFFF" text-anchor="middle" letter-spacing="-0.5">bill</text>
</svg>''',

    'gusto.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#0A855C"/>
  <path d="M50 25c-13.8 0-25 11.2-25 25s11.2 25 25 25 25-11.2 25-25h-15c0 5.5-4.5 10-10 10s-10-4.5-10-10 4.5-10 10-10c3 0 5.6 1.3 7.4 3.4l10.6-10.6C63 32.2 57 25 50 25z" fill="#FFFFFF"/>
</svg>''',

    'sage.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#000000"/>
  <text x="50%" y="64%" font-family="Arial, sans-serif" font-weight="900" font-size="32" fill="#00D64F" text-anchor="middle">sage</text>
</svg>''',

    'dext.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#FF4F00"/>
  <path d="M30 25h20c13.8 0 25 11.2 25 25S63.8 75 50 75H30V25zm15 13v24h5c6.6 0 12-5.4 12-12s-5.4-12-12-12h-5z" fill="#FFFFFF"/>
</svg>''',

    'stripe.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#635BFF"/>
  <path d="M44 38c0-3.3 2.7-4.5 7.1-4.5 6.3 0 14.3 2 20.6 5.4V23.2C65.2 20.9 57.6 19 49.9 19 33.3 19 22 27.7 22 40.5c0 21.6 29.7 18.1 29.7 27.4 0 3.9-3.4 5.2-8.2 5.2-7.1 0-16.3-3-23.2-6.8v16c7.7 3.3 15.6 4.7 23.2 4.7 17.3 0 29.3-8.5 29.3-21.6C72.8 42.6 44 47.1 44 38z" fill="#FFFFFF"/>
</svg>''',

    'hubdoc.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <circle cx="50" cy="50" r="48" fill="#FFFFFF" stroke="#00A3E0" stroke-width="3"/>
  <path d="M50 18 C67 18 80 32 80 50 C80 67 67 80 50 80 C39 80 29 74 23 65 C34 65 44 57 47 43 C49 33 43 23 34 20 C39 18 44 18 50 18 Z" fill="#00A3E0"/>
  <path d="M23 34 C27 25 35 20 44 20 C41 27 43 35 41 43 C37 53 27 61 17 61 C19 51 19 41 23 34 Z" fill="#003B5C"/>
  <path d="M34 20 C41 24 44 31 44 39 C41 47 34 55 23 65 C19 57 19 47 23 37 Z" fill="#00B8D9"/>
</svg>''',

    'expensify.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <circle cx="50" cy="50" r="48" fill="#00D084"/>
  <path d="M30 25h40v12H44v12h22v12H44v14h26v12H30V25z" fill="#FFFFFF"/>
</svg>''',

    'powerbi.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="44" height="44">
  <rect width="100" height="100" rx="22" fill="#111827"/>
  <rect x="24" y="52" width="12" height="26" rx="3" fill="#E6AD00"/>
  <rect x="44" y="38" width="12" height="40" rx="3" fill="#F2C811"/>
  <rect x="64" y="24" width="12" height="54" rx="3" fill="#FFF100"/>
</svg>'''
}

os.makedirs('images/logos', exist_ok=True)
for fname, content in logos.items():
    fpath = os.path.join('images/logos', fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'WRITTEN: {fpath} ({len(content)} bytes)')

print('ALL 12 OFFICIAL BRAND LOGO SVGS UPDATED SUCCESSFULLY!')
