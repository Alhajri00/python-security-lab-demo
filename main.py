# Secure code example
# Fixed vulnerabilities: removed shell=True and os.system, replaced MD5 with SHA-256

import subprocess
import hashlib

# Secure command execution
# Use subprocess.run() with argument list and without shell=True
subprocess.run(["echo", "from", "subprocess"], check=True)

# Secure hash function
# Replace MD5 with SHA-256 for cryptographic security
print(hashlib.sha256(b"hello").hexdigest())
