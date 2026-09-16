import glob
import re

for f in sorted(glob.glob('roteiros/*.html')):
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()

    orig = c

    # Fix code blocks with text-slate-700 on dark background
    c = c.replace(
        'class="bg-slate-950 rounded-xl p-4 border border-slate-800 font-mono text-xs overflow-x-auto text-slate-700"',
        'class="bg-[#0d1117] rounded-xl p-4 border border-slate-800 font-mono text-xs overflow-x-auto text-slate-100"'
    )
    c = c.replace(
        'class="bg-slate-950 rounded-xl p-4 border border-slate-800 text-slate-700"',
        'class="bg-[#0d1117] rounded-xl p-4 border border-slate-800 font-mono text-xs overflow-x-auto text-slate-100"'
    )
    c = c.replace(
        'class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs text-slate-700 space-y-1 h-24 overflow-y-auto"',
        'class="bg-[#0d1117] p-3 rounded-xl border border-slate-800 font-mono text-xs text-slate-100 space-y-1 h-24 overflow-y-auto"'
    )
    c = c.replace(
        '<div id="journey-output" class="mt-6 p-4 rounded-xl bg-slate-900 border border-slate-800 font-mono text-xs text-slate-700 flex items-center justify-between">',
        '<div id="journey-output" class="mt-6 p-4 rounded-xl bg-white border border-slate-200 shadow-xs font-mono text-xs text-slate-800 flex items-center justify-between">'
    )
    c = c.replace(
        '<div class="flex justify-between"><span>Sinalização:</span> <span class="text-slate-700 font-mono">SCCP / SIP</span></div>',
        '<div class="flex justify-between"><span>Sinalização:</span> <span class="text-slate-300 font-mono">SCCP / SIP</span></div>'
    )
    # in 12
    c = c.replace(
        '<span id="stp-status-text" class="text-slate-700">Árvore de Spanning Tree',
        '<span id="stp-status-text" class="text-slate-200">Árvore de Spanning Tree'
    )

    if c != orig:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(c)
        print(f"Updated: {f}")
