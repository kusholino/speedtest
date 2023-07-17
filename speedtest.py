import subprocess
import time
from datetime import datetime

file_path = '/root/speedtest/logs.txt'

while True:
    command = 'speedtest'
    result = subprocess.check_output(command, shell = True, text = True)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(file_path, 'a') as file:
        file.write(f"[{timestamp}: \n {result} \n \n")
    time.sleep(10800)