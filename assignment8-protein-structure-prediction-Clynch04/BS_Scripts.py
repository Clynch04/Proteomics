from chimerax.core.commands import run

# Change to the directory containing the PDB files
run(session, "cd 'C:/Users/Connor Lynch/Proteomics/assignment8-protein-structure-prediction-Clynch04'")

# Open the three PDB structures
run(session, "open Swissprot.pdb")
run(session, "open Alphafold_3n1r.pdb")
run(session, "open 3n1r.pdb1")

# Hide atoms for better visualization
run(session, "hide atoms")

# Align Swissprot to 3n1r (reference)
run(session, "matchmaker #1 to #3")

# Align Alphafold to 3n1r (reference)
run(session, "matchmaker #2 to #3")

# Select areas in original structure that were modified
run(session, "select #3:105-106, 112-113, 160-161, 165-166, 182-183") # P, G, P, P, P respectively

# Color the selection for visualization
run(session, "color sel green")

# Zoom in on the selected areas
run(session, "view sel clip false")