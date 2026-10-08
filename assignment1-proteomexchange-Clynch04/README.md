# ProteomeXchange Dataset Analysis

## Overview

This repository contains my solution for the Week 2 assignment on programmatic access to proteomics databases within the ProteomeXchange Consortium. The goal was to search for datasets corresponding to specific species, analyze their distribution across repositories and years, and visualize the results.

## How I Built on the Starting Code

I began with the starter code provided, which demonstrated how to access the OmicsDI API and retrieve proteomics datasets. I extended this code in several ways:

- **Species Search:** Adapted the code to search for three different species: *Methanococcus maripaludis*, *Trametes versicolor*, and *Borrelia burgdorferi*.
- **Year Extraction:** Extracted the publication year from each dataset's metadata.
- **CSV Output:** Wrote the relevant dataset information (ID, repository, title, year, and species) to CSV files for each species.
- **Dataset Count Plots:** Generated bar plots showing the number of datasets per source repository for each species.
- **Yearly Analysis:** Created an additional notebook to combine the CSV outputs and plot the number of datasets published per year for each species, including years with zero datasets.

## How to Run the Code

1. **Install Requirements**  
   Make sure you have the following packages installed:
   - `requests`
   - `pandas`
   - `matplotlib`
   - `csv`
   - `pprint`
   - `numpy`

2. **Run the Species Search Notebooks**  
Execute the following Jupyter notebooks in order. Each will output a CSV file and a plot for its respective species:
- `methanococcus_maripaludis_search.ipynb`
- `trametes_versicolor_search.ipynb`
- `borrelia_burgdorferi_search.ipynb`

3. **Run the Publication Analysis Notebook**  
After generating the CSV files, run:
- `species_publication_analysis.ipynb`

This will produce a grouped bar chart showing the number of datasets per year for each species.

## Assignment Tasks

> 1. Use programmatic access to ProteomeXchange datasets (e.g. through OmicsDI) to find all datasets corresponding to the species Methanococcus maripaludis.  
> 2. Make sure that the analyzed species was indeed Methanococcus maripaludis (e.g. check the species information), and then count the number of datasets for each database that they are extracted from.  
> 3. Repeat steps 1 and 2 for a different species of your choice.  
> 4. Report your findings either as a csv table and as a graph.  
> 5. Make sure to comment your code, so that others can read and understand it easily.  
> 6. Create a README file describing how to run your code. Include requirements (e.g. Python packages that need to be installed) in that description, or as a separate requirements.txt file.  
> 7. Commit all your input files, scripts, and result files to your GitHub Classroom repository.  
> 8. (Bonus) Search for a total of 3 species (including Methanococcus maripaludis) from different genera.  
> 9. (Bonus) Count the number of datasets per year of publication for each species, and display the results in a graph.

## Notes

- All code is commented for clarity.
- The CSV and plot files will be generated in the repository directory after running the notebooks.
- If you have any questions, please let me know!

---