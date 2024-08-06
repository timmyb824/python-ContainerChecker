import argparse
import concurrent.futures

from containerchecker.config import read_yaml_file
from containerchecker.log_handler import setup_logging
from containerchecker.ssh import process_server


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Process servers and check for running containers."
    )
    parser.add_argument(
        "--file", type=str, default="servers.yaml", help="Path to servers.yaml"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def main():
    """Main function."""
    args = parse_args()

    logger = setup_logging(args.verbose)

    if args.verbose:
        logger.debug("Verbose output enabled")

    servers = read_yaml_file(args.file)

    if servers is None:
        logger.error(f"Failed to read servers from {args.file}")
        return

    server_list = servers.get("servers", [])
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(
                process_server,
                server["host"],
                server.get("port", 22),
                server["user"],
                server.get("password"),
                server.get("ssh_key"),
                server.get("ssh_key_password"),
            )
            for server in server_list
        ]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logger.exception(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
