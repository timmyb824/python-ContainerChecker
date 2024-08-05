import warnings

from cryptography.utils import CryptographyDeprecationWarning

with warnings.catch_warnings(action="ignore", category=CryptographyDeprecationWarning):
    import paramiko

from src.containers import check_installed_package, display_containers


def create_ssh_client(
    hostname, port, username, password=None, key_filename=None, key_password=None
):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if key_filename:
            # if using rsa keys then need to use RSAKey instead of Ed25519Key
            key = paramiko.Ed25519Key.from_private_key_file(
                key_filename, password=key_password
            )
            ssh.connect(hostname, port, username=username, pkey=key)
        else:
            ssh.connect(hostname, port, username=username, password=password)
        return ssh
    except paramiko.AuthenticationException as e:
        print(f"Authentication failed: {e}")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


def process_server(host, port, user, password, ssh_key, ssh_key_password):
    try:
        ssh_client = create_ssh_client(
            host, port, user, password, ssh_key, ssh_key_password
        )

        if ssh_client is None:
            print(f"Failed to connect to {host}")
            return

        print(f"Server: {host}")

        if check_installed_package(ssh_client, "podman"):
            print("Podman is installed.")
            display_containers(ssh_client, "podman")
        elif check_installed_package(ssh_client, "docker"):
            print("Docker is installed.")
            display_containers(ssh_client, "docker")
        else:
            print("Neither Podman nor Docker is installed.")

    except Exception as e:
        print(f"Failed to connect to {host}: {e}")
    finally:
        if "ssh_client" in locals() and ssh_client:
            ssh_client.close()
