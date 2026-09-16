import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in ['roteiros/09-switches-idf-mdf-trunk.html', 'roteiros/10-voip.html', 'roteiros/11-nat-e-hierarquia-dns.html', 'roteiros/12-spanning-tree-protocol.html', 'roteiros/13-trabalho-minimum-spanning-tree.html']:
    content = open(f, encoding='utf-8').read()
    idx = content.find('id="simulador"')
    print(f"=== {f} ===")
    print(content[idx:idx+900])
    print("\n" + "="*40 + "\n")
