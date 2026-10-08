from chimerax.core.commands import run

# open adenylate kinase structure (open and closed conformations)
run(session, "open 1AKE 4AKE")
# superimpose the two structures
run(session, "matchmaker #1 to #2")
# create a morph animation between the two structures
run(session, "morph #1, 2")