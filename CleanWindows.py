import os
import shutil
from pathlib import Path
import winshell

tempPath = Path.home() / "AppData" / "Local" / "Temp"
downloadsPath = Path.home() / "Downloads"


def clear_folder(path):
    global file_path
    if path:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as ex:
                print('Failed to delete %s. Reason: %s' % (file_path, ex))


if tempPath.exists():
    clear_folder(str(tempPath))
else:
    print("Not a valid temp path." + str(tempPath))

if tempPath.exists():
    clear_folder(str(downloadsPath))
else:
    print("Not a valid Downloads path." + str(downloadsPath))

try:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
except Exception as e:
    print('Failed to empty recycle bin. Reason: %s' % e)
