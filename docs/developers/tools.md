---
title: Library and command-line tool
sidebar_label: Library & CLI
sidebar_position: 3
description: Control Busy Tag from your own code with the BusyTag.Lib .NET library, or from a terminal with busytag-cli.
---

Busy Tag can be controlled without the app. Over USB the device speaks a text protocol of
[AT commands](/hardware/at-commands), so any language with serial-port access works. Two
open-source tools save you the work.

## BusyTag.Lib (.NET)

[busytag-lib on GitHub](https://github.com/busy-tag/busytag-lib) ·
[NuGet package](https://www.nuget.org/packages/BusyTag.Lib/) · MIT licence

The .NET library the Busy Tag app itself is built on. It finds devices, talks to them over
USB, transfers files with progress events, controls LEDs and patterns, scans Wi-Fi networks,
connects to the Busy Tag cloud and can recover a device in boot mode.

```bash
dotnet add package BusyTag.Lib
```

```csharp
using BusyTag.Lib;

using var manager = new BusyTagManager();
var ports = await manager.FindBusyTagDevice();
if (ports?.Any() == true)
{
    var device = new BusyTagDevice(ports.First());
    await device.Connect();
    Console.WriteLine($"{device.DeviceName}, firmware {device.FirmwareVersion}");
}
```

Runs on .NET 8 and 9 on Windows 10 (1903) or later and macOS 10.15 or later. Linux support is
experimental (`EnableExperimentalLinuxSupport = true`; your user must be in the `dialout` group).
The README has the full API and the changelog.

## Busy Tag CLI

[busytag-cli on GitHub](https://github.com/busy-tag/busytag-cli) ·
[NuGet .NET tool](https://www.nuget.org/packages/BusyTag.CLI) · MIT licence

A command-line tool for scripts, build lights and quick checks. Without arguments it starts an
interactive menu.

```bash
# macOS (Homebrew)
brew tap busy-tag/busytag
brew install busytag-cli

# Windows, macOS, Linux (.NET 8 or later)
dotnet tool install -g BusyTag.CLI
```

| Command | Example |
|:--|:--|
| Find devices | `busytag-cli scan` |
| Device information | `busytag-cli info COM3` |
| Set a colour (name, hex or RGB, optional brightness) | `busytag-cli color COM3 red 75` |
| Play an LED pattern (count 1–254, 255 = forever) | `busytag-cli pattern COM3 "Police 1" 3` |
| Upload and show an image | `busytag-cli upload COM3 busy.png` then `busytag-cli show COM3 busy.png` |
| List files, storage | `busytag-cli files COM3`, `busytag-cli storage COM3` |
| Recover a device in boot mode | `busytag-cli recover COM5` |

On macOS the port looks like `/dev/cu.usbmodem…`; `busytag-cli scan` prints it.

## Other languages

Open the serial port and send AT commands terminated with `\r\n`. The
[AT Command Manual](/hardware/at-commands#programming-example) has complete Python, C# and Swift
examples. Busy Tag 2 can also be controlled over HTTP on the local network; see the
[Local Network Guide](/hardware/local-network).
