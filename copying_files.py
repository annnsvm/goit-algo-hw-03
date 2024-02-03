import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursive directory copy and sorting.")
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Path to the destination directory (default: dist)")
    return parser.parse_args()

def copy_and_sort_files(source_dir, destination_dir):
    try:
        copy_and_sort(source_dir, destination_dir)
        print("Files copied and sorted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def copy_and_sort(source_dir, destination_dir):
    os.makedirs(destination_dir, exist_ok=True)

    for entity in os.listdir(source_dir):
        source = os.path.join(source_dir, entity)
        
        if os.path.isfile(source):
            extension = os.path.splitext(entity)[1][1:]
            destination_sub_dir = os.path.join(destination_dir, extension)
            os.makedirs(destination_sub_dir, exist_ok=True)
            shutil.copy2(source, destination_sub_dir)

        if os.path.isdir(source):
            copy_and_sort(entity, destination_dir)


def main():
    args = parse_arguments()
    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    copy_and_sort_files(source_dir, destination_dir)

if __name__ == "__main__":
    main()