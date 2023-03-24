import sys
import os

def main(path: str, prefix: str):
    # iterate over all files with .stl extension
    for file in os.listdir(path):
        if file.endswith(".stl"):
            solidName = os.path.splitext(file)[0]
            if solidName.startswith(prefix):
                solidName = solidName.replace(prefix, "", 1)
                with open(os.path.join(path, file), "r") as f:
                    lines = f.readlines()
                    lines[0] = lines[0].split(" ", 1)[0] + " " + solidName + "\n"
                    lines[-1] = lines[-1].split(" ", 1)[0] + " " + solidName + "\n"

                    with open(os.path.join(path, file), "w") as f:
                        f.writelines(lines)
            else:
                print("File <" + file + "> does not start with <" + prefix + ">, skipping it")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: renameSolids.py <path> <prefix to be removed>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])


