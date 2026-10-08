#!/usr/bin/env python
import pathlib
import sys
import ursgal
import os
import glob

# usage:  python PXD047095_quant.py <path/to/mzml_folder> <path/to/merged_evidence_file.csv>


def main(mzml_folder, merged_result):
    params = {
        "isotopic_distribution_tolerance": 5,
        "normalize_intensities": True,
        "integrate_peak_areas": False,
        "only_precursor_charge": False,
        "match_between_runs": True,
        "match_between_runs_RT_window": 0.5,  # maybe 1?
        "require_msms_id": False,
        "bayesian_fold_change": True,
        "bayesian_fold_change_control_condition": "Culture_0",
        "fold_change_cutoff": 0.1,
        "markov_chain_iterations": 3000,
        "markov_chain_burn_in_iterations": 1000,
        "use_shared_peptides": True,
        "random_seed": 200,
    }
    uc = ursgal.UController(
        verbose=True,
        params=params,
        profile="QExactive+",
    )

    experiment_setup = {
        "1": {
            "FileName": "2020-08-16_I3_0_2",
            "Condition": "Culture_0",
            "Biorep": 1,
            "Fraction": 1,
            "Techrep": 1,
        },
        "2": {
            "FileName": "2020-08-16_I3_0_3",
            "Condition": "Culture_0",
            "Biorep": 2,
            "Fraction": 1,
            "Techrep": 1,
        },
        "3": {
            "FileName": "2020-08-16_I3_0_4",
            "Condition": "Culture_0",
            "Biorep": 3,
            "Fraction": 1,
            "Techrep": 1,
        },
        "4": {
            "FileName": "2020-08-16_I3_0_5",
            "Condition": "Culture_0",
            "Biorep": 4,
            "Fraction": 1,
            "Techrep": 1,
        },
        "5": {
            "FileName": "2020-08-16_I3_0_6",
            "Condition": "Culture_0",
            "Biorep": 5,
            "Fraction": 1,
            "Techrep": 1,
        },
        "6": {
            "FileName": "2020-08-16_I3_1_1",
            "Condition": "Culture_1",
            "Biorep": 1,
            "Fraction": 1,
            "Techrep": 1,
        },
        "7": {
            "FileName": "2020-08-16_I3_1_2",
            "Condition": "Culture_1",
            "Biorep": 2,
            "Fraction": 1,
            "Techrep": 1,
        },
        "8": {
            "FileName": "2020-08-16_I3_1_3",
            "Condition": "Culture_1",
            "Biorep": 3,
            "Fraction": 1,
            "Techrep": 1,
        },
        "9": {
            "FileName": "2020-08-16_I3_1_4",
            "Condition": "Culture_1",
            "Biorep": 4,
            "Fraction": 1,
            "Techrep": 1,
        },
        "10": {
            "FileName": "2020-08-16_I3_1_5",
            "Condition": "Culture_1",
            "Biorep": 5,
            "Fraction": 1,
            "Techrep": 1,
        },
        "11": {
            "FileName": "2020-08-16_I3_2_1",
            "Condition": "Culture_2",
            "Biorep": 1,
            "Fraction": 1,
            "Techrep": 1,
        },
        "12": {
            "FileName": "2020-08-16_I2_2_2",
            "Condition": "Culture_2",
            "Biorep": 2,
            "Fraction": 1,
            "Techrep": 1,
        },
        "13": {
            "FileName": "2020-08-16_I3_2_3",
            "Condition": "Culture_2",
            "Biorep": 3,
            "Fraction": 1,
            "Techrep": 1,
        },
        "14": {
            "FileName": "2020-08-16_I3_2_4",
            "Condition": "Culture_2",
            "Biorep": 4,
            "Fraction": 1,
            "Techrep": 1,
        },
        "15": {
            "FileName": "2020-08-16_I3_2_5",
            "Condition": "Culture_2",
            "Biorep": 5,
            "Fraction": 1,
            "Techrep": 1,
        },
        "16": {
            "FileName": "2020-08-16_I3_8_1",
            "Condition": "Culture_8",
            "Biorep": 1,
            "Fraction": 1,
            "Techrep": 1,
        },
        "17": {
            "FileName": "2020-08-16_I3_8_2",
            "Condition": "Culture_8",
            "Biorep": 2,
            "Fraction": 1,
            "Techrep": 1,
        },
        "18": {
            "FileName": "2020-08-16_I3_8_3",
            "Condition": "Culture_8",
            "Biorep": 3,
            "Fraction": 1,
            "Techrep": 1,
        },
        "19": {
            "FileName": "2020-08-16_I3_8_4",
            "Condition": "Culture_8",
            "Biorep": 4,
            "Fraction": 1,
            "Techrep": 1,
        },
        "20": {
            "FileName": "2020-08-16_I3_8_5",
            "Condition": "Culture_8",
            "Biorep": 5,
            "Fraction": 1,
            "Techrep": 1,
        },
    }

    uc.params["csv_filter_rules"] = [
        ["Protein ID", "contains", "Methanococcus maripaludis"]
    ]

    filtered_search_results = uc.execute_misc_engine(
        input_file=merged_result,
        engine="filter_csv_1_0_0",
    )

    uc.params["experiment_setup"] = experiment_setup
    uc.params["quantification_evidences"] = filtered_search_results
    mzml_files = []
    for mzml in glob.glob(os.path.join(mzml_folder, "*.mzML")):
        mzml_files.append(mzml)

    quantified_peaks = uc.quantify(
        input_file=mzml_files, multi=True, engine="flash_lfq_1_1_1", force=True
    )


if __name__ == "__main__":
    main(
        sys.argv[1],
        sys.argv[2],
    )
    pass
