---
title: Connect your Busy Tag
sidebar_position: 2
description: Connect Busy Tag over USB to a computer, or set it up on Wi-Fi from your phone.
---

Busy Tag is powered over USB-C and always needs a power source: a computer, a USB charger, a
USB hub or a power bank. How the app talks to it depends on where you run the app.

| You use the app on | Connection | Works with |
|:--|:--|:--|
| Windows or macOS | **USB** cable to the computer | Every Busy Tag |
| Android or iOS | **Wi-Fi**, through the Busy Tag cloud | Wi-Fi models (firmware 3.0 or later) |

:::tip[Use a data cable]
Some USB-C cables only carry power. With such a cable the device lights up but the app never
finds it. If your computer does not detect Busy Tag, try another cable first.
:::

## On a computer (USB)

1. Install and open the Busy Tag app.
2. Plug Busy Tag into the computer with a USB-C data cable.
3. The app finds the device automatically. Its name and **Connected via USB** appear in the
   device menu at the top of the app.

If the app reports that the port **is in use by another application**, close the other program
that has the serial port open (a serial terminal, the Arduino IDE or a second Busy Tag window).
The device reconnects by itself.

## On a phone or tablet (Wi-Fi)

A new Wi-Fi Busy Tag starts its own small Wi-Fi network and shows a **QR code** on its screen.
The app uses it to hand the device your home Wi-Fi details.

1. Power on Busy Tag. The QR code appears on its display.
2. In the app open Settings → **Add device** and choose **Scan Device QR Code**.
3. Scan the QR code on the device. The phone joins the device's Wi-Fi.
4. Enter your router's Wi-Fi name and password, or pick the network from the list the device
   found, and tap **Configure Device**.
5. The device joins your network and registers with the Busy Tag cloud. Wait for
   **Configuration Complete!**

From then on your phone controls the device over the internet, so it does not need to be on the
same network.

:::note[No QR code on the display?]
A device that was already set up does not show the QR code. Press and hold its reset button for
**3 seconds** to factory reset it; the QR code comes back.
:::

:::note[Android]
If the phone refuses to stay on the device's Wi-Fi ("no internet"), turn off mobile data during
setup and try again.
:::

## Change the Wi-Fi network later

Open the device's settings (Settings → your device) and tap **Configure Wi-Fi**. You can pick a
new network or switch the mode:

| Mode | What it does |
|:--|:--|
| Connect to Wi-Fi network | Joins your router (normal use). |
| Hotspot only | Only the device's own Wi-Fi network, no internet. |
| Network + hotspot | Joins your router and keeps its own network available. |
| Off | Wi-Fi off; use USB only. |

Wi-Fi settings need firmware 3.0 or later.

## Share a device with someone else

The owner of a device can let other people control it from their own app:

1. **Owner:** open the device's settings and tap **Share Device**. The app shows a QR code and a
   **Copy link** button. The link expires after a while.
2. **Other person:** in Settings → **Add device** choose **Add Shared Device**, then scan the QR
   code (phone) or paste the link (computer).

:::info
A device with firmware older than 3.0 has no Wi-Fi. It can still be shared, but only while it is
plugged into a computer that is running the Busy Tag app.
:::

## Remove a device

In the device's settings, **Disconnect** removes the device and **factory resets** it: its Wi-Fi
details and settings are erased and it restarts. This cannot be undone.

## Next step

[Learn your way around the app →](/getting-started/using-the-app)
