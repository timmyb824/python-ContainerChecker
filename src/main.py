from tabulate import tabulate

from src.config import read_yaml
from src.ssh import create_ssh_client
from src.containers import check_installed_package, get_running_containers

def main():
    servers = read_yaml('servers.yaml')['servers']

    for server in servers:
        host = server['host']
        port = server.get('port', 22)
        user = server['user']
        password = server.get('password')
        ssh_key = server.get('ssh_key')
        ssh_key_password = server.get('ssh_key_password')

        try:
            ssh_client = create_ssh_client(host, port, user, password, ssh_key, ssh_key_password)

            if ssh_client is None:
                print(f"Failed to connect to {host}")
                continue

            if podman_installed := check_installed_package(ssh_client, 'podman'):
                print(f"Server: {host}")
                print("Podman is installed.")
                if containers := get_running_containers(ssh_client, 'podman'):
                    print("Running Podman Containers:")
                    print(tabulate(containers, headers=["Name", "ID"], tablefmt="grid"))
                else:
                    print("No running Podman containers.")
                print("")
                ssh_client.close()
                continue

            if docker_installed := check_installed_package(ssh_client, 'docker'):
                print(f"Server: {host}")
                print("Docker is installed.")
                if containers := get_running_containers(ssh_client, 'docker'):
                    print("Running Docker Containers:")
                    print(tabulate(containers, headers=["Name", "ID"], tablefmt="grid"))
                else:
                    print("No running Docker containers.")
                print("")
                ssh_client.close()
                continue

            print(f"Server: {host}")
            print("Neither Podman nor Docker is installed.")
            ssh_client.close()

        except Exception as e:
            print(f"Failed to connect to {host}: {e}")


if __name__ == "__main__":
    main()