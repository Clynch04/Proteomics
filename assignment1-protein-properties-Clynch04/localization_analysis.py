from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt

def clean_sequence(seq):
    # Replace 'U' (Selenocysteine) with 'C' (Cysteine)
    return seq.replace('U', 'C')

# Load localization results
localization = {}
with open("localization_predictions.csv") as f:
    next(f)  # skip header
    for line in f:
        # Split each line into protein ID and localization
        pid, loc = line.strip().split("\t")
        # Store in dictionary
        localization[pid] = loc

# Group proteins by category
hydro_by_category = {}

for record in SeqIO.parse("methanococcus_maripaludis_proteome.fasta", "fasta"):
    # Parse each protein record
    pid = record.id
    if pid not in localization:
        # Skip if no localization info
        continue

    loc = localization[pid]
    seq = clean_sequence(str(record.seq))
    # Calculate GRAVY score
    analysis = ProteinAnalysis(seq)
    gravy = analysis.gravy()

    # Store GRAVY score by localization category
    hydro_by_category.setdefault(loc, []).append(gravy)

# Plot distributions
plt.figure(figsize=(8, 6))

for loc, values in hydro_by_category.items():
    plt.hist(
        values,
        bins=30,
        alpha=0.5,
        label=f"{loc} (n={len(values)})"
    )

plt.xlabel("GRAVY score (Kyte–Doolittle)")
plt.ylabel("Number of proteins")
plt.title("Hydrophobicity (GRAVY) distributions by predicted localization")
plt.legend()
plt.tight_layout()
plt.savefig("hydrophobicity_distribution.jpg", dpi=300)  # Save the figure as a .jpg file
plt.show()
