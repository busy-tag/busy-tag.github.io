---
title: Technical specifications
sidebar_label: Specifications
sidebar_position: 0
description: Size, screen, LEDs, connectivity and power of the Busy Tag device.
---

## At a glance

| | |
|:--|:--|
| Screen | Colour LCD, 240 × 280 pixels; shows PNG and animated GIF images |
| LEDs | RGB LED bar with 7 individually addressable LEDs, solid colours and animated patterns |
| Processor | Espressif ESP32-S3, dual-core 240 MHz |
| Storage | Internal flash with a FAT file system for images and settings; GIFs up to 1 MB |
| Connection | USB-C (USB serial / CDC). Wi-Fi models: also Wi-Fi 802.11 b/g/n, 2.4 GHz |
| Power | 5 V over USB-C from a computer, charger, hub or power bank. No battery |
| Size and weight | 36 × 46 × 8 mm, 20 g |
| Mounting | Double-sided magnets included |
| Buttons | BOOT/RESET button, reachable through a small hole on the back |
| Sensors | Internal chip temperature |

## Models

Busy Tag exists with and without Wi-Fi. Both have the same screen and LEDs; the firmware tells
them apart.

| | Without Wi-Fi | With Wi-Fi (hardware 2.0) |
|:--|:--|:--|
| Firmware | 2.x | 3.x |
| Controlled from | Desktop app over USB | Desktop app over USB, phone app over Wi-Fi |
| Phone app | Only while plugged into a computer running the app | Directly, through the Busy Tag cloud |
| Local network API | – | [HTTP API](/hardware/local-network) |
| Command reference | [AT commands 2.x](/hardware/at-commands-v2) | [AT commands 3.x](/hardware/at-commands) |

To see which one you have, open the device's settings in the app: the firmware version is shown
under **Device firmware**, and Wi-Fi models have a **Wi-Fi** section.

## USB identification

The device enumerates as a USB CDC serial port with vendor ID `303A` and product ID `81DF`. It
appears as `COMx` on Windows and `/dev/cu.usbmodem…` on macOS. See the
[AT Command Manual](/hardware/at-commands) for the protocol.

## In the box

The device and double-sided magnets. Newer packages also include a USB-C data cable; any
standard USB-C cable that carries data works.
