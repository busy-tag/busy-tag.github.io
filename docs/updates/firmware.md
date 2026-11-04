---
title: Firmware updates
sidebar_position: 1
description: Check the firmware version, update Busy Tag's firmware and recover a device that no longer starts.
---

The firmware is the software that runs inside Busy Tag. Updates add features and fix problems,
so keep it current. Updates are installed by the Busy Tag app on **Windows or macOS** over USB.

## Firmware versions

| Firmware | Devices | What it adds |
|:--|:--|:--|
| 2.x | Busy Tag models without Wi-Fi | Screen, LEDs, file storage and the USB [AT command set](/hardware/at-commands-v2). |
| 3.x | Busy Tag models with Wi-Fi (hardware 2.0) | Everything in 2.x plus Wi-Fi, cloud control from the phone app, device sharing without a computer, the on-screen setup QR code, the status toolbar and the [local network API](/hardware/local-network). See the [3.x command manual](/hardware/at-commands). |

A device cannot move between these lines: each one matches its hardware.

## Check your version

Open Settings → your device. Under **Device firmware** the app shows the **Current firmware
version** and the **Newest firmware version**. If a newer version exists, the app also tells you
so when you open the device settings.

Over USB you can also ask the device itself with the AT command `AT+GFV`.

## Update the firmware

1. Connect Busy Tag to a Windows or macOS computer with a USB-C **data** cable.
2. Open the Busy Tag app, go to Settings and select the device.
3. Under **Device firmware** click **Upgrade firmware** (or **Update** in the
   "new firmware version is available" message).
4. Wait. The device shows an update screen while the app uploads the firmware, then installs it
   and restarts. Do not unplug it.
5. When the app reports that the firmware was updated, let the device restart. It reconnects by
   itself.

:::warning[Keep it plugged in]
Unplugging the device or closing the app during the update interrupts it. If that happens, wait
for the device to restart and run the update again. If it no longer starts at all, use
[device recovery](#recover-a-device-that-does-not-start).
:::

:::note[Phones and the Mac App Store version]
Firmware updates over Wi-Fi are not supported yet, so the phone apps cannot install firmware.
The Mac App Store version uploads firmware slowly; if an update fails there, use the direct
installer from [busytag.com/software](https://www.busytag.com/software).
:::

## Recover a device that does not start

If an update was interrupted and the device no longer starts, the desktop app can erase it and
install the firmware again. This deletes everything stored on the device.

1. Unplug the USB cable.
2. Press and hold the **BOOT/RESET** button on the device.
3. Plug the USB cable in while you keep holding the button, then release it. The device is now
   in *boot mode*; its screen stays dark.
4. In the app open Settings → **Device recovery**. The device appears in the list.
5. Click **Recover Device** and confirm. The app detects the hardware, erases the flash and
   installs the firmware.
6. When it reports success, unplug the cable and plug it in again.

Device recovery uses the `esptool` utility. If the app cannot find it, it asks you to install
Python (with pip) or Homebrew so it can install `esptool` itself.

The [Busy Tag CLI](/developers/tools#busy-tag-cli) can do the same with `busytag-cli recover`.
