import subprocess, os

def run():
    print("[#FF1420]To run the program you need to has python installed and pip to work[/#FF1420]")
    subprocess.run('bash', '-c', 'pip install hashlib cryptography rich tabulate')
