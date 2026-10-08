from Bio import SeqIO
from Bio.SeqUtils import molecular_weight
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import csv

# lists to collect protein IDs and molecular weights
proteins = []
mw_list = []
pI_list = []

# parsing a FASTA file with protein sequences
for record in SeqIO.parse(
    "methanococcus_maripaludis_proteome.fasta", "fasta"
):
    # calculating molecular weight for each protein sequence
    mw = molecular_weight(record.seq, seq_type="protein")
    # storing protein IDs and molecular weights
    proteins.append(record.id)
    mw_list.append(mw)
    #print(f"{record.id}\t{mw}")

    # creating a ProteinAnalysis object for each protein sequence
    analysis = ProteinAnalysis(record.seq)
    # calculating the isoelectric point (pI)
    pI = analysis.isoelectric_point()
    pI_list.append(pI)
    #print(f"{record.id}\t{pI:.2f}")

# to write them into a file, you first have to open a file:
with open("protein_properties.csv", "w") as csv_out:
    # then you can use the csv DictWriter class to define how the csv should look like
    writer = csv.DictWriter(
        csv_out, fieldnames=["Protein ID", "MW", "pI"], lineterminator="\n"
    )
    # and then you can write the header
    writer.writeheader()
    # now you can iterate over the protein entries and write them into a csv:
    for n, prot in enumerate(proteins):
        writer.writerow({"Protein ID": prot, "MW": mw_list[n], "pI": pI_list[n]})

import matplotlib.pyplot as plt
import seaborn as sns

# Plot Molecular Weight Distribution
plt.figure(figsize=(10, 5))
sns.histplot(mw_list, bins=50, kde=True)
plt.title("Distribution of Molecular Weights")
plt.xlabel("Molecular Weight (Da)")
plt.ylabel("Frequency")
plt.savefig("mw.jpg", dpi=300)  # Save the figure as a .jpg file
#plt.show()

# Plot Isoelectric Point Distribution
plt.figure(figsize=(10, 5))
sns.histplot(pI_list, bins=50, kde=True)
plt.title("Distribution of Isoelectric Points (pI)")
plt.xlabel("Isoelectric Point (pI)")
plt.ylabel("Frequency")
plt.savefig("pI.jpg", dpi=300)  # Save the figure as a .jpg file
#plt.show()