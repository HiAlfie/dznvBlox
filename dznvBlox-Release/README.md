![Image](data/assets/dznvbloxokay.jpg)

![Python](https://img.shields.io/badge/python-3.9+-blue)
![OS](https://img.shields.io/badge/OS-Windows%2010%2F11-green)
![License](https://img.shields.io/badge/license-MIT-orange)

[![Discord](https://img.shields.io/badge/Discord-Join%20Server-5865F2?logo=discord)](https://discord.gg/tMtdpUSrdM)

# ![icon](data/assets/dznvlogoblox.png) dznvBlox v0.0.6

**dznvBlox** is an advanced, beginner-friendly **Roblox multi-instance manager** written in Python with a full graphical interface.  
It allows you to run **multiple Roblox accounts at the same time** by automatically handling Roblox’s singleton restrictions, monitoring processes in real-time, and giving you deep insight into each running instance.

**Requires no setup, run dznvBlox, then simply join with as many roblox accounts as you want via browsers or bootstrappers. That's it.**

dznvBlox is designed to work not only with the **default Roblox launcher** and on **browsers**, but also with **custom bootstrappers**.

Roblox normally prevents you from opening more than one client at a time using internal **mutexes and events**.  
dznvBlox automatically detects newly launched Roblox processes, **closes the required handles**, and lets you open **as many Roblox instances as your system can handle**.

On top of that, dznvBlox provides:
- Real-time process detection
- Roblox account identification (username, user ID, avatar)
- Per-instance process analytics
- Custom automation (scripts on open/close)
- Extensive logging & debugging tools
- A clean, modern GUI

All of this runs **locally**, without injecting code into Roblox.

---

## 🤙 For Support

Join our discord server for any questions, bugs, suggestions, etc

Link : https://discord.gg/tMtdpUSrdM

---

## ✨ Features

- ✅ Bypasses 773 teleportation error
- ✅ Bypasses Roblox single-instance limitations automatically
- ✅ Allows running unlimited Roblox accounts simultaneously (system dependent)
- ✅ Automatically detects new Roblox processes in real time
- ✅ Works with the default Roblox launcher or browsers
- ✅ Fully compatible with custom Roblox bootstrappers (Bloxstrap, Fishstrap, Voidstrap, etc.)
- ✅ Closes `ROBLOX_singletonEvent` handles automatically
- ✅ Closes `ROBLOX_singletonMutex` handles automatically
- ✅ Supports advanced regex-based handle detection
- ✅ Allows custom regex patterns for future Roblox updates
- ✅ Optional forced handle closure for stubborn instances
- ✅ Uses process and handle management only
- ✅ Live Roblox instance list with real-time updates
- ✅ Displays each instance’s PID Informations
- ✅ Thread-based stability indicator
- ✅ Detects handle state per instance (Event & Mutex)
- ✅ Dedicated per-instance information window
- ✅ Extracts UserID automatically from Roblox logs
- ✅ Fetches Roblox username & profile avatar automatically
- ✅ Gracefully handles Roblox API rate limits
- ✅ Gracefully handles missing or corrupted log files
- ✅ Built-in low CPU usage mode
- ✅ Dynamic sleep scaling when idle
- ✅ Designed for long-running sessions
- ✅ Advanced settings panel with instant toggles
- ✅ Automatically saves settings to JSON
- ✅ Persistent configuration storage
- ✅ Installer quarantine system to prevent forced Roblox updates
- ✅ Temporarily moves Roblox installers to a safe TEMP location
- ✅ Automatically restores installers on exit
- ✅ Custom script execution on Roblox launch & close
- ✅ Supports `.py`, `.ps1`, `.bat`, `.js`, `.go` scripts
- ✅ Perfect for automation workflows
- ✅ Integrated logging system (debugger)
- ✅ Color-coded logs (success, info, error)
- ✅ Timestamped log files
- ✅ Optional automatic log saving
- ✅ Clean and modern GUI
- ✅ Animated activity indicators
- ✅ Beginner-friendly interface
- ✅ Built-in documentation
- ✅ Fully local execution (no external services required)
- ✅ Open-source and transparent
- ✅ Designed for stability and safety
- ✅ Educational and personal-use focused

---


---

## ▶️ Usage

### Option 1: Prebuilt Executable
1. Download the release
2. Extract the folder
3. Run `START.BAT`
4. Launch Roblox accounts normally (browser or bootstrapper)

### Option 2: Run From Source
```bash
START.bat
```

---

## 📦 Requirements (Source Code)

- Windows 10 / 11

- Python 3.9+

- Required libraries:
```
pip install psutil requests pillow pyperclip
```

**Additional requirements:**

- handle64.exe (Sysinternals Handle tool)

Must be located in:

- handle/handle64.exe

---

## 🧠 Notes

- No code injection

- No Roblox memory modification

- Uses process & handle management only

- Designed to be as safe and stable as possible

---

## 🔒 About `handle64.exe` (Safe & Official)

dznvBlox uses **handle64.exe**, a tool from the **Microsoft Sysinternals Suite**, to safely interact with Roblox process handles.

- **Official Microsoft page:**  
[https://learn.microsoft.com/en-us/sysinternals/downloads/handle](https://learn.microsoft.com/en-us/sysinternals/downloads/handle)

- **Purpose:**  
`handle64.exe` lists and manages open system handles.

- **Why dznvBlox uses it:**  
Roblox locks certain handles to prevent multiple sessions. dznvBlox uses handle64.exe to detect and release these locks, allowing unlimited sessions.

**Important:** `handle64.exe` is **safe, legitimate, and maintained by Microsoft**.

---

## ⭐️ Star this repository

Please star this repository to support me, it takes 2 seconds 😊

---

