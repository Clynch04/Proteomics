from chimerax.core.commands import run

# open lysozyme + substrate structure
run(session, "open 1HEW")
# select alpha helix
run(session, "select helix")
# color selected helixes
run(session, "color sel green")
# show hydrogen bonds between alpha helices
run(session, "hbonds sel")
