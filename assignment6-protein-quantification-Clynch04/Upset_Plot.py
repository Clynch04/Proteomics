import pandas as pd
import sys
import numpy as np
import os
from upsetplot import from_contents, plot
from matplotlib import pyplot as plt

def group_columns_from_tsv(file_path):
    # Reads the TSV file and groups columns based on "Treatment Condition" and "False Discovery Rate".
    df = pd.read_csv(file_path, sep="\t")
    groups = []
    start_col = "Protein Group"
    end_col = "False Discovery Rate"

    current_group = []
    collecting = False

    # Iterate through columns to group them based on the specified start and end markers
    for col in df.columns:
        if col.startswith(start_col):
            collecting = True
            current_group = [col]
        elif collecting:
            current_group.append(col)
            if col.startswith(end_col):
                groups.append(current_group)
                collecting = False

    grouped_dfs = {}
    # For each group, determine the condition name from the "Treatment Condition" column and store the corresponding DataFrame
    for group in groups:
        condition_name = ""
        for col in group:
            if col.startswith("Treatment Condition"):
                condition_name = str(df.loc[0, col])
        grouped_dfs[condition_name] = df[group]
    return grouped_dfs

def get_da_proteins(df):
    # Returns a set of Protein IDs passing thresholds.
    pep_col = [c for c in df.columns if c.startswith("Posterior Error Probability")][0]
    fc_col = [c for c in df.columns if c.startswith("Protein Log2 Fold-Change")][0]
    id_col = [c for c in df.columns if c.startswith("Protein Group")][0]

    # Thresholds: |Log2FC| > 1 and -log10(PEP) > 2
    df['-log10_PEP'] = -np.log10(df[pep_col].replace(0, 1e-10))
    mask = (df[fc_col].abs() > 1.0) & (df['-log10_PEP'] > 2.0)
    
    return set(df.loc[mask, id_col].dropna())

def create_master_outputs(grouped_dfs):
    # Collect DA proteins for each condition and build a master list of all unique DA proteins.
    da_sets = {}
    all_da_proteins = set()

    # 1. Collect all DA proteins per condition
    for name, df in grouped_dfs.items():
        proteins = get_da_proteins(df)
        da_sets[name] = proteins
        all_da_proteins.update(proteins)
        print(f"Condition {name}: {len(proteins)} DA proteins.")

    if not all_da_proteins:
        print("No proteins met the thresholds in any condition.")
        return

    # 2. Build the Master Binary Matrix
    master_list = []
    for prot_id in sorted(list(all_da_proteins)):
        row = {"Protein Group": prot_id}
        for name in da_sets.keys():
            row[name] = 1 if prot_id in da_sets[name] else 0
        master_list.append(row)
    
    master_df = pd.DataFrame(master_list)
    master_df.to_csv("DA_Proteins_Summary.csv", index=False)
    print("\nMaster CSV saved as 'DA_Proteins_Summary.csv'")

    # 3. Generate UpSet Plot
    upset_data = from_contents(da_sets)
    plt.figure(figsize=(12, 8))
    plot(upset_data, subset_size='count', show_counts=True)
    plt.suptitle("Intersection of DA Proteins across Cultures")
    plt.savefig("DA_Proteins_Upset_Plot.png", bbox_inches='tight')
    print("UpSet plot saved as 'DA_Proteins_Upset_Plot.png'")
    #plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py BayesianFoldChangeAnalysis.tsv")
    else:
        file_path = sys.argv[1]
        dataframes = group_columns_from_tsv(file_path)
        create_master_outputs(dataframes)