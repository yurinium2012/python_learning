rw_data = " mAtTHewww, saRAH, BoB, jenIffER, AliCe "

rw_data = rw_data.strip()

names = rw_data.split(",")

cnames = []

for name in names:
    cnames.append(name.strip().title())

if "Bob" in cnames:
    cnames.remove("Bob")

cnames.append("Charlie")
cnames.sort()

index = cnames.index("Jeniffer")

print("final list:", cnames)
print("jennifer is at index:",index)