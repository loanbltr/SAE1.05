from scapy.all import *
from argparse import *
import ipaddress

def decouverteA(target_ip, export_file=None):
    packet = IP(dst=target_ip)/ICMP()
    response = sr1(packet, timeout=1, verbose=0)

    if response:
        result_message = f"L'hôte {target_ip} est actif."
        print(result_message)

        if export_file:
            with open(export_file, 'a') as file:
                file.write(result_message + '\n')
    else:
        print(f"L'hôte {target_ip} est inactif.")

def decouverteR(network, export_file=None):
    network = ipaddress.IPv4Network(network, strict=False)
    for host_ip in network.hosts():
        decouverteA(str(host_ip), export_file)

def decouvertP(target_ip, export_file=None):
    def arp_display(pkt):
        if pkt[ARP].op == 2:  # is-at (response)
            if pkt[ARP].psrc == target_ip:
                result = f"Passive host detected: {pkt[ARP].psrc}"
                if export_file:
                    with open(export_file, 'a') as file:
                        file.write(result + '\n')
                else:
                    print(result)

    sniff(prn=arp_display, filter="arp", store=0)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Découverte active avec Scapy.")
    parser.add_argument("-a", "--address", help="Adresse IP de l'hôte cible", default=None)
    parser.add_argument("-x", "--export", help="Exporter le résultat dans un fichier", default=None)
    parser.add_argument("-t", "--network", help="Adresse réseau pour tester tous les hôtes", default=None)
    parser.add_argument("-p", "--passive", help="Découverte passive avec ARP", default=None)

    args = parser.parse_args()

    target_ip = args.address
    export_file = args.export
    network = args.network

    if network:
        if target_ip:
            print("L'option -t ne peut pas être utilisée avec -a. Veuillez choisir l'une des deux.")
            sys.exit(1)
        decouverteR(network, export_file)
    elif target_ip:
        decouverteA(target_ip, export_file)
    elif args.passive:
        if target_ip:
            print("L'option -t ne peut pas être utilisée avec -a. Veuillez choisir l'une des deux.")
            sys.exit(1)
        decouvertP(args.passive, export_file)
    else:
        print("Veuillez spécifier une adresse IP avec -a, une adresse réseau avec -t, ou activer la découverte passive avec -p.")