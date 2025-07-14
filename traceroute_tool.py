import os
import platform
import subprocess

host = input("Enter host to traceroute (e.g., google.com): ")

if platform.system().lower() == "windows":
    cmd = f"tracert {host}"
else:
    cmd = f"traceroute {host}"

print(f"Running traceroute to {host}...\n")
subprocess.call(cmd, shell=True)