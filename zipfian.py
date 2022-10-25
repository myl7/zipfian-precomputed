# Copyright (C) 2022 myl7
# SPDX-License-Identifier: MIT

import pickle
import sys
import multiprocessing as mp
import itertools
import math

from scipy.stats import zipfian

ZIPFIAN_A = 0.99
zipfian_n = int(sys.argv[1])


def f(args):
    id, xs = args
    results = []
    for i, x in enumerate(xs):
        if x is None:
            return results
        result = zipfian.pmf(x, ZIPFIAN_A, zipfian_n)
        results.append(result)
        print(f'Thread {id} computed {i}th(st,rd) result x = {x}')
    return results


PROCESS_N = mp.cpu_count() - 2
pool = mp.Pool(PROCESS_N)

xs = list(range(1, zipfian_n + 1))
args_list = itertools.zip_longest(*[iter(xs)] * math.ceil(zipfian_n / PROCESS_N))
results_list = pool.map(f, enumerate(args_list))
results = [result for results in results_list for result in results]

with open('zipfian.pkl', 'wb') as f:
    pickle.dump(results, f)
