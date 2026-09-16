import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for filename in sorted(glob.glob('roteiros/*.html')):
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()

    matches = list(re.finditer(r'<h[1-6][^>]*text-white[^>]*>', c))
    if matches:
        print(f"=== {filename} ({len(matches)} matches) ===")
        for m in matches:
            idx = m.start()
            container = c[max(0, idx-180):idx]
            # find opening tag before idx
            print(f"  Container snippet: ...{container[-120:]}")
            print(f"  Tag: {m.group(0)}")
            print()
