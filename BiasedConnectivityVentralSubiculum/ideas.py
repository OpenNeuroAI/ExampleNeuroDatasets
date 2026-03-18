# Load a dataset and use plotly to show 3d plots

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


PFC_color = "#FFDB6E"
NAc_color = "#BF43CC"
LH_color = "#87FFE1"

# Load the .csv file for coronal CTB data
df = pd.read_csv("coronal_CTBLabelled_dataset.csv")
df.head(5)

# Filter dataframe by projection type
df_subset_PFC = df[df.Projection == "PFC"]
df_subset_NAc = df[df.Projection == "NAc"]
df_subset_LH = df[df.Projection == "LH"]

opacity = 0.7
size = 2

fig = px.scatter_3d(df_subset_PFC, x="AP", y="ML", z="DV", opacity=opacity)

fig.update_traces(marker_size=size)
fig.update_traces(marker_color=PFC_color)

fig.add_trace(
    go.Scatter3d(
        x=df_subset_NAc["AP"][:],
        y=df_subset_NAc["ML"][:],
        z=df_subset_NAc["DV"][:],
        opacity=opacity,
        mode="markers",
        marker=dict(size=size, color=NAc_color),
        name="NAc",
    )
)

fig.add_trace(
    go.Scatter3d(
        x=df_subset_LH["AP"][:],
        y=df_subset_LH["ML"][:],
        z=df_subset_LH["DV"][:],
        opacity=opacity,
        mode="markers",
        marker=dict(size=size, color=LH_color),
        name="LH",
    )
)

fig["layout"].update(width=1200, height=800, autosize=False)

fig.update_scenes(aspectmode="data")

fig.show()
