import socket

target = input("Enter IP Address or Hostname: ")

print(f"\nScanning {target}...\n")

ports = {
    21: ("FTP", "High"),
    22: ("SSH", "Low"),
    23: ("Telnet", "High"),
    25: ("SMTP", "Medium"),
    53: ("DNS", "Low"),
    80: ("HTTP", "Medium"),
    443: ("HTTPS", "Low")
}

open_ports = []

for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:

        service, risk = ports[port]

        print(f"Port {port} OPEN ({service}) Risk: {risk}")

        open_ports.append((port, service, risk))

    s.close()

print("\n----- Security Report -----")

for port, service, risk in open_ports:

    if port == 80:
        print("HTTP detected -> Consider HTTPS")

    elif port == 23:
        print("Telnet detected -> Replace with SSH")

    elif port == 21:
        print("FTP detected -> Use SFTP")

print("\nScan Complete")
