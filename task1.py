import argparse
import shutil
import sys
from pathlib import Path


def copy_by_extension(directory: Path, destination: Path) -> None:
    try:
        for item in directory.iterdir():
            if item.is_symlink():
                continue
            if item.is_dir():
                print("Directory:", item)
                copy_by_extension(item, destination)
            elif item.is_file():
                extension = item.suffix.lower().removeprefix(".") or "no_extension"
                target_directory = destination / extension
                try:
                    target_directory.mkdir(parents=True, exist_ok=True)
                    target_file = target_directory / item.name
                    counter = 1
                    while target_file.exists():
                        target_file = target_directory / f"{item.stem}_{counter}{item.suffix}"
                        counter += 1
                    shutil.copy2(item, target_file)
                    print("File", target_file, "was copied")
                except OSError as error:
                    print(f"Error copying {item}: {error}", file=sys.stderr)
    except OSError as error:
        print(f"Error reading {directory}: {error}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Copy files into subfolders by extension.")
    parser.add_argument("source", help="source directory")
    parser.add_argument("dest", nargs="?", default="dist", help="destination directory (default: dist)")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    dest = Path(args.dest).resolve()

    if not source.exists():
        print("Path does not exist", file=sys.stderr)
        return 1
    if not source.is_dir():
        print("Path is not a directory", file=sys.stderr)
        return 1
    if dest == source or dest.is_relative_to(source):
        print("Destination folder should not be inside the source folder", file=sys.stderr)
        return 1

    copy_by_extension(source, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())