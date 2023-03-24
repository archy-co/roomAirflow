import sys

def main(filename: str):
    # read filename, where each line is velocity vector of form (x y z), average x, y, z for all lines and find average velocity magnitude
    avg_vel = 0
    with open(filename, "r") as f:
        for line in f:
            # remove ( and  ) at the beggining and end of line
            line = line[1:-2]
            x, y, z = line.split()
            if avg_vel == 0:
                avg_vel = (float(x) ** 2 + float(y) ** 2 + float(z) ** 2) ** 0.5
            else:
                avg_vel = (avg_vel + (float(x) ** 2 + float(y) ** 2 + float(z) ** 2) ** 0.5) / 2
    print(f"Average velocity magnitude: {avg_vel}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: average_temp.py <filename>")
        sys.exit(1)
    main(sys.argv[1])
