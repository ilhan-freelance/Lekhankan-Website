"""
Replace the 3 industry images with PURE INDUSTRY FACILITY & ARCHITECTURE photos:
NO PEOPLE, NO OFFICE WORK DESKS, NO STETHOSCOPES/BOOKS.
PURE INDUSTRY INFRASTRUCTURE & BUILDINGS ONLY:

1. E-Commerce: Seaport cargo container logistics hub & automated shipping terminal
2. Healthcare & Medical: Modern glass medical center hospital building exterior
3. Professional Services: Executive financial district skyscraper towers & corporate headquarters
"""
import urllib.request
import os
from PIL import Image
import io

industry_facility_images = [
    (
        "ecommerce_business_portrait.png",
        "https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "E-Commerce: Global shipping cargo container hub & logistics terminal"
    ),
    (
        "healthcare_accounting_portrait.png",
        "https://images.unsplash.com/photo-1587354246490-7e26e63fdb62?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "Healthcare: Modern hospital building exterior & medical center architecture"
    ),
    (
        "professional_services_portrait.png",
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "Professional Services: Corporate glass tower headquarters architecture"
    )
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

out_dir = os.path.join(os.path.dirname(__file__), "images")
TW, TH = 800, 1000

for filename, url, desc in industry_facility_images:
    out_path = os.path.join(out_dir, filename)
    print(f"Downloading industry facility photo: {desc}")
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

print("Done updating pure industry infrastructure images!")
