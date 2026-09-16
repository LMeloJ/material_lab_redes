import glob
import re

files = sorted(glob.glob('roteiros/*.html') + ['exemplo.html'])

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    issues = []
    
    # Check 1: dark outer container in simulator
    if 'id="simulador"' in content:
        idx = content.find('id="simulador"')
        snippet = content[idx:idx+800]
        if 'bg-slate-900 border border-slate-800 rounded-2xl' in snippet:
            issues.append('Simulator has dark outer container bg-slate-900 border border-slate-800 rounded-2xl')
        if 'bg-slate-900 border border-indigo-500/40' in snippet:
            issues.append('Simulator has dark outer container bg-slate-900 border border-indigo-500/40')

    # Check 2: text-white on headings or labels inside mental models or general cards
    # Pattern: <h4 class="font-bold text-white
    matches = re.findall(r'<h[1-6][^>]*class="[^"]*text-white[^"]*"', content)
    for m in matches:
        # check if it's NOT inside a dark card
        # Let's count them
        issues.append(f'Heading with text-white: {m}')

    # Check 3: text-slate-700 inside terminal/code blocks with dark background (bg-slate-900, bg-slate-950, bg-black)
    dark_slate700 = re.findall(r'bg-(?:slate-950|slate-900|black)[^>]*>[^<]*<[^>]*text-slate-700', content)
    if dark_slate700:
        issues.append(f'{len(dark_slate700)} occurrences of text-slate-700 inside dark container')

    if issues:
        print(f"=== {f} ({len(issues)} issues) ===")
        for i in issues[:5]:
            print(f"  {i}")
