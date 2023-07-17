import subprocess

subprocess.run(["curl", "-s", "https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash"])
subprocess.run(["apt-get", "install", " speedtest"])
subprocess.run(["mv", "/root/speedtest/speedtest.service", "/etc/systemd/system"])
subprocess.run(["systemctl", "enable", "speedtest.service"])
subprocess.run(["systemctl", "start", "speedtest.service"])
print('Setup OK')