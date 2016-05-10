import suffixtree

output = [i[:-1] for i in open("stralg-project2-testdata/gene42.out")]
coutput = [i[:-1] for i in open("gene42_2.out")]

i, j = 0, 0
mismatches = []

while i<len(output) and j<len(coutput):
    if output[i]==coutput[j]:
        i += 1
        j += 1
        continue
    else:
        if output[i+1]==coutput[j]:
            mismatches.append(("Given", output[i]))
            i += 1
            continue
        if output[i]==coutput[j+1]:
            mismatches.append(("Found", output[j]))
            j += 1
            continue
        i += 1
        j += 2

for i in mismatches:
    print i
