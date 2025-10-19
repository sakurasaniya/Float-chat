import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "outputs"

def generate_plot():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Mock salinity profile plot
    depths = [0, 100, 200, 500, 1000]
    salinity = [34.5, 34.8, 35.0, 35.2, 35.3]

    plt.figure()
    plt.plot(salinity, depths, marker="o")
    plt.gca().invert_yaxis()
    plt.xlabel("Salinity (PSU)")
    plt.ylabel("Depth (m)")
    plt.title("Sample Salinity Profile")
    path = os.path.join(OUTPUT_DIR, "plot.png")
    plt.savefig(path)
    plt.close()
    return path
