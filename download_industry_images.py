"""
Download clean industry images (architecture/facilities/machinery, NO HUMANS/PEOPLE)
for the "Industries We Serve" section on Lekhankan Website.
Save into images/ directory with exact filenames expected by industries.php.
"""
import urllib.request
import os
from PIL import Image
import io

industry_images = [
    (
        "cpa_firms_portrait.png",
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "CPA & Accounting Firms: Modern glass corporate tower architecture"
    ),
    (
        "ecommerce_business_portrait.png",
        "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "E-Commerce: High-tech logistics warehouse & fulfillment facility"
    ),
    (
        "healthcare_accounting_portrait.png",
        "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "Healthcare: Modern medical clinic & hospital interior facility"
    ),
    (
        "real_estate_portrait.png",
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "Real Estate: Modern commercial & luxury residential building facade"
    ),
    (
        "construction_job_costing_portrait.png",
        "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "Construction: Building site structural cranes and development framework"
    ),
    (
        "professional_services_portrait.png",
        "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "Professional Services: Sleek modern corporate office interior design"
    )
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

out_dir = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(out_dir, exist_ok=True)

# Target resolution for industry display card (4:5 portrait ratio or 16:10 landscape - let's check size)
# 800x1000 (4:5) fits great in industry display card
TW, TH = 800, 1000

for filename, url, desc in industry_images:
    out_path = os.path.join(out_dir, filename)
    print(f"Downloading: {desc}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        
        img = Image.open(io.BytesIO(data)).convert("RGB")
        w, h = img.size
        
        scale = max(TW / w, TH / h)
        nw, nh = int(w * scale), int(h * scale)
        img = img.resize((nw, nh), Image.LANCZOS)
        
        left = (nw - TW) // 2
        top = (nh - TH) // 2
        img_cropped = img.crop((left, top, left + TW, top + TH))
        
        img_cropped.save(out_path, "PNG", optimize=True)
        print("OK " + filename + " (" + str(TW) + "x" + str(TH) + ")")
    except Exception as e:
        print("FAIL " + filename + ": " + str(e))

print("Done downloading industry images!")
