import argparse
import socket
import socks
import time

banner = r"""
 _                               _       
(_) ___  ___  ___ _ __ ___  __ _| |_ ___ 
| |/ _ \/ __|/ __| '__/ _ \/ _` | __/ _ \
| | (_) \__ \ (__| | |  __/ (_| | ||  __/
|_|\___/|___/\___|_|  \___|\__,_|\__\___|
"""

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Service inconnu"

def get_service_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return "Banner inconnu"

def scan_ports(target, proxy):
    print("+" + "-"*40 + "+")
    print("|{:^40}|".format(f"Scanning des ports ouverts sur {target} (anonyme)"))
    print("+" + "-"*40 + "+")
    print(banner)  # Affiche la bannière

    open_ports = []
    for port in port_range:
        if scan_port(target, port, proxy):
            open_ports.append(port)
            time.sleep(0.1)  # Ralentissement du rythme de scan

    if open_ports:
        print("|{:^40}|".format("Ports ouverts :"))
        for port in open_ports:
            service_name = get_service_name(port)
            service_banner = get_service_banner(target, port)
            print("|{:<10} : {:<24} | Version : {:<20}|".format(f"Port {port}", service_name, service_banner))
    else:
        print("|{:^40}|".format("Aucun port ouvert trouvé."))

    print("+" + "-"*40 + "+")

def main():
    parser = argparse.ArgumentParser(description="Scan de ports simple avec argparse")
    parser.add_argument("target", help="Adresse IP ou nom de domaine du site sûr")
    parser.add_argument("-p", "--proxy", help="Proxy à utiliser (format: ip:port)")
    args = parser.parse_args()

    target = args.target
    proxy = args.proxy
    scan_ports(target, proxy)

if __name__ == "__main__":
    port_range = range(1, 1025)
    main()
