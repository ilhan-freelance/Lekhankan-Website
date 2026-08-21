# Build index.html from PHP partials
import re

def strip_php(content):
    """Replace PHP template tags with static equivalents"""
    content = content.replace("<?= base_url('", "")
    content = content.replace("<?= base_url(\"", "")
    content = content.replace("') ?>", "")
    content = content.replace("\" ?>", "")
    content = content.replace("<?= base_url('#", "#")
    content = content.replace("<?= date('Y') ?>", "2026")
    content = content.replace("<?= htmlspecialchars($pageTitle ?? '", "")
    content = content.replace("<?= htmlspecialchars($metaDescription ?? '", "")
    # Remove remaining PHP tags
    content = re.sub(r'<\?[^?]*\?>', '', content)
    return content

base = r"c:\Users\asus\Documents\LEKHANKAN Websitee"

# Read all partials
files = {
    'header': f"{base}\\app\\Views\\templates\\header.php",
    'navbar': f"{base}\\app\\Views\\templates\\navbar.php",
    'hero': f"{base}\\app\\Views\\sections\\hero.php",
    'brand_story': f"{base}\\app\\Views\\sections\\brand_story.php",
    'why_us': f"{base}\\app\\Views\\sections\\why_us.php",
    'services': f"{base}\\app\\Views\\sections\\services.php",
    'industries': f"{base}\\app\\Views\\sections\\industries.php",
    'cpa_partner': f"{base}\\app\\Views\\sections\\cpa_partner.php",
    'process': f"{base}\\app\\Views\\sections\\process.php",
    'team': f"{base}\\app\\Views\\sections\\team.php",
    'lead_magnets': f"{base}\\app\\Views\\sections\\lead_magnets.php",
    'contact': f"{base}\\app\\Views\\sections\\contact.php",
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

# Read the home.php to get section order
home_path = f"{base}\\app\\Views\\pages\\home.php"
try:
    with open(home_path, 'r', encoding='utf-8') as f:
        home_content = f.read()
    print("home.php section order:")
    for line in home_content.strip().split('\n'):
        line = line.strip()
        if 'section' in line.lower() or 'include' in line.lower() or 'echo' in line.lower():
            print(f"  {line}")
except:
    print("Could not read home.php")

# Build the header (everything up to </head><body>)
header = parts['header']

# The header ends with </body></html> in the footer, so strip the closing from header
# header.php has the opening HTML, head, and body tag
# footer.php has the closing script, /body, /html

# Build index.html
sections_order = [
    'navbar',
    'hero',
    'brand_story',
    'why_us',
    'services',
    'industries',
    'cpa_partner',
    'process',
    'team',
    'lead_magnets',
    'contact',
]

html = header + "\n"
for section in sections_order:
    html += parts[section] + "\n"
html += parts['footer']

output_path = f"{base}\\index.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated index.html: {len(html)} bytes, {html.count(chr(10))} lines")
print("Done!")
