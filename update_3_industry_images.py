"""
Update 3 specific industry images with iconic, highly relevant photography (No people/humans):
1. E-Commerce Businesses: Delivery package boxes & shopping logistics close-up
2. Healthcare & Medical: Stethoscope & medical clinical setup
3. Professional Services: Wooden gavel & law books / professional consulting emblem
"""
import urllib.request
import os
from PIL import Image
import io

new_industry_images = [
    (
        "ecommerce_business_portrait.png",
        "https://images.unsplash.com/photo-1566576721346-d4a3b4eaeb55?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "E-Commerce: Delivery packaging & shipping boxes setup"
    ),
    (
        "healthcare_accounting_portrait.png",
        "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "Healthcare: Stethoscope & clinical medical chart"
    ),
    (
        "professional_services_portrait.png",
        "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1000&h=1200&fit=crop&crop=center&auto=format&q=85",
        "Professional Services: Legal gavel, law books & advisory emblem"
    )
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

out_dir = os.path.join(os.path.dirname(__file__), "images")
TW, TH = 800, 1000

for filename, url, desc in new_industry_images:
    out_path = os.path.join(out_dir, filename)
    print(f"Downloading updated: {desc}")
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

print("Done updating the 3 industry images!")
