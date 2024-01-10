"""Given an array of N items, Merge Sort will:
Merge each pair of individual element (which is by default, sorted) into sorted arrays of 2 elements,
Merge each pair of sorted arrays of 2 elements into sorted arrays of 4 elements,
Repeat the process...,
Final step: Merge 2 sorted arrays of N/2 elements (for simplicity of this discussion, we assume that N is even) to obtain a fully sorted array of N elements.
This is just the general idea and we need a few more details before we can discuss the true form of Merge Sort."""