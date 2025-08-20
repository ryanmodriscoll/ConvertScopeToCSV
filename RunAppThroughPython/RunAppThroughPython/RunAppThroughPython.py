import subprocess

# Full path to the EXE
exe_path = r"C:\Program Files (x86)\Beckhoff\TwinCAT\Functions\TF3300-Scope-Server\TC3ScopeExportTool.exe"

# Arguments to pass to the tool
args = [
    exe_path,
    r"svd=C:\Scope\Records\Record1.svdx",                    # Native Scope Record Data File
    r"target=C:\Scope\CSV\Record1.csv",                      # File you wish to save the Converted CSV to
    r"config=C:\Scope\Templates\ScopeExporterSettings.xml",  # The CSV file settings 
    "silent"
]

# Run the command
try:
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    print("Execution successful.")
    print("Output:\n", result.stdout)
    print("Errors:\n", result.stderr)
except subprocess.CalledProcessError as e:
    print("Execution failed!")
    print("Return code:", e.returncode)
    print("Output:\n", e.stdout)
    print("Errors:\n", e.stderr)

