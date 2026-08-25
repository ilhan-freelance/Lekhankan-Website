# Build index.html from PHP partials
import re
import os

def strip_php(content):
    """Replace PHP template tags with static equivalents"""
    content = content.replace("<?= htmlspecialchars($pageTitle ?? 'Lekhankan | Offshore Bookkeeping & Accounting KPO — USA & Canada') ?>", "Lekhankan | Offshore Bookkeeping & Accounting KPO — USA & Canada")
    content = content.replace("<?= htmlspecialchars($metaDescription ?? 'Lekhankan provides dedicated offshore bookkeeping, accounting outsourcing, and virtual accounting services for businesses and CPA firms across USA & Canada. Reduce costs by up to 60% with CA-supervised dedicated accounting teams.') ?>", "Lekhankan provides dedicated offshore bookkeeping, accounting outsourcing, and virtual accounting services for businesses and CPA firms across USA & Canada. Reduce costs by up to 60% with CA-supervised dedicated accounting teams.")
    content = content.replace("<?= base_url('", "")
    content = content.replace("<?= base_url(\"", "")
    content = content.replace("') ?>", "")
    content = content.replace("\" ?>", "")
    content = content.replace("<?= base_url('#", "#")
    content = content.replace("<?= date('Y') ?>", "2026")
    # Remove remaining PHP tags
    content = re.sub(r'<\?[^?]*\?>', '', content)
    return content

base = r"c:\Users\asus\Documents\LEKHANKAN Websitee"

files = {
    'header': f"{base}\\app\\Views\\templates\\header.php",
    'navbar': f"{base}\\app\\Views\\templates\\navbar.php",
    'hero': f"{base}\\app\\Views\\sections\\hero.php",
    'why_us': f"{base}\\app\\Views\\sections\\why_us.php",
    'services': f"{base}\\app\\Views\\sections\\services.php",
    'industries': f"{base}\\app\\Views\\sections\\industries.php",
    'technology': f"{base}\\app\\Views\\sections\\technology.php",
    'cpa_partner': f"{base}\\app\\Views\\sections\\cpa_partner.php",
    'brand_story': f"{base}\\app\\Views\\sections\\brand_story.php",
    'brand_video': f"{base}\\app\\Views\\sections\\brand_video.php",
    'about_lekhankan': f"{base}\\app\\Views\\sections\\about_lekhankan.php",
    'virtual_dept': f"{base}\\app\\Views\\sections\\virtual_dept.php",
    'process': f"{base}\\app\\Views\\sections\\process.php",
    'team': f"{base}\\app\\Views\\sections\\team.php",
    'lead_magnets': f"{base}\\app\\Views\\sections\\lead_magnets.php",
    'insights': f"{base}\\app\\Views\\sections\\insights.php",
    'contact': f"{base}\\app\\Views\\sections\\contact.php",
    'final_cta': f"{base}\\app\\Views\\sections\\final_cta.php",
    'footer': f"{base}\\app\\Views\\templates\\footer.php",
}

parts = {}
for key, path in files.items():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            parts[key] = strip_php(f.read())
    except FileNotFoundError:
        print(f"WARNING: {key} not found at {path}")
        parts[key] = f"<!-- {key} not found -->"

sections_order = [
    'navbar',
    'hero',
    'why_us',
    'services',
    'industries',
    'technology',
    'cpa_partner',
    'brand_story',
    'brand_video',
    'about_lekhankan',
    'virtual_dept',
    'process',
    'team',
    'lead_magnets',
    'insights',
    'contact',
    'final_cta',
]

html = parts['header'] + "\n"
for section in sections_order:
    if section in parts:
        html += parts[section] + "\n"
html += parts['footer']

output_path = f"{base}\\index.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated index.html: {len(html)} bytes, {html.count(chr(10))} lines")
print("Done!")
