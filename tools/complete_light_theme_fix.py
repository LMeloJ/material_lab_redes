import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def apply_fixes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Quick Jump Navigation: dark pill links to clean light pill links
    content = re.sub(
        r'class="px-3 py-1\.5 rounded-lg whitespace-nowrap bg-slate-900 border border-slate-800 text-slate-700 hover:border-[a-z0-9\-/]+ hover:text-white transition"',
        'class="px-3 py-1.5 rounded-lg whitespace-nowrap bg-white border border-slate-200 text-slate-700 hover:border-indigo-400 hover:text-indigo-700 shadow-xs transition"',
        content
    )
    content = re.sub(
        r'class="px-3 py-1\.5 rounded-lg whitespace-nowrap bg-[a-z]+-950/60 border border-[a-z]+-500/40 text-[a-z]+-300 hover:border-[a-z]+-500 hover:text-white transition font-medium flex items-center gap-1"',
        'class="px-3 py-1.5 rounded-lg whitespace-nowrap bg-indigo-50 border border-indigo-200 text-indigo-700 hover:border-indigo-300 hover:text-indigo-900 font-semibold shadow-xs transition font-medium flex items-center gap-1"',
        content
    )

    # 2. Hero banners
    content = re.sub(
        r'class="mb-12 bg-gradient-to-br from-slate-900 via-[^"]+ to-slate-900 border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-xl"',
        'class="mb-12 bg-gradient-to-br from-indigo-50/80 via-white to-purple-50/50 border border-indigo-100 rounded-2xl p-6 sm:p-8 shadow-sm"',
        content
    )
    # H2 in hero banner
    content = content.replace(
        '<h2 class="text-3xl sm:text-4xl font-extrabold text-white mt-3 mb-4 tracking-tight">',
        '<h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-3 mb-4 tracking-tight">'
    )

    # 3. Checkbox inputs
    content = content.replace(
        'class="lab-check mt-1 w-4 h-4 rounded text-emerald-600 focus:ring-emerald-500 border-slate-700 bg-slate-900"',
        'class="lab-check mt-1 w-4 h-4 rounded text-emerald-600 focus:ring-emerald-500 border-slate-300 bg-white shadow-xs"'
    )

    # 4. Badges beside titles
    content = re.sub(
        r'<span class="text-xs bg-slate-800 text-slate-700 px-3 py-1 rounded-full border border-slate-700([^>]*)">',
        r'<span class="text-xs bg-indigo-50 text-indigo-700 px-3 py-1 rounded-full border border-indigo-200 font-medium\1">',
        content
    )

    # 5. Simulator tab switcher buttons
    content = content.replace(
        '<div class="flex items-center gap-1 bg-slate-900 p-1 rounded-lg border border-slate-800 text-xs">',
        '<div class="flex items-center gap-1 bg-slate-100 p-1 rounded-lg border border-slate-200 text-xs">'
    )
    content = content.replace(
        '<div class="flex items-center gap-1 bg-slate-900 p-1 rounded-lg border border-slate-800 text-xs">',
        '<div class="flex items-center gap-1 bg-slate-100 p-1 rounded-lg border border-slate-200 text-xs">'
    )
    content = content.replace(
        'text-slate-400 hover:text-white transition',
        'text-slate-600 hover:text-slate-900 transition'
    )

    # 6. Simulator outer containers for view-pat and view-dns in 11
    content = content.replace(
        '<div id="view-pat" class="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-2xl">',
        '<div id="view-pat" class="bg-white border-2 border-slate-200/90 rounded-2xl overflow-hidden shadow-lg">'
    )
    content = content.replace(
        '<div id="view-dns" class="hidden bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-2xl">',
        '<div id="view-dns" class="hidden bg-white border-2 border-slate-200/90 rounded-2xl overflow-hidden shadow-lg">'
    )

    # 7. Simulator status banners
    content = content.replace(
        '<div class="mt-6 p-4 rounded-xl bg-slate-900 border border-slate-800 text-xs flex items-center justify-between flex-wrap gap-2">',
        '<div class="mt-6 p-4 rounded-xl bg-white border border-slate-200 shadow-xs text-xs flex items-center justify-between flex-wrap gap-2">'
    )
    content = content.replace(
        '<div class="mt-8 p-4 rounded-xl bg-slate-900 border border-slate-800 text-xs flex items-center justify-between flex-wrap gap-2">',
        '<div class="mt-8 p-4 rounded-xl bg-white border border-slate-200 shadow-xs text-xs flex items-center justify-between flex-wrap gap-2">'
    )

    # 8. Tables and bottom panels in 11 and 13
    content = content.replace(
        '<div class="p-5 bg-slate-900 border-t border-slate-200">',
        '<div class="p-5 bg-slate-50 border-t border-slate-200">'
    )
    content = content.replace(
        '<div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs overflow-x-auto">',
        '<div class="bg-white p-3 rounded-xl border border-slate-200 font-mono text-xs overflow-x-auto shadow-xs">'
    )
    content = content.replace(
        '<tbody id="algo-table-body" class="divide-y divide-slate-850 text-slate-700">',
        '<tbody id="algo-table-body" class="divide-y divide-slate-200 text-slate-800">'
    )
    content = content.replace(
        '<tbody id="pat-table-rows" class="divide-y divide-slate-850 text-slate-700">',
        '<tbody id="pat-table-rows" class="divide-y divide-slate-200 text-slate-800">'
    )
    content = content.replace(
        '<div class="text-xs font-bold text-white uppercase tracking-wider mb-2 font-mono flex items-center justify-between">',
        '<div class="text-xs font-bold text-slate-900 uppercase tracking-wider mb-2 font-mono flex items-center justify-between">'
    )
    content = content.replace(
        '<h4 class="text-xs font-bold text-white uppercase tracking-wider flex items-center gap-2">',
        '<h4 class="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-2">'
    )
    content = content.replace(
        '<h4 class="text-sm font-bold text-white flex items-center gap-2">',
        '<h4 class="text-sm font-bold text-slate-900 flex items-center gap-2">'
    )

    # 9. Graph nodes in 13
    for node in ['A', 'B', 'C', 'D', 'E', 'F']:
        content = content.replace(
            f'<div id="node-{node}" class="p-3 rounded-xl bg-slate-900 border-2 border-slate-800 shadow-lg">\n                <div class="text-lg">🔀</div>\n                <div class="font-bold text-xs text-white">Switch {node}</div>',
            f'<div id="node-{node}" class="p-3 rounded-xl bg-white border-2 border-slate-300 shadow-md">\n                <div class="text-lg">🔀</div>\n                <div class="font-bold text-xs text-slate-900">Switch {node}</div>'
        )
    content = content.replace(
        '<div class="p-6 bg-slate-950/50">',
        '<div class="p-6 bg-slate-50 border-b border-slate-200">'
    )

    # 10. In 14: Device cards
    content = re.sub(
        r'<div id="([^"]+)" class="p-3 rounded-lg bg-slate-900 border border-slate-800 transition text-center">',
        r'<div id="\1" class="p-3 rounded-lg bg-white border border-slate-300 shadow-xs transition text-center">',
        content
    )
    content = re.sub(
        r'<div id="([^"]+)" class="p-2\.5 rounded-lg bg-slate-900 border border-slate-800 transition text-center">',
        r'<div id="\1" class="p-2.5 rounded-lg bg-white border border-slate-300 shadow-xs transition text-center">',
        content
    )
    content = content.replace(
        '<div class="font-bold text-slate-800">',
        '<div class="font-bold text-slate-900">'
    )
    content = content.replace(
        '<div class="font-bold text-slate-800 text-[11px]">',
        '<div class="font-bold text-slate-900 text-[11px]">'
    )

    # 11. In 15: Keypad buttons and phone label
    content = re.sub(
        r'<button onclick="pressDigit\(\'([0-9])\'\)" class="p-2 rounded bg-slate-800 hover:bg-slate-700 text-slate-700 font-bold transition">',
        r'<button onclick="pressDigit(\'\1\')" class="p-2 rounded bg-white hover:bg-slate-100 text-slate-800 border border-slate-300 font-bold transition shadow-xs">',
        content
    )
    content = content.replace(
        '<button onclick="pressDigit(\'clear\')" class="p-2 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 transition">C</button>',
        '<button onclick="pressDigit(\'clear\')" class="p-2 rounded bg-white hover:bg-slate-100 text-slate-600 border border-slate-300 font-bold transition shadow-xs">C</button>'
    )
    content = content.replace(
        '<span class="font-bold text-slate-700">Telefone IP 7960</span>',
        '<span class="font-bold text-slate-100">Telefone IP 7960</span>'
    )

    # 12. In 16:
    content = content.replace(
        '<div class="text-sm font-bold text-slate-100">SW-ACC-IDF</div>',
        '<div class="text-sm font-bold text-slate-900">SW-ACC-IDF</div>'
    )
    content = content.replace(
        '<span class="text-slate-800 font-bold">Porta Fa0/12 (PortFast + BPDU Guard):</span>',
        '<span class="text-slate-100 font-bold">Porta Fa0/12 (PortFast + BPDU Guard):</span>'
    )
    content = content.replace(
        '<div class="mt-6 p-4 rounded-xl bg-black/50 border border-slate-800">',
        '<div class="mt-6 p-4 rounded-xl bg-white border border-slate-200 shadow-xs">'
    )
    content = content.replace(
        '<span class="text-xs font-bold text-slate-700 flex items-center gap-2">',
        '<span class="text-xs font-bold text-slate-900 flex items-center gap-2">'
    )

    # 13. In 08:
    content = content.replace(
        '<span class="font-mono font-bold text-xs text-slate-700">PC-Admin (10.0.0.11) — Command Prompt</span>',
        '<span class="font-mono font-bold text-xs text-slate-200">PC-Admin (10.0.0.11) — Command Prompt</span>'
    )
    content = content.replace(
        '<div id="cli-screen" class="h-64 bg-slate-900/90 p-4 rounded-xl font-mono text-xs text-slate-700 overflow-y-auto space-y-2 border border-slate-800">',
        '<div id="cli-screen" class="h-64 bg-[#0d1117] p-4 rounded-xl font-mono text-xs text-slate-100 overflow-y-auto space-y-2 border border-slate-800">'
    )
    content = content.replace(
        '<div class="text-slate-700">OpenSSH_8.2p1',
        '<div class="text-slate-300">OpenSSH_8.2p1'
    )
    content = content.replace(
        '<div class="mt-4 p-3 rounded-lg bg-slate-50 border border-slate-200 text-[11px] text-slate-400">\n              <span class="text-white font-bold block mb-1">Status da Chave RSA:</span>',
        '<div class="mt-4 p-3 rounded-lg bg-slate-50 border border-slate-200 text-[11px] text-slate-600">\n              <span class="text-slate-900 font-bold block mb-1">Status da Chave RSA:</span>'
    )

    # 14. In 02: Challenge section
    content = content.replace(
        'bg-gradient-to-br from-rose-950/30 via-slate-900 to-slate-900 border-2 border-rose-500/40 rounded-2xl p-6 sm:p-8 shadow-2xl',
        'bg-gradient-to-br from-rose-50 via-white to-red-50/60 border-2 border-rose-200 rounded-2xl p-6 sm:p-8 shadow-lg'
    )
    content = content.replace(
        '<span class="px-2.5 py-0.5 rounded text-xs font-bold bg-rose-500/20 text-rose-400 border border-rose-500/40">',
        '<span class="px-2.5 py-0.5 rounded text-xs font-bold bg-rose-100 text-rose-700 border border-rose-200">'
    )
    content = content.replace(
        '<h4 class="text-xl font-bold text-white mt-1">rede_com_problemas.pkt</h4>',
        '<h4 class="text-xl font-bold text-slate-900 mt-1">rede_com_problemas.pkt</h4>'
    )
    content = content.replace(
        '<p class="text-xs text-slate-700 mt-1">\n              Topologia contendo 2 sub-redes',
        '<p class="text-xs text-slate-600 mt-1">\n              Topologia contendo 2 sub-redes'
    )

    # 15. In 13: Section 3 guide box
    content = content.replace(
        'bg-gradient-to-br from-purple-950/20 via-slate-900 to-slate-900 border-2 border-purple-500/40 rounded-2xl p-6 shadow-xl space-y-4 text-xs leading-relaxed text-slate-700',
        'bg-gradient-to-br from-purple-50 via-white to-purple-50/60 border-2 border-purple-200 rounded-2xl p-6 shadow-md space-y-4 text-xs leading-relaxed text-slate-700'
    )

    # 16. In 01: Checklist heading
    content = content.replace(
        '<h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">',
        '<h3 class="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">'
    )

    # 17. In 02: Step headings
    content = re.sub(
        r'<span class="w-7 h-7 rounded-full bg-cyan-500 text-slate-950 font-bold flex items-center justify-center text-xs">(\d)</span>\s*<h4 class="text-lg font-bold text-white">',
        r'<span class="w-7 h-7 rounded-full bg-cyan-600 text-white font-bold flex items-center justify-center text-xs">\1</span>\n          <h4 class="text-lg font-bold text-slate-900">',
        content
    )

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

files = sorted(glob.glob('roteiros/*.html') + ['exemplo.html'])
count = 0
for f in files:
    if apply_fixes(f):
        count += 1
        print(f"Fixed: {f}")

print(f"Total modified files: {count}")
