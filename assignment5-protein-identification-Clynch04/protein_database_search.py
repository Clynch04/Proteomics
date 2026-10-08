#!/usr/bin/env python3
# encoding: utf-8
import ursgal
import sys
import glob
import os


def main(folder=None, target_decoy_database=None):
    """
    An example test script to search all mzML files which are present in the
    specified folder. The search is currently performed on 3 search engines.

    The digestion enzyme has to be specified as well as the target-decoy
    database.

    usage:

        ./do_it_all_folder_wide.py <mzML_folder> <target_decoy_database>

    """
    # define folder with mzML_files as sys.argv[1]
    mzML_files = []
    for mzml in glob.glob(os.path.join("{0}".format(folder), "*.mzML")):
        mzML_files.append(mzml)

    # We specify all search engines and validation engines that we want to use in a list
    # (version numbers might differ on windows or mac):
    search_engines = [
        "xtandem_alanine",
        "msfragger_3_0",
        #"msgfplus_v9979",
        "msgfplus_2019_07_03",
        "omssa_2_1_9",
    ]

    validation_engine = "percolator_3_4_0"

    # Modifications that should be included in the search
    all_mods = [
        "C,fix,any,Carbamidomethyl",
        "M,opt,any,Oxidation",
        "*,opt,Prot-N-term,Acetyl",
        "*,opt,Prot-N-term,Formyl",
        "E,opt,any,Glu->pyro-Glu",
        "Q,opt,any,Gln->pyro-Glu",
    ]

    # Initializing the Ursgal UController class with
    # our specified modifications and mass spectrometer
    params = {
        "database": target_decoy_database,
        "enzyme": "trypsin",
        "modifications": all_mods,
        "precursor_mass_tolerance_minus": 5,
        "precursor_mass_tolerance_plus": 5,
        "precursor_mass_tolerance_unit": "ppm",
        "frag_mass_tolerance": 15,
        "frag_mass_tolerance_unit": "ppm",
        "csv_filter_rules": [
            ["Is decoy", "equals", "false"],
            ["PEP", "lte", 0.01],
        ],
        "cpus": 1,
        "-xmx": "4g",
        "calibrate_mass": True,
    }

    uc = ursgal.UController(params=params)

    # complete workflow:
    # every spectrum file is searched with every search engine,
    # results are validated (for each engine seperately),
    # validated results are merged and filtered for targets and PEP <= 0.01.
    # In the end, all filtered results from all spectrum files are merged
    result_files = []
    for spec_file in mzML_files:
        validated_results = []
        for search_engine in search_engines:
            unified_search_results = uc.search(
                input_file=spec_file,
                engine=search_engine,
            )
            validated_csv = uc.validate(
                input_file=unified_search_results,
                engine=validation_engine,
            )
            validated_results.append(validated_csv)

        validated_results_from_all_engines = uc.execute_misc_engine(
            input_file=validated_results,
            engine="merge_csvs_1_0_0",
        )
        filtered_validated_results = uc.execute_misc_engine(
            input_file=validated_results_from_all_engines,
            engine="filter_csv_1_0_0",
        )
        result_files.append(filtered_validated_results)

    results_all_files = uc.execute_misc_engine(
        input_file=result_files,
        engine="merge_csvs_1_0_0",
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(main.__doc__)
        sys.exit(1)
    main(
        folder=sys.argv[1],
        target_decoy_database=sys.argv[2],
    )
