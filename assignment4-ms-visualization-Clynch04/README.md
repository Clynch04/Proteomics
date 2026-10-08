# MS Visualization Assignment - Week 5

## Overview

This project implements proteomics workflows to visualize and interpret mass spectrometry (MS) data. The assignment involves in silico peptide digestion, theoretical m/z calculation, matching against measured spectra, and creating extracted ion chromatograms (EICs) to visualize peptide detection across a LC-MS run.

## Files

### Jupyter Notebooks
- **`lab5_BS.ipynb`** - Core tasks for all students (Tasks 1-7):
  - In silico tryptic digest of Methanococcus maripaludis proteome
  - Theoretical m/z calculation for peptide ions (charge states +2, +3)
  - MS1 spectrum analysis with peptide matching (10 ppm tolerance)
  - MS2 precursor ion identification
  - Visualization of matched peaks in mass spectra

- **`lab5_MS.ipynb`** - Advanced MS tasks (Task 8):
  - Selects a single protein with ≥5 peptides
  - Extracts intensities for all matching peptide ions across the entire LC-MS run
  - Generates extracted ion chromatograms (EICs) with retention time information
  - Marks MS2 fragmentation events on the EICs for each peptide

### Reference Data
- **`methanococcus_maripaludis_proteome.fasta`** - Reference proteome FASTA file containing all proteins from Methanococcus maripaludis
- **`2020-08-16_I3_0_2.mzML`** - Raw mass spectrometry data in mzML format (from dataset PXD047095) - **NOT included** due to large file size. Download from PXD047095 if needed.

### Image Data
- **`spectrum_peak_match.png`** - Screenshot taken of the result of task 3, zoomed in on the target mz value match and red triangle.

## Setup

### Requirements

Install the following Python packages:

```bash
pip install pyteomics holoviews biopython pymzml pandas
```

**Package Descriptions:**
- **pyteomics** - Proteomics data analysis library for peptide digestion and mass calculations
- **biopython** - Bioinformatics toolkit for parsing FASTA files
- **pymzml** - Parser for mzML mass spectrometry data files
- **holoviews** - Interactive visualization library for creating EIC plots
- **pandas** - Data manipulation and analysis

### Running the Code

1. **Ensure the following data file is in the same directory as the notebooks:**
   - `methanococcus_maripaludis_proteome.fasta`
   
   **Note:** The mzML file (`2020-08-16_I3_0_2.mzML`) is not included due to its large size but is required to run the MS tasks. Download it from dataset PXD047095 and place it in the same directory.

2. **Run the BS tasks notebook first:**
   ```bash
   jupyter notebook lab5_BS.ipynb
   ```
   Execute all cells sequentially. This notebook will:
   - Generate theoretical peptide ions from in silico digestion
   - Show peptide matching statistics
   - Display matched peaks in MS1 spectra

3. **Run the MS tasks notebook next:**
   ```bash
   jupyter notebook lab5_MS.ipynb
   ```
   This notebook builds on the BS tasks and will:
   - Select a protein for detailed analysis
   - Extract intensity data across the entire run
   - Display interactive extracted ion chromatograms with MS2 selection points marked

## Workflow Overview

### Task 1-3: Peptide Digestion and MS1 Matching
- In silico tryptic digest of the reference proteome
- Calculate monoisotopic m/z for each peptide (charges +2, +3)
- Match theoretical ions to observed MS1 peaks (10 ppm tolerance)
- Visualize matches in the mass spectrum

### Task 4: MS2 Precursor Analysis
- Extract precursor m/z and charge from all MS2 scans
- Count MS2 scans corresponding to M. maripaludis peptides

### Task 8: MS Student Task - EIC Generation
- Select a single protein with at least 5 tryptic peptides
- Extract all matching peak intensities across all MS1 scans
- Generate extracted ion chromatograms (EICs) for each peptide
- Overlay MS2 fragmentation events (shown as red markers)
- Interactive holoviews visualization with zoom and pan capabilities

## Output

The notebooks generate:
- Print summaries of matched peptide ions
- Interactive holoviews visualizations of EICs
- Mass spectrum plots with highlighted matches





