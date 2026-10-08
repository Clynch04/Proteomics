from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def clean_sequence(seq):
    # Replace 'U' (Selenocysteine) with 'C' (Cysteine) for simplicity
    # This ensures compatibility with ProtParam methods
    return seq.replace('U', 'C')

def average_hydrophobicity(seq):
    # Calculate average hydrophobicity (GRAVY score) using Kyte-Doolittle scale
    seq = clean_sequence(seq)
    return ProteinAnalysis(seq).gravy()

def has_signal_peptide(seq):
    # Simple heuristic for signal peptide detection:
    # Check first 30 amino acids for positive charge and hydrophobicity
    n_term = clean_sequence(seq[:30])
    pos_charge = sum(n_term.count(x) for x in "KR")
    hydro = average_hydrophobicity(n_term)
    # A simple threshold for signal peptide presence
    return pos_charge >= 1 and hydro > 1.2

def count_tm_helices(seq, window=20, threshold=1.6):
    # Count transmembrane helices using a sliding window approach
    seq = clean_sequence(seq)
    count = 0
    in_helix = False

    for i in range(len(seq) - window):
        # Calculate hydrophobicity for the current window
        window_seq = seq[i:i + window]
        hydro = average_hydrophobicity(window_seq)

        if hydro > threshold and not in_helix:
            count += 1
            in_helix = True
        elif hydro <= threshold:
            in_helix = False

    return count

def classify_protein(seq):
    # Classify protein localization based on signal peptide and TM helices
    tm_count = count_tm_helices(seq)
    sp = has_signal_peptide(seq)

    if sp and tm_count <= 1:
        return "Secreted"
    elif tm_count > 1:
        return "Membrane"
    else:
        return "Cytoplasmic"

def predict_localization(
    # Predict protein localization for sequences in a FASTA file
    fasta_file="methanococcus_maripaludis_proteome.fasta",
    output_file="localization_predictions.csv"
):
    results = []
    # Iterate over each protein sequence in the FASTA file
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq)
        localization = classify_protein(seq)
        # Store the prediction results
        results.append((record.id, localization))

    with open(output_file, "w") as out:
        # Write header
        out.write("Protein_ID\tLocalization\n")
        for pid, loc in results:
            # Write each prediction
            out.write(f"{pid}\t{loc}\n")

    print(f"Predictions saved to: {output_file}")
    return results

if __name__ == "__main__":
    predict_localization(
        fasta_file="methanococcus_maripaludis_proteome.fasta",
        output_file="localization_predictions.csv"
    )
