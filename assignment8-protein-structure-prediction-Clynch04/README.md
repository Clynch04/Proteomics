# Assignment Week 10: Protein Structure Prediction Comparison

## Overview
This assignment compares three structure prediction methods on modified protein sequences using homology modeling and machine learning-based prediction tools. Two sets of analyses are included: BS tasks (single protein) and MS task (protein complex).

---

## BS Tasks: Single Protein Analysis (3N1R - Sonic Hedgehog Protein)

### Task 1: Sequence Modification
**Protein**: 3N1R (Sonic Hedgehog protein)  
**Modification Strategy**: Introduced prolines (P) and glycines (G) into secondary structures to disrupt local structure.  
**Note**: Limited number of substitutions resulted in minimal structural change.  
**Details**: See "Original vs. Modified.pdf" for exact sequence changes.

### Task 2: Homology Modeling Result
**Output**: `Swissprot.pdb`  
Generated using Swiss-Model with the modified sequence.

### Task 3: AlphaFold Prediction Result
**Output**: `alphafold_3n1r.pdb`  
Generated using AlphaFold with the modified sequence.

### Tasks 4-6: Structure Alignment & Visualization
**Script**: `BS_Scripts.py`

This script automatically:
1. Opens the original 3N1R structure, Swiss-Model prediction, and AlphaFold prediction
2. Aligns all three structures using ChimeraX's matchmaker (paired alignment to 3N1R as reference)
3. Selects and highlights residues with sequence modifications (105-106, 112-113, 160-161, 165-166, 182-183; P, G, P, P, P)
4. Colors modified regions in green for easy visualization
5. Zooms to the modified areas

#### How to Run:
1. Open ChimeraX
2. Edit `BS_Scripts.py` and update the file path at the top to match your directory:
   ```python
   run(session, "cd C:/path/to/your/directory")
   ```
3. In ChimeraX command line, run:
   ```
   runscript "path/to/BS_Scripts.py"
   ```
4. The three structures will load, align, and highlight the modified regions.

---

## MS Task: Protein Complex Analysis (1BRS - Barnase-Barstar Complex)

### Task 9: Complex Structure Prediction
**Protein Complex**: 1BRS (Barnase-Barstar complex)  
**Prediction Method**: AlphaFold (via alphafoldserver.com)  
**Output**: `Alphafold_1brs.cif`  

Predicted the quaternary structure of the complex using individual FASTA sequences for each polymer and compared with the experimental structure.

#### How to Run:
**Script**: `MS_Scripts.py`

This script automatically:
1. Opens the experimentally validated 1BRS structure (with correct assembly selected)
2. Loads the AlphaFold-predicted complex structure
3. Superimposes the predicted structure onto the experimental one for comparison

1. Edit `MS_Scripts.py` and update the file path to your directory
2. In ChimeraX command line, run:
   ```
   runscript "path/to/MS_Scripts.py"
   ```
3. Compare the predicted and experimental structures visually in ChimeraX.

---

## Deliverables

### Files Included:
- **3n1r.pdb1** – Original experimental structure (PDB entry 3N1R)
- **Swissprot.pdb** – Swiss-Model homology modeling result
- **alphafold_3n1r.pdb** – AlphaFold prediction (or similar name)
- **BS_Scripts.py** – ChimeraX script for tasks 4-6 (BS)
- **MS_Scripts.py** – ChimeraX script for task 9 (MS bonus)
- **Original vs. Modified.pdf** – Detailed sequence change documentation
- **Alphafold_1brs.cif** – AlphaFold predicted quaternary structure (MS task)

---

## Key Notes

- Both scripts require **ChimeraX** to be installed and the correct file paths in the scripts
- Use the `runscript` command to execute scripts in ChimeraX
- Forward slashes (`/`) work best for file paths in scripts
- Default reference structure for alignment: 3N1R for BS task; 1BRS for MS task

