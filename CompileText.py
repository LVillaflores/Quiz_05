filename = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt']
with open('6P.txt', 'w') as outfile:
    for fname in filename:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)