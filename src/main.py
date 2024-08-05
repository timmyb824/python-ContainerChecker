from src.config import read_yaml
from src.ssh import process_server


def main():
    servers = read_yaml("servers.yaml")["servers"]

    for server in servers:
        host = server["host"]
        port = server.get("port", 22)
        user = server["user"]
        password = server.get("password")
        ssh_key = server.get("ssh_key")
        ssh_key_password = server.get("ssh_key_password")

        process_server(host, port, user, password, ssh_key, ssh_key_password)


if __name__ == "__main__":
    main()
