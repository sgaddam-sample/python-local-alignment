# python-local-alignment

Find the highest-scoring local alignment between two strings.

Given two amino acid strings, the max score of a local alignment of the strings is returned, followed by this max scoring local alignment. The PAM250 scoring matrix and indel penalty σ = 5 were used. If multiple local alignments achieving the maximum score exist, any such alignment is returned. 

Example
-------
Sample Data:

MEANLY  
PENALTY


Sample Output:

15  
EANL-Y  
ENALTY
