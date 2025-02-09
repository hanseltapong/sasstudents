import os
import platform
import subprocess
import sys

def ping_server(server):
Determine the command based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', server]  # Ping 4 times

    try:
Execute the ping command
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(f"Ping Output:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {server}. Error:\n{e.output}")

if name == "main":
    if len(sys.argv) != 2:
        print("Usage: python ping_server.py ")
        sys.exit(1)

    server_to_ping = sys.argv[1]
    ping_server(server_to_ping)

