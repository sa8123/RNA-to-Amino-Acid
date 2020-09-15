
'''
Team 8

A program to read a RNA sequence from a fasta file, pre-process it
by removing the start codon, translate it according to the standard
genetic code, and print the resulting amino acid sequence to the screen.

'''
import GenetiCode as gene
from ReadFile import readfasta


def rna2aa(rna):
    # replace the following line with the real code of this function
    #get the amino acid dictionary.
    #This is the way to access dictionary elements.
    #print(gene.code["UUG"])
    # print("Debugger for dict")
    # print(gene.code[rna[3:6]])
    # print("Debugger from rna2aa method")
    # print(rna[0:10])
    not_finished = True
    amino_acid = ''
    index = 0
    while not_finished:
        base_pair = rna[index: index + 3]
        # Check if the length of base pair is 3 or not.
        if len(base_pair) < 3:
            # We have finished reading the sequence.
            not_finished = False
        else:
            # We have to check through the dictionary for matching
            # the rna to amino acid sequence.
            amino_acid = amino_acid + gene.code[base_pair]
        index += 3
    return amino_acid

def main():
    # read in the rna from disk
    # we will process only the first sequence in the fasta file
    rnainfo = readfasta('Assignment1Sequences.txt')
    sequence_1 = rnainfo[0]
    sequence_2 = rnainfo[1]
    sequence_3 = rnainfo[2]
    rnasequence_1 = sequence_1[1]
    rnasequence_2 = sequence_2[1]
    rnasequence_3 = sequence_3[1]
    print("Sequences  " + str(rnasequence_1))
    print("Sequences  " + str(rnasequence_2))
    print("Sequences  " + str(rnasequence_3))
    # remove the start codon

    # translate the rna sequence
    aasequence_1 = rna2aa(rnasequence_1)
    aasequence_2 = rna2aa(rnasequence_2)
    aasequence_3 = rna2aa(rnasequence_3)

    # some test cases
    test_1 = ''
    aasequence_test_1 = rna2aa(test_1)

    # print the results
    print('The resulting amino acid sequence for gene 1 is :')
    print(aasequence_1)
    print('The resulting amino acid sequence for gene 2 is :')
    print(aasequence_2)
    print('The resulting amino acid sequence for gene 3 is :')
    print(aasequence_3)
    print('The resulting amino acid sequence for test 1 is:')
    print(aasequence_test_1)

main()
