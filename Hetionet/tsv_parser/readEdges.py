import csv
import tarfile

# open tar files
tarfile_list = tarfile.open("projectI_hetionet.tar.gz")
file_list = tarfile_list.extractall()
countLine = 0

with open(r'projectI_hetionet\edges.tsv')as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for eline in tsvreader:
        # eline
        countLine = countLine + 1
