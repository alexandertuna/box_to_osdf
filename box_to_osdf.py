"""
Copy a folder from Box to OSDF.

Run like:
  python box_to_osdf.py --box <BOX_FOLDER_URL> --osdf <OSDF_DESTINATION_URL> > go.sh
  source go.sh

For example:
  python box_to_osdf.py --box https://app.box.com/folder/123456 --osdf osdf:///namespace/subdir/ > go.sh
  source go.sh

Things to consider for improvements:
- Walking through Box folder contents recursively instead of downloading everything at once
- Error handling for Box and pelican commands
- Especially: Retrying `pelican object sync`
"""

import argparse
import time
NOW = time.strftime("%Y_%m_%d_%Hh%Mm%Ss")


def main():
    args = parse_args()
    check_args(args)
    download_from_box(args.box)
    upload_to_osdf(args.osdf)


def download_from_box(box_folder_url: str):
    # print(f"NAME=$(box folders:get {folder_id} --json | jq -r '.name')")
    folder_id = box_folder_url.rstrip("/").split("/")[-1]
    cmd = f"box folders:download {folder_id} --destination ./{NOW}"
    print(cmd)


def upload_to_osdf(osdf_destination_url: str):
    cmd = f"pelican object sync ./{NOW} {osdf_destination_url}"
    print(cmd)


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

