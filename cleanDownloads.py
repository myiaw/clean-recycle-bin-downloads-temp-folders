import os
import shutil
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")
for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
