import os
import re

def convert_to_light_theme(html_content):
    # 1. Body tag
    html_content = re.sub(
        r'<body([^>]*)class="([^"]*)bg-slate-950([^"]*)text-slate-100([^"]*)"',
        r'<body\1class="\2bg-slate-50\3text-slate-900\4"',
        html_content
    )

    # 2. Sticky Header
    html_content = html_content.replace('bg-slate-950/80 backdrop-blur-md border-b border-slate-800/80', 'bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-xs')
    html_content = html_content.replace('bg-slate-950/80 backdrop-blur-md border-b border-slate-800', 'bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-xs')
    html_content = html_content.replace('bg-slate-950/90 backdrop-blur-md border-b border-slate-800', 'bg-white/90 backdrop-blur-md border-b border-slate-200 shadow-xs')
    html_content = html_content.replace('border-b border-slate-800/80', 'border-b border-slate-200')
    html_content = html_content.replace('border-b border-slate-800', 'border-b border-slate-200')

    # 2b. Hero box
    html_content = html_content.replace('bg-gradient-to-br from-slate-900 via-indigo-950/30 to-slate-900 border border-slate-800/80 rounded-2xl p-6 sm:p-8 shadow-xl', 'bg-gradient-to-br from-indigo-50/80 via-white to-purple-50/50 border border-indigo-100 rounded-2xl p-6 sm:p-8 shadow-sm')
    html_content = html_content.replace('bg-gradient-to-br from-slate-900 via-indigo-950/30 to-slate-900 border border-slate-800 rounded-2xl p-6 sm:p-8 shadow-xl', 'bg-gradient-to-br from-indigo-50/80 via-white to-purple-50/50 border border-indigo-100 rounded-2xl p-6 sm:p-8 shadow-sm')
    html_content = html_content.replace('bg-gradient-to-br from-slate-900 via-indigo-950/30 to-slate-900', 'bg-gradient-to-br from-indigo-50/80 via-white to-purple-50/50')
    html_content = html_content.replace('border border-slate-800/80', 'border border-slate-200')
    html_content = html_content.replace('border-slate-800/80', 'border-slate-200')

    # 3. Canvas Alert box
    html_content = html_content.replace('bg-gradient-to-r from-amber-500/10 via-amber-500/5 to-slate-900 border-2 border-amber-500/50 shadow-xl', 'bg-gradient-to-r from-amber-50 via-amber-50/60 to-orange-50/40 border-2 border-amber-300 shadow-xs')
    html_content = html_content.replace('bg-amber-500/20 text-amber-300', 'bg-amber-100 text-amber-800 border border-amber-200')
    html_content = html_content.replace('text-amber-200 flex items-center', 'text-amber-950 flex items-center')
    html_content = html_content.replace('bg-amber-950/60 border border-amber-500/30 text-amber-300', 'bg-amber-100 border border-amber-300 text-amber-900 font-medium')
    html_content = html_content.replace('bg-indigo-950/80 border border-indigo-500/40 text-indigo-300 hover:text-white', 'bg-indigo-50 border border-indigo-200 text-indigo-700 hover:text-indigo-900 font-medium')

    # 4. Quick Jump Bar
    html_content = html_content.replace('bg-slate-900 border border-slate-800 text-slate-300 hover:border-indigo-500/50 hover:text-white', 'bg-white border border-slate-200 text-slate-700 hover:border-indigo-400 hover:text-indigo-700 shadow-xs')
    html_content = html_content.replace('bg-indigo-950/60 border border-indigo-500/40 text-indigo-300 hover:border-indigo-500 hover:text-white', 'bg-indigo-50 border border-indigo-200 text-indigo-700 hover:border-indigo-300 hover:text-indigo-900 font-semibold')
    html_content = html_content.replace('bg-emerald-950/40 border border-emerald-500/30 text-emerald-300 hover:border-emerald-500 hover:text-white', 'bg-emerald-50 border border-emerald-200 text-emerald-800 hover:border-emerald-300 hover:text-emerald-950 font-semibold')
    html_content = html_content.replace('bg-amber-950/40 border border-amber-500/30 text-amber-300 hover:border-amber-500 hover:text-white', 'bg-amber-50 border border-amber-200 text-amber-800 hover:border-amber-300 hover:text-amber-950 font-semibold')

    # 5. Section Titles and Subtitles
    html_content = html_content.replace('text-xl font-bold text-slate-100', 'text-xl font-bold text-slate-900')
    html_content = html_content.replace('text-2xl font-bold text-white', 'text-2xl font-bold text-slate-900')
    html_content = html_content.replace('text-3xl sm:text-4xl font-extrabold text-white', 'text-3xl sm:text-4xl font-extrabold text-slate-900')
    html_content = html_content.replace('text-base font-bold text-slate-100', 'text-base font-bold text-slate-900')
    html_content = html_content.replace('text-xs text-slate-400', 'text-xs text-slate-500')
    html_content = html_content.replace('text-sm text-slate-400', 'text-sm text-slate-600')
    html_content = html_content.replace('text-slate-400 leading-relaxed', 'text-slate-600 leading-relaxed')

    # 6. Mental Models & Walkthrough Cards
    html_content = html_content.replace('bg-slate-900/60 border border-slate-800 hover:border-indigo-500/40', 'bg-white border border-slate-200 shadow-sm hover:border-indigo-300 hover:shadow-md')
    html_content = html_content.replace('bg-slate-900/60 border border-slate-800', 'bg-white border border-slate-200 shadow-sm')
    html_content = html_content.replace('bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-2xl backdrop-blur-md', 'bg-white border border-slate-200 rounded-2xl p-6 shadow-md')
    html_content = html_content.replace('bg-slate-900 border border-slate-800 rounded-2xl p-6', 'bg-white border border-slate-200 rounded-2xl p-6 shadow-sm')
    html_content = html_content.replace('bg-slate-900 border border-slate-800 rounded-xl', 'bg-white border border-slate-200 rounded-xl shadow-sm')

    # 7. Step Indicators (e.g. badge 1, 2, 3)
    html_content = html_content.replace('bg-indigo-500/20 text-indigo-400 font-bold flex items-center justify-center text-sm border border-indigo-500/30', 'bg-indigo-50 text-indigo-700 font-bold flex items-center justify-center text-sm border border-indigo-200')
    html_content = html_content.replace('bg-amber-500/20 text-amber-400 font-bold flex items-center justify-center text-sm border border-amber-500/30', 'bg-amber-50 text-amber-800 font-bold flex items-center justify-center text-sm border border-amber-200')
    html_content = html_content.replace('bg-emerald-500/20 text-emerald-400 font-bold flex items-center justify-center text-sm border border-emerald-500/30', 'bg-emerald-50 text-emerald-800 font-bold flex items-center justify-center text-sm border border-emerald-200')

    # 8. Pitfall Cards
    html_content = html_content.replace('bg-red-950/20 border border-red-500/30 hover:border-red-500/50', 'bg-red-50 border border-red-200 shadow-xs hover:border-red-300')
    html_content = html_content.replace('bg-amber-950/20 border border-amber-500/30 hover:border-amber-500/50', 'bg-amber-50 border border-amber-200 shadow-xs hover:border-amber-300')
    html_content = html_content.replace('bg-cyan-950/20 border border-cyan-500/30 hover:border-cyan-500/50', 'bg-sky-50 border border-sky-200 shadow-xs hover:border-sky-300')
    html_content = html_content.replace('text-red-300 text-sm font-bold', 'text-red-900 text-sm font-bold')
    html_content = html_content.replace('font-bold text-red-300 text-sm', 'font-bold text-red-900 text-sm')
    html_content = html_content.replace('font-bold text-amber-300 text-sm', 'font-bold text-amber-900 text-sm')
    html_content = html_content.replace('font-bold text-cyan-300 text-sm', 'font-bold text-sky-900 text-sm')

    # 9. Checklist list items
    html_content = html_content.replace('bg-slate-950/50 border border-slate-800/80 cursor-pointer hover:bg-slate-800/40', 'bg-slate-50 border border-slate-200 cursor-pointer hover:bg-indigo-50/30 hover:border-indigo-200')
    html_content = html_content.replace('bg-slate-950/50 border border-slate-800/80', 'bg-slate-50 border border-slate-200')
    html_content = html_content.replace('font-semibold text-slate-200', 'font-semibold text-slate-800')
    html_content = html_content.replace('w-full bg-slate-800 rounded-full h-2.5', 'w-full bg-slate-200 rounded-full h-2.5')

    # 10. Nav buttons & footer
    html_content = html_content.replace('bg-slate-800 hover:bg-slate-700 text-slate-200 transition border border-slate-700', 'bg-slate-100 hover:bg-slate-200 text-slate-700 transition border border-slate-200')
    html_content = html_content.replace('border-t border-slate-800', 'border-t border-slate-200')

    # 11. Simulator sub-panels
    html_content = html_content.replace('bg-slate-950/60 border border-slate-800', 'bg-slate-50 border border-slate-200')
    html_content = html_content.replace('bg-slate-950/80 border border-slate-800', 'bg-slate-50 border border-slate-200')
    html_content = html_content.replace('bg-slate-950/90 border border-slate-800', 'bg-slate-50 border border-slate-200')
    html_content = html_content.replace('bg-slate-950 border border-slate-800', 'bg-slate-50 border border-slate-200')
    html_content = html_content.replace('bg-slate-950 border-2 border-slate-800', 'bg-slate-50 border-2 border-slate-200')
    html_content = html_content.replace('bg-slate-950/60 border-2 border-slate-800', 'bg-slate-50 border-2 border-slate-200')
    html_content = html_content.replace('bg-slate-950/80 border-2 border-slate-800', 'bg-slate-50 border-2 border-slate-200')
    html_content = html_content.replace('font-bold text-slate-200', 'font-bold text-slate-800')
    html_content = html_content.replace('text-slate-300 font-bold', 'text-slate-800 font-bold')
    html_content = html_content.replace('text-slate-200', 'text-slate-700')
    html_content = html_content.replace('text-slate-300', 'text-slate-700')

    return html_content

if __name__ == '__main__':
    roteiros_dir = r'c:\Users\leonm\projects\lab-redes\roteiros'
    files = [os.path.join(roteiros_dir, f) for f in os.listdir(roteiros_dir) if f.endswith('.html')]
    files.append(r'c:\Users\leonm\projects\lab-redes\exemplo.html')

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = convert_to_light_theme(content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Converted: {os.path.basename(file_path)}")
