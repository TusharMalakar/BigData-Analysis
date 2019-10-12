import csv
import tarfile

# open tar files
tarfile_list = tarfile.open("projectI_hetionet.tar.gz")
file_list = tarfile_list.extractall()

with open(r'projectI_hetionet\edges.tsv')as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        print(line[1])
