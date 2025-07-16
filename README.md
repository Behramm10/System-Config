# 🖥️ System Config Extractor Tool

The **System Config Extractor** is a lightweight Python-based desktop application designed to collect and report essential system configuration details on Windows. It gathers information about your system’s hardware (CPU, RAM, storage, graphics), user details, Windows specifications, and a list of installed software, saving all of this in a convenient text file.

🧩 The tool has been packaged into a standalone executable using PyInstaller, allowing users to run it without having Python installed.

---

## 📦 Features

- 🧠 **Automatic system data extraction** on launch
- 🖥️ Collects:
  - Processor details
  - RAM size
  - Storage partition info
  - Installed graphics cards
  - Windows OS edition, version, and build
  - List of installed software
- 👤 Detects current user
- 📄 Saves output as a structured `system_info.txt` file
- 🗂️ Clean and minimal UI-free experience
- 🪟 Packaged into a Windows `.exe` for portability

---

## 🛠️ How to Build the Executable (Python Launcher)

You can package this app into a standalone `.exe` using **PyInstaller**:

### 1. Install PyInstaller

```bash
pip install pyinstaller
````

### 2. Project Folder Structure

Make sure your folder looks like this:

```
SystemConfigExtractor/
├── system_config_extractor.py
├── requirements.txt
```

Ensure your main Python script (`system_config_extractor.py`) includes the following:

```python
if __name__ == "__main__":
    save_to_txt()
```

### 3. Build the Executable

Run the following command inside the project folder:

```bash
pyinstaller --onefile --noconsole system_config_extractor.py
```

* `--onefile`: Packages everything into a single `.exe`
* `--noconsole`: Hides the terminal window (optional for non-GUI apps)

### 4. Locate the Executable

After the build, PyInstaller creates:

```
dist/
└── system_config_extractor.exe
build/
system_config_extractor.spec
```

The final executable is in the `dist/` folder.

### 5. Distribute the App

You can now share `system_config_extractor.exe` with users. It runs out-of-the-box on Windows—**no Python installation needed**.

✅ Test it on another system (without Python) to verify it works as expected.

---

## 🚀 How to Use

### 🪟 Launch the App

* Double-click `system_config_extractor.exe`

### 📊 Extract System Information

* The app runs silently and collects system details

### 📁 Access the Report

* A text file `system_info.txt` will be saved in the same directory
* Open this file to view system data

---

## 📝 Output File Includes

```
Processor Name
Device Name
Installed RAM (GB)
Storage Partition Info (Size, Free Space)
Graphics Card(s)
Current User
Windows Edition, Version, Build
Installed Software List (from Registry)
```

---

## 🔍 Function Overview

| Function                            | Description                                    |
| ----------------------------------- | ---------------------------------------------- |
| `get_processor()`                   | Retrieves processor name                       |
| `get_device_name()`                 | Gets the hostname                              |
| `get_installed_ram()`               | Returns installed RAM in GB                    |
| `get_storage()`                     | Fetches partition sizes and free space         |
| `get_graphics_card()`               | Lists GPU(s) installed                         |
| `get_current_user()`                | Gets the current username                      |
| `get_windows_specifications()`      | Returns edition, version, build                |
| `get_installed_software_registry()` | Reads installed software from Windows registry |
| `save_to_txt()`                     | Runs all above and writes to `system_info.txt` |

---

## ⚠️ Error Handling & Logs

* ❌ **Permission Issues**: If the tool can't access certain components (like registry or drives), it will skip them and continue.
* 🪵 **Optional Logging**: You can extend the script to log errors in an `error_log.txt` for debugging.

---

## ⚠️ Limitations

* 🪟 **Windows-only**: Uses Windows-specific modules (`wmi`, `winreg`)
* 🔐 Some data may require **Administrator privileges**
* 📁 Output file may not be generated if run in a restricted environment

---

## 🌟 Future Enhancements

* 🌐 **Cross-platform** support (Linux/macOS)
* 🧬 More hardware info (e.g., motherboard, network adapters)
* 🖼️ **GUI version** with export options (PDF, CSV)
* 🔍 Real-time display of data in-app

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Behramm Umrigar**
GitHub: [@behramm10](https://github.com/behramm10)

---


