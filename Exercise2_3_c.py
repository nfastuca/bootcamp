import os

with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_lines = f.readlines()
    descriptor = f_lines[1]
    seq = ''.join(f_lines[1::])
    seq = seq.replace('\n', '')
    seq = seq.upper()

def gc_blocks(sequence, block_size):
    """
    Splits a DNA 'sequence' into non-overlapping chunks of
    size 'block_size' and computes the combined percentage
    of GC in each chunk
    """

    if type(block_size)  != int or block_size<= 0:
        raise RuntimeError('block_size is not a positive integer.')

    #split sequence into chunks of size 'block_size'
    start_indicies = range(0, len(sequence), block_size)
    chunks = []
    for i in start_indicies:
        chunks.append(sequence[0 + i: block_size + i])

    #calculates GC content of each chunk, appends
    #result to list which is returned
    gc_contents = []
    for piece in chunks:
        count = piece.count('G') + piece.count('C')
        gc_contents.append(count/block_size)
    return gc_contents, chunks

def gc_map(sequence, block_size, gc_thresh):
    """
    Highlights regions of 'sequence' with GC
    content > gc_thresh
    """
    gc_contents, chunks = gc_blocks(sequence, block_size)
    gc_highlight = ''
    for i, cont in enumerate(gc_contents):
        if cont >= gc_thresh:
            gc_highlight += chunks[i]
        else:
            gc_highlight += chunks[i].lower()
    return gc_highlight

#run gc_map function
gc_map_salmonella = gc_map(seq, 1000, 0.45)

#write result of gc_map function to new file
with open('data/salmonella_spi1_region_gc_map.fasta', 'w') as f_out:
    f_out.write(descriptor)
    i = 0
    while i < len(gc_map_salmonella) - 59:
        f_out.write(gc_map_salmonella[i:i+60] + '\n')
        i += 60
    f_out.write(gc_map_salmonella[i:])
