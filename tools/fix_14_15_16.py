for f in ['roteiros/14-projeto-final-aula-01.html', 'roteiros/15-voip-avancado.html', 'roteiros/16-topologias-e-stp.html']:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    c = c.replace(
        'bg-slate-950 rounded-xl p-4 border border-slate-800 font-mono text-xs text-slate-700 overflow-x-auto">',
        'bg-[#0d1117] rounded-xl p-4 border border-slate-800 font-mono text-xs text-slate-100 overflow-x-auto">'
    )
    c = c.replace(
        'class="absolute top-3 right-3 px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-700 text-xs transition border border-slate-700"',
        'class="absolute top-3 right-3 px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs transition border border-slate-700/60"'
    )
    # in case classes are slightly different:
    c = c.replace(
        'rounded bg-slate-800 hover:bg-slate-700 text-slate-700',
        'rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700/60'
    )
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)

print("Updated 14, 15, 16 code containers.")
