# Protein Identification Assignment: Lab 6

## Overview 

Protein Database Search & PSM Analysis
This repository contains the workflow for performing a protein database search on Methanococcus maripaludis datasets using the Ursgal framework  and subsequent spectral analysis.

## Important Note on Environment

All analysis was conducted on the Oedipus Server.

Commands: A full list of commands used can be found in commands_used.txt.

File Paths: The file paths in the Python notebooks are hardcoded for the Oedipus environment. If running elsewhere, paths must be updated. They are currently configured to run within: /home/cplcgns/proteomics/lab6

## Requirements

Install the following Python packages:

```bash
pip install pandas numpy pymzml holoviews
```

## Workflow: Bachelor of Science (BS) Tasks

The BS workflow focuses on standard protein identification and identification of unique peptides/proteins.

**Database Generation:**
Generated a target-decoy database using generate_target_decoy_from_fasta.py. This script takes the M. maripaludis proteome and the cRAP (common Repository of Adventitious Proteins) fasta files as input.

**Data Acquisition:**
Copied pointers of the .mzML files from the class directory on the Oedipus server to the local project directory.

**Search & Post-Processing:**
Executed protein_database_search.py using the .mzML folder and the target-decoy FASTA. This handles the search and statistical post-processing (FDR/PEP filtering), outputting a comprehensive CSV file of PSM information.

**Spectral Analysis (bs_lab6.ipynb):**

Converts the resulting CSV into a DataFrame.

Calculates theoretical b- and y-ions for a selected peptide.

Uses pymzml to match these theoretical ions against the experimental peaks in the corresponding .mzML file.

Generates an annotated spectrum plot highlighting matched ions.

## Workflow: Master of Science (MS) Tasks

The MS workflow extends the search to include Post-Translational Modifications (PTMs).

**PTM Search:**
Modified the search parameters in protein_database_search.py to include phosphorylation: "*,opt,any,Phospho".

**Modification Analysis (ms_lab6.ipynb):**

Loads the PTM-aware CSV results.

Identifies PSMs that underwent phosphorylation.

Ion Calculation: Recalculates b- and y-ions, specifically accounting for the m/z shifts caused by the phosphate group.

Visualization: Produces an annotated spectrum where ions with shifted m/z values due to the PTM are bolded or specifically highlighted to demonstrate the shift.

## File Structure
- **`generate_target_decoy_from_fasta.py`**: Script for database generation.

- **`protein_database_search.py`**: Script for search and FDR filtering.

- **`bs_lab6.ipynb`**: Analysis notebook for standard peptides.

- **`ms_lab6.ipynb`**: Analysis notebook for phosphorylated peptides.

- **`commands_used.txt`**: Sequential log of terminal commands.