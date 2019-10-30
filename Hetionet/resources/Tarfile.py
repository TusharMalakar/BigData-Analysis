import tarfile

# open tar files
tarfile_list = tarfile.open(r"data\projectI_hetionet.tar.gz")
file_list = tarfile_list.extractall()
