from chimerax.core.commands import run

# open lysozyme + substrate structure
run(session, "open 1HEW")
# show hydrogen bonds between ligand and protein
run(session, "hbonds ligand")
# show charge interactions between ligand and protein
run(session, "coulombic")
# select ligand
run(session, "select ligand")
# zoom in on ligand and its interactions
run(session, "view sel clip false")

