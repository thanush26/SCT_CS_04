# SCT_CS_04
Python Keylogger (For Educational and Ethical Use)

This repository contains a basic keylogger implemented in Python using the `pynput` library. The script captures keyboard input and logs it to a local file (`key_log.txt`). It is intended solely for educational purposes, particularly for students and professionals exploring cybersecurity concepts such as input monitoring and threat detection.

 Features
- Captures both printable characters and special keys (e.g., Enter, Space, Ctrl)
- Logs keystrokes in real-time using `pynput.keyboard.Listener`
- Appends data to a persistent log file for analysis
- Compatible with Linux and Windows environments

 Prerequisites
Ensure the following are installed on your system:

- Python 3.x
- `pynput` library

Install dependencies using pip:

```bash
pip install pynput
```
Usage

 Running the Script

```bash
python3 keylogger.py
```

Viewing Logged Keystrokes

```bash
cat key_log.txt
```
 File Structure

```
keylogger.py       # Main script for capturing keystrokes
key_log.txt        # Output file containing logged keys
README.md          # Project documentation
```
Ethical Considerations

Important Notice  
This tool is intended strictly for ethical and educational use. Do not deploy or execute this script on any system without the owner's explicit consent. Unauthorized use may violate privacy laws and institutional policies. This project is designed to promote responsible learning and awareness of cybersecurity threats.

 Learning Objectives
- Understand the fundamentals of keylogging and input capture
- Explore Python's event-driven programming capabilities
- Gain insight into ethical hacking and system monitoring techniques

Author

Thanush
Cybersecurity Engineering Student  
Coorg Institute of Technology, Ponnampet  
Focused on ethical hacking, Python development, and practical cybersecurity tools
