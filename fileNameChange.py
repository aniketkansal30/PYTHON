import os
desktop=os.path.join(os.path.expanduser("~"), "Desktop")
ss=os.path.join(desktop,"SS")
files=os.listdir(ss)
i = 1
for file in files:
    if file.endswith(".png"):
        old_path = os.path.join(ss, file)
        new_path = os.path.join(ss, f"{i}.png")
        print(f"Renaming: {file} -> {i}.png")
        os.rename(old_path, new_path)
        i += 1