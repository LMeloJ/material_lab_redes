import glob
import re

for f in sorted(glob.glob('roteiros/*.html') + ['exemplo.html']):
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()

    orig = c

    # Previous lab button at bottom
    c = c.replace(
        'class="px-4 py-2 rounded-xl text-xs font-semibold bg-slate-900 hover:bg-slate-850 text-slate-700 border border-slate-800 transition flex items-center gap-1.5"',
        'class="px-4 py-2 rounded-xl text-xs font-semibold bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 shadow-xs transition flex items-center gap-1.5"'
    )
    c = c.replace(
        'class="px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-slate-700 text-xs font-semibold hover:border-indigo-500/50 hover:text-white transition"',
        'class="px-4 py-2 rounded-xl bg-white border border-slate-300 text-slate-700 text-xs font-semibold hover:bg-slate-100 shadow-xs transition"'
    )

    # In roteiros/02: PDU simulator bottom panel
    c = c.replace(
        'class="p-3 rounded-lg bg-slate-900 border border-slate-800 text-slate-700 space-y-1.5 leading-relaxed"',
        'class="p-3 rounded-lg bg-white border border-slate-200 text-slate-800 shadow-xs space-y-1.5 leading-relaxed"'
    )
    c = c.replace(
        'class="w-full text-left p-2.5 rounded-lg bg-slate-900 hover:bg-slate-850 border border-slate-800 text-slate-700 transition"',
        'class="w-full text-left p-2.5 rounded-lg bg-white hover:bg-slate-100 border border-slate-200 text-slate-800 shadow-xs transition"'
    )
    c = c.replace(
        '<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col justify-between">',
        '<div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs flex flex-col justify-between">'
    )

    if c != orig:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(c)
        print(f"Updated: {f}")
