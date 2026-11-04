---
title: Accessibility Conformance Report (VPAT)
sidebar_label: VPAT report
sidebar_position: 2
description: "VPAT 2.5 accessibility conformance report for the Busy Tag app 1.7.4 (November 2026): WCAG 2.1, Section 508 and EN 301 549."
---

:::info[PDF version]
This report is also available as a [PDF](pathname:///pdf/BusyTag_VPAT.pdf). A plain-language
summary is on the [Accessibility](/about/accessibility) page.
:::

## Busy Tag Application - Accessibility Conformance Report

**Based on VPAT® Version 2.5**

### Product Information

| Field | Details |
|-------|---------|
| **Product Name** | Busy Tag |
| **Product Version** | 1.7.4 |
| **Product Type** | Cross-platform Mobile/Desktop Application |
| **Technology** | .NET MAUI (.NET 10) |
| **Report Date** | November 2026 |
| **Report Version** | 1.9 (Updated for v1.7.4: 13 languages, re-audit of all pages, popups and controls) |
| **Contact** | hello@busytag.com |

### Applicable Standards/Guidelines

This report covers the degree of conformance for the following accessibility standards:

| Standard | Included in Report |
|----------|-------------------|
| Web Content Accessibility Guidelines (WCAG) 2.1 | Level A, AA |
| Revised Section 508 Standards | Yes |
| EN 301 549 Accessibility requirements | Yes |

### Terms

The terms used in the Conformance Level column are defined as follows:

| Term | Definition |
|------|------------|
| **Supports** | The functionality of the product has at least one method that meets the criterion without known defects or meets with equivalent facilitation. |
| **Partially Supports** | Some functionality of the product does not meet the criterion. |
| **Does Not Support** | The majority of product functionality does not meet the criterion. |
| **Not Applicable** | The criterion is not relevant to the product. |
| **Not Evaluated** | The product has not been evaluated against the criterion. |

---

## Platform Support

| Platform | Minimum Version | Status |
|----------|-----------------|--------|
| Windows | 10.0.17763.0+ | Supported |
| macOS (Mac Catalyst) | macOS 12.0+ | Supported |
| Android | 7.0+ (API 24) | Supported |
| iOS | 15.0+ | Supported |

---

## WCAG 2.1 Report

### Table 1: Success Criteria, Level A

| Criteria | Conformance Level | Remarks and Explanations |
|----------|-------------------|--------------------------|
| **1.1.1 Non-text Content** | Partially Supports | Exceptions found in the v1.7.4 audit: the drop-down arrow buttons of the picker controls, the password-visibility button on the Wi-Fi settings page and one button on the plugin configuration page have no accessible name. SemanticProperties.Description added to images and interactive elements on all 20 pages, all 21 popup dialogs, and all 20 custom controls (66 of 79 XAML files, 84% coverage). Decorative elements marked with AutomationProperties.IsInAccessibleTree=False. All accessibility descriptions localized in 13 languages (EN, LV, DE, ES, FR, JA, RU, UK, PL, PT, IT, ET, LT). |
| **1.2.1 Audio-only and Video-only (Prerecorded)** | Not Applicable | Application does not contain prerecorded audio-only or video-only content. |
| **1.2.2 Captions (Prerecorded)** | Not Applicable | Application does not contain prerecorded synchronized media. |
| **1.2.3 Audio Description or Media Alternative (Prerecorded)** | Not Applicable | Application does not contain prerecorded synchronized media. |
| **1.3.1 Info and Relationships** | Partially Supports | SemanticProperties.HeadingLevel (Level1-Level3) added to page titles, section headers, collapsible panels, and popup titles on all pages. All custom controls now have SemanticProperties. AutomationProperties.LabeledBy usage is minimal across the codebase. |
| **1.3.2 Meaningful Sequence** | Partially Supports | Visual layout follows logical sequence, but programmatic reading order not explicitly defined via TabIndex. |
| **1.3.3 Sensory Characteristics** | Partially Supports | Text labels added below color preset buttons in LED page. All icon-only buttons now have SemanticProperties.Description. Some visual indicators may still lack non-visual alternatives. |
| **1.4.1 Use of Color** | Partially Supports | **Phase 1 improvements:** Text labels added below all 8 color preset buttons in LED page (Red, Green, Blue, Yellow, Magenta, Cyan, White, Off). Color is no longer the sole identifier for these controls. Some status indicators in other areas may still rely on color alone. |
| **1.4.2 Audio Control** | Not Applicable | Application does not auto-play audio. |
| **2.1.1 Keyboard** | Partially Supports | Relies on MAUI platform defaults. No custom keyboard navigation implemented. No explicit TabIndex. Complex controls (sliders, color pickers) may not be fully keyboard accessible. |
| **2.1.2 No Keyboard Trap** | Supports | No keyboard traps identified. Users can navigate away from all controls using platform defaults. |
| **2.1.4 Character Key Shortcuts** | Not Applicable | Application does not implement single character key shortcuts. |
| **2.2.1 Timing Adjustable** | Partially Supports | Focus Session (Pomodoro timer) has user-configurable durations. No other time limits identified. |
| **2.2.2 Pause, Stop, Hide** | Supports | Animated content (GIF thumbnails) does not auto-play continuously. User controls playback of animations. |
| **2.3.1 Three Flashes or Below Threshold** | Supports | No content flashes more than three times per second. LED animations are user-controlled. |
| **2.4.1 Bypass Blocks** | Partially Supports | Shell navigation provides section jumping. No skip links or landmark regions explicitly implemented. |
| **2.4.2 Page Titled** | Supports | Each page has a Title property defined (e.g., "Device Settings", "Designs", "LED Control"). |
| **2.4.3 Focus Order** | Does Not Support | No explicit TabIndex or focus order defined. Relies on platform default which may not follow visual order. |
| **2.4.4 Link Purpose (In Context)** | Partially Supports | Navigation items have icons and labels. Some icon-only buttons lack text alternatives. |
| **2.5.1 Pointer Gestures** | Supports | All functionality achievable through single-pointer actions. No complex gestures required. |
| **2.5.2 Pointer Cancellation** | Supports | Standard MAUI button behavior allows cancellation by moving pointer away. |
| **2.5.3 Label in Name** | Supports | SemanticProperties.Description implemented for interactive controls across all 20 pages, 21 popups, and 20 custom controls. 199 accessibility strings plus 759 UI strings (958 total) localized in 13 languages (EN, LV, DE, ES, FR, JA, RU, UK, PL, PT, IT, ET, LT), covering navigation buttons, sliders, ImageButtons, action buttons, tabs, list items, pickers, form fields, error messages, and status text. |
| **2.5.4 Motion Actuation** | Not Applicable | Application does not use device motion for functionality. |
| **3.1.1 Language of Page** | Partially Supports | Application supports 13 languages (EN, LV, DE, ES, FR, JA, RU, UK, PL, PT, IT, ET, LT) via localization. All 199 accessibility strings and 759 UI/error message strings (958 total) are localized in all supported languages. Language not explicitly declared for assistive technology at the platform level. |
| **3.2.1 On Focus** | Supports | Focus changes do not initiate unexpected changes of context. |
| **3.2.2 On Input** | Supports | Form input changes do not automatically cause context changes without user confirmation. |
| **3.3.1 Error Identification** | Partially Supports | Error messages displayed for connection failures, firmware updates, Wi-Fi setup, and invalid inputs. All error messages are localized in 13 languages. Errors may not be programmatically associated with fields. |
| **3.3.2 Labels or Instructions** | Partially Supports | Some form fields have visible labels. Instructions provided for device setup. Not all labels are programmatically associated. |
| **4.1.1 Parsing** | Supports | XAML markup is well-formed and validates correctly. |
| **4.1.2 Name, Role, Value** | Partially Supports | SemanticProperties and AutomationProperties implemented across all pages, popups, and custom controls. Interactive elements have accessible names via SemanticProperties.Description, with the exceptions listed below. Decorative elements marked with AutomationProperties.IsInAccessibleTree=False. Overall coverage: 66 of 79 XAML files (84%). Exceptions: several toggles and a slider in the device status-overlay settings, the Wi-Fi mode picker and toggle, and two check boxes have no accessible name. Remaining files without accessibility are non-interactive components, tab content sub-pages, and resource/style files. |

### Table 2: Success Criteria, Level AA

| Criteria | Conformance Level | Remarks and Explanations |
|----------|-------------------|--------------------------|
| **1.3.4 Orientation** | Supports | Application supports both portrait and landscape orientations. No content restricted to single orientation. |
| **1.3.5 Identify Input Purpose** | Does Not Support | Input fields do not specify autocomplete purpose or input type semantics for assistive technology. |
| **1.4.3 Contrast (Minimum)** | Partially Supports | Primary text (Gray900 #131114) on white backgrounds meets 4.5:1. Some secondary colors (Gray100 #C4BCCC) may not meet contrast requirements. |
| **1.4.4 Resize Text** | Partially Supports | Relies on platform text scaling settings. Custom font sizes used but may not scale proportionally in all cases. |
| **1.4.5 Images of Text** | Supports | Application uses system fonts. Logo and branding are only instances of text in images. |
| **1.4.10 Reflow** | Partially Supports | Responsive layouts using Grid and FlexLayout. OnIdiom conditionals for different screen sizes. Some fixed-size elements may not reflow optimally. |
| **1.4.11 Non-text Contrast** | Partially Supports | UI components have visible borders. Some icons may not meet 3:1 contrast ratio against backgrounds. |
| **1.4.12 Text Spacing** | Not Evaluated | Text spacing adjustments via platform accessibility settings not tested. |
| **1.4.13 Content on Hover or Focus** | Partially Supports | Tooltips appear on hover but may not be keyboard accessible. Tooltips do not persist on hover. |
| **2.4.5 Multiple Ways** | Supports | Multiple navigation methods: Shell flyout menu, tab navigation, direct page links. |
| **2.4.6 Headings and Labels** | Partially Supports | Pages have visible titles. Section headers present but may not be programmatically identified as headings. |
| **2.4.7 Focus Visible** | Partially Supports | Platform default focus indicators used. No custom focus styling implemented. May not be sufficiently visible on all platforms. |
| **3.1.2 Language of Parts** | Not Applicable | Application content is in single language per localization setting. |
| **3.2.3 Consistent Navigation** | Supports | Navigation structure consistent across all pages via AppShell. |
| **3.2.4 Consistent Identification** | Supports | Icons and controls used consistently throughout application. Same icons for same functions. |
| **3.3.3 Error Suggestion** | Partially Supports | Some error messages provide suggestions (e.g., device connection). Not all error scenarios provide remediation guidance. |
| **3.3.4 Error Prevention (Legal, Financial, Data)** | Supports | Confirmation dialogs for destructive actions (delete designs). No legal/financial transactions. |
| **4.1.3 Status Messages** | Partially Supports | SemanticScreenReader.Announce() implemented for connection state changes and progress/warning status updates. Status messages are announced to screen readers when connection state changes or file transfer progress updates occur. |

---

## Revised Section 508 Report

### Chapter 3: Functional Performance Criteria

| Criteria | Conformance Level | Remarks and Explanations |
|----------|-------------------|--------------------------|
| **302.1 Without Vision** | Partially Supports | SemanticProperties.Description implemented on all pages, popups, and controls. SemanticScreenReader.Announce() provides dynamic status announcements. Systematic screen reader testing (VoiceOver, TalkBack, Narrator) has not yet been performed. |
| **302.2 With Limited Vision** | Partially Supports | Supports platform text scaling. Some contrast issues exist. No magnification features beyond platform zoom. |
| **302.3 Without Perception of Color** | Partially Supports | Text labels added to color preset buttons. Some status indicators may still rely on color alone. |
| **302.4 Without Hearing** | Supports | Application is primarily visual. No audio-only content. Notifications are visual. |
| **302.5 With Limited Hearing** | Not Applicable | No audio content requiring hearing. |
| **302.6 Without Speech** | Supports | Application does not require speech input. |
| **302.7 With Limited Manipulation** | Partially Supports | Touch targets generally adequate. Some precision required for color pickers and sliders. Keyboard alternatives not fully implemented. |
| **302.8 With Limited Reach and Strength** | Supports | Application does not require simultaneous actions or physical strength. |
| **302.9 With Limited Language, Cognitive, and Learning Abilities** | Partially Supports | Clear iconography and simple navigation. Complex features (design editor) may require learning. Help section available. |

### Chapter 4: Hardware

Not Applicable - Busy Tag is a software application. Hardware accessibility for the physical Busy Tag device is outside scope of this report.

### Chapter 5: Software

| Criteria | Conformance Level | Remarks and Explanations |
|----------|-------------------|--------------------------|
| **501.1 Scope** | Applicable | Software application on multiple platforms. |
| **502.2.1 User Control of Accessibility Features** | Supports | Application does not override platform accessibility settings. |
| **502.2.2 No Disruption of Accessibility Features** | Supports | Application does not disrupt platform screen readers or accessibility features. |
| **502.3.1 Object Information** | Partially Supports | SemanticProperties and AutomationProperties provide role and name information for all pages, popups, and controls. State and boundary information may not be fully exposed for all custom controls. |
| **502.3.2 Modification of Object Information** | Does Not Support | Screen readers cannot modify accessible values. No accessibility API integration. |
| **502.3.3 Row, Column, and Headers** | Not Applicable | Application does not use data tables. |
| **502.3.4 Values** | Partially Supports | Slider values exposed via AutomationProperties. Picker values may not be fully exposed. |
| **502.3.5 Modification of Values** | Does Not Support | Values cannot be modified via assistive technology. |
| **502.3.6 Label Relationships** | Partially Supports | AutomationProperties.LabeledBy implemented for many controls. Not all label relationships established. |
| **502.3.7 Hierarchical Relationships** | Partially Supports | MAUI framework exposes basic hierarchy. Custom component hierarchy may not be fully exposed. |
| **502.3.8 Text** | Partially Supports | Text content readable. Text attributes (font, size) may not be fully exposed. |
| **502.3.9 Modification of Text** | Supports | Entry and Editor controls allow text modification. |
| **502.3.10 List of Actions** | Does Not Support | Available actions not exposed to assistive technology. |
| **502.3.11 Actions on Objects** | Does Not Support | Actions cannot be executed via accessibility API. |
| **502.3.12 Focus Cursor** | Partially Supports | Platform default focus management. Custom focus order not implemented. |
| **502.3.13 Modification of Focus Cursor** | Partially Supports | Platform allows focus modification. No custom focus management. |
| **502.3.14 Event Notification** | Partially Supports | SemanticScreenReader.Announce() provides announcements for connection state changes and progress/warning status updates. Not all UI changes are announced. |
| **502.4 Platform Accessibility Features** | Partially Supports | Uses MAUI framework accessibility support. Application-level implementation covers SemanticProperties and AutomationProperties across all pages and controls, with SemanticScreenReader.Announce() for dynamic updates. Not all platform accessibility APIs are utilized. |
| **503.2 User Preferences** | Supports | Respects platform accessibility preferences (text size, high contrast). |
| **503.3 Alternative User Interfaces** | Not Applicable | No alternative interfaces provided. |
| **503.4 User Controls for Captions and Audio Description** | Not Applicable | No synchronized media content. |

### Chapter 6: Support Documentation and Services

| Criteria | Conformance Level | Remarks and Explanations |
|----------|-------------------|--------------------------|
| **602.2 Accessibility and Compatibility Features** | Does Not Support | Documentation does not describe accessibility features. |
| **602.3 Electronic Support Documentation** | Partially Supports | Help section uses WebView. External documentation accessibility depends on web content. |
| **602.4 Alternate Formats for Non-Electronic Support Documentation** | Not Applicable | All documentation is electronic. |
| **603.2 Information on Accessibility and Compatibility Features** | Does Not Support | No accessibility feature documentation available. |
| **603.3 Accommodation of Communication Needs** | Not Evaluated | Support channels not evaluated for accessibility. |

---

## EN 301 549 Report

### Chapter 5: Generic Requirements

| Criteria | Conformance Level | Remarks and Explanations |
|----------|-------------------|--------------------------|
| **5.2 Activation of Accessibility Features** | Supports | Application does not block platform accessibility feature activation. |
| **5.3 Biometrics** | Not Applicable | Application does not use biometric identification. |
| **5.4 Preservation of Accessibility Information** | Partially Supports | User-created content (designs) may not preserve accessibility information. |
| **5.5.1 Means of Operation** | Supports | Controls operable without requiring specific body part beyond touch or standard input. |
| **5.5.2 Operable Parts Discernibility** | Partially Supports | Interactive elements visually distinguishable. May not be discernible by non-sighted users. |
| **5.6.1 Tactile or Auditory Status** | Not Applicable | Software application; no hardware status indicators. |
| **5.6.2 Visual Status** | Supports | Connection status, sync status visually indicated. |
| **5.7 Key Repeat** | Not Applicable | Uses platform keyboard settings. |
| **5.8 Double-strike Key Acceptance** | Not Applicable | Uses platform keyboard settings. |
| **5.9 Simultaneous User Actions** | Supports | No simultaneous input required for basic operation. |

### Chapter 11: Software

| Criteria | Conformance Level | Remarks and Explanations |
|----------|-------------------|--------------------------|
| **11.1.1.1 Non-text Content** | Supports | See WCAG 1.1.1 |
| **11.1.2.1-11.1.2.5 Time-based Media** | Not Applicable | No time-based media content. |
| **11.1.3.1 Info and Relationships** | Partially Supports | See WCAG 1.3.1 |
| **11.1.3.2 Meaningful Sequence** | Partially Supports | See WCAG 1.3.2 |
| **11.1.3.3 Sensory Characteristics** | Partially Supports | See WCAG 1.3.3 |
| **11.1.3.4 Orientation** | Supports | See WCAG 1.3.4 |
| **11.1.3.5 Identify Input Purpose** | Does Not Support | See WCAG 1.3.5 |
| **11.1.4.1 Use of Color** | Partially Supports | See WCAG 1.4.1 |
| **11.1.4.3 Contrast (Minimum)** | Partially Supports | See WCAG 1.4.3 |
| **11.1.4.4 Resize Text** | Partially Supports | See WCAG 1.4.4 |
| **11.1.4.5 Images of Text** | Supports | See WCAG 1.4.5 |
| **11.1.4.10 Reflow** | Partially Supports | See WCAG 1.4.10 |
| **11.1.4.11 Non-text Contrast** | Partially Supports | See WCAG 1.4.11 |
| **11.1.4.12 Text Spacing** | Not Evaluated | See WCAG 1.4.12 |
| **11.1.4.13 Content on Hover or Focus** | Partially Supports | See WCAG 1.4.13 |
| **11.2.1.1 Keyboard** | Partially Supports | See WCAG 2.1.1 |
| **11.2.1.2 No Keyboard Trap** | Supports | See WCAG 2.1.2 |
| **11.2.1.4 Character Key Shortcuts** | Not Applicable | See WCAG 2.1.4 |
| **11.2.2.1 Timing Adjustable** | Partially Supports | See WCAG 2.2.1 |
| **11.2.2.2 Pause, Stop, Hide** | Supports | See WCAG 2.2.2 |
| **11.2.3.1 Three Flashes or Below Threshold** | Supports | See WCAG 2.3.1 |
| **11.2.4.3 Focus Order** | Does Not Support | See WCAG 2.4.3 |
| **11.2.4.4 Link Purpose** | Partially Supports | See WCAG 2.4.4 |
| **11.2.4.6 Headings and Labels** | Partially Supports | See WCAG 2.4.6 |
| **11.2.4.7 Focus Visible** | Partially Supports | See WCAG 2.4.7 |
| **11.2.5.1 Pointer Gestures** | Supports | See WCAG 2.5.1 |
| **11.2.5.2 Pointer Cancellation** | Supports | See WCAG 2.5.2 |
| **11.2.5.3 Label in Name** | Supports | See WCAG 2.5.3 |
| **11.2.5.4 Motion Actuation** | Not Applicable | See WCAG 2.5.4 |
| **11.3.1.1 Language of Software** | Partially Supports | See WCAG 3.1.1 |
| **11.3.2.1 On Focus** | Supports | See WCAG 3.2.1 |
| **11.3.2.2 On Input** | Supports | See WCAG 3.2.2 |
| **11.3.3.1 Error Identification** | Partially Supports | See WCAG 3.3.1 |
| **11.3.3.2 Labels or Instructions** | Partially Supports | See WCAG 3.3.2 |
| **11.3.3.3 Error Suggestion** | Partially Supports | See WCAG 3.3.3 |
| **11.3.3.4 Error Prevention** | Supports | See WCAG 3.3.4 |
| **11.4.1.1 Parsing** | Supports | See WCAG 4.1.1 |
| **11.4.1.2 Name, Role, Value** | Partially Supports | See WCAG 4.1.2 |
| **11.4.1.3 Status Messages** | Partially Supports | See WCAG 4.1.3 |
| **11.5.2.1-11.5.2.17 Accessibility Services** | Partially Supports | SemanticProperties and AutomationProperties provide accessibility service support across 66 of 79 XAML files (84% coverage). 199 accessibility strings plus 759 UI strings (958 total) localized in 13 languages. SemanticScreenReader.Announce() provides dynamic announcements. Full platform accessibility API integration is not complete for all scenarios. |
| **11.6.2 No Disruption of Accessibility Features** | Supports | Application does not disrupt platform accessibility. |
| **11.7 User Preferences** | Supports | Respects platform preferences for text size and display settings. |
| **11.8.1-11.8.5 Authoring Tools** | Partially Supports | Design editor creates visual content. No accessibility features for created content. |

---

## Summary

### Overall Conformance Assessment

| Standard | Level | Conformance |
|----------|-------|-------------|
| WCAG 2.1 | Level A | Partial Conformance (Phase 1-4 + Localization Complete) |
| WCAG 2.1 | Level AA | Partial Conformance |
| Section 508 | - | Partial Conformance |
| EN 301 549 | - | Partial Conformance |

### Accessibility Coverage Summary

- **XAML Coverage**: 66 of 79 files (84%) - all 20 pages, 21 popups, 20 custom controls
- **Accessibility Strings**: 199 (Acc_* prefixed) localized in 13 languages
- **Total Localized Strings**: 958 across all 13 languages (EN, LV, DE, ES, FR, JA, RU, UK, PL, PT, IT, ET, LT)
- **Dynamic Announcements**: SemanticScreenReader.Announce() for connection state and progress updates
- **Decorative Elements**: Marked with AutomationProperties.IsInAccessibleTree=False

### Remaining Accessibility Gaps

1. **Unnamed Controls**: A few icon buttons, toggles and check boxes have no accessible name (see 1.1.1 and 4.1.2)
2. **Keyboard Navigation**: No explicit TabIndex defined for custom tab order
3. **Focus Visible**: No custom focus styling; relies on platform defaults
4. **Screen Reader Testing**: Systematic testing with VoiceOver, TalkBack, and Narrator not yet performed
5. **Skip Links**: No skip navigation links implemented

### Recommendations for Remediation

#### Priority 1 (High)
1. Define `TabIndex` for logical keyboard navigation order
2. Implement visible focus indicators
3. Ensure color contrast meets WCAG 4.5:1 for all text
4. Complete `AutomationProperties.LabeledBy` for all form controls

#### Priority 2 (Medium)
1. Test with actual screen readers (VoiceOver, TalkBack, Narrator)
2. Add keyboard shortcuts for common actions
3. Create user-facing accessibility documentation
4. Add skip navigation links

#### Priority 3 (Enhancement)
1. Add high contrast theme option
2. Implement reduced motion preferences
3. Add voice control support
4. Create accessibility statement

---

## Legal Disclaimer

This document is provided for informational purposes and reflects an accessibility assessment at a point in time. Conformance levels are based on evaluation against stated standards and may change with product updates. This VPAT does not constitute legal advice or guarantee compliance with any accessibility laws or regulations.

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | December 2024 | Generated Assessment | Initial VPAT creation |
| 1.1 | December 2024 | Phase 1 Implementation | Added accessibility to AppShell, DeviceSettings, LedPage, NavButton, CustomTabView, TabItemView. |
| 1.2 | December 2024 | Phase 2 Implementation | Added accessibility to secondary pages and gallery/plugin templates. |
| 1.3 | December 2024 | Phase 3 Implementation | Added accessibility to SettingsPage, HsvColorPicker, and all 11 popup dialogs. |
| 1.4 | March 2026 | VPAT 2.5 Reformat | Updated to v1.4.8. Reformatted to VPAT 2.5 Rev INT. Full codebase audit of 63 XAML files. |
| 1.5 | March 2026 | Phase 4 | Added SemanticProperties to all remaining pages and controls. SemanticScreenReader.Announce() for dynamic status. Localized 197 accessibility strings in EN and LV. Coverage increased to 73%. |
| 1.6 | March 2026 | Localization Expansion | Added DE, ES, FR, JA localizations. All 197 accessibility strings in 6 languages. Coverage increased to 78% (49/63 XAML files). |
| 1.7 | March 2026 | v1.5.0 Update | Added 112 localized UI/error message strings (807 total). Covered firmware updates, QR/Wi-Fi setup, device setup, LED control, plugins. Improved exception handling and firmware logic. Added WiX Burn bootstrapper for Windows installer. |
| 1.9 | November 2026 | v1.7.4 Update | Re-audit of the v1.7.4 release: 79 XAML files, 66 with accessibility properties (84%) - all 20 pages, 21 popup dialogs and 20 custom controls. 199 accessibility strings and 958 strings in total, localized in 13 languages (added RU, UK, PL, PT, IT, ET, LT). New UI audited: Video to GIF, design import from link, integration playlist countdown, plugin sign-in. 1.1.1 lowered to Partially Supports for unnamed icon buttons found in the audit. Platform minimums corrected (Android 7.0, macOS 12). |
| 1.8 | July 2026 | v1.6.5 Update | Re-audit for new UI added since v1.5.0: Wi-Fi setup flow (WifiSetupPage, WiFiSettingsPage, WifiScanPopup), device management (MyDevicesPage), floating device preview, developer logs, and new design/plugin popups (SaveAsNewDesign, ShareDesign, DuplicateImport, DesignsMoreOptions, InstallPlugin, PluginTemplateContextMenu) plus PaginationControl. Added missing SemanticProperties to SaveAsNewDesignPopup and PaginationControl with 4 new accessibility strings (192 total, 925 overall) in all 6 languages. Coverage: 62 of 76 XAML files (82%) - all pages, popups, and custom controls covered. |

---

*This VPAT was created based on the ITI VPAT® Version 2.5 template. VPAT® is a registered trademark of the Information Technology Industry Council (ITI).*
