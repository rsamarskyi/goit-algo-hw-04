import argparse
import shutil
from pathlib import Path

def read_directory(directory, destination):
    try:
        for item in directory.iterdir():
            if item.is_dir():
                print("Directory: ", item)
                read_directory(item, destination)
            elif item.is_file():
                extension = item.suffix.lower().removeprefix(".")
                if not extension:
                    extension = "no_extension"
                target_directory = destination/extension
                try:
                    target_directory.mkdir(parents=True, exist_ok=True)
                    target_file = target_directory/item.name
                    counter = 1
                    while target_file.exists():
                        target_file = target_directory / f"{item.stem}_{counter}{item.suffix}"
                        counter += 1
                    shutil.copy2(item, target_file)
                    print("File ", target_file," was copied")
                except OSError as error:    
                    print(item, error) 
    except OSError as error:
        print(directory, error)
parser = argparse.ArgumentParser()
parser.add_argument("source")
parser.add_argument("dest", nargs="?", default="dist")

args = parser.parse_args()

path = Path(args.source).resolve()
dest = Path(args.dest).resolve()
print(path, dest)
if not path.exists():
    print("Path does not exist")
elif not path.is_dir():
    print("Path is not a directory")
elif dest == path or dest.is_relative_to(path):
    print("Destination folder should not be inside the source folder")
else:
    read_directory(path, dest)