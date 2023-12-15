import socket
import time
from collections import defaultdict
import sys

def read_hostnames_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def resolve_hostname_to_ip(hostnames):
    ip_addresses = []
    for hostname in hostnames:
        try:
            ip_addresses.append(socket.gethostbyname(hostname))
            time.sleep(1)  # Rate limit to 1 resolution per second
        except socket.gaierror:
            print(f"Failed to resolve: {hostname}")
        except socket.timeout:
            print(f"Timeout occurred while resolving: {hostname}")
    return ip_addresses

def group_ips_into_cidrs(ip_addresses):
    cidr_groups = defaultdict(set)
    for ip in ip_addresses:
        subnet = '.'.join(ip.split('.')[:3])
        cidr_groups[subnet].add(ip)

    cidrs = [f"{subnet}.0/24" for subnet in cidr_groups]
    return cidrs

# Main execution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <hosts_file>")
        sys.exit(1)

    file_path = sys.argv[1]  # Get file path from command line argument
    hostnames = read_hostnames_from_file(file_path)
    resolved_ips = resolve_hostname_to_ip(hostnames)
    cidrs = group_ips_into_cidrs(resolved_ips)

    # Print CIDRs in the desired format
    for cidr in cidrs:
        print(cidr)
