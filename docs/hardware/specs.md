---
title: Technical specifications
sidebar_label: Specifications
sidebar_position: 0
description: Size, screen, LEDs, connectivity and power of the Busy Tag device.
---

## At a glance

| Feature | Details |
|:--|:--|
| Screen | Colour LCD, 240 × 280 pixels; shows PNG and animated GIF images |
| LEDs | RGB LED bar with 7 individually addressable LEDs, solid colours and animated patterns |
| Processor | Espressif ESP32-S3, dual-core 240 MHz: ESP32-S3-MINI module (Busy Tag) or ESP32-S3-WROOM module (Busy Tag 2) |
| Storage | Internal flash with a FAT file system for images and settings; GIFs up to 1 MB |
| Connection | USB-C (USB serial / CDC). Busy Tag 2: also Wi-Fi 802.11 b/g/n, 2.4 GHz |
| Power | 5 V over USB-C from a computer, charger, hub or power bank. No battery |
| Size and weight | 36 × 46 × 8 mm, 20 g (both models) |
| Mounting | Double-sided magnets included |
| Buttons | BOOT/RESET button, reachable through a small hole on the back |
| Sensors | Internal chip temperature |

## Models

There are two models: the original **Busy Tag** (hardware 1.0) and **Busy Tag 2** (hardware
2.0). They have the same size, screen and LEDs; they differ in the ESP32-S3 module and in what the
firmware does with it.

| Feature | Busy Tag (hardware 1.0) | Busy Tag 2 (hardware 2.0) |
|:--|:--|:--|
| Module | ESP32-S3-MINI | ESP32-S3-WROOM |
| Wi-Fi | Not used by the firmware | Yes, 2.4 GHz |
| Firmware | 2.x | 3.x |
| Controlled from | Desktop app over USB | Desktop app over USB, phone app over Wi-Fi |
| Phone app | Only while plugged into a computer running the app | Directly, through the Busy Tag cloud |
| Local network API | – | [HTTP API](/hardware/local-network) |
| Command reference | [AT commands 2.x](/hardware/at-commands-v2) | [AT commands 3.x](/hardware/at-commands) |

To see which one you have, open the device's settings in the app: the firmware version is shown
under **Device firmware** (2.x on Busy Tag, 3.x on Busy Tag 2), and Busy Tag 2 has a **Wi-Fi**
section. Over USB, `AT+GHV` returns the hardware version (`2.0` on Busy Tag 2).

## USB identification

The device enumerates as a USB CDC serial port with vendor ID `303A` and product ID `81DF`. It
appears as `COMx` on Windows and `/dev/cu.usbmodem…` on macOS. See the
[AT Command Manual](/hardware/at-commands) for the protocol.

## In the box

- **Busy Tag 2:** the device, double-sided magnets and a USB-C data cable.
- **Busy Tag:** the device and double-sided magnets; the USB-C cable is sold separately.

Any standard USB-C cable that carries data works.
