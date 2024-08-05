def check_installed_package(ssh_client, package_name):
    stdin, stdout, stderr = ssh_client.exec_command(f'command -v {package_name}')
    return bool(stdout.read().decode())

def get_running_containers(ssh_client, package_name):
    if package_name == 'docker':
        command = 'docker ps --format "{{.Names}} {{.ID}}"'
    elif package_name == 'podman':
        command = 'podman ps --format "{{.Names}} {{.ID}}"'
    else:
        return []

    stdin, stdout, stderr = ssh_client.exec_command(command)
    containers = stdout.read().decode().splitlines()
    return [container.split() for container in containers]