def readfasta(filename):
    result_list = []
    with open(filename, 'r') as infile:

        # process the first line, which must be a header line
        line = infile.readline()
        header_line = line.rstrip()
        label = header_line[1:].split(' ')[0]

        # initialize the sequence accumulator
        sequence = ''

        # process all the rest of the lines in the file
        for line in infile:
            line = line.rstrip()

            # ignore blank lines
            if line != '':

                # if it's a header line, finish the previous sequence
                # and start a new one
                if line[0] == '>':
                    result_list.append([label, sequence])

                    label = line[1:].split(' ')[0]
                    sequence = ''

                    # if we're here, we must be in letters of the sequence
                else:
                    sequence += line

    # we're done, so clean up, terminate the last sequence, and return
    result_list.append([label, sequence])
    return result_list
