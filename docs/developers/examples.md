---
title: Example projects
sidebar_position: 4
description: Open-source Python examples that drive Busy Tag over USB and, on Busy Tag 2, over Wi-Fi.
---

[busytag-python-examples](https://github.com/busy-tag/busytag-python-examples) is a collection of
small open-source Python projects that show Busy Tag in action. They make good starting points
for your own ideas. They work with the current firmware:

| Device | Firmware | Connection |
|:--|:--|:--|
| Busy Tag (hardware 1.0) | 2.x | USB |
| Busy Tag 2 (hardware 2.0) | 3.x | USB, Wi-Fi ([local HTTP API](/hardware/local-network)) |

All examples use one small helper, `busytag.py`, which finds the device, sends
[AT commands](/hardware/at-commands) and uploads pictures. Firmware 2.x and 3.x no longer show up
as a USB drive, so pictures are uploaded with `AT+UF` instead of being copied to a drive.

```python
from busytag import BusyTag, text_image

with BusyTag.connect() as tag:          # finds Busy Tag on USB
    tag.set_color("FF0000")             # all LEDs red
    tag.show_image(text_image("Busy"))  # draw text, upload it and show it
```

:::tip[Before you start]
Close the Busy Tag app while an example runs: only one program can use the serial port at a
time. The [README](https://github.com/busy-tag/busytag-python-examples#getting-started) lists
the setup steps.
:::

## Learning course

Seven short lessons, from switching on one LED to live system data.

| Lesson | What it does |
|:--|:--|
| 1. LED control | Switch on single LEDs with the LED mask |
| 2. LED colour control | LED colours picked from a picture |
| 3. LED pattern control | Build and play a custom LED pattern |
| 4. Text to image | Show your text on the screen |
| 5. LED to ASCII | Draw the current LED state on the screen |
| 6. System uptime | How long the computer has been running |
| 7. System usage | CPU, RAM and GPU load, with the LEDs as a load meter |

## Widgets

| Widget | What it shows | Needs |
|:--|:--|:--|
| Air temperature | Current temperature where you are | – |
| Crypto tracker | Price of a crypto pair, LEDs show the trend | – |
| Moon phase | The moon phase for a date | – |
| Internet speed test | Download and upload speed | – |
| Mouse click counter | A live count of mouse clicks | – |
| Dice roller | A die you roll from a small window | – |
| Pomodoro timer | Work and break countdowns | – |
| YouTube subscribers | A channel's subscriber count | YouTube Data API key |
| Google Calendar | Current and next event, LEDs show busy / soon / free | Google OAuth client |
| Outlook calendar | Current and next event, LEDs show busy / soon / free | Microsoft Entra app registration |
| Spotify now playing | Album art and the track playing | Spotify app client ID |

## Wi-Fi (Busy Tag 2)

**Status light** sets up the local HTTP server once over USB, then switches the device between
Busy, Free and Away from any computer on the same network, without a cable.

---

Several of these ideas are also built into the app as [integrations](/plugins), with no code
needed. To add your own to the app, write a [plugin](/developers/plugin-development); for .NET
projects see the [library and CLI](/developers/tools).
