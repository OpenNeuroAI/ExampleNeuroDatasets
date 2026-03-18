# Some ideas...

import h5py
import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Open file
filepath = "Chemotaxis-Data-and-Analysis/Mock_worms/chemotaxis_mock_25825_1_20250725_153953/metadata_featuresN_oneworm.hdf5"

if len(sys.argv) > 1:
    if "-a" in sys.argv:
        filepath = "Chemotaxis-Data-and-Analysis/Aversive_worms/chemotaxis_avsv_24_1_23_03_20240124_142324/metadata_featuresN_oneworm.hdf5"
    elif "-m" in sys.argv:
        filepath = "Chemotaxis-Data-and-Analysis/Mock_worms/chemotaxis_mock_210825_3_20250722_161220/metadata_featuresN_oneworm.hdf5"
    elif "-m1" in sys.argv:
        filepath = "Chemotaxis-Data-and-Analysis/Mock_worms/chemotaxis_mock_24_2_23_04_20240123_140216/metadata_featuresN_oneworm.hdf5"
    elif "-s" in sys.argv:
        filepath = "Chemotaxis-Data-and-Analysis/sexually_conditioned_worms/chemotaxis_sexc_24_1_26_13_20240126_152252/metadata_featuresN_oneworm.hdf5"
    else:
        filepath = sys.argv[1]


# Check that file exists
if not os.path.exists(filepath):
    print(
        f"\nFile not found: {filepath}!\nPlease clone the repository into this folder using:\n"
    )
    print(
        "    git clone https://github.com/Barrios-Lab/Chemotaxis-Data-and-Analysis.git\n"
    )
    quit()

print(f"Loading dataset from: {filepath}...")


def load_dataset(filepath, show_plot=True, save_plot=False, output_dir="."):

    odor_patch = None

    with h5py.File(filepath, "r") as f:
        print("Loaded dataset from:", filepath)
        # List all datasets
        print("Keys for datasets:", list(f.keys()))

        # Load trajectories data as DataFrame
        traj_data = pd.DataFrame(f["trajectories_data"][:])
        print(
            f"Trajectory data loaded with shape: {traj_data.shape} and columns: {traj_data.columns.tolist()}"
        )

        # Load timeseries features (if present)
        if "timeseries_data" in f:
            timeseries = pd.DataFrame(f["timeseries_data"][:])
            print(
                f"Timeseries data loaded with shape: {timeseries.shape} and columns: {timeseries.columns.tolist()}"
            )

        base_coordinates = f["base_coordinates"][:]
        print(f"Base coordinates: {base_coordinates}")

        neck_x = f["neck_x"][:]
        neck_y = f["neck_y"][:]
        print(
            f"Neck coordinates: ({neck_x[0]}, {neck_y[0]}, ..., {neck_x[-1]}, {neck_y[-1]})"
        )

        # Load odor patch coordinates
        if "food_cnt_coord" in f:
            odor_patch = f["food_cnt_coord"][:]
            print(
                f"Odor patch defined by {len(odor_patch)} boundary points, ({odor_patch[0]}, {odor_patch[1]}, ..., {odor_patch[-1]})"
            )

        # Load skeleton coordinates
        # coords = f['coordinates'][:]  # Shape: (n_frames, n_segments, 2)

    # Creating a 2D plot in matplotlib of the odor patch
    plt.figure(figsize=(6, 6))

    if odor_patch is not None:
        plt.plot(odor_patch[:, 0], odor_patch[:, 1], "r-", label="Odor Patch Boundary")

    strange_scale = 13  # Why is this scaling factor needed? microns to pixels?

    plt.scatter(
        [i * strange_scale for i in traj_data["coord_x"]],
        [i * strange_scale for i in traj_data["coord_y"]],
        s=1,
        c="blue",
        label="Worm centroid trajectory",
    )

    plt.scatter(
        neck_x,
        neck_y,
        s=3,
        c="black",
        label="Worm neck trajectory",
    )

    plt.scatter(
        base_coordinates[:, 0],
        base_coordinates[:, 1],
        s=1,
        c="green",
        label="Base coordinates",
    )

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    plt.title("Dataset: %s" % filepath.split("/")[-2])
    plt.legend()
    plt.axis("equal")
    if save_plot:
        plt.savefig(os.path.join(output_dir, filepath.split("/")[-2] + "_plot.png"))
    if show_plot:
        plt.show()


if __name__ == "__main__":
    load_dataset(filepath)
