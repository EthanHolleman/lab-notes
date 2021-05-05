import numpy as np
from Bio import SeqIO
from multiprocessing import Pool


def energy_crawl_one_base(previous_value, previous_base, next_base):
    pair = previous_base + next_base
    return previous_value + BD_ENEICT[pair]

# RNA - DNA hybrid energies RNA 5' -> 3' 

ENERGY_DICT = {
    'CC':-0.36,
    'CG':-0.16,
    'CT':-0.1,
    'CA':-0.06,
    'GC':0.97,
    'GG':0.34,
    'GT':0.45,
    'GA':0.38,
    'TC':-0.12,
    'TG':-0.16,
    'TT':0.6,
    'TA':-0.12,
    'AC':.45,
    'AG':.5,
    'AT':.28,
    'AA':.8
}


    
def read_fasta_entries(fasta_path):
    return SeqIO.parse(fasta_path, 'fasta')


def seq_hybrid_energy(seq):
    di_nucs = zip(seq[:-1], seq[1:])
    np.array([ENERGY_DICT[di_nuc] for di_nuc in di_nucs])


def define_thread_ranges(n_bases, num_threads):
    part_len = round(n_bases / num_threads)
    thread_ranges = []
    for i in range(0, n_bases, part_len):
        thread_ranges.append(
            (i, i+part_len)
        )
    return thread_ranges



def windowed_hybrid_energy(record, window_size, dist_between_windows, threads=1):
    record_regions = define_thread_ranges(len(record), threads)
    with Pool(threads) as pool:
        args = [(str(record.seq)[start:end], window_size, dist_between_windows)
                for start, end in record_regions]
        results = []
        for a in args:
            results.append(windowed_hybrid_energy_region(*a))
        #pool.starmap(windowed_hybrid_energy_region, args)
    
    return results
    
    
def windowed_hybrid_energy_region(seq, window_size, dist_between_windows):
    window_position = 0
    previous_window_vals = None
    window_energies = {}
    while window_position < len(seq):
        window_seq = seq[window_position:window_position + window_size]
        print(window_seq)
        window_vals = window_energy(
            window_seq, dist_between_windows, previous_window_vals 
        )
        window_energies[(window_position, window_position+window_size)] = window_vals.sum()
        previous_window_vals = window_vals
        window_position += dist_between_windows
    
    return window_energies


def window_energy(window_seq, dist_between_windows, previous_window_vals=None):

    if type(previous_window_vals) == np.array:
        pre_calculated = previous_window_vals[dist_between_windows:]
        window_vals = np.concatenate(
            previous_window[dist_between_windows:],
            np.full(dist_between_windows-1, 0.0)
        )
        start_energy_calc_index = len(window_seq) - dist_between_windows
    else:
        start_energy_calc_index = 0
        window_vals = np.full(len(window_seq)-1, 0.0)
    
    for i in range(start_energy_calc_index, len(window_seq)-1):
        di_nuc = window_seq[i] + window_seq[i+1]
        try:
            window_vals[i] = ENERGY_DICT[di_nuc]
        except KeyError as e:
            return np.zeros(len(window_vals))
    print(window_vals, 'w')
    print(previous_window_vals, 'p')
    assert len(window_vals) == len(previous_window_vals)
    print('done')
    return window_vals



records = read_fasta_entries('/home/ethan/Documents/github/lab-notes/test')
a = windowed_hybrid_energy(next(records), 10, 2)
print(a)
        







