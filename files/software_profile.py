import json
import platform
import subprocess

def get_os_info():
    os_info = {
        "os_name": str(platform.system()),
        "os_version": str(platform.release()),
        "os_distribution": "unknown"
    }
    try:
        system = platform.system().lower()
        if system == "linux":
            try:
                result = subprocess.run(["lsb_release", "-ds"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    os_info["os_distribution"] = result.stdout.strip()
            except (subprocess.SubprocessError, FileNotFoundError):
                try:
                    with open("/etc/os-release", "r") as f:
                        for line in f:
                            if line.startswith("PRETTY_NAME"):
                                os_info["os_distribution"] = line.split("=")[1].strip().strip('"')
                                break
                except Exception:
                    pass
        elif system == "windows":
            try:
                result = subprocess.run(["systeminfo"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    for line in result.stdout.splitlines():
                        if "OS Name" in line:
                            os_info["os_distribution"] = line.split(":", 1)[1].strip()
                            break
            except (subprocess.SubprocessError, FileNotFoundError):
                pass
        elif system == "darwin":
            try:
                result = subprocess.run(["sw_vers", "-productName"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    os_info["os_distribution"] = result.stdout.strip()
                result = subprocess.run(["sw_vers", "-productVersion"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    os_info["os_version"] = result.stdout.strip()
            except (subprocess.SubprocessError, FileNotFoundError):
                pass
    except Exception:
        pass
    return os_info

def get_application_info():
    apps = {}
    # Python
    try:
        result = subprocess.run(["python3", "--version"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            apps["python_version"] = result.stdout.strip().split()[1]
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    # Java
    try:
        result = subprocess.run(["java", "-version"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if "java version" in line.lower():
                    apps["java_version"] = line.split('"')[1]
                    break
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    # Node.js
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            apps["nodejs_version"] = result.stdout.strip().lstrip('v')
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    # Docker
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            apps["docker_version"] = result.stdout.strip().split(',')[0].split('version')[1].strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    # Podman
    try:
        result = subprocess.run(["podman", "--version"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            apps["podman_version"] = result.stdout.strip().split('version')[1].strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    # Terraform
    try:
        result = subprocess.run(["terraform", "--version"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            apps["terraform_version"] = result.stdout.splitlines()[0].split('v')[1].strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    # Git
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            apps["git_version"] = result.stdout.strip().split('version')[1].strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    return apps

def main():
    profile = {}
    profile.update(get_os_info())
    profile.update(get_application_info())
    print(json.dumps(profile))

if __name__ == "__main__":
    main()
