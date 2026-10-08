# Proteomics In Silico Digestion and LC-HPLC Analysis

## Overview

This project performs an in silico analysis of protein digestion and chromatographic separation, simulating a typical proteomics sample processing workflow. The analysis includes:

1. **Tryptic Digestion**: In silico digestion of all proteins in a FASTA file using trypsin
2. **Non-Proteotypic Peptide Analysis**: Identification of peptides shared between multiple proteins
3. **Peptide Length Analysis**: Investigation of how peptide length affects proteotypicity
4. **Retention Time Prediction**: Machine learning-based prediction of C18 RP-HPLC retention times using DeepLC
5. **Peak Overlap Analysis**: Theoretical calculation of peptide elution peak overlaps under Gaussian distribution

## Requirements

### Required Packages
- `biopython` - FASTA file parsing and sequence handling
- `pyteomics` - Proteolytic enzyme cleavage prediction (trypsin digestion)
- `deeplc` - Machine learning model for retention time prediction
- `pandas` - Data manipulation and analysis
- `matplotlib` - Data visualization and plotting
- `numpy` - Numerical computing

### Installation

Install all required packages using pip:

```bash
pip install biopython pyteomics deeplc pandas matplotlib numpy
```

## Input Data

### Reference Genome/Proteome
The analysis uses the **Methanococcus maripaludis** reference proteome, saved as `methanococcus_maripaludis_proteome.fasta`

## Usage

### Running the Analysis

Open the Jupyter notebook in your environment:

```bash
jupyter notebook lab3.ipynb
```

Then execute the cells in order:

1. **Cell 1-2**: Import required libraries
2. **Cell 3-6**: Perform tryptic digestion and build peptide dictionary
3. **Cell 7**: Calculate percentage of non-proteotypic peptides
4. **Cell 8**: Generate plots analyzing peptide length vs. proteotypicity
5. **Cell 9-10**: Prepare data for DeepLC
6. **Cell 11**: Predict retention times using DeepLC machine learning model
7. **Cell 12**: Visualize retention time distributions
8. **Cell 13**: Calculate and compare peak overlap percentages for different conditions

### Expected Output

- **Console Output**: Peptide dictionary, non-proteotypic percentages, retention time statistics, peak overlap analysis
- **Plots Generated**:
  - Length distribution of non-proteotypic peptides (histogram)
  - Percentage of non-proteotypic peptides by length (line plot)
  - Distribution of predicted retention times (histogram)

## Task Details

### Task 1: Tryptic Digestion
Performs in silico cleavage of all protein sequences using trypsin enzyme rules (cleaves after K and R, unless followed by P).

### Task 2: Non-Proteotypic Peptides
Identifies and quantifies peptides found in multiple proteins. These shared peptides cannot uniquely identify a single protein in proteomics experiments.

### Task 3: Length vs. Proteotypicity
Analyzes whether longer peptides are more likely to be proteotypic (unique to a single protein) through visualization.

### Task 4: Retention Time Prediction
Uses DeepLC, a deep learning model trained on experimental retention time data, to predict C18 RP-HPLC retention times for all unique peptides (0-60 min scale).

### Task 5: Peak Overlap Analysis
Calculates the percentage of peptides with theoretically overlapping elution peaks under Gaussian distribution assumptions for two scenarios:
- **Scenario 1**: 60 min retention window, 30 second peak width
- **Scenario 2**: 120 min retention window, 35 second peak width (increased diffusion)

