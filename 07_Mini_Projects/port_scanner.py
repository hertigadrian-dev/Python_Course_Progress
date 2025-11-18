import socket
import subprocess

def check_port(port):
    result = subprocess.run(
        ["lsof", "-i", f":{port}"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

target = "127.0.0.1"

for port in range(1, 65535):   # port ALWAYS stays integer
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

        info = check_port(port)
        print(info)

        choice = input("Close this program? (yes/no): ").lower()

        if choice == "yes":
            # extract PID safely
            try:
                pid = int(info.split()[1])
                subprocess.run(["kill", "-9", str(pid)])
                print(f"Process {pid} closed.")
            except (IndexError, ValueError) as e:
                print(f"Could not extract PID: {e}")
        else:
            print("Not closing.")
    
    s.close()

