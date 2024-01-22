import os

def get_servers():
    servers = []
    while True:
        server_ip = input("Enter the IP of the Grafana server (or 'done' to finish): ")
        if server_ip.lower() == 'done':
            break
        servers.append(server_ip)
    return servers

def create_inventory_file(servers, filename="inventory.ini"):
    with open(filename, 'w') as file:
        file.write("[grafana_servers]\n")
        for server in servers:
            file.write(f"{server}\n")

def main():
    print("Grafana Server Configuration")
    servers = get_servers()
    if servers:
        create_inventory_file(servers)
        print(f"Inventory file created with {len(servers)} servers.")
    else:
        print("No servers were added.")

if __name__ == "__main__":
    main()
