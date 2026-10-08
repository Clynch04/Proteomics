# Protein Properties Analysis for Methanococcus maripaludis

## Files and Scripts

- **mw_pI_calculations.py**  
  Calculates molecular weight and isoelectric point for all proteins in the FASTA file.  
  Outputs:  
  - `protein_properties.csv` (Protein ID, MW, pI)
  - `mw.jpg` (MW distribution plot)
  - `pI.jpg` (pI distribution plot)

- **localization_predictor.py**  
  Predicts protein localization (cytoplasmic, membrane, secreted) based on signal peptide and transmembrane helix heuristics.  I was not able to use either DeepTMHMM or SignalP due to the large size of the file, so this is a very basic script to accomplish the localization predictions.
  Outputs:  
  - `localization_predictions.csv` (Protein ID, Localization)

- **localization_analysis.py**  
  Plots hydrophobicity (GRAVY score) distributions for each predicted localization category.  
  Outputs:  
  - `hydrophobicity_distribution.jpg` (GRAVY score distributions by localization)

## How to Run

1. **Prepare the input:**  
   Download the proteome FASTA file and place it in the project directory as `methanococcus_maripaludis_proteome.fasta`.

2. **Calculate protein properties:**  
   ```
   python mw_pI_calculations.py
   ```
   This generates `protein_properties.csv`, `mw.jpg`, and `pI.jpg`.

3. **Predict protein localization:**  
   ```
   python localization_predictor.py
   ```
   This generates `localization_predictions.csv`.

4. **Analyze and plot hydrophobicity by localization:**  
   ```
   python localization_analysis.py
   ```
   This generates `hydrophobicity_distribution.jpg`.