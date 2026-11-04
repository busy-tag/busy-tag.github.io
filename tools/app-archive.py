"""Build src/data/app-archive.json from the public installer archive.

Usage: python tools/app-archive.py --latest 1.7.4 [--url https://greynut.com/BusyTagApp/]

The archive also holds builds that were uploaded but not released, and Microsoft Store
submission bundles. Only versions up to --latest (the newest released version) are listed, and
store bundles are skipped. Rerun after each release and commit the JSON.
"""
import json, os, re, sys, urllib.request
from datetime import datetime

URL = sys.argv[sys.argv.index('--url') + 1] if '--url' in sys.argv else 'https://greynut.com/BusyTagApp/'
if '--latest' not in sys.argv:
    sys.exit('--latest <version> is required (the newest released app version)')
LATEST = sys.argv[sys.argv.index('--latest') + 1]
OUT = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'app-archive.json')

# One <tr> per file: <a href="NAME">, then the date cell, then the size cell.
ROW = re.compile(r'href="(BusyTagApp_[^"]+)".*?(\d{4}-\d\d-\d\d) \d\d:\d\d.*?>\s*([\d.]+[KMG]?)\s*<')
NAME = re.compile(r'BusyTagApp_(mac|win)(?:_(x64|arm64|store))?_(\d+\.\d+\.\d+)(?:\.\d+)?\.(pkg|msix|msixbundle|exe)$')


def vkey(v):
    return tuple(int(x) for x in v.split('.'))


html = urllib.request.urlopen(urllib.request.Request(URL, headers={'User-Agent': 'busytag-docs'})).read().decode('utf-8', 'replace')
versions = {}
for href, date, size in ROW.findall(html):
    m = NAME.match(href)
    if not m:
        continue
    os_, arch, ver, ext = m.groups()
    if arch == 'store' or vkey(ver) > vkey(LATEST):
        continue
    v = versions.setdefault(ver, {'version': ver, 'date': date, 'files': []})
    v['date'] = min(v['date'], date)
    if os_ == 'mac':
        platform, label = 'macOS', 'Installer (.pkg)'
    else:
        platform = 'Windows Arm64' if arch == 'arm64' else 'Windows x64'
        label = 'Setup (.exe)' if ext == 'exe' else 'App package (.msix)'
    v['files'].append({'platform': platform, 'label': label, 'url': URL + href,
                       'size': size.replace('M', ' MB').replace('G', ' GB').replace('K', ' KB')})

order = {'Windows x64': 0, 'Windows Arm64': 1, 'macOS': 2}
data = sorted(versions.values(), key=lambda v: vkey(v['version']), reverse=True)
for v in data:
    v['files'].sort(key=lambda f: (order[f['platform']], f['label'] != 'Setup (.exe)'))
    v['dateLabel'] = datetime.strptime(v['date'], '%Y-%m-%d').strftime('%-d %B %Y' if os.name != 'nt' else '%#d %B %Y')

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump({'source': URL, 'latest': LATEST, 'versions': data}, open(OUT, 'w', encoding='utf-8', newline='\n'), indent=2)
print('wrote %d versions (%s ... %s) to %s' % (len(data), data[-1]['version'], data[0]['version'], os.path.normpath(OUT)))
