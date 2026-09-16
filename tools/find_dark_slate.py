import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('roteiros/*.html') + ['exemplo.html']):
    content = open(f, encoding='utf-8').read()
    
    matches = re.finditer(r'(class="[^"]*(?:bg-slate-900|bg-slate-950|to-slate-900)[^"]*">)([\s\S]{1,600}?)(text-slate-[78]00)', content)
    found = list(matches)
    if found:
        print(f"=== {f} ({len(found)} instances) ===")
        for m in found[:3]:
            print(f"  Container: {m.group(1)}")
            print(f"  Snippet: {m.group(2)[-80:]} -> {m.group(3)}")
            print()
