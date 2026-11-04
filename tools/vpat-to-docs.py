"""Publish the app's VPAT (accessibility conformance report) on the docs site.

Usage: python tools/vpat-to-docs.py <app repo docs/vpat dir> <site dir>

Reads VPAT.md, writes docs/about/vpat.md (front matter, PDF link, the report without its H1) and
copies BusyTag_VPAT.pdf to static/pdf/.
"""
import os, re, shutil, sys

SRC, SITE = sys.argv[1], sys.argv[2]
md = open(os.path.join(SRC, 'VPAT.md'), encoding='utf-8-sig').read().replace('\r\n', '\n')
version = re.search(r'\*\*Product Version\*\* \| ([^|]+?) \|', md).group(1)
date = re.search(r'\*\*Report Date\*\* \| ([^|]+?) \|', md).group(1)

# Drop the H1 (the page title comes from the front matter) and demote nothing else.
body = re.sub(r'\A# [^\n]*\n+', '', md)

head = f'''---
title: Accessibility Conformance Report (VPAT)
sidebar_label: VPAT report
sidebar_position: 2
description: "VPAT 2.5 accessibility conformance report for the Busy Tag app {version} ({date}): WCAG 2.1, Section 508 and EN 301 549."
---

:::info[PDF version]
This report is also available as a [PDF](pathname:///pdf/BusyTag_VPAT.pdf). A plain-language
summary is on the [Accessibility](/about/accessibility) page.
:::

'''
out = os.path.join(SITE, 'docs', 'about', 'vpat.md')
open(out, 'w', encoding='utf-8', newline='\n').write(head + body)
os.makedirs(os.path.join(SITE, 'static', 'pdf'), exist_ok=True)
shutil.copy(os.path.join(SRC, 'BusyTag_VPAT.pdf'), os.path.join(SITE, 'static', 'pdf', 'BusyTag_VPAT.pdf'))
print('wrote', out, 'for version', version)
