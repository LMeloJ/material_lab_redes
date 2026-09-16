import glob
import re

def upgrade_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Code blocks dark header & button contrast fixes
    # Header container
    content = content.replace(
        'class="bg-slate-950 px-4 py-3 border-b border-slate-200 flex items-center justify-between"',
        'class="bg-[#161b22] px-4 py-2.5 border-b border-slate-800 flex items-center justify-between"'
    )
    # Header title text
    content = content.replace(
        'class="font-mono text-xs font-medium text-slate-700 ml-2"',
        'class="font-mono text-xs font-medium text-slate-200 ml-2"'
    )
    content = content.replace(
        'class="font-mono text-xs font-medium text-slate-700"',
        'class="font-mono text-xs font-medium text-slate-200"'
    )
    # Copy button text on dark button
    content = content.replace(
        'class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-700 px-2.5 py-1 rounded transition flex items-center gap-1"',
        'class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700/60 px-2.5 py-1 rounded transition flex items-center gap-1"'
    )
    # Dark code container body font color
    content = content.replace(
        'class="p-4 bg-slate-950 font-mono text-xs overflow-x-auto text-slate-700 leading-relaxed flex-1"',
        'class="p-4 bg-[#0d1117] font-mono text-xs overflow-x-auto text-slate-100 leading-relaxed flex-1"'
    )
    # Code block footer notes
    content = content.replace(
        'class="p-3 bg-slate-900 border-t border-slate-200 text-[11px] text-slate-400"',
        'class="p-3 bg-slate-50 border-t border-slate-200 text-[11px] text-slate-600"'
    )

    # 2. Fix text-white on headings inside light cards
    content = content.replace('<h4 class="font-bold text-white text-sm"', '<h4 class="font-bold text-slate-900 text-sm"')
    content = content.replace('<h4 class="font-bold text-white text-sm mb-2"', '<h4 class="font-bold text-slate-900 text-sm mb-2"')
    content = content.replace('<h4 class="text-base font-bold text-white flex items-center gap-2"', '<h4 class="text-base font-bold text-slate-900 flex items-center gap-2"')
    content = content.replace('<h4 class="text-sm font-bold text-white"', '<h4 class="text-sm font-bold text-slate-900"')

    # Fix pale indigo-300 / blue-300 headings on white cards
    content = content.replace('class="text-base font-bold text-indigo-300 mb-2"', 'class="text-base font-bold text-indigo-700 mb-2"')
    content = content.replace('class="text-base font-bold text-indigo-300 mb-1"', 'class="text-base font-bold text-indigo-700 mb-1"')
    content = content.replace('class="text-base font-bold text-cyan-300 mb-2"', 'class="text-base font-bold text-cyan-700 mb-2"')

    # 3. Simulator outer container replacements
    content = content.replace(
        '<div class="bg-slate-900 border border-indigo-500/40 rounded-2xl p-6 shadow-2xl">',
        '<div class="bg-white border-2 border-slate-200/90 rounded-2xl p-6 shadow-lg">'
    )
    content = content.replace(
        '<div class="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-2xl">',
        '<div class="bg-white border-2 border-slate-200/90 rounded-2xl overflow-hidden shadow-lg">'
    )
    content = content.replace(
        '<div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl">',
        '<div class="bg-white border-2 border-slate-200/90 rounded-2xl p-6 shadow-lg">'
    )
    content = content.replace(
        '<div class="bg-slate-900 border border-indigo-500/40 rounded-2xl overflow-hidden shadow-2xl">',
        '<div class="bg-white border-2 border-slate-200/90 rounded-2xl overflow-hidden shadow-lg">'
    )

    # Simulator top control bars
    content = content.replace(
        '<div class="bg-slate-950/80 p-4 border-b border-slate-200 flex flex-wrap items-center justify-between gap-4">',
        '<div class="bg-slate-50 p-4 border-b border-slate-200 flex flex-wrap items-center justify-between gap-4">'
    )
    content = content.replace(
        '<div class="bg-slate-950/80 p-4 border-b border-slate-800 flex flex-wrap items-center justify-between gap-4">',
        '<div class="bg-slate-50 p-4 border-b border-slate-200 flex flex-wrap items-center justify-between gap-4">'
    )

    # Reset button inside simulators
    content = content.replace(
        'class="px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-700 border border-slate-700 transition"',
        'class="px-3 py-1.5 rounded-lg text-xs font-medium bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 transition shadow-xs"'
    )
    content = content.replace(
        'class="bg-slate-800 hover:bg-slate-700 text-slate-700 text-xs py-2 px-3 rounded-lg transition"',
        'class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 text-xs py-2 px-3 rounded-lg transition shadow-xs"'
    )
    content = content.replace(
        'class="text-xs bg-slate-800 text-slate-700 px-3 py-1 rounded-full border border-slate-700"',
        'class="text-xs bg-cyan-50 text-cyan-700 px-3 py-1 rounded-full border border-cyan-200 font-medium"'
    )

    # Wi-Fi distance slider in roteiro 01
    content = content.replace(
        '<div class="mb-6 bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">',
        '<div class="mb-6 bg-slate-50 p-4 rounded-xl border border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">'
    )
    content = content.replace(
        '<span class="text-xs font-semibold text-slate-800 block">Distância Física do Notebook',
        '<span class="text-xs font-semibold text-slate-700 block">Distância Física do Notebook'
    )
    # Selects inside roteiro 01 simulator
    content = content.replace(
        '<select id="sim-src-select" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-100 font-mono outline-none focus:border-indigo-500">',
        '<select id="sim-src-select" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-xs text-slate-900 font-mono outline-none focus:border-indigo-500">'
    )
    content = content.replace(
        '<select id="sim-dst-select" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-100 font-mono outline-none focus:border-indigo-500">',
        '<select id="sim-dst-select" class="w-full bg-slate-50 border border-slate-300 rounded-lg px-3 py-2 text-xs text-slate-900 font-mono outline-none focus:border-indigo-500">'
    )

    # Simulator scenario buttons in roteiro 02
    content = content.replace(
        '<div class="inline-flex rounded-lg bg-slate-900 p-1 border border-slate-800 text-xs">',
        '<div class="inline-flex rounded-lg bg-slate-200/70 p-1 border border-slate-300 text-xs">'
    )
    content = content.replace(
        'class="px-3 py-1 rounded-md font-medium text-slate-400 hover:text-white transition"',
        'class="px-3 py-1 rounded-md font-medium text-slate-600 hover:text-slate-900 transition"'
    )

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

files = sorted(glob.glob('roteiros/*.html') + ['exemplo.html'])
updated = []
for f in files:
    if upgrade_file(f):
        updated.append(f)

print(f"Updated {len(updated)} files:")
for u in updated:
    print(f" - {u}")
