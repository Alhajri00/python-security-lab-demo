# Guaranteed Bandit hits: B605 (os.system), B602/B603 (shell=True), B303 (MD5)
import os, subprocess, hashlib

os.system("echo from os.system")           # B605
subprocess.call("echo from shell", shell=True)  # B602/B603
print(hashlib.md5(b"hello").hexdigest())   # B303
