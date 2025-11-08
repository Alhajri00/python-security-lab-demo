import subprocess
import hashlib
import yaml
import pickle
import os

def run_shell(cmd):
    # B602/B603: shell=True command injection
    subprocess.Popen(cmd, shell=True)

def use_eval(expr):
    # B307: use of eval
    return eval(expr)

def weak_hash(data: bytes):
    # B303: MD5 is insecure
    return hashlib.md5(data).hexdigest()

# B506: unsafe yaml.load without Loader
with open("config.yaml", "r") as f:
    cfg = yaml.load(f)

# B301: unsafe pickle loads
pickle.loads(b"cos\nsystem\n(S'echo Pickle!'\ntR.")

# Trigger the functions with untrusted-like input
user_input = cfg.get("user_input", "echo Hello from Bandit")
run_shell(user_input)
use_eval("1+1")
weak_hash(b"hello")
os.system("echo also unsafe")  # (Bandit may also flag this)
