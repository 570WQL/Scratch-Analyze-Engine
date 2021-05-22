import json
from tkinter import filedialog
import zipfile
import os
import time
file = filedialog.askopenfilename()
file = zipfile.ZipFile(file, "r")
project_json = json.loads(file.read(file.namelist()[0]).decode())
