
def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a DNA sequence."""
    #create reversed sequence in lowercase
    rev_seq = seq[::-1].lower()
    #replace elements stepwise with comp base by creating new mod rev_seq
    if material == 'DNA':
        rev_seq_a = rev_seq.replace('a', 'T')
        rev_seq_t = rev_seq_a.replace('t', 'A')
        rev_seq_c = rev_seq_t.replace('c', 'G')
        rev_seq_g = rev_seq_c.replace('g', 'C')
        return rev_seq_g
    #replace elements in rev RNA seq with comp bases
    elif material == 'RNA':
        rev_seq_a = rev_seq.replace('a', 'U')
        rev_seq_u = rev_seq_a.replace('u', 'A')
        rev_seq_c = rev_seq_u.replace('c', 'G')
        rev_seq_g = rev_seq_c.replace('g', 'C')
        return rev_seq_g
    else:
        raise RuntimeError('Invalid material.')
