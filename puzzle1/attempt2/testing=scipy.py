import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if scipy is installed
try:
    import scipy
    print("scipy is already installed")
except ImportError:
    print("scipy is not installed. Installing...")
    install("scipy")
    import scipy  # Now try importing it again to verify
    print("scipy has been successfully installed")
