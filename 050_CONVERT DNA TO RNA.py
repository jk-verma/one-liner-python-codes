'''
Problem    : CONVERT DNA TO RNA
Description: The dna_to_rna function takes a DNA sequence as input and converts it into its corresponding RNA sequence.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''
def dna_to_rna(dna):
    conversion = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(conversion.get(base, '') for base in dna)
print(dna_to_rna("ATTGC"))
# Output: UAAAC