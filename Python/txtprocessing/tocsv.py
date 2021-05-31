import glob
import re
import csv


with open('Data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["PERATURAN", "BAB", "PASAL"])
    for filename in glob.glob('../../DataConverted/*.txt'):
        with open(filename, 'rb') as f:
            data = ' '.join([x.decode('utf-8').strip() for x in f.readlines()])
            splitBAB = re.split(r'\bBAB\b', data)
            realFileName = re.search(r'\\.*\.', filename).group(0)[1:]
            for i in range(len(splitBAB)):
                if i > 0:
                    bab = ' '.join(re.findall(r'\b[A-Z]+\b', splitBAB[i])[:5])
                    splitPasal = re.split(r'\bPasal\b',splitBAB[i])
                    for j in range(len(splitPasal)):
                        if j>0:
                            bunyiPasal = re.sub(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})','',splitPasal[j])
                            writer.writerow([realFileName, bab, bunyiPasal])




