# start engtool

import os

folder = os.path.normpath((os.path.dirname(__file__)))
exefile = os.path.join(folder, "engtool", "builds", "engtool.exe")

s=f"start {exefile} -s localhost -p 2402"
os.system(s)
