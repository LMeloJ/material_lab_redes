import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('roteiros/*.html') + ['exemplo.html']):
    content = open(f, encoding='utf-8').read()
    
    # 1. text-white inside light backgrounds
    # look for bg-white or bg-slate-50 followed within 300 chars by text-white
    matches_white_on_light = list(re.finditer(r'(bg-(?:white|slate-50|slate-100|indigo-50|cyan-50)[\s\S]{1,400}?)(text-white)', content))
    
    # 2. text-slate-700 or 800 inside dark backgrounds
    matches_dark_on_dark = list(re.finditer(r'(bg-(?:slate-950|slate-900|black)[\s\S]{1,400}?)(text-slate-[78]00)', content))

    # 3. simulator outer container
    dark_sim = re.findall(r'id="simulador"[\s\S]{1,600}?bg-slate-900', content)

    if matches_white_on_light or matches_dark_on_dark or dark_sim:
        print(f"=== {f} ===")
        if dark_sim:
            print(f"  [SIMULATOR] Has dark outer wrapper")
        if matches_white_on_light:
            print(f"  [WHITE-ON-LIGHT] {len(matches_white_on_light)} potential invisible texts:")
            for m in matches_white_on_light[:3]:
                snippet = m.group(1)[-80:].replace('\n', ' ')
                print(f"    ...{snippet} -> text-white")
        if matches_dark_on_dark:
            print(f"  [DARK-ON-DARK] {len(matches_dark_on_dark)} unreadable dark texts:")
            for m in matches_dark_on_dark[:3]:
                snippet = m.group(1)[-80:].replace('\n', ' ')
                print(f"    ...{snippet} -> {m.group(2)}")
        print()
