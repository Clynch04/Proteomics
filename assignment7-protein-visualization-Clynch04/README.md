[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HpJmo7r6)
# Assignment Week 9: Protein Structure Visualization with ChimeraX

## Introduction
This assignment involves visualizing protein structures using ChimeraX, exploring the Protein Data Bank, and creating scripts to automate visualization of protein structures and their interactions. All Python scripts are designed to be executed within ChimeraX using the command:
`
runscript <file_path>
`

## Protein Structures Used
The assignment utilizes **Lysozyme (PDB ID: 1HEW)** and **Adenylate Kinase (PDB IDs: 1AKE and 4AKE)** structures from the Protein Data Bank to demonstrate various visualization techniques and protein-ligand interactions.

## Input Data
You can use any protein structure in the Protein Data Bank (PDB) as your starting point, since ChimeraX can directly fetch protein structures from PDB. You can use the search function on the PDB website to identify a structure that you want to work with. Select a structure that allows you to visualize e.g. an enzyme-substrate interaction, or a receptor-ligand interaction, or the DNA binding of a protein, or a protein-protein interaction.

## Solutions by Task

### Tasks 2 & 3: Secondary Structure Highlighting and Hydrogen Bonds
**Script:** helix_hbonds.py

This script accomplishes both tasks 2 and 3 by:
- Opening the lysozyme structure (1HEW) in ChimeraX
- Selecting all α-helices in the protein
- Highlighting the helices with green color for easy visualization
- Displaying all hydrogen bonds within the selected helices using ChimeraX's built-in hydrogen bond detection

**Usage:**
`
runscript helix_hbonds.py
`

---

### Task 4: Protein-Ligand Interactions (Part 1 - Hydrogen Bonds)
**Script:** hbond_interaction.py

This script visualizes hydrogen bonding between the protein and its ligand substrate:
- Opens the lysozyme + substrate structure (1HEW)
- Identifies and displays all hydrogen bonds between the protein and ligand
- Selects the ligand and zooms in for detailed visualization of the binding interaction

**Usage:**
`
runscript hbond_interaction.py
`

---

### Task 4: Protein-Ligand Interactions (Part 2 - Charge Interactions)
**Script:** charge_interaction.py

This script visualizes multiple types of interactions between the protein and its ligand:
- Opens the lysozyme + substrate structure (1HEW)
- Displays hydrogen bonds between the protein and ligand
- Shows electrostatic/coulombic interactions (charge interactions) using ChimeraX's coulombic coloring
- Selects the ligand and zooms in to focus on the interaction region

**Usage:**
`
runscript charge_interaction.py
`

---

### Task 7: Protein Conformational Animation
**Script:** animation.py

This script creates a dynamic animation showing structural changes in a protein:
- Opens two different conformations of adenylate kinase (1AKE: open form, 4AKE: closed form)
- Superimposes the two structures for alignment
- Creates a morphing animation that transitions between the open and closed conformations

**Usage:**
`
runscript animation.py
`

---

## Running the Scripts

All scripts are executed within ChimeraX using the runscript command. Ensure ChimeraX is open with an active session before executing any script. Each script is self-contained and includes comments explaining the visualization steps.

Example ChimeraX workflow:
1. Open ChimeraX
2. In the ChimeraX command line, run: runscript path/to/script.py
3. The script will automatically fetch the protein structure(s) and apply the visualization parameters