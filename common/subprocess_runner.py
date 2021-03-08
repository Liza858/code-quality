import subprocess
from typing import List


def run_in_subprocess(command: List[str]) -> str:
    process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout = process.stdout.decode()
    stderr = process.stderr.decode()
    if stderr:
        print(stderr)

    return stdout
