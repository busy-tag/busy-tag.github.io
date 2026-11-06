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

All examples use one small helper, [`busytag.py`](https://github.com/busy-tag/busytag-python-examples/blob/main/busytag.py), which finds the device, sends
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
| [1. LED control](https://github.com/busy-tag/busytag-python-examples/blob/main/learning-course/01_led_control.py) | Switch on single LEDs with the LED mask |
| [2. LED colour control](https://github.com/busy-tag/busytag-python-examples/blob/main/learning-course/02_led_color_control.py) | LED colours picked from a picture |
| [3. LED pattern control](https://github.com/busy-tag/busytag-python-examples/blob/main/learning-course/03_led_pattern_control.py) | Build and play a custom LED pattern |
| [4. Text to image](https://github.com/busy-tag/busytag-python-examples/blob/main/learning-course/04_text_to_image.py) | Show your text on the screen |
| [5. LED to ASCII](https://github.com/busy-tag/busytag-python-examples/blob/main/learning-course/05_led_to_ascii.py) | Draw the current LED state on the screen |
| [6. System uptime](https://github.com/busy-tag/busytag-python-examples/blob/main/learning-course/06_system_uptime.py) | How long the computer has been running |
| [7. System usage](https://github.com/busy-tag/busytag-python-examples/blob/main/learning-course/07_system_usage.py) | CPU, RAM and GPU load, with the LEDs as a load meter |

## Widgets

| Widget | What it shows | Needs |
|:--|:--|:--|
| [Air temperature](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/air_temperature.py) | Current temperature where you are | – |
| [Crypto tracker](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/crypto_tracker.py) | Price of a crypto pair, LEDs show the trend | – |
| [Moon phase](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/moon_phase.py) | The moon phase for a date | – |
| [Internet speed test](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/internet_speed_test.py) | Download and upload speed | – |
| [Mouse click counter](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/mouse_click_counter.py) | A live count of mouse clicks | – |
| [Dice roller](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/dice_roller.py) | A die you roll from a small window | – |
| [Pomodoro timer](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/pomodoro_timer.py) | Work and break countdowns | – |
| [YouTube subscribers](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/youtube_subscribers.py) | A channel's subscriber count | YouTube Data API key |
| [Google Calendar](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/google_calendar.py) | Current and next event, LEDs show busy / soon / free | Google OAuth client |
| [Outlook calendar](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/outlook_calendar.py) | Current and next event, LEDs show busy / soon / free | Microsoft Entra app registration |
| [Spotify now playing](https://github.com/busy-tag/busytag-python-examples/blob/main/widgets/spotify_now_playing.py) | Album art and the track playing | Spotify app client ID |

## Wi-Fi (Busy Tag 2)

**[Status light](https://github.com/busy-tag/busytag-python-examples/blob/main/wifi/status_light.py)** sets up the local HTTP server once over USB, then switches the device between
Busy, Free and Away from any computer on the same network, without a cable.

---

Several of these ideas are also built into the app as [integrations](/plugins), with no code
needed. To add your own to the app, write a [plugin](/developers/plugin-development); for .NET
projects see the [library and CLI](/developers/tools).
