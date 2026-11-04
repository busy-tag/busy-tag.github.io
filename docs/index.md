---
title: Busy Tag Documentation
sidebar_label: Welcome
sidebar_position: 1
slug: /
description: User guides and developer documentation for the Busy Tag status display.
---

Busy Tag is a status display with a 240 × 280 colour screen and an RGB LED. You manage it from
the **Busy Tag app** on Windows, macOS, Android and iOS. This site has guides for using the
app's plugins, documentation for developers who build their own, and the device's command
reference.

## Plugin user guides

Each built-in plugin (Integrations in the app) has a guide. It explains how to add and configure
the plugin, what it shows on your Busy Tag, and how to fix common problems.

[Browse the plugin guides →](/plugins)

## Developer guides

- [Plugin Development Guide](/developers/plugin-development): build your own plugin with HTML,
  CSS and JavaScript. Covers the plugin lifecycle, the `busyTagPlugin` API, the screen limits and
  packaging.
- [Busy Tag Design format](/developers/design-format): the `.busytagdesign` file format used to
  share designs.

## Hardware & firmware

- [AT Command Manual (firmware 3.x)](/hardware/at-commands): every USB serial command of the
  Wi-Fi Busy Tag: LEDs, display, files, Wi-Fi, cloud and the local HTTP server.
- [Local Network Guide](/hardware/local-network): control Busy Tag over Wi-Fi without the cloud,
  in access-point, station or STA+AP mode, through its HTTP API.
- [AT Command Manual (firmware 2.x)](/hardware/at-commands-v2): the command set of Busy Tag
  devices without Wi-Fi.

## Source code

The [busy-tag GitHub organisation](https://github.com/busy-tag) hosts the open-source parts of
Busy Tag, including the .NET communication library, the command-line tool and example widgets.
