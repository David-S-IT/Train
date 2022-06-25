from solution import Armor, GhostInArmor
from solution_train import train

# ar = Armor(("helmet", 1), ("glove", 2))
# ar.add("bib")
# print(ar)
# print()
# ar = Armor()
# ar.add("bib")
# print(ar)
# print()
# print(Armor())





# ar = GhostInArmor(("helmet", 1), ("glove", 2))
# ar.add("bib")
# print(ar)
# print()
# ar = GhostInArmor()
# ar.add("bib")
# print(ar)
# print()
# print(GhostInArmor())
















# gia = GhostInArmor(("knee pad", 2), ("handlebar", 1), ("shoe", 1), name="Ghost")
# # gia = GhostInArmor()
# gia.add("bib")
# gia.add("bib")
# gia.add("bib2")
# print(gia)
#
# print()
#
# print(gia["knee pad"])
# del gia["bib"]
# del gia["helmet"]
# del gia["knee pad"]
# print(gia["knee pad"])
# print(gia)
#
# print()
#
# for piece in gia:
#     print(piece)
#
# print()
#
# print(gia.items())
# print(type(gia.items()))
#
# print()
#
# # del gia["handlebar"], gia["shoe"], gia["sdfsdc"]
# print(len(gia))




train("out.png")
