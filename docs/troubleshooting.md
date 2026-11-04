---
title: Troubleshooting & FAQ
sidebar_label: Troubleshooting & FAQ
sidebar_position: 4
description: Solutions for common Busy Tag problems and answers to frequent questions.
---

## Connection

### The computer does not find Busy Tag

- **Use a data cable.** Many USB-C cables only carry power: the device lights up but the computer
  does not see it. Try another cable.
- Plug the device straight into the computer instead of a hub or monitor port.
- Close other programs that may have opened the serial port (a serial terminal, the Arduino IDE
  or a second Busy Tag window). The app shows **is in use by another application** when this
  happens; the device reconnects once the port is free.
- Unplug the device, wait a few seconds and plug it in again.

### The phone app cannot set up the device

- The phone setup needs a Busy Tag 2 (Wi-Fi, firmware 3.x). The original Busy Tag is
  controlled from the desktop app over USB.
- Make sure the device shows the setup QR code. If it was set up before, it does not; hold the
  reset button for **3 seconds** to factory reset it and the QR code returns.
- Android: turn off mobile data during setup if the phone leaves the device's Wi-Fi because it has
  "no internet".
- Allow the camera (for the QR code) and, on Android, location and nearby-devices permissions:
  Android needs them to scan and join Wi-Fi networks.
- Busy Tag uses 2.4 GHz Wi-Fi. Pick a 2.4 GHz network on your router.

### The device is offline in the phone app

- Check that the device has power and that your router is working.
- Weak signal causes dropouts. Open the device's Wi-Fi settings to see the signal strength and
  move the device closer to the router if needed.
- If the router name or password changed, set up the Wi-Fi again: the device's settings →
  **Configure Wi-Fi**, or factory reset it and repeat the setup.

### A shared device does not respond

The original Busy Tag has no Wi-Fi. Other people can control it only while it is
plugged into a computer that is running the Busy Tag app.

## Display and designs

### The screen does not change

The device has power but no data connection. See
[The computer does not find Busy Tag](#the-computer-does-not-find-busy-tag).

### A GIF is not shown or is cut short

Busy Tag stores GIFs of up to **1 MB**. The app optimises larger GIFs automatically, which can
lower their quality. Shorter clips, fewer colours and a smaller moving area give better results.

### Which image formats work?

PNG and GIF images (static or animated) and text. In the design editor you can also turn a video
into a GIF. The screen is 240 × 280 pixels; images are scaled to fit or cropped to fill.

## Integrations and focus sessions

### An integration stops updating on my phone

On Android and iOS integrations and focus sessions run only while the app is open and in the
foreground. When the phone locks or you switch apps they pause until you return. For continuous
updates, run them from the desktop app.

### An integration shows an error

Open its settings and check the account or sign-in. Each integration has a
[user guide](/plugins) with its own troubleshooting section.

## Firmware

### The firmware update failed

Run it again with the device connected over USB. If the device no longer starts, follow
[Recover a device that does not start](/updates/firmware#recover-a-device-that-does-not-start).
On a Mac, use the direct installer from [busytag.com/software](https://www.busytag.com/software)
if the Mac App Store version fails.

## General

### Does Busy Tag have a battery?

No. It needs USB power at all times. It works from a USB charger or power bank and then shows the
last design it received.

### Can I use Busy Tag without the app?

Yes. Developers can control it directly over USB with
[AT commands](/hardware/at-commands), the [.NET library or CLI](/developers/tools), or over the
local network with the [HTTP API](/hardware/local-network).

### How many devices can one app manage?

Several. Pick the device to control from the device menu at the top of the app.

### Where do I get more help?

See the [FAQ on busytag.com](https://www.busytag.com/faq) or contact
[hello@busytag.com](mailto:hello@busytag.com).
