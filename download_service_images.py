"""
Download 5 horizontal service images from Unsplash for Lekhankan website.
Heritage + Modern photography style, no calculators/western offices/stock clichés.
Images: 1200x750 landscape (16:10)
"""
import urllib.request
import os
from PIL import Image
import io

# Unsplash direct image source URLs — free to use (Unsplash license)
# Each tuple: (output_filename, unsplash_source_url, description)
images = [
    (
        "bookkeeping_horizontal.png",
        "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=1200&h=750&fit=crop&crop=center&auto=format&q=85",
        # Old worn leather journal/ledger book close-up — Heritage bookkeeping
        "Bookkeeping: Heritage ledger book"
    ),
    (
        "accounting_outsourcing_horizontal.png",
        "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1200&h=750&fit=crop&crop=center&auto=format&q=85",
        # Financial charts/data analysis, team collaboration — Modern accounting
        "Accounting Outsourcing: Financial data analysis"
    ),
    (
        "accounts_payable_horizontal.png",
        "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&h=750&fit=crop&crop=center&auto=format&q=85",
        # Clean desk with invoice documents and pen — Modern AP workflow
        "Accounts Payable: Invoice & document workflow"
    ),
    (
        "accounts_receivable_horizontal.png",
        "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=1200&h=750&fit=crop&crop=center&auto=format&q=85",
        # Financial dashboard data visualization — Modern AR tracking
        "Accounts Receivable: Financial dashboard"
    ),
    (
        "payroll_accounting_horizontal.png",
        "https://images.unsplash.com/photo-1586282391129-76a6df230234?w=1200&h=750&fit=crop&crop=center&auto=format&q=85",
        # Person reviewing payroll/salary documents with pen — Modern payroll
        "Payroll: Document review workflow"
    ),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

out_dir = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(out_dir, exist_ok=True)

for filename, url, desc in images:
    out_path = os.path.join(out_dir, filename)
    print(f"Downloading: {desc}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        
        # Open, verify and save as PNG 1200x750
        img = Image.open(io.BytesIO(data))
        img = img.convert("RGB")
        
        # Center-crop to exactly 1200x750 (16:10)
        target_w, target_h = 1200, 750
        w, h = img.size
        
        # Scale to fill target dimensions maintaining aspect ratio
        scale = max(target_w / w, target_h / h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        
        # Center crop
        left = (new_w - target_w) // 2
        top = (new_h - target_h) // 2
        img = img.crop((left, top, left + target_w, top + target_h))
        
        img.save(out_path, "PNG", optimize=True)
        print(f"  ✓ Saved {filename} ({target_w}x{target_h})")
    except Exception as e:
        print(f"  ✗ FAILED {filename}: {e}")

print("\nDone! All service images processed.")
