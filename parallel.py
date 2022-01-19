from knotprot import get_proteins, download_link, time_it, setup_download_dir


#print(get_proteins())

# simply opening a webpage

def run_seq(my_dir):
    for p in get_proteins():
        download_link(my_dir, p)

def run_multiprocessing(my_dir):
    proteins = get_proteins()
    download = partial(download_link, my_dir)
    with Pool(16) as pl:
        pl.map(download, proteins)
    # it doesn't have to be the number of cores in your computer
    # limitations is the number of connections the server will allow -> they can limit it

my_dir = setup_download_dir()
#time_it(run_seq, my_dir)
time_it(run_multiprocessing, my_dir)

#what took two and a half minutes, took 11 seconds now

#copy and paste the code from his github if we want to see it
#thumbnails