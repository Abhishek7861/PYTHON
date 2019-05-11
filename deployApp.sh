# 1: Install pyinstaller tarball from https://www.pyinstaller.org/downloads.html
# 2: Extract it and cd into the folder
# 3: Run 
python3 pyinstaller.py setup.py
# 4: Go to project directory that houses your application.py
# 5: Run command
python3 /path/to/pyinstaller.py_file --windowed --onefile application.py --hidden-import module1, module2, etc 