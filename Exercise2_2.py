
with open('data/salmonella_spi1_region.fna', 'r') as f:
    f_lines = f.readlines()
    seq = ''.join(f_lines[1::])
    seq = seq.replace('\n', '')
    seq = seq.upper()

def gc_blocks(sequence, block_size):
    """
    Splits a DNA 'sequence' into non-overlapping chunks of
    size 'block_size' and computes the combined percentage
    of GC in each chunk
    """

    block_size = int(block_size)

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
    gc_blocks(sequence, block_size)
    gc_highlight = ''
    for i, cont in enumerate(gc_contents):
        if cont >= gc_thresh:
            gc_highlight.append(chunks[i])
        else:
            gc_highlight.append(chunks[i].lower())
