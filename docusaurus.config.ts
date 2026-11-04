import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Busy Tag Docs',
  tagline: 'User guides and developer documentation for Busy Tag',
  favicon: 'img/favicon.svg',

  future: {
    v4: true,
  },

  url: 'https://busy-tag.github.io',
  baseUrl: '/',

  organizationName: 'busy-tag',
  projectName: 'busy-tag.github.io',
  trailingSlash: false,

  onBrokenLinks: 'throw',

  markdown: {
    // .md files are parsed as CommonMark (the generated guides), .mdx as MDX.
    format: 'detect',
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          // Docs-only site: documentation is served from the site root.
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: [
    [
      '@easyops-cn/docusaurus-search-local',
      {
        hashed: true,
        docsRouteBasePath: '/',
        indexBlog: false,
        highlightSearchTermsOnTargetPage: true,
      },
    ],
  ],

  themeConfig: {
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Busy Tag Docs',
      logo: {
        alt: 'Busy Tag',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docs',
          position: 'left',
          label: 'Documentation',
        },
        {
          href: 'https://www.busytag.com',
          label: 'busytag.com',
          position: 'right',
        },
        {
          href: 'https://github.com/busy-tag',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {label: 'Plugin user guides', to: '/plugins'},
            {label: 'Developer guides', to: '/developers'},
            {label: 'Hardware & firmware', to: '/hardware'},
          ],
        },
        {
          title: 'Busy Tag',
          items: [
            {label: 'Website', href: 'https://www.busytag.com'},
            {label: 'GitHub', href: 'https://github.com/busy-tag'},
          ],
        },
        {
          title: 'Follow us',
          items: [
            {label: 'YouTube', href: 'https://www.youtube.com/@BusyTaghello'},
            {label: 'Instagram', href: 'https://www.instagram.com/busytag'},
            {label: 'TikTok', href: 'https://www.tiktok.com/@busytag'},
            {label: 'Facebook', href: 'https://www.facebook.com/people/BusyTag/61555324800331/'},
            {label: 'LinkedIn', href: 'https://www.linkedin.com/company/busytag/'},
            {label: 'X', href: 'https://x.com/busytag'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} SIA BUSY TAG`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['json', 'bash', 'csharp'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
