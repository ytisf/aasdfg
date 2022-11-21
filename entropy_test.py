#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aasdfg import GenerateSeed

folds = [ 2, 4, 8]
snaps = [1, 2, 4]

print("Starting tests...")
print("Folds\tSnaps\tSize\tEntropy")
for snap in snaps:
    for fold in folds:
        seed, size, entropy = GenerateSeed(snap, fold, False)
        print("{}\t{}\t{}\t{}".format(fold, snap, size, entropy))
