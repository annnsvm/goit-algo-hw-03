import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Початкова папка з файлами"
        )
    parser.add_argument(
        "-d", "--dist", type=Path, default=Path("dist"), help="Папка для копіювання"
    )
    return parser.parse_args()


def recursive_copy(source: Path, dist: Path):
    try:
        for el in source.iterdir():
            if el.is_dir():
                recursive_copy(el, dist)
            else:
                folder = el.suffix
                folder = dist / folder
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy(el, folder)
    except FileNotFoundError:
        # Обробка помилки, якщо файл не знайдено
        print("File Not Found Error: No such file or directory")
        exit()
    except PermissionError:
        # Обробка помилки, якщо є проблеми з доступом до файлу
        print("Permission Denied Error: Access is denied")
        exit()


def main():
    args = parse_argv()
    recursive_copy(args.source, args.dist)
    print(args)


if __name__ == "__main__":
    main()