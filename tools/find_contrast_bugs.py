import glob
import re

files = sorted(glob.glob('roteiros/*.html') + ['exemplo.html'])

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Find simulador blocks
    for m in re.finditer(r'(<(?:section|div)[^>]*id=["\']simulador["\'][^>]*>)', c):
        print(f"{f} -> {m.group(1)}")
    
    # Also find any direct child div after section id="simulador"
    for m in re.finditer(r'<section[^>]*id=["\']simulador["\'][^>]*>\s*(?:<div[^>]*>.*?</div>\s*)?<div[^>]*class=["\']([^"\']*)["\']', c, re.DOTALL):
        print(f"  sub-container: {m.group(1)[:60]}")
