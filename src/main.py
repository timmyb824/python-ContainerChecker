from tabulate import tabulate
from src.config import read_yaml
from src.ssh import create_ssh_client
from src.containers import check_installed_package, get_running_containers

def display_containers(ssh_client, package_name):
    if containers := get_running_containers(ssh_client, package_name):
        print(f"Running {package_name.capitalize()} Containers:")
        print(tabulate(containers, headers=["Name", "ID"], tablefmt="grid"))
    else:
        print(f"No running {package_name.capitalize()} containers.")
    print("")

def process_server(host, port, user, password, ssh_key, ssh_key_password):
    try:
        ssh_client = create_ssh_client(host, port, user, password, ssh_key, ssh_key_password)

        if ssh_client is None:
            print(f"Failed to connect to {host}")
            return

        print(f"Server: {host}")

        if check_installed_package(ssh_client, 'podman'):
            print("Podman is installed.")
            display_containers(ssh_client, 'podman')
        elif check_installed_package(ssh_client, 'docker'):
            print("Docker is installed.")
            display_containers(ssh_client, 'docker')
        else:
            print("Neither Podman nor Docker is installed.")

    except Exception as e:
        print(f"Failed to connect to {host}: {e}")
    finally:
        if 'ssh_client' in locals() and ssh_client:
            ssh_client.close()

def main():
    servers = read_yaml('servers.yaml')['servers']

    for server in servers:
        host = server['host']
        port = server.get('port', 22)
        user = server['user']
        password = server.get('password')
        ssh_key = server.get('ssh_key')
        ssh_key_password = server.get('ssh_key_password')

        process_server(host, port, user, password, ssh_key, ssh_key_password)

if __name__ == "__main__":
    main()