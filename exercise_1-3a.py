def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of a base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
        else :
            raise RuntimeError('Invalid material.')
    elif base in 'TtUu':
        return 'A'
    elif base in 'gG':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a DNA sequence."""

    #initialize empty string
    rev_comp = ''

    #loop through and add comp bases
    for i, base in enumerate(seq):
        rev_comp += complement_base(base, material=material)
    rev_comp = rev_comp[::-1]
    return rev_comp
