import glob
import re
import os

DISCLAIMER_ROTEIRO = '''    <!-- AI Disclaimer -->
    <div class="mb-5 p-3.5 sm:p-4 rounded-xl bg-indigo-50/70 border border-indigo-200 text-xs sm:text-sm text-indigo-950 flex items-center justify-between flex-wrap gap-3">
      <div class="flex items-center gap-2.5">
        <span class="text-base sm:text-lg">🤖</span>
        <span><strong>Nota de Autoria:</strong> Este roteiro experimental e seu material didático foram gerados por Inteligência Artificial (<strong>Gemini 3.8 Flash</strong>) e adaptados para o ambiente do laboratório.</span>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-100 text-indigo-700 border border-indigo-300">
        ✨ IA • Gemini 3.8 Flash
      </span>
    </div>
'''

def update_roteiros():
    files = sorted(glob.glob('roteiros/*.html'))
    for path in files:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # 1. Add top disclaimer if not present
        if 'Gemini 3.8 Flash' not in content:
            # Look for max-w-7xl with py-8
            pattern = r'(<div[^>]*class="[^"]*max-w-7xl[^"]*py-8[^"]*"[^>]*>\s*)'
            m = re.search(pattern, content)
            if m:
                # Insert right after opening tag
                content = content[:m.end()] + DISCLAIMER_ROTEIRO + '\n' + content[m.end():]
                changed = True
                print(f"Added top disclaimer to {path}")
            else:
                print(f"WARNING: Could not find main container in {path}")

        # 2. Add/update footer mention if not present
        if 'Gerado por IA (Gemini 3.8 Flash)' not in content:
            if '<span>Laboratório de Redes de Computadores • 2026.2</span>' in content:
                content = content.replace(
                    '<span>Laboratório de Redes de Computadores • 2026.2</span>',
                    '<span>Laboratório de Redes de Computadores • 2026.2 • Gerado por IA (Gemini 3.8 Flash)</span>'
                )
                changed = True
                print(f"Updated footer span in {path}")
            elif 'Laboratório de Redes de Computadores • Ciência da Computação / Engenharia' in content:
                content = content.replace(
                    'Laboratório de Redes de Computadores • Ciência da Computação / Engenharia',
                    'Laboratório de Redes de Computadores • 2026.2 • Gerado por IA (Gemini 3.8 Flash)'
                )
                changed = True
                print(f"Updated footer span in {path}")

        if changed:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

def update_index():
    path = 'index.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    DISCLAIMER_INDEX = '''    <!-- AI Disclaimer -->
    <div style="margin-bottom: 2rem; padding: 0.9rem 1.25rem; border-radius: 12px; background: rgba(99, 102, 241, 0.08); border: 1px solid rgba(99, 102, 241, 0.25); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem; font-size: 0.85rem; color: var(--text-secondary);">
      <div style="display: flex; align-items: center; gap: 0.6rem;">
        <span style="font-size: 1.2rem;">🤖</span>
        <span><strong>Nota de Autoria:</strong> Este portal e seus roteiros experimentais foram desenvolvidos com apoio de Inteligência Artificial (<strong>Gemini 3.8 Flash</strong>) e adaptados para as aulas práticas.</span>
      </div>
      <span style="display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.25rem 0.65rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 600; background: rgba(99, 102, 241, 0.15); color: #818cf8; border: 1px solid rgba(99, 102, 241, 0.3);">
        ✨ IA • Gemini 3.8 Flash
      </span>
    </div>
'''

    if 'Gemini 3.8 Flash' not in content:
        # Insert before course-summary or at start of main
        target = '<main class="main-content">'
        if target in content:
            idx = content.find(target) + len(target)
            content = content[:idx] + '\n' + DISCLAIMER_INDEX + content[idx:]
            changed = True
            print("Added top disclaimer to index.html")

        # Update footer
        footer_target = '<p>Material didático interativo estruturado para GitHub Pages e Canvas LMS • Professor Leonardo de Mélo João</p>'
        if footer_target in content:
            replacement = footer_target + '\n      <p style="font-size: 0.8rem; color: var(--text-muted); opacity: 0.85;">✨ Conteúdo e roteiros gerados com Inteligência Artificial (<strong>Gemini 3.8 Flash</strong>)</p>'
            content = content.replace(footer_target, replacement)
            changed = True
            print("Updated footer in index.html")

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

def update_exemplo():
    path = 'exemplo.html'
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    if 'Gemini 3.8 Flash' not in content:
        pattern = r'(<div[^>]*class="[^"]*max-w-7xl[^"]*py-8[^"]*"[^>]*>\s*)'
        m = re.search(pattern, content)
        if m:
            content = content[:m.end()] + DISCLAIMER_ROTEIRO + '\n' + content[m.end():]
            changed = True
            print("Added top disclaimer to exemplo.html")

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    update_roteiros()
    update_index()
    update_exemplo()
