# 🛡️ Honeypot Server to Detect Attack Patterns

## 📌 Objective
Deploy a honeypot that simulates vulnerable SSH/FTP services, logs attackers' activity, and visualizes attack patterns and origins.

## 🧰 Tools & Technologies
- 🐍 Python 3
- 🐮 Cowrie (SSH/Telnet honeypot)
- 🧱 Fail2Ban (for banning brute-force IPs)
- 📈 Matplotlib + GeoIP for data analysis
- 🐧 Ubuntu (Tested on Ubuntu 20.04/22.04)


## 🚀 Features & Deliverables

### ✅ Running Honeypot
- Emulates SSH service on a fake server
- Captures unauthorized login attempts, IPs, and commands

### ✅ Detailed Logs
- `cowrie.log` for SSH/Telnet activity
- `fail2ban.log` for real-time IP blocking
- Tracks credentials, attacker commands, and timestamps

### ✅ Visual Attack Reports
- Bar graph of most frequent attackers
- Geolocation map of source IPs

---

## 📂 Project Structure

```bash
honeypot_project/
│
├── cowrie.log                # Sample log from Cowrie
├── fail2ban.log              # Sample log from Fail2Ban
├── screenshot_1.png          # Cowrie terminal output
├── screenshot_2.png          # Fail2Ban activity
├── screenshot_3.png          # Attack graph visualization
├── screenshot_4.png          # Sample logfile breakdown
└── README.md                 # Project instructions

# Author: Suhani Pandey
