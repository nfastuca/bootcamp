def ratio(x, y):
    """The ratio of 'x' to 'y'"""
    return x/y
def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """Simpler program that Deep Thought's, I bet."""
    return 42

def think_too_much():
    """Express Caesar's skepticism about Cassius"""
    print("""Yond Cassius has a lean and hungry look,
    He thinks too much; such men are dangerous.""")

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

    #loop through and add rev comp bases
    for base in reversed(seq):
        rev_comp += complement_base(base, material=material)
    return rev_comp
