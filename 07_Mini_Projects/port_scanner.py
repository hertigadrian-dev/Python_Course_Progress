# import socket
# import subprocess

# def check_port(port):
#     result = subprocess.run(
#         ["lsof", "-i", f":{port}"],
#         capture_output=True,
#         text=True
#     )
#     return result.stdout.strip()

# target = "127.0.0.1"

# for port in range(1, 65535):   # port ALWAYS stays integer
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.settimeout(0.01)
    
#     result = s.connect_ex((target, port))

#     if result == 0:
#         print(f"[OPEN] Port {port}")

#         info = check_port(port)
#         print(info)

#         choice = input("Close this program? (yes/no): ").lower()

#         if choice == "yes":
#             # extract PID safely
#             try:
#                 pid = int(info.split()[1])
#                 subprocess.run(["kill", "-9", str(pid)])
#                 print(f"Process {pid} closed.")
#             except (IndexError, ValueError) as e:
#                 print(f"Could not extract PID: {e}")
#         else:
#             print("Not closing.")
    
#     s.close()


#------------------------------


# import socket
# import subprocess # Still needed if you insist on local OS commands
# import sys

# # --- Constants ---
# TARGET_HOST = "127.0.0.1"
# MIN_PORT = 1
# MAX_PORT = 6024  # Limit the range for faster testing
# TIMEOUT = 0.1    # Increased timeout for reliability

# def is_port_open(target, port, timeout):
#     """Attempts to connect to a port and returns True if open."""
#     # The 'with' statement automatically handles s.close()
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.settimeout(timeout)
#         # connect_ex returns 0 on success (open)
#         return s.connect_ex((target, port)) == 0

# # NOTE: This function is non-portable (only works on Unix/Linux)
# def check_port_lsof(port):
#     """Uses lsof to check which process is using the port (Non-portable)."""
#     try:
#         result = subprocess.run(
#             ["lsof", "-i", f":{port}"],
#             capture_output=True,
#             text=True,
#             check=True # Raise error if lsof fails
#         )
#         return result.stdout.strip()
#     except (FileNotFoundError, subprocess.CalledProcessError):
#         # lsof command not found or failed execution
#         return "ERROR: lsof command failed or is not available on this system."

# def main_scanner():
#     print(f"Starting port scan on {TARGET_HOST}...")
    
#     # Iterate through the port range
#     for port in range(MIN_PORT, MAX_PORT + 1):
#         if is_port_open(TARGET_HOST, port, TIMEOUT):
#             print(f"[OPEN] Port {port}")
            
#             # --- OS-Specific Interaction (needs improvement for portability) ---
#             info = check_port_lsof(port)
#             print(info)
            
#             # Simplified user interaction loop
#             choice = input("Attempt to close the associated process? (yes/no): ").lower()
            
#             if choice == "yes":
#                 # Basic, brittle PID extraction (needs heavy improvement)
#                 try:
#                     # Assumes lsof output structure is consistent: COMMAND PID USER...
#                     pid = int(info.split()[1])
#                     print(f"Attempting to kill process {pid}...")
                    
#                     # Try soft kill first (SIGTERM, default)
#                     subprocess.run(["kill", str(pid)]) 
#                     print(f"Process {pid} closed gracefully (SIGTERM).")
                    
#                 except (IndexError, ValueError) as e:
#                     print(f"Could not extract PID from lsof output: {e}")
#                 except Exception as e:
#                     print(f"Failed to kill process: {e}")
            
# if __name__ == "__main__":
#     try:
#         main_scanner()
#     except KeyboardInterrupt:
#         print("\nScan interrupted by user.")
#         sys.exit(0)
#     print("Scan complete.")

#----------------------------------------------
''' IP and PORT scanner '''


# import socket
# import subprocess
# import threading

# # ------------------------------
# # 1. Find active IPs on the network
# # ------------------------------

# def ping(ip):
#     # Works on macOS/Linux (-c 1), Windows users use (-n 1)
#     command = ["ping", "-c", "1", ip]
#     result = subprocess.run(command, stdout=subprocess.DEVNULL)
#     if result.returncode == 0:
#         print(f"[+] Active IP found: {ip}")
#         active_ips.append(ip)


# # ------------------------------
# # 2. Scan ports on each active IP
# # ------------------------------

# def scan_port(ip, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.settimeout(0.5)
#     if sock.connect_ex((ip, port)) == 0:
#         print(f"    → Port {port} OPEN on {ip}")
#     sock.close()


# # ------------------------------
# # Start Scanning
# # ------------------------------

# active_ips = []

# # Change this to match your network (e.g., 192.168.1.* or 10.0.0.*)
# network_prefix = "192.168.1."

# print("[*] Scanning for active devices...")

# threads = []

# for i in range(1, 255):
#     ip = network_prefix + str(i)
#     t = threading.Thread(target=ping, args=(ip,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# print("\n[*] Starting port scan on active IPs...")
# ports_to_scan = range(1, 65535)

# for ip in active_ips:
#     print(f"\nScanning {ip}...")
#     for port in ports_to_scan:
#         scan_port(ip, port)
#-------------------------------------


from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
import socket

# ------------------------------
# Scan local network for IP + MAC
# ------------------------------

def scan_network(network_prefix="192.168.1.0/24"):
    print("[*] Scanning network for devices...")
    arp = ARP(pdst=network_prefix)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []

    for sent, received in result:
        try:
            vendor = MacLookup().lookup(received.hwsrc)
        except:
            vendor = "Unknown Manufacturer"

        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "vendor": vendor
        })

    return devices

# ------------------------------
# Port scanner
# ------------------------------

def scan_ports(ip, ports=[22, 80, 443, 8080, 631]):
    print(f"\nScanning ports on {ip}...")
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.4)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# ------------------------------
# Main
# ------------------------------

devices = scan_network("192.168.1.0/24")

print("\n=== Devices Found on Network ===")
for d in devices:
    print(f"IP: {d['ip']}\nMAC: {d['mac']}\nVendor: {d['vendor']}\n")

print("\n=== Port Scan ===")
for d in devices:
    ports = scan_ports(d["ip"])
    if ports:
        print(f"{d['ip']} ({d['vendor']}) → Open Ports: {ports}")
    else:
        print(f"{d['ip']} ({d['vendor']}) → No common open ports found.")


