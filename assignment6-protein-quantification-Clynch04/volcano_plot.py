# This script was generated with the help of ChatGPT
import pandas as pd
import sys
import plotly.express as px
import numpy as np

pd.options.mode.chained_assignment = None


def group_columns_from_tsv(file_path):
    # Read the TSV file
    df = pd.read_csv(file_path, sep="\t")

    # Identifying the groups
    groups = []
    start_col = "Protein Group"
    end_col = "False Discovery Rate"

    current_group = []
    collecting = False

    for col in df.columns:
        if col.startswith(start_col):
            collecting = True
            current_group = [col]
        elif collecting:
            current_group.append(col)
            if col.startswith(end_col):
                groups.append(current_group)
                collecting = False
    # Creating separate data frames using 'Treatment Condition' as the name
    grouped_dfs = {}
    for group in groups:
        for col in group:
            if col.startswith("Treatment Condition"):
                condition_name = df.loc[0, col]
        grouped_dfs[condition_name] = df[group]

    return grouped_dfs


def create_volcano_plot(df, condition_name):
    # Adjust naming of columns
    # Transform "Posterior Error Probability" to -log10
    for col in df.columns:
        if col.startswith("Posterior Error Probability"):
            df["-log10_Posterior_Error_Probability"] = -np.log10(df[col])
        elif col.startswith("Protein Log2 Fold-Change"):
            df["Protein Log2 Fold-Change"] = df[col]
        elif col.startswith("Protein Group"):
            df["Protein Group"] = df[col]

    # Remove rows where "Posterior Error Probability" is 0
    df = df[df["-log10_Posterior_Error_Probability"] > 0]

    # Create a new column to indicate point color (red, green, or default)
    df["color"] = "blue"  # Default color

    # Apply red color to points where "Protein Log2 Fold-Change" < -1 and "-log10_Posterior_Error_Probability" > 2
    df.loc[
        (df["Protein Log2 Fold-Change"] < -1)
        & (df["-log10_Posterior_Error_Probability"] > 2),
        "color",
    ] = "red"

    # Apply green color to points where "Protein Log2 Fold-Change" > 1 and "-log10_Posterior_Error_Probability" > 2
    df.loc[
        (df["Protein Log2 Fold-Change"] > 1)
        & (df["-log10_Posterior_Error_Probability"] > 2),
        "color",
    ] = "green"

    # Create volcano plot using Plotly
    fig = px.scatter(
        df,
        x="Protein Log2 Fold-Change",
        y="-log10_Posterior_Error_Probability",
        title=f"Volcano Plot for {condition_name}",
        labels={
            "Protein Log2 Fold-Change": "Log2 Fold-Change",
            "-log10_Posterior_Error_Probability": "-Log10(Posterior Error Probability)",
        },
        color="color",  # Use the "color" column to color the points
        color_discrete_map={
            "blue": "blue",
            "red": "red",
            "green": "green",
        },  # Map colors to points
        hover_data=["Protein Group"],  # Include "Protein Group" in the hover information
    )

    # Customize the appearance of the volcano plot
    fig.update_traces(
        marker=dict(size=7, opacity=0.7, line=dict(width=1, color="DarkSlateGrey")),
        selector=dict(mode="markers"),
    )
    # Update layout for white background and black axis lines
    fig.update_layout(
        plot_bgcolor="white",  # Set the plot background color to white
        paper_bgcolor="white",  # Set the paper background color to white
        xaxis=dict(
            showline=True, linecolor="black"
        ),  # Set the x-axis line color to black
        yaxis=dict(
            showline=True, linecolor="black"
        ),  # Set the y-axis line color to black
        title_font=dict(size=16),  # Optional: Adjust title font size
    )

    # Save the plot as an HTML file
    fig.write_html(f"{condition_name}_volcano_plot.html")


if __name__ == "__main__":
    file_path = sys.argv[1]
    grouped_dataframes = group_columns_from_tsv(file_path)

    # For each group in grouped_dfs, generate a volcano plot
    for name, group_df in grouped_dataframes.items():
        print(f"{name}:\n", group_df.head())
        create_volcano_plot(group_df, name)
