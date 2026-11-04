---
title: App release notes
sidebar_position: 2
description: What changed in each version of the Busy Tag app.
---

What changed in each Busy Tag app release. Store versions can reach you a few days after the
release date. Your installed version is shown under Settings → **App info**. Installers of every
version are in the [download archive](/updates/downloads).

## 1.7.4 — September 2026 {#v1-7-4}

- New integrations: **GitHub Copilot Usage** and **Codex Usage**.
- Claude Code and Codex usage show the remaining time in days, hours and minutes.
- Sign-in for integrations goes through a Busy Tag server, so no secrets are stored in plugins.
- Integration playback resumes after the app restarts.
- Android: update check and **Open on Google Play**.
- Fixed outdated firmware information and update prompts after refreshing device info, and a
  crash on iOS.

## 1.7.1 — August 2026 {#v1-7-1}

- New languages: Russian, Ukrainian, Estonian, Polish, Portuguese, Italian and Lithuanian.
- **Video to GIF:** turn a video clip (up to 20 seconds) into a GIF for a design.
- **Import design from link**, and `busytag://` links open in the desktop app.
- iOS and Android: sign-in for integrations that need an account (Google, Microsoft).
- Integration playlist countdown and better plugin configuration pages.
- New **⋯** menu for items in Designs, and accessibility improvements throughout the app.
- Moved to .NET 10, with support for Android 16.
- Fixes for device cloud sync, secure storage, popups and a Windows crash when selecting items.

## 1.6.4 — July 2026 {#v1-6-4}

- **Device sharing** improvements.
- Wi-Fi settings: enter a network name by hand, rescan networks, live signal strength.
- Windows: native Arm64 builds, and separate x64 and Arm64 installers.
- Gmail and Google Drive integrations use narrower Google permissions.

## 1.6.2 — June 2026 {#v1-6-2}

- **Share devices** with other people using a QR code or link.
- **Share and import designs** as `.busytagdesign` files, links or QR codes.
- **Install integrations from a file** (`.busytagplugin`).
- New integrations: **Google Calendar**, **Gmail**, **Google Drive**, **Google Tasks** and
  **Claude Code Usage**, with redesigned integration settings pages.
- New Wi-Fi setup, device setup for the first device, and Wi-Fi signal indicator.
- Faster Gallery with offline caching and category browsing.
- Factory reset confirmation and automatic time zone for Busy Tag 2.

## 1.5.8 — April 2026 {#v1-5-8}

- Smoother progress display while images upload to the device.

## 1.5.7 — April 2026 {#v1-5-7}

*Windows setup only.*

- Tooltips on buttons throughout the app.
- Firmware updates are downloaded from a new server, and the firmware update flow is clearer in
  store versions of the app.

## 1.5.6 — April 2026 {#v1-5-6}

- Gallery: search moved to the header, and a new layout.
- Design editor: colour picker in a popup, and search for online images and GIFs.
- Updated Spanish translation.

## 1.5.5 — April 2026 {#v1-5-5}

- First version for the Mac App Store.
- Fixes for macOS and Windows.

## 1.5.2 — March 2026 {#v1-5-2}

- **Device recovery** on Windows and macOS: reinstall the firmware on a device that no longer
  starts.
- New languages: German, French, Spanish and Japanese.
- Windows: new setup program (`.exe`) next to the app package.
- Screen-reader support: accessible names and announcements across the app.
- Smaller GIFs thanks to better encoding, and clearer firmware update steps.

## 1.4.5 — February 2026 {#v1-4-5}

- Images and GIFs are optimised automatically to fit the device.
- Design editor: search online photos and GIFs (Pexels, KLIPY), choose **fill** or **fit**
  scaling, vertical text alignment and a live preview.

## 1.3.9 — January 2026 {#v1-3-9}

- Drag and drop to reorder designs and integrations.
- Custom icon colours for integrations.
- Integration updates keep your settings.
- Desktop: cloud sync for Busy Tag 2.
- New app icons and layouts for tablets.

## 1.3.3 — December 2025 {#v1-3-3}

*Windows.*

- Accessibility improvements and `busytag://` links.
- Fixes for cloud sync and file uploads.

## 1.3.0 — December 2025 {#v1-3-0}

*macOS.*

- **Busy Tag 2 support:** Wi-Fi setup, cloud connection and remote control.
- **Share devices** by QR code.
- Android and iOS support.
- New colour picker.
- Latvian language.
- Firmware files can be dropped onto the app to install them.

## 1.1.0 — April 2025 {#v1-1-0}

- **Integrations:** live content on Busy Tag, with a playlist that rotates through them. The
  first integrations: Analog Clock, Digital Clock, Weather, Weather Forecast, Countdown, Days
  Since, Days Left This Year, Lunar Phase, Marquee Text, Stock Price, Bitcoin Price and Microsoft
  Teams.
- Integrations can animate, play LED patterns and open web pages.

## 1.0.6 — April 2025 {#v1-0-6}

- Menu button navigation for small windows.
- The app reopens the page you used last.
- Fixes for Windows single-instance mode and macOS.

## 1.0.5 — April 2025 {#v1-0-5}

- Fixed: the device was not found on the first launch after a clean install.
- Crash and error reporting, and anonymous usage statistics.

## 1.0.2 — March 2025 {#v1-0-2}

*Windows. On macOS the same changes shipped as 1.0.1.*

- LED page with patterns.
- Only one copy of the app runs at a time on Windows.
- Fixed GIF optimisation and firmware updates on macOS.

## 1.0.1 — March 2025 {#v1-0-1}

*macOS.* See [1.0.2](#v1-0-2). Adds the option to start the app when you log in.

## 1.0.0 — March 2025 {#v1-0-0}

- New **Designs** page.
- New **LED** page with a colour picker.
- **Online gallery** designs come with LED colours.
- The app tells you at start-up when a new version is available.
- Faster USB transfers on macOS, and the start-at-login option works again.

## 0.2.5 — February 2025 {#v0-2-5}

*Windows.* Preview of the 1.0.0 changes.

## 0.2.2 — February 2025 {#v0-2-2}

- **Online gallery** page.
- Settings are stored more reliably.

## 0.2.1 — November 2024 {#v0-2-1}

- Fixed: default designs were hidden after a clean install.

## 0.2.0 — November 2024 {#v0-2-0}

- **Focus Session:** a Pomodoro timer and countdown shown on Busy Tag.
- Create designs from templates, and edit designs you made earlier.
- Cancel an image that is being sent to the device.

## 0.1.6 — October 2024 {#v0-1-6}

- Your affirmation images are saved.
- A warning when an image is larger than the 1 MB the device accepts.
- Dropped files are filtered to supported types, and drag and drop works on macOS.

## 0.1.5 — October 2024 {#v0-1-5}

First release for Windows and macOS:

- Create images with text, fonts, colours and backgrounds, and send them to Busy Tag.
- Set the LED colour and the screen and LED brightness.
- Firmware updates, automatic clean-up of old images on the device, and the Help and Learning
  centre pages.
