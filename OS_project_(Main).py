import os
import shutil

class FileSystem:
    """
    A simple file system handler for basic operations like
    file and directory creation, reading, writing, copying, and deletion.
    """
    def __init__(self, root):
        self.root = os.path.abspath(root)
        os.makedirs(self.root, exist_ok=True)
        print(f"[INFO] Root directory set to '{self.root}'\n")

    def _get_path(self, name):
        return os.path.join(self.root, name)

    def create_directory(self, dirname):
        try:
            os.makedirs(self._get_path(dirname), exist_ok=True)
            print(f"[INFO] Directory '{dirname}' created.")
        except Exception as e:
            print(f"[ERROR] Failed to create directory '{dirname}': {e}")

    def list_directory(self, dirname=""):
        path = self._get_path(dirname)
        if os.path.exists(path):
            try:
                items = os.listdir(path)
                print(f"[INFO] Contents of '{dirname or 'root'}':")
                for item in items:
                    print(f"  - {item}")
            except Exception as e:
                print(f"[ERROR] Failed to list directory '{dirname}': {e}")
        else:
            print(f"[ERROR] Directory '{dirname}' not found.")

    def delete_directory(self, dirname):
        path = self._get_path(dirname)
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"[INFO] Directory '{dirname}' deleted.")
            except Exception as e:
                print(f"[ERROR] Failed to delete directory '{dirname}': {e}")
        else:
            print(f"[ERROR] Directory '{dirname}' not found.")
    def create_file(self, filename):
        try:
            open(self._get_path(filename), 'w').close()
            print(f"[INFO] File '{filename}' created.")
        except Exception as e:
            print(f"[ERROR] Failed to create file '{filename}': {e}")

    def write_to_file(self, filename, data):
        try:
            with open(self._get_path(filename), 'w') as f:
                f.write(data)
            print(f"[INFO] Data written to '{filename}'.")
        except Exception as e:
            print(f"[ERROR] Failed to write to file '{filename}': {e}")

    def read_file(self, filename):
        path = self._get_path(filename)
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    content = f.read()
                print(f"[INFO] Contents of '{filename}':\n{content}")
            except Exception as e:
                print(f"[ERROR] Cannot read file '{filename}': {e}")
        else:
            print(f"[ERROR] File '{filename}' not found.")

    def copy_file(self, src, dest):
        try:
            shutil.copy(self._get_path(src), self._get_path(dest))
            print(f"[INFO] File '{src}' copied to '{dest}'.")
        except Exception as e:
            print(f"[ERROR] Failed to copy '{src}': {e}")

    def delete_file(self, filename):
        path = self._get_path(filename)
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"[INFO] File '{filename}' deleted.")
            except Exception as e:
                print(f"[ERROR] Could not delete file '{filename}': {e}")
        else:
            print(f"[ERROR] File '{filename}' not found.")

    def rename_file(self, old_name, new_name):
        try:
            os.rename(self._get_path(old_name), self._get_path(new_name))
            print(f"[INFO] Renamed '{old_name}' to '{new_name}'.")
        except Exception as e:
            print(f"[ERROR] Rename failed: {e}")


def main():
    root_dir = input("Enter root directory for file system: ")
    fs = FileSystem(root_dir)

    menu = """
    ================================
           FILE SYSTEM MENU
    ================================
    1.  Create Directory
    2.  List Directory
    3.  Delete Directory
    4.  Create File
    5.  Write to File
    6.  Read File
    7.  Copy File
    8.  Delete File
    9.  Rename File  
    10. Exit
    """

    operations = {
        '1': (fs.create_directory, ["Enter directory name: "]),
        '2': (fs.list_directory, ["Enter directory (leave blank for root): "]),
        '3': (fs.delete_directory, ["Enter directory name: "]),
        '4': (fs.create_file, ["Enter file name: "]),
        '5': (fs.write_to_file, ["Enter file name: ", "Enter data: "]),
        '6': (fs.read_file, ["Enter file name: "]),
        '7': (fs.copy_file, ["Enter source file: ", "Enter destination file: "]),
        '8': (fs.delete_file, ["Enter file name: "]),
        '9': (fs.rename_file, ["Enter old name: ", "Enter new name: "]),
        
    }

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == '10':
            print("[INFO] Exiting File System...")
            break
        elif choice in operations:
            args = [input(prompt) for prompt in operations[choice][1]]
            operations[choice][0](*args)
        else:
            print("[ERROR] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
