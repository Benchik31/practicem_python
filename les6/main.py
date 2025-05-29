from config import ROOT_DIR
from utils import resolve_and_check_path
from pathlib import Path
import shutil

current_dir = ROOT_DIR

def cmd_pwd():
    print(current_dir.relative_to(ROOT_DIR))

def cmd_ls():
    for item in current_dir.iterdir():
        print(f"{'[D]' if item.is_dir() else '[F]'} {item.name}")

def cmd_cd(path_str):
    global current_dir
    try:
        new_path = resolve_and_check_path(Path(current_dir) / path_str)
        if not new_path.is_dir():
            print("Ошибка: путь не является директорией.")
            return
        current_dir = new_path
    except PermissionError as e:
        print(f"Ошибка доступа: {e}")
    except FileNotFoundError:
        print("Ошибка: директория не найдена.")

def cmd_touch(filename):
    try:
        path = resolve_and_check_path(current_dir / filename)
        if path.exists():
            print("Файл уже существует.")
        else:
            path.touch()
            print("Файл создан.")
    except Exception as e:
        print(f"Ошибка: {e}")

def cmd_read(filename):
    try:
        path = resolve_and_check_path(current_dir / filename)
        if not path.is_file():
            print("Файл не найден.")
            return
        with open(path, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print(f"Ошибка чтения: {e}")

def cmd_write(filename):
    try:
        path = resolve_and_check_path(current_dir / filename)
        text = input("Введите текст для записи: ")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print("Файл перезаписан.")
    except Exception as e:
        print(f"Ошибка записи: {e}")

def cmd_rm(filename):
    try:
        path = resolve_and_check_path(current_dir / filename)
        if not path.exists():
            print("Файл не найден.")
        elif path.is_dir():
            print("Это директория, используйте rmdir.")
        else:
            path.unlink()
            print("Файл удалён.")
    except Exception as e:
        print(f"Ошибка удаления: {e}")

def cmd_cp(src, dst):
    try:
        src_path = resolve_and_check_path(current_dir / src)
        dst_path = resolve_and_check_path(current_dir / dst)
        if src_path.is_file():
            shutil.copy2(src_path, dst_path)
            print("Файл скопирован.")
        elif src_path.is_dir():
            shutil.copytree(src_path, dst_path)
            print("Директория скопирована.")
        else:
            print("Источник не найден.")
    except Exception as e:
        print(f"Ошибка копирования: {e}")

def cmd_mv(src, dst):
    try:
        src_path = resolve_and_check_path(current_dir / src)
        dst_path = resolve_and_check_path(current_dir / dst)
        shutil.move(src_path, dst_path)
        print("Перемещение выполнено.")
    except Exception as e:
        print(f"Ошибка перемещения: {e}")

def cmd_rename(old_name, new_name):
    try:
        old_path = resolve_and_check_path(current_dir / old_name)
        new_path = resolve_and_check_path(current_dir / new_name)
        old_path.rename(new_path)
        print("Переименование выполнено.")
    except Exception as e:
        print(f"Ошибка переименования: {e}")

def cmd_mkdir(dirname):
    try:
        path = resolve_and_check_path(current_dir / dirname)
        path.mkdir()
        print("Директория создана.")
    except FileExistsError:
        print("Такая директория уже существует.")
    except Exception as e:
        print(f"Ошибка создания директории: {e}")

def cmd_rmdir(dirname):
    try:
        path = resolve_and_check_path(current_dir / dirname)
        if not path.exists():
            print("Директория не найдена.")
        elif not path.is_dir():
            print("Это не директория.")
        elif any(path.iterdir()):
            print("Директория не пуста.")
        else:
            path.rmdir()
            print("Директория удалена.")
    except Exception as e:
        print(f"Ошибка удаления директории: {e}")

if __name__ == "__main__":
    print(f"Рабочая директория: {ROOT_DIR}")
    while True:
        prompt_path = current_dir.relative_to(ROOT_DIR)
        command = input(f"fm:/{prompt_path if prompt_path != Path('.') else ''}> ").strip()
        if command.lower() in ["exit", "quit"]:
            break
        elif command == "pwd":
            cmd_pwd()
        elif command == "ls":
            cmd_ls()
        elif command.startswith("cd "):
            _, path = command.split(" ", 1)
            cmd_cd(path)
        elif command.startswith("touch "):
            _, name = command.split(" ", 1)
            cmd_touch(name)
        elif command.startswith("read "):
            _, name = command.split(" ", 1)
            cmd_read(name)
        elif command.startswith("write "):
            _, name = command.split(" ", 1)
            cmd_write(name)
        elif command.startswith("rm "):
            _, name = command.split(" ", 1)
            cmd_rm(name)
        elif command.startswith("cp "):
            _, args = command.split(" ", 1)
            src, dst = args.split(" ", 1)
            cmd_cp(src, dst)
        elif command.startswith("mv "):
            _, args = command.split(" ", 1)
            src, dst = args.split(" ", 1)
            cmd_mv(src, dst)
        elif command.startswith("rename "):
            _, args = command.split(" ", 1)
            old_name, new_name = args.split(" ", 1)
            cmd_rename(old_name, new_name)
        elif command.startswith("mkdir "):
            _, name = command.split(" ", 1)
            cmd_mkdir(name)
        elif command.startswith("rmdir "):
            _, name = command.split(" ", 1)
            cmd_rmdir(name)
        else:
            print("Неизвестная команда")
