---
title: Accessibility
sidebar_position: 1
description: How accessible the Busy Tag app is, which assistive features it supports and its known limitations.
---

We want everyone to be able to use Busy Tag. This statement describes the accessibility of the
**Busy Tag app** on Windows, macOS, Android and iOS. It is based on our accessibility
conformance report (VPAT® 2.5) for app version 1.6.5.

## Conformance

| Standard | Status |
|:--|:--|
| WCAG 2.1 Level A | Partially conforms |
| WCAG 2.1 Level AA | Partially conforms |
| Revised Section 508 | Partially conforms |
| EN 301 549 | Partially conforms |

*Partially conforms* means that some parts of the app do not yet fully meet the standard.

## What the app supports

- **Screen readers.** Buttons, images and controls on all pages and dialogs have accessible
  names, and decorative images are hidden from assistive technology. Connection changes and
  progress messages are announced.
- **Headings.** Page titles, section headers and dialog titles are marked as headings.
- **Colour.** The LED colour presets have text labels, so colour is not the only way to tell
  them apart.
- **Text size and orientation.** The app follows the system text-size setting and works in
  portrait and landscape.
- **Languages.** The interface, including accessibility labels, is available in 13 languages.
- **Timing.** The only timed feature, Focus Session, has adjustable durations.
- **No flashing content** in the app above three flashes per second. LED animations on the
  device are chosen by you.

## Known limitations

- **Keyboard navigation** relies on platform defaults; the focus order is not always the visual
  order and focus indicators can be faint.
- Some **secondary text and icons** do not reach the recommended contrast ratios.
- Complex controls such as the **colour picker** and sliders may be hard to operate without a
  pointer or with assistive technology.
- Content you create in the design editor (images on the device) has no text alternative.
- Systematic testing with VoiceOver, TalkBack and Narrator is still in progress.

We are working on these points in upcoming releases.

## The Busy Tag device

This statement covers the app. The device itself is a visual status display; its information is
always also available in the app.

## Feedback and full report

If something in the app is hard to use for you, or you need the full conformance report (VPAT),
contact us at [hello@busytag.com](mailto:hello@busytag.com).
