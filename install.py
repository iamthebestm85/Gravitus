import os
import subprocess
import sys
import shutil

# Required npm packages from your Node.js script
npm_packages = [
    "axios"
]

def install_npm():
    """Install npm if not installed."""
    try:
        subprocess.run(["npm", "--version"], check=True, stdout=subprocess.DEVNULL)
        print("[+] npm already installed")
    except:
        print("[+] Installing npm...")
        subprocess.run(["apt", "update"], check=True)
        subprocess.run(["apt", "install", "-y", "nodejs", "npm"], check=True)

def install_packages():
    """Install npm dependencies."""
    if not os.path.exists("package.json"):
        print("[+] Initializing npm project...")
        subprocess.run(["npm", "init", "-y"], check=True)

    if npm_packages:
        print(f"[+] Installing packages: {', '.join(npm_packages)}")
        subprocess.run(["npm", "install"] + npm_packages, check=True)

def run_gravitus():
    """Run Gravitus."""
    if os.path.exists("gravitus.js"):
        print("[+] Running Gravitus...")
        subprocess.run(["node", "gravitus.js"])
    else:
        print("[-] gravitus.js not found!")
        sys.exit(1)

def self_destruct():
    """Delete this install.py script."""
    file_path = os.path.realpath(__file__)
    print(f"[+] Deleting installer: {file_path}")
    os.remove(file_path)

if __name__ == "__main__":
    # Check for root (optional)
    if os.geteuid() != 0:
        print("[-] Please run as root (sudo python3 install.py)")
        sys.exit(1)

    install_npm()
    install_packages()
    run_gravitus()
    self_destruct()
