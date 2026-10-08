from chimerax.core.commands import run

# Change to the directory containing the PDB files
run(session, "cd 'C:/Users/Connor Lynch/Proteomics/assignment8-protein-structure-prediction-Clynch04'")

# Open the experimentally validated complex and the first assembly
run(session, "open 1brs")
run(session, "sym #1 assembly 1")
run(session, "color #2.1 cyan")

# Open the alphafoldserver predicted structure
run(session, "open Alphafold_1brs.cif")
run(session, "color #3 magenta")

# Hide atoms for better visualization
run(session, "hide atoms")

# Show cartoon representation for all structures
run(session, "show cartoons")

# Align Swissprot to 3n1r (reference)
run(session, "matchmaker #3 to #2.1")