import warnings
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings(action="ignore", category=CryptographyDeprecationWarning):
    import paramiko


def create_ssh_client(hostname, port, username, password=None, key_filename=None, key_password=None):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if key_filename:
            # if using rsa keys then need to use RSAKey instead of Ed25519Key
            key = paramiko.Ed25519Key.from_private_key_file(key_filename, password=key_password)
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