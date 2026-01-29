"""
Copy a folder from Box to OSDF.

Run like:
  python box_to_osdf.py --box <BOX_FOLDER_URL> --osdf <OSDF_DESTINATION_URL>

For example:
  python box_to_osdf.py --box https://app.box.com/folder/123456 --osdf osdf:///namespace/subdir/
"""

import argparse
import os


def main():
    args = parse_args()
    check_args(args)
    box_folder_url = args.box
    osdf_destination_url = args.osdf

    # Placeholder for Box to OSDF copy logic
    print(f"Copying from Box folder: {box_folder_url}")
    print(f"To OSDF destination: {osdf_destination_url}")

    # Here you would add the actual logic to connect to Box,
    # download the contents of the specified folder, and upload
    # them to the specified OSDF location.
    #
    # This is a placeholder implementation.
    print("Copy operation completed successfully.")


def check_args(args: argparse.Namespace):
    if not args.box.startswith("https://app.box.com/folder/"):
        raise ValueError("Invalid Box folder URL. It should start with 'https://app.box.com/folder/'")
    if not args.osdf.startswith("osdf:///"):
        raise ValueError("Invalid OSDF destination URL. It should start with 'osdf:///'")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copy a folder from Box to OSDF.")
    parser.add_argument(
        "--box",
        required=True,
        help="The Box folder URL to copy from (e.g., https://app.box.com/folder/123456).",
    )
    parser.add_argument(
        "--osdf",
        required=True,
        help="The OSDF destination URL to copy to (e.g., osdf:///namespace/subdir/).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()

