# homelab-usb-device-tracker

Homelabs accumulate USB drives, dongles, and test hardware with no inventory. Lose a drive, plug in a rogue device, and you have no audit trail.

This daemon fingerprints USB devices on Windows/Linux by VID/PID/Serial, maintains a SQLite registry, and alerts on first-seen, removed, or unauthorized devices. Ideal for labs with shared PCs and compliance-sensitive NAS.

### Features
- Cross-platform enumeration via pyusb / wmi
- Persistent SQLite registry with first/last seen
- Allowlist/blocklist
- JSON webhook for alerts

### Usage
```bash
pip install -r requirements.txt
python -m usb_tracker monitor --db usb.db --allowlist allowlist.json
```

License: MIT
