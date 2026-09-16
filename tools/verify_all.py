import os
import glob

files = glob.glob('roteiros/*.html') + ['index.html', 'test-iframe.html', 'exemplo.html']
print(f"Total HTML files verified: {len(files)}")
print("-" * 75)

for f in sorted(files):
    size = os.path.getsize(f)
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    has_canvas = 'canvas' in content.lower()
    is_light = ('bg-slate-50' in content) or ('data-theme="light"' in content) or ('background: #eef2f6' in content) or ('bg-slate-100' in content)
    status = "OK" if (has_canvas and is_light) else "CHECK"
    print(f"[{status}] {f:<42} | {size:>6} B | Canvas: {has_canvas} | Light: {is_light}")
