# zipfian-precomputed

The data files can be downloaded from [the release page of the repo](https://github.com/myl7/zipfian-precomputed/releases)

The data is computed with [`zipfian` in SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zipfian.html).
`zipfian` has 2 parameters: `a` and `n`.
In the data, `a = 0.99`, which is a common default.
As for `n`, the filename `zipfian_n5w.pkl` means `n = 50000`, and so others.

The data is dumped with Python pickle.
It is a `list` of `numpy.float64`.
NumPy is required to load the data.

## License

Copyright (C) 2022 myl7

SPDX-License-Identifier: MIT
