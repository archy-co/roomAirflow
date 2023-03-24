import sys
import os
import matplotlib.pyplot as plt

def single_file_stat(filename: str, vector: bool = True):
    avgg = 0
    minn = float("inf")
    maxx = float("-inf")

    with open(filename, "r") as f:
        i = -1

        for line in f:
            i += 1

            if i < 21:
                continue

            if line == ")\n":
                break

            val = 0
            if vector:
                line = line[1:-2]
                x, y, z = line.split()
                val = (float(x) ** 2 + float(y) ** 2 + float(z) ** 2) ** 0.5
            else:
                val = float(line)

            if i == 0:
                avgg = val
            else:
                avgg = (avgg + val ** 0.5) / 2

            if val < minn:
                minn = val

            if val > maxx:
                maxx = val

    return avgg, minn, maxx

def main(path: str):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d != "0" and d.replace(".", "", 1).isdigit()]

    dirs.sort(key=lambda x: float(x))

    dirs = dirs[2:]

    U_avgs = []
    U_mins = []
    U_maxs = []

    p_avgs = []
    p_mins = []
    p_maxs = []

    for d in dirs:
        U_avgg, U_minn, U_maxx = single_file_stat(os.path.join(path, d, "U"), vector=True)
        p_avgg, p_minn, p_maxx = single_file_stat(os.path.join(path, d, "p"), vector=False)

        U_avgs.append(U_avgg)
        U_mins.append(U_minn)
        U_maxs.append(U_maxx)

        p_avgs.append(p_avgg)
        p_mins.append(p_minn)
        p_maxs.append(p_maxx)

    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    dirs = [float(d) for d in dirs]

    # write U_avgs and p_avgs to file 
    with open("U_avgs.txt", "w") as f:
        for i in range(len(U_avgs)):
            f.write(f"{dirs[i]} {U_avgs[i]}\n")

    with open("p_avgs.txt", "w") as f:
        for i in range(len(p_avgs)):
            f.write(f"{dirs[i]} {p_avgs[i]}\n")

    axs[0, 0].plot(dirs, U_avgs)
    axs[0, 0].set_title("U_avg")
    axs[0, 1].plot(dirs, U_mins)
    axs[0, 1].set_title("U_min")
    axs[0, 2].plot(dirs, U_maxs)
    axs[0, 2].set_title("U_max")

    axs[1, 0].plot(dirs, p_avgs)
    axs[1, 0].set_title("p_avg")
    axs[1, 1].plot(dirs, p_mins)
    axs[1, 1].set_title("p_min")
    axs[1, 2].plot(dirs, p_maxs)
    axs[1, 2].set_title("p_max")

    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: average_temp.py <path>")
        sys.exit(1)
    main(sys.argv[1])
