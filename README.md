# Busy Tag Docs

Source for **https://busy-tag.github.io**: user guides and developer documentation for Busy Tag.
Built with [Docusaurus](https://docusaurus.io/) and deployed to GitHub Pages by
`.github/workflows/deploy.yml` on every push to `main`.

## Local development

```bash
npm install
npm start          # dev server with live reload at http://localhost:3000
npm run build      # production build into ./build (fails on broken links)
npm run serve      # serve the production build locally
```

## Layout

```
docs/
  index.md                  Landing page (served at /)
  getting-started/          Install, connect, app tour        (hand-written)
  troubleshooting.md        Troubleshooting & FAQ             (hand-written)
  updates/                  Firmware updates, app release notes (hand-written)
                            downloads.mdx renders src/data/app-archive.json; after a release run
                            python tools/app-archive.py --latest <version>  (only released versions)
  about/                    Accessibility, privacy & legal    (hand-written)
                            vpat.md generated: python tools/vpat-to-docs.py <vpat-dir> .
  plugins/                  Plugin user guides  -> /plugins/<name>
  developers/               Developer guides (generated) + tools.md, examples.md (hand-written)
  hardware/                 Specs (hand-written), AT command manuals, local network guide
  */img/                    Figures (SVG) referenced by the guides
  */_category_.json         Sidebar label, order and index page per section
static/pdf/                 PDF versions linked from each guide
static/img/                 Logo and favicon
tools/latex-to-docs/        LaTeX -> Markdown converter (see below)
```

Pages are plain CommonMark `.md` files (`markdown.format: 'detect'`), so `{` and `<` need no
escaping. Use `.mdx` only when a page needs React components. Admonitions (`:::tip`, `:::note`,
`:::warning`) work in both.

## Regenerating from the LaTeX sources

The plugin guides, the Plugin Development Guide, the design-format spec and the hardware manuals
are written in LaTeX in separate source repositories. `tools/latex-to-docs/convert.py` turns them
into the Markdown pages here:

- Text goes through pandoc. Tip/note/warning boxes become admonitions, and section references
  become links.
- Each TikZ screen illustration is compiled with the guide's own preamble (pdflatex/xelatex),
  cropped and exported as SVG with PyMuPDF.
- The PDFs next to the `.tex` files are copied to `static/pdf/`.

Requirements: Python 3.10+, a TeX distribution (MiKTeX/TeX Live) with the packages the guides use.

```bash
python -m venv .venv
.venv/Scripts/pip install -r tools/latex-to-docs/requirements.txt   # bin/ on macOS/Linux
.venv/Scripts/python tools/latex-to-docs/convert.py <app-docs-dir> .
.venv/Scripts/python tools/latex-to-docs/convert.py <app-docs-dir> . --only AnalogClock
# hardware manuals (only released firmware; the list is HW_DOCS in convert.py)
.venv/Scripts/python tools/latex-to-docs/convert.py <app-docs-dir> . --hw <firmware-docs-dir> --only AtCommands
```

The converter overwrites the generated pages, so make lasting text changes in the `.tex` sources,
or stop regenerating that page once it has been edited here.
