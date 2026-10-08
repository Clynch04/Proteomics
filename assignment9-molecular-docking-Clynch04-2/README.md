# Assignment 9: Molecular Docking

## Overview
This assignment involved molecular docking using the ligand-receptor complex from PDB ID: 1IEP (CRYSTAL STRUCTURE OF THE C-ABL KINASE DOMAIN IN COMPLEX WITH STI-571). The goal was to prepare input files, perform docking with two different tools, evaluate results, and explore an alternative ligand.

## Task 1: Preparing Input Files
Separate receptor and ligand files were prepared from the original 1IEP structure using ChimeraX.

### Receptor Preparation:
- Opened the 1IEP structure in ChimeraX
- Executed commands: `delete ligand`, `dockprep`
- Saved as `1iep_receptor.pdb`

### Ligand Preparation:
- Selected the ligand: `select ligand`
- Inverted selection: `select ~sel`
- Deleted selected atoms: `delete sel`
- Deleted B chains: `delete /B`
- Used Tools → Structure Editing → Dock Prep with options: "delete solvent", "delete non-metal-complex ions", and "add hydrogens"
- Saved as `1iep_ligand.pdb` and `1iep_ligand.mol2`

These files are located in the `Original_Structures/` folder.

## Task 2: Molecular Docking
Docking was performed using two tools: SwissDock (https://www.swissdock.ch/) and DiffDock (https://build.nvidia.com/mit/diffdock).

### SwissDock:
- Input ligand: `1iep_ligand.mol2`
- Input receptor: `1iep_receptor.pdb`
- Parameters:
  - Box center: 14 -56 -16
  - Box size: 30-30-30
  - Sampling exhaustivity: 15
- Results downloaded as zip, ligand predictions extracted and renamed to `swissdock_ligand.pdb`

### DiffDock:
- Input ligand: `1iep_ligand.mol2`
- Input receptor: `1iep_receptor.pdb`
- Parameters: Generated Poses: 20, Diffusion Steps: 18, Diffusion Time Divisions: 20 (default)
- Results downloaded as zip, ligand predictions extracted and renamed to `diffdock_ligand.pdb`

Docked ligand files are in the `Docking_Result_Structures/` folder.

### Visualization and Screenshots:
- Opened the original 1IEP structure in ChimeraX
- Highlighted the original ligand
- Overlaid the docking prediction files
- Screenshots taken and saved in the `Screenshots/` folder:
  - `SwissDock.png`: All SwissDock predictions
  - `DiffDock.png`: All DiffDock predictions
  - `All_results.png`: All predictions from both tools
  - `SwissDock_Best_Closeup.png`: Closeup of the best SwissDock prediction
  - `DiffDock_Best_Closeup.png`: Closeup of the best DiffDock prediction

## Task 3: Quality Evaluation
The DiffDock results appeared more widely dispersed than SwissDock, likely due to DiffDock generating 20 predictions compared to SwissDock's 10. However, DiffDock included one prediction positioned far outside the complex, indicating a potential error in the tool. The best predictions from both tools aligned well with the original ligand locations.

## Task 5: Alternative Ligand Search (MS Bonus)
Used SwissSimilarity to identify a potential alternative ligand.
- Input: SMILES string of the original ligand
- Compound class: Bioactive
- Parameters:
  - Library screened: CHEMBL
  - Screening method: Combined
- Selected molecule: CHEMBL2386594

## Task 6: Docking Alternative Ligand (MS Bonus)
Performed docking with the alternative ligand using SwissDock, using the same parameters as Task 2 but replacing the ligand input with the CHEMBL2386594 SMILES string.
- Visualized in ChimeraX and compared:
  - `SwissDock_MS.png`: Comparison of the new ligand (MS) with the original ligand
  - `SwissDock_MS_and_BS.png`: Comparison of the new ligand (MS) with the original ligand and the previous SwissDock prediction (BS)

## How to Navigate the Results
- **Original_Structures/**: Contains the prepared input files (`1iep_ligand.mol2`)
- **Docking_Result_Structures/**: Contains the docked ligand prediction files (`swissdock_ligand.pdb`, `diffdock_ligand.pdb`)
- **Screenshots/**: Contains all visual comparisons and evaluations as PNG images

To reproduce or view the results, open the original 1IEP structure in ChimeraX, load the prediction files from `Docking_Result_Structures/`, and refer to the screenshots for reference overlays.
