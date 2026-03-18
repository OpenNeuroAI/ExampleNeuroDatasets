from ideas import load_dataset
import os

readme = "# Plotting all datasets\n\nThis script iterates through all the datasets in the `Chemotaxis-Data-and-Analysis` folder, loads each one using the `load_dataset` function from `ideas.py`, and saves a plot for each dataset in an `images` folder."
output_dir = "images"

for conditions in ["Mock_worms", "Aversive_worms", "sexually_conditioned_worms"]:
    print(f"Processing condition: {conditions}...")

    dirnames = f"Chemotaxis-Data-and-Analysis/{conditions}"

    readme += f"\n\n## {conditions}\n\n"

    for dirname in os.listdir(dirnames):
        print(f"    Processing {dirname}...")
        hdf_file = os.path.join(
            dirnames, os.path.join(dirname, "metadata_featuresN_oneworm.hdf5")
        )
        print(f"        Looking for file: {hdf_file}...")
        if os.path.isfile(hdf_file):
            print(f"        Loading dataset from: {hdf_file}...")

            readme += f"### Dataset: {dirname}\n\n"
            readme += f"![Plot for {dirname}](./{dirname}_plot.png)\n\n"

            load_dataset(
                hdf_file, show_plot=False, save_plot=True, output_dir=output_dir
            )


with open(os.path.join(output_dir, "README.md"), "w") as f:
    f.write(readme)
