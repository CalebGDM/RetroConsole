# Retro Console

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![MicroPython Version](https://img.shields.io/badge/MicroPython-v1.19.1-blue)

A bare-metal game console built with *Raspberry Pi Pico* using only native MicroPython modules. No third-party libraries, no shortcuts - just hardware, machine, and framebuf.


## 📖 Story Behind the Project

> "I thought you had participated"  
> - My electronics professor, after sharing a competition link I'd missed

This casual remark sparked my quest to *build a console at its most fundamental level*:
- No emulators (RetroPie is forbidden)
- No game engines (PyGame/Unity = cheating)
- Only native MicroPython: machine, framebuf, time
- Bit-banging when necessary

## 🛠 Hardware Requirements

| Component              | Specification           | Notes                          |
|------------------------|-------------------------|--------------------------------|
| Raspberry Pi Pico      | RP2040, 264KB RAM       | Any variant works              |
| SH1106 OLED            | 128x64, I2C            | With 4-pin interface            |
*at the moment

## 💻 Software Setup (Thonny)

1. *Install MicroPython* on Pico:
   - Hold BOOTSEL while connecting USB
   - In Thonny: Tools > Options > Interpreter
   - Select "MicroPython (Raspberry Pi Pico)"

2. *Upload Code*:
   ```python
   # Clone this repo first
   # In Thonny: File > Open > main.py
   # Save to Pico: File > Save as... > Raspberry Pi Pico
3. Required Modules:
   Only native: machine, framebuf, time, math

## 🎮 Key Features
**Bare-Metal Graphics**
```'python
# Manual SH1106 initialization
init_sequence = [
    0xAE,        # Display OFF
    0xD5, 0x80,  # Clock divide
    # ... 20+ commands
]
```
**Memory-Optimized Rendering**
- 1KB framebuffer (128x64 ÷ 8 bits)
- Page-based updates (8-row chunks)
- Dirty rectangle tracking

## 🚧 Current Limitations
- 30FPS max refresh rate
- No sound (WIP)

## 🤝 How to Contribute
1. Fork the repository
2. Create a new branch (git checkout -b feature)
3. Test changes in Thonny
4. Submit a pull request

**First time contributing? Try:**
- Adding a new demo game (when the engine is ready)
- Optimizing the display driver
- Implementing audio support

## 📜 License
MIT - Do what you want, but credit appreciated!

> Built with ❤ and Thonny's excellent MicroPython support

### Key Features:
1. *Thonny-Centric Workflow*: Clear instructions for MicroPython beginners
2. *Hardware Table*: Quick-reference for part sourcing
3. *Performance Transparency*: Shows current limitations
4. *Contribution Guide*: Lowers barrier for community input
5. *Visual Placeholders*: Ready for your actual project photos

Would you like me to:
1. Add a *troubleshooting section* for common Thonny/Pico issues?
2. Include *benchmark scripts* to verify performance?
3. Create a *simple game example* to demonstrate capabilities?
