System Config Extractor Tool 

Overview
The System Config Extractor is a Python-based desktop application designed to collect essential system configuration details. This tool gathers information about the system's hardware (e.g., processor, RAM, storage, graphics), the current user, Windows specifications, and installed software. It then saves this data into a text file for easy access and review.
The app has been packaged into a Python launcher application for a smoother user experience, allowing users to run it without requiring the Python environment to be explicitly set up.

Creating the Python Launcher (EXE File)
To make the System Config Extractor a standalone executable (EXE) that runs without requiring Python to be installed on the user’s system, follow these steps:
1. Install PyInstaller
PyInstaller is a tool that bundles a Python application and all its dependencies into a single executable file.
pip install pyinstaller
2. Organize Your Project Folder
Make sure your project folder looks like this:
SystemConfigExtractor/
├── system_config_extractor.py
├── requirements.txt
⚠️ Ensure that your main script file (e.g., system_config_extractor.py) contains a main() function or a check like:
if __name__ == "__main__":
    save_to_txt()
   
4. Build the Executable
Use the following command inside the project folder:
pyinstaller --onefile --noconsole system_config_extractor.py
--onefile: Packages everything into a single EXE.
--noconsole: (Optional) Hides the console window. Use this only if your script doesn't need to show output.

5. Locate the Executable
After running the above command, PyInstaller will generate several folders:
dist/
└── system_config_extractor.exe
build/
system_config_extractor.spec

Your standalone EXE file will be located inside the dist/ folder.
5. Distribute the App
You can now share system_config_extractor.exe with users. They don’t need Python installed to run it — just double-click and it will generate the system_info.txt file.
Test the executable on another machine (without Python installed) to ensure it runs correctly.

How to Use the Launcher App
Launch the Application:
Windows: Double-click the System_Config.exe file associated with the launcher. If packaged correctly, it will run the app without needing to interact with the Python interpreter directly.

Extract System Information:
Upon launching, the app automatically gathers system details and stores them in a text file named system_info.txt.

Access the Report:
After the process completes, the generated system_info.txt file will be saved in the same directory as the application. Open this file to review the extracted system data.

Output File Example:
 The file will contain the following system details:
Processor information
RAM size
Storage (partition) details
Installed graphics card(s)
Windows OS specifications (Edition, Version, Installation Date, OS Build)
List of installed software

Function Breakdown
The core functionalities of the tool remain the same, though packaged into a standalone application for simplicity.
get_processor():
Retrieves the name of the processor installed on the system.

get_device_name():
Retrieves the full device name (hostname).

get_installed_ram():
Retrieves the total installed RAM size in gigabytes (GB).

get_storage():
Collects information about all disk partitions and their respective sizes.

get_graphics_card():
Retrieves a list of installed graphics card(s) on the system.

get_current_user():
Returns the current system username.

get_windows_specifications():
Retrieves the Windows edition, version, installation date, and build number.

get_installed_software_registry():
Extracts a list of installed software and their versions from the Windows registry.

save_to_txt():
This function runs automatically when the app is launched. It calls the other functions, formats the data, and writes it to system_info.txt.

Error Handling and Logs
Permission Issues: If the app encounters permission issues (e.g., accessing disk partitions or registry keys), it will skip the problematic sections and proceed with the rest of the data collection.
Log File: You can modify the app to create a log file (e.g., error_log.txt) if errors occur, for debugging purposes.

Limitations
The app is Windows-only and relies on Windows-specific modules (like wmi and winreg).
Users must have administrator permissions for certain system information retrieval, especially for installed software and registry details.
The output file may not be created if the app is run in a restricted environment with limited access to the system's hardware or software data.

Future Enhancements
Cross-Platform Support: Extend the tool to work on Linux and macOS, retrieving system information appropriate for those platforms.
More Hardware Information: Include additional details like network adapters, system motherboard, and more.
Improved GUI: Create a fully featured GUI with buttons for saving reports, viewing details in the app, and exporting to different formats (e.g., PDF, CSV).



