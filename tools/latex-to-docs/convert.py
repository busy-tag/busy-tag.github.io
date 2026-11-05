"""Convert Busy Tag LaTeX docs into Docusaurus Markdown + SVG figures.

Usage: python convert.py <docs_src_dir> <site_dir> [--hw FIRMWARE_DOCS_DIR] [--only NAME] [--no-figs] [--include-dev]

--hw points at the docs/ folder of the firmware sources; its manuals listed in
HW_DOCS are published under /hardware.

Plugin guides are published only for plugins that regular users can see. A plugin whose
manifest.json (BusyTag/Resources/Raw/DefaultPlugins/<Name>/manifest.json in the app repo) has
"developerOnly": true is hidden in the app unless developer mode is on, so its guide is skipped
and any previously generated page, figures and PDF are removed. --include-dev publishes them anyway.
"""
import os, re, sys, shutil, subprocess, json, tempfile, glob

SRC = sys.argv[1]
SITE = sys.argv[2]
ONLY = sys.argv[sys.argv.index('--only') + 1] if '--only' in sys.argv else None
NOFIGS = '--no-figs' in sys.argv
INCLUDE_DEV = '--include-dev' in sys.argv
HW_SRC = sys.argv[sys.argv.index('--hw') + 1] if '--hw' in sys.argv else None
PLUGINS_DIR = os.path.join(SRC, '..', 'BusyTag', 'Resources', 'Raw', 'DefaultPlugins')
import pypandoc

DEV_DESCRIPTIONS = {
    'PluginDevelopment': 'Build your own Busy Tag plugin with HTML, CSS and JavaScript: lifecycle, API, screen limits and packaging.',
    'DesignFormat': 'The .busytagdesign file format used to share and import Busy Tag designs.',
}

# Firmware repo manuals: file stem -> (job name, slug, sidebar position, title, description).
# Only manuals for RELEASED firmware: the current 3.x manual plus the 2.x manual for USB-only
# devices, and the local network guide for 3.0. Not yet published: at_command_manual_3.1 and
# local_network_guide (both describe the unreleased firmware 3.1; when 3.1 ships, point the
# AtCommands and LocalNetwork entries at them); user_manual.tex is superseded by the AT manuals.
HW_DOCS = {
    'at_command_manual_3.0': ('AtCommands', 'at-commands', 1, 'AT Command Manual (firmware 3.x)',
                              'USB serial AT command reference for Busy Tag 2 (hardware 2.0, firmware 3.0, Wi-Fi).'),
    'local_network_guide_3.0': ('LocalNetwork', 'local-network', 2, 'Local Network Guide (firmware 3.x)',
                                'Control Busy Tag over the local network without the cloud: access point, station and STA+AP modes and the built-in HTTP API (firmware 3.0).'),
    'at_command_manual_2.0': ('AtCommandsV2', 'at-commands-v2', 3, 'AT Command Manual (firmware 2.x)',
                              'USB serial AT command reference for the original Busy Tag (hardware 1.0, firmware 2.x, no Wi-Fi).'),
}
HW_BY_NAME = {v[0]: v for v in HW_DOCS.values()}

SLUG_OVERRIDES = {'YouTubeSubscribers': 'youtube-subscribers', 'YouTubeVideoStats': 'youtube-video-stats',
                  'JetBrainsAiUsage': 'jetbrains-ai-usage'}


def kebab(name):
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', '-', name).lower()


def slug_for(name):
    if name in HW_BY_NAME: return HW_BY_NAME[name][1]
    return SLUG_OVERRIDES.get(name, kebab(name))


def is_developer_only(name):
    path = os.path.join(PLUGINS_DIR, name, 'manifest.json')
    if not os.path.exists(path):
        sys.exit('No manifest for plugin %s at %s; cannot tell whether it is developer-only.' % (name, path))
    return bool(json.load(open(path, encoding='utf-8-sig')).get('developerOnly', False))


def remove_generated(tex, sect, name):
    slug = slug_for(name)
    removed = []
    for p in [os.path.join(SITE, 'docs', sect, slug + '.md'),
              os.path.join(SITE, 'static', 'pdf', os.path.basename(tex).replace('.tex', '.pdf'))] + \
             glob.glob(os.path.join(SITE, 'docs', sect, 'img', slug + '-fig-*.svg')):
        if os.path.exists(p):
            os.remove(p); removed.append(p)
    return removed


JOBS = []  # (tex path, out dir rel to site/docs, slug, kind, sidebar_position)
for f in sorted(glob.glob(os.path.join(SRC, 'plugin-user-guides', '*_UserGuide.tex'))):
    name = os.path.basename(f).replace('_UserGuide.tex', '')
    if not INCLUDE_DEV and is_developer_only(name):
        if not ONLY or ONLY == name:
            gone = remove_generated(f, 'plugins', name)
            print('%-22s skipped (developerOnly)%s' % (name, ', removed %d files' % len(gone) if gone else ''))
        continue
    JOBS.append((f, 'plugins', name, 'plugin', None))
JOBS.append((os.path.join(SRC, 'busytagplugin', 'BusyTag_Plugin_Development_Guide.tex'), 'developers', 'PluginDevelopment', 'dev', 1))
JOBS.append((os.path.join(SRC, 'busytagdesign', 'BusyTagDesign_Format.tex'), 'developers', 'DesignFormat', 'dev', 2))
if HW_SRC:
    for stem, (name, slug, pos, _, _) in HW_DOCS.items():
        JOBS.append((os.path.join(HW_SRC, stem + '.tex'), 'hardware', name, 'hw', pos))

DRAW_RE = re.compile(r'\\begin\{(tikzpicture|scope)\}|\\(node|draw|fill|filldraw|path|shade|shadedraw|clip|tikz|pic)\b')
FONT_RE = re.compile(r'\\(fontsize|selectfont|fontfamily|fontseries|fontshape|usefont)\b')
ADMON_ENVS = {'tipbox': 'tip', 'notebox': 'note', 'warnbox': 'warning', 'cmdbox': 'CMD'}
RECURSE_ENVS = {'itemize', 'enumerate', 'description', 'tipbox', 'notebox', 'warnbox'}
FIG_ENVS = {'center', 'figure', 'minipage', 'tikzpicture', 'flushleft', 'flushright'}


def group(s, i):
    """s[i] == '{' or '['; return index just past the matching close."""
    o = s[i]; c = '}' if o == '{' else ']'
    depth = 0; j = i
    while j < len(s):
        ch = s[j]
        if ch == '\\':
            j += 2; continue
        if ch == o: depth += 1
        elif ch == c:
            depth -= 1
            if depth == 0: return j + 1
        j += 1
    raise ValueError('unbalanced at %d' % i)


def strip_comments(s):
    out = []
    for line in s.split('\n'):
        m = re.search(r'(?<!\\)%', line)
        out.append(line[:m.start()] if m else line)
    return '\n'.join(out)


def parse_defs(pre):
    """Return {name: (kind, nargs, body_text, full_def_text)} for newcommand/newenvironment."""
    defs = {}
    for m in re.finditer(r'\\(newcommand|renewcommand|DeclareRobustCommand|newenvironment|newtcolorbox|newtcblisting)\*?\s*(\{\\?([A-Za-z@]+)\}|\\([A-Za-z@]+))', pre):
        kind = m.group(1); name = m.group(3) or m.group(4)
        j = m.end(); nargs = 0
        while j < len(pre) and pre[j] in ' \n\t': j += 1
        if j < len(pre) and pre[j] == '[':
            e = group(pre, j); nargs = int(pre[j+1:e-1]) if pre[j+1:e-1].strip().isdigit() else 0; j = e
            while j < len(pre) and pre[j] in ' \n\t': j += 1
            if j < len(pre) and pre[j] == '[':
                j = group(pre, j)
        while j < len(pre) and pre[j] in ' \n\t': j += 1
        bodies = []
        reps = 2 if kind == 'newenvironment' else 1
        for _ in range(reps):
            while j < len(pre) and pre[j] in ' \n\t': j += 1
            if j < len(pre) and pre[j] == '{':
                e = group(pre, j); bodies.append(pre[j+1:e-1]); j = e
        defs[name] = (kind, nargs, '\n'.join(bodies), pre[m.start():j])
    return defs


def drawing_names(defs, pre):
    draw = set()
    for n, (k, a, b, full) in defs.items():
        if DRAW_RE.search(b): draw.add(n)
    changed = True
    while changed:
        changed = False
        for n, (k, a, b, full) in defs.items():
            if n in draw: continue
            if any(re.search(r'\\%s(?![A-Za-z])|\\begin\{%s\}' % (re.escape(d), re.escape(d)), b) for d in draw):
                draw.add(n); changed = True
    return draw


def has_drawing(text, draw):
    if DRAW_RE.search(text): return True
    for d in draw:
        if re.search(r'\\%s(?![A-Za-z])|\\begin\{%s\}' % (re.escape(d), re.escape(d)), text):
            return True
    return False


def find_env_end(s, i, name):
    """s[i:] starts with \\begin{name}; return index past matching \\end{name}."""
    pat = re.compile(r'\\(begin|end)\{%s\}' % re.escape(name))
    depth = 0
    for m in pat.finditer(s, i):
        depth += 1 if m.group(1) == 'begin' else -1
        if depth == 0: return m.end()
    raise ValueError('no end for ' + name)


def figure_ranges(s, base, draw, out):
    """Collect (start,end) figure ranges in s (offset base)."""
    i = 0; para_start = 0
    beg = re.compile(r'\\begin\{([^}]+)\}')
    pieces = []  # (start, end, kind, name)
    while i < len(s):
        m = beg.search(s, i)
        if not m: break
        e = find_env_end(s, m.start(), m.group(1))
        pieces.append((m.start(), e, m.group(1)))
        i = e
    # text between environments: split into paragraphs
    cur = 0
    segs = []
    for (a, e, name) in pieces:
        segs.append(('text', cur, a, None)); segs.append(('env', a, e, name)); cur = e
    segs.append(('text', cur, len(s), None))
    for kind, a, e, name in segs:
        if kind == 'env':
            body = s[a:e]
            if not has_drawing(body, draw): continue
            if name in RECURSE_ENVS:
                inner_start = s.index('}', a) + 1
                inner_end = s.rindex('\\end{', a, e)
                figure_ranges(s[inner_start:inner_end], base + inner_start, draw, out)
            else:
                out.append((base + a, base + e, name))
        else:
            # paragraphs
            text = s[a:e]
            for pm in re.finditer(r'(?:(?!\n\s*\n).)+', text, re.S):
                if has_drawing(pm.group(0), draw):
                    out.append((base + a + pm.start(), base + a + pm.end(), 'para'))
    return out


def plain(t):
    t = re.sub(r'\\href\{[^}]*\}', '', t)
    t = re.sub(r'\\\\', ' ', t)
    t = re.sub(r'\\texttt\{([^}]*)\}', r'\1', t)
    t = re.sub(r'\\[A-Za-z]+\*?(\[[^\]]*\])?', '', t)
    t = t.replace('---', '—').replace('--', '–')
    t = t.replace('{', '').replace('}', '').replace('~', ' ').replace('``', '"').replace("''", '"')
    t = t.replace('\\#', '#').replace('\\%', '%').replace('\\&', '&').replace('\\_', '_')
    return re.sub(r'\s+', ' ', t).strip()


def alt_text(block):
    caps = []
    for m in re.finditer(r'\\textit\{', block):
        e = group(block, m.end() - 1)
        caps.append(plain(block[m.end():e-1]))
    caps = [c for c in caps if c]
    return ('; '.join(caps))[:300] or 'Busy Tag screen example'


def gh_slug(t):
    t = t.lower().strip()
    t = re.sub(r'[^\w\- ]', '', t)
    return t.replace(' ', '-')


def render_figures(pre, figs, outdir, prefix, engine):
    """Compile every figure onto its own PDF page, crop to the inked area, export SVG."""
    import pymupdf
    if not figs: return []
    tmp = tempfile.mkdtemp(prefix='btfig')
    if engine != 'xelatex' and 'lmodern' not in pre:
        # Vector Latin Modern instead of bitmap EC fonts, so every glyph converts to paths.
        pre = re.sub(r'(\\usepackage\[T1\]\{fontenc\})', r'\1\n\\usepackage{lmodern}', pre, count=1)
    doc = pre + '\n\\begin{document}\n\\pagestyle{empty}\n'
    for f in figs:
        doc += '\\thispagestyle{empty}\n' + f + '\n\\clearpage\n'
    doc += '\\end{document}\n'
    open(os.path.join(tmp, 'f.tex'), 'w', encoding='utf-8').write(doc)
    cmd = ['xelatex' if engine == 'xelatex' else 'pdflatex', '-interaction=nonstopmode', 'f.tex']
    r = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True, encoding='utf-8', errors='replace')
    pdf = os.path.join(tmp, 'f.pdf')
    if not os.path.exists(pdf):
        print('  !! TeX failed:', r.stdout[-1500:]); return []
    errs = re.findall(r'^! .*', r.stdout, re.M)
    if errs: print('  !! TeX errors:', errs[:5])
    os.makedirs(outdir, exist_ok=True)
    names = []
    d = pymupdf.open(pdf)
    if len(d) != len(figs):
        print('  !! expected %d pages, got %d' % (len(figs), len(d)))
    for k, page in enumerate(d, 1):
        box = pymupdf.Rect()
        for _, rect in page.get_bboxlog():
            rr = pymupdf.Rect(rect)
            if rr.is_empty or rr.width >= page.rect.width * 0.99: continue
            box |= rr
        if box.is_empty:
            print('  !! empty figure page', k); continue
        box = (box + (-3, -3, 3, 3)) & page.rect
        page.set_cropbox(box)
        svg = page.get_svg_image(matrix=pymupdf.Matrix(1.4, 1.4), text_as_path=True)
        n = '%s-fig-%d.svg' % (prefix, k)
        open(os.path.join(outdir, n), 'w', encoding='utf-8').write(svg); names.append(n)
    d.close()
    shutil.rmtree(tmp, ignore_errors=True)
    return names


def convert(job):
    path, sect, name, kind, sidebar_pos = job
    raw = open(path, encoding='utf-8').read()
    src = strip_comments(raw)
    pre, body = src.split('\\begin{document}', 1)
    body = body.rsplit('\\end{document}', 1)[0]
    defs = parse_defs(pre)
    draw = drawing_names(defs, pre)
    engine = 'xelatex' if 'fontspec' in pre else 'latex'
    slug = slug_for(name)

    # ---- metadata
    m = re.search(r'pdftitle=\{([^}]*)\}', pre)
    title = plain(m.group(1)) if m else name
    title = re.sub(r'^Busy Tag\s+', '', title)
    title = re.sub(r'\s+[-–—]+\s+User Guide$', '', title).strip()
    title = title.replace('--', '–')
    if kind == 'hw': title = HW_BY_NAME[name][3]
    first_sec = re.search(r'\\section\*?\{', body)
    front = body[:first_sec.start()]
    body = body[first_sec.start():]
    desc = ''
    tm = re.search(r'\\textit\{', front)
    if tm:
        desc = plain(front[tm.end():group(front, tm.end() - 1) - 1])
    am = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', front, re.S)
    if am: body = am.group(1) + '\n\n' + body

    # ---- cross references -> links (done before figure extraction so captions get them too)
    labels = {}; numbers = {}; sec = sub = 0
    for lm in re.finditer(r'\\(section|subsection)(\*?)\{', body):
        e = group(body, lm.end() - 1); t = plain(body[lm.end():e-1])
        if not lm.group(2):
            if lm.group(1) == 'section': sec += 1; sub = 0; numbers['%d' % sec] = t
            else: sub += 1; numbers['%d.%d' % (sec, sub)] = t
        ll = re.match(r'\s*\\label\{([^}]+)\}', body[e:])
        if ll: labels[ll.group(1)] = t
    def link(t): return '\\href{\\#%s}{%s}' % (gh_slug(t), t)
    def ref(mm):
        lab = mm.group(2)
        if lab in labels: return link(labels[lab])
        return (mm.group(1) or '') + 'below'
    body = re.sub(r'((?:[Ss]ection|[Tt]able|[Ff]igure|[Aa]ppendix)~)?\\(?:auto|name)?ref\{([^}]+)\}', ref, body)
    body = re.sub(r'[Ss]ection~(\d+(?:\.\d+)?)(?![\d.]*\d)',
                  lambda mm: link(numbers[mm.group(1)]) if mm.group(1) in numbers else mm.group(0), body)
    body = re.sub(r'\\label\{[^}]+\}', '', body)

    # ---- figures
    rngs = sorted(figure_ranges(body, 0, draw, []))
    figs = [body[a:e] for a, e, _ in rngs]
    alts = [alt_text(f) for f in figs]
    imgdir = os.path.join(SITE, 'docs', sect, 'img')
    body_colors = '\n'.join(re.findall(r'\\(?:definecolor|colorlet)\{[^}]*\}(?:\{[^}]*\}){1,2}', body))
    names = [] if NOFIGS else render_figures(pre + '\n' + body_colors, figs, imgdir, slug, engine)
    if NOFIGS: names = ['%s-fig-%d.svg' % (slug, k + 1) for k in range(len(figs))]
    nb = []; cur = 0
    for k, (a, e, _) in enumerate(rngs):
        nb.append(body[cur:a]); nb.append('\n\nFIGPLACEHOLDER%d\n\n' % k); cur = e
    nb.append(body[cur:]); body = ''.join(nb)

    # ---- verbatim macros (\newcommand{\cmd}[1]{\texttt{\detokenize{#1}}}): pandoc expands
    # \detokenize to nothing, so turn each use into \texttt with the argument escaped.
    VERB_ESC = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '_': r'\_', '#': r'\#', '%': r'\%',
                '&': r'\&', '$': r'\$', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    for n, (k, a, b, full) in defs.items():
        if a != 1 or '\\detokenize' not in b: continue
        pat = re.compile(r'\\%s(?![A-Za-z])\s*\{' % re.escape(n)); parts = []; pos = 0
        for mm in pat.finditer(body):
            if mm.start() < pos: continue
            e = group(body, mm.end() - 1)
            arg = ''.join(VERB_ESC.get(ch, ch) for ch in body[mm.end():e-1])
            parts.append(body[pos:mm.start()]); parts.append('\\texttt{%s}' % arg); pos = e
        parts.append(body[pos:]); body = ''.join(parts)

    # ---- admonitions
    def admon(mm):
        # A box title ([Title]) is carried hex-encoded so pandoc leaves it alone.
        env = mm.group(1); t = plain(mm.group(2)[1:-1]) if mm.group(2) else ''
        return '\n\nADMONOPEN-%s%s\n\n' % (ADMON_ENVS[env], '-' + t.encode('utf-8').hex() if t else '')
    body = re.sub(r'\\begin\{(%s)\}(\[[^\]]*\])?' % '|'.join(ADMON_ENVS), admon, body)
    body = re.sub(r'\\end\{(%s)\}' % '|'.join(ADMON_ENVS), '\n\nADMONCLOSE\n\n', body)
    # codewin env (dev guide) -> lstlisting
    body = re.sub(r'\\begin\{codewin\}(\[[^\]]*\])?(\{[^}]*\})?', r'\\begin{lstlisting}', body)
    body = body.replace('\\end{codewin}', '\\end{lstlisting}')
    for junk in [r'\\newpage', r'\\clearpage', r'\\tableofcontents', r'\\needspace\{[^}]*\}', r'\\vfill', r'\\noindent',
                 r'\\renewcommand\{\\arraystretch\}\{[^}]*\}', r'\\(small|footnotesize|scriptsize)(?![A-Za-z])']:
        body = re.sub(junk, '', body)
    # \multicolumn{n}{spec}{content} -> content & & ...
    out_parts = []; pos = 0
    pat = re.compile(r'\\multicolumn\{(\d+)\}\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}')
    for mm in pat.finditer(body):
        if mm.start() < pos: continue
        n = int(mm.group(1)); e = group(body, mm.end())
        out_parts.append(body[pos:mm.start()]); out_parts.append(body[mm.end()+1:e-1] + ' &' * (n - 1)); pos = e
    out_parts.append(body[pos:]); body = ''.join(out_parts)
    # tabular column specs: drop @{...} and >{...} decorations pandoc dislikes
    def colspec(mm):
        j = mm.end()
        if mm.group(1) == 'tabularx':
            e = group(body, j); j = e  # width arg
        e = group(body, j); spec = body[j+1:e-1]
        spec = re.sub(r'[@<>]\{(?:[^{}]|\{[^{}]*\})*\}', '', spec)
        colspec.res.append((mm.start(), e, '\\begin{%s}%s{%s}' % (mm.group(1), body[mm.end():j], spec)))
    colspec.res = []
    for mm in re.finditer(r'\\begin\{(tabularx|tabular|longtable)\}', body): colspec(mm)
    for a, e, rep in reversed(colspec.res): body = body[:a] + rep + body[e:]
    # simple inline math symbols -> unicode
    SYM = {'blacktriangleright': '▶', 'rightarrow': '→', 'leftarrow': '←', 'times': '×', 'swarrow': '↙',
           'nearrow': '↗', 'searrow': '↘', 'uparrow': '↑', 'downarrow': '↓', 'ldots': '…', 'dots': '…',
           'pm': '±', 'le': '≤', 'ge': '≥', 'leq': '≤', 'geq': '≥', 'cdot': '·', 'approx': '≈', 'checkmark': '✓',
           'blacksquare': '■', 'square': '□', 'circ': '°', 'bullet': '•', 'Rightarrow': '⇒', 'to': '→', 'sim': '~', 'neq': '≠', 'infty': '∞'}
    def mathsym(mm):
        inner = mm.group(1) or mm.group(2)
        t = inner.strip()
        t2 = re.sub(r'\\([A-Za-z]+)', lambda x: SYM.get(x.group(1), x.group(0)), t)
        t2 = re.sub(r'\^\{?\\?circ\}?', '°', t2).replace('{', '').replace('}', '').replace('~', ' ')
        return t2 if '\\' not in t2 and '^' not in t2 and '_' not in t2 else mm.group(0)
    body = re.sub(r'\\\((.*?)\\\)|(?<!\\)\$([^$\n]{1,40})\$', mathsym, body)
    body = re.sub(r'\\(rightarrow|leftarrow|blacktriangleright|textrightarrow)\b', lambda x: SYM.get(x.group(1), '→'), body)

    # ---- macro preamble for pandoc: keep simple text macros
    mp = ['\\newcommand{\\swatch}[1]{}', '\\newcommand{\\degC}{°C}', '\\newcommand{\\degF}{°F}']
    for n, (k, a, b, full) in defs.items():
        if n in draw or k not in ('newcommand', 'DeclareRobustCommand') or n in ('swatch', 'degC', 'degF'):
            continue
        if FONT_RE.search(b) or '\\color' in b or '\\rule' in b or '\\fcolorbox' in b:
            args = ''.join('{}' for _ in range(a))
            mp.append('\\newcommand{\\%s}%s{%s}' % (n, '[%d]' % a if a else '', ' '.join('#%d' % (i+1) for i in range(a)) if n not in ('px',) else ''))
            continue
        mp.append(full.replace('\\renewcommand', '\\newcommand').replace('\\DeclareRobustCommand', '\\newcommand'))
    tex = '\n'.join(mp) + '\n' + body
    md = pypandoc.convert_text(tex, 'gfm-raw_html', format='latex',
                               extra_args=['--wrap=none', '--shift-heading-level-by=1'])
    md = md.replace('\r\n', '\n')

    # ---- post-process
    def fig(mm):
        k = int(mm.group(1))
        return '![%s](./img/%s)' % (alts[k].replace('[', '(').replace(']', ')'), names[k]) if k < len(names) else ''
    md = re.sub(r'FIGPLACEHOLDER(\d+)', fig, md)
    out = []; mode = None; buf = []
    for line in md.split('\n'):
        mo = re.match(r'^ADMONOPEN-([A-Za-z]+)(?:-([0-9a-f]+))?\s*$', line.strip()) if line.strip().startswith('ADMONOPEN') else None
        if mo:
            mode = mo.group(1)
            ttl = '[%s]' % bytes.fromhex(mo.group(2)).decode('utf-8') if mo.group(2) else ''
            if mode != 'CMD': out.append(':::%s%s' % (mode, ttl))
            else: buf = []
            continue
        if line.strip() == 'ADMONCLOSE':
            if mode == 'CMD':
                code = '\n'.join(buf).strip()
                code = re.sub(r'`([^`]*)`', r'\1', code).replace('\\', '')
                code = re.sub(r'\*\*([^*]*)\*\*', r'\1', code)
                code = '\n'.join(l.strip() for l in code.split('\n') if l.strip())
                out.append('```text\n%s\n```' % code)
            else:
                while out and out[-1] == '': out.pop()
                out.append(''); out.append(':::')
            mode = None; continue
        if mode == 'CMD': buf.append(line)
        else: out.append(line)
    md = '\n'.join(out)
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = re.sub(r'(:::\w+(?:\[[^\]\n]*\])?)\n\n', r'\1\n', md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r'\n\n:::\n', '\n:::\n', md).strip() + '\n'
    # tighten simple lists (pandoc emits loose lists for LaTeX items)
    while True:
        md2 = re.sub(r'(\n(?:-|\d+\.)\s+[^\n]+)\n\n(?=(?:-|\d+\.)\s)', r'\1\n', md)
        if md2 == md: break
        md = md2
    md = md.replace('``` lstlisting', '```').replace('``` text', '```text')
    # code fence languages: listings names -> Prism names ("``` [Sharp]C" -> "```csharp")
    LANGS = {'[sharp]c': 'csharp', 'c#': 'csharp', 'javascript': 'javascript', 'python': 'python',
             'swift': 'swift', 'html': 'html', 'json': 'json', 'bash': 'bash', 'sh': 'bash',
             'httpapi': 'http', 'xml': 'xml', 'powershell': 'powershell'}
    md = re.sub(r'^```[ \t]+(\S+)[ \t]*$', lambda m: '```' + LANGS.get(m.group(1).lower(), m.group(1).lower()),
                md, flags=re.M)

    # display math: the site has no KaTeX, so write simple formulas in Unicode
    def unimath(m):
        t = m.group(1).strip()
        for _ in range(3):
            t = re.sub(r'\\(?:mathrm|text|mathit)\{([^{}]*)\}', r'\1', t)
            t = re.sub(r'\\sqrt\{([^{}]*)\}', r'√(\1)', t)
            t = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1)/(\2)', t)
        t = re.sub(r'\^\{?2\}?', '²', t)
        t = re.sub(r'\^\{?3\}?', '³', t)
        t = t.replace('\\cdot', '·').replace('\\times', '×').replace(' - ', ' − ')
        if '\\' in t:
            print('   !! math left as LaTeX:', t)
        return '\n*%s*\n' % t if '\\' not in t else m.group(0)
    md = re.sub(r'^```math\n(.*?)\n```$', unimath, md, flags=re.M | re.S)

    # GFM tables: a '|' inside a code span still splits the cell, so escape it
    def pipes(line):
        if not line.startswith('|'): return line
        return re.sub(r'`[^`\n]*`', lambda m: re.sub(r'(?<!\\)\|', r'\\|', m.group(0)), line)
    md = '\n'.join(pipes(l) for l in md.split('\n'))

    # GFM tables have no colspan: a \multicolumn group row ("| *Clock face* |  |  |") becomes a
    # bold label above its own table (same header), and all-empty rows (longtable ends) are dropped.
    def cells(line):
        return [c.strip() for c in re.split(r'(?<!\\)\|', line.strip())[1:-1]]
    def tables(text):
        out, block = [], []
        for line in text.split('\n') + ['']:
            if line.startswith('|'):
                block.append(line); continue
            if block:
                out.extend(fix_table(block)); block = []
            out.append(line)
        return '\n'.join(out[:-1])
    def fix_table(block):
        if len(block) < 2 or not re.match(r'^\|[\s:|-]+\|$', block[1].strip()): return block
        head, res, open_ = block[:2], [], True
        res.extend(head)
        for row in block[2:]:
            c = cells(row)
            if not any(c): continue
            if len(c) > 1 and c[0] and not any(c[1:]):
                label = re.sub(r'^\*+|\*+$', '', c[0])
                if res[-1] == head[1]: res = res[:-2]   # nothing under the header yet
                else: res.append('')
                res.extend(['**%s**' % label, ''] + head)
                continue
            res.append(row)
        return res
    md = tables(md)

    fm = ['---', 'title: "%s"' % title.replace('"', '\\"')]
    if kind == 'plugin':
        fm.append('sidebar_label: "%s"' % re.sub(r'\s+Plugin$', '', title))
        fm.append('slug: /plugins/%s' % slug)
    else:
        fm.append('sidebar_position: %d' % sidebar_pos)
        fm.append('slug: /%s/%s' % (sect, slug))
    # Without a description Docusaurus uses the first paragraph (the PDF note) on index cards.
    desc = desc or DEV_DESCRIPTIONS.get(name, '') or (HW_BY_NAME[name][4] if kind == 'hw' else '')
    if desc: fm.append('description: "%s"' % desc.replace('"', '\\"'))
    fm.append('---')
    head = '\n'.join(fm) + '\n\n'
    if desc and kind == 'plugin': head += '*%s*\n\n' % desc
    pdf = os.path.basename(path).replace('.tex', '.pdf')
    head += ':::info[PDF version]\nThis guide is also available as a [PDF](pathname:///pdf/%s).\n:::\n\n' % pdf
    os.makedirs(os.path.join(SITE, 'docs', sect), exist_ok=True)
    open(os.path.join(SITE, 'docs', sect, slug + '.md'), 'w', encoding='utf-8', newline='\n').write(head + md)
    pdfsrc = path.replace('.tex', '.pdf')
    if os.path.exists(pdfsrc):
        os.makedirs(os.path.join(SITE, 'static', 'pdf'), exist_ok=True)
        shutil.copy(pdfsrc, os.path.join(SITE, 'static', 'pdf', pdf))
    print('%-22s figs=%2d draw-macros=%d engine=%s' % (name, len(figs), len(draw), engine))
    for (a, e, n), f in zip(rngs, figs):
        if n not in ('center', 'para', 'tikzpicture', 'minipage', 'figure'):
            print('   fig env=%s: %s' % (n, f[:80].replace('\n', ' ')))


for j in JOBS:
    if ONLY and j[2] != ONLY: continue
    try:
        convert(j)
    except Exception as ex:
        import traceback; print('FAILED', j[2]); traceback.print_exc()
