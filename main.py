# Guaranteed Bandit hits: B602/B603 (shell=True), B303 (MD5), B605 (os.system)
import os
import subprocess
import hashlib

# B605: os.system
os.system("echo from os.system")

# B602/B603: shell=True
subprocess.call("echo from shell", shell=True)

# B303: weak hash
print(hashlib.md5(b"hello").hexdigest())
