codon = input('Input your codon:')
codon_list = ['UAA', 'UAG', 'UGA']

if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in codon_list:
    print('This is a stop codon')
else:
    print('This codon is neither a stop codon or start codon.')
