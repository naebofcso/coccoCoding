#Class meant to calculate the hydrophobic moment of possible helices in a given sequence or sequences using a given helix length and choosing a hydrophobicity table
#Author: Jacob Wolff

import math

residueHydrophobicity = {}


class crunchHelices:

    def __init__ (self, sequence, helixLength):

        self.dataList = list(list(sequence))
        for aa in range(int(helixLength/2), len(sequence) - (helixLength-int(helixLength/2))):
            helix = sequence[aa-helixLength/2:aa+(helixLength - int(helixLength/2))]
            xvalues = []
            yvalues = []
            index = 0
            for residue in sequence:
                xvalues.append(residueHydrophobicity[residue]*cos(radians(100)*index))
                yvalues.append(residueHydrophobicity[residue]*sin(radians(100)*index))
                index += 1
            hMoment = sqrt((sum(xvlaues)**2) + sum(yvalues)**2)
            self.dataList[aa].append()

    def printResults(self, data):
        #print hydrophobic moment values above residues labeled as positionresidue (134N 135K 136P) so on and so forth
        #data is a list of lists where the outer list is the position in the sequence
        #and the inner list is the residue and hydrophobic moment with that residue as the center of the assumed helix
        for item in range(0, len(data)):
            


class FastAreader:
    '''
    Class to provide reading of a file containing one or more FASTA
    formatted sequences:
    object instantiation:
    FastAreader(<file name>):
    object attributes:

    fname: the initial file name
    methods:
    readFasta() : returns header and sequence as strings.
    Author: David Bernick
    Date: April 19, 2013
    '''

    def __init__ (self, fname=''):
        '''contructor: saves attribute fname '''

        self.fname = fname

    def doOpen (self):
        if self.fname is '':
            return sys.stdin
        else:
            return open(self.fname)

    def readFasta (self):
        '''
        using filename given in init, returns each included FastA record
        as 2 strings - header and sequence. If filename was not provided,
        stdin is used. Whitespace is removed, and sequence is upcased.
        The initial '>' is removed from the header.
        '''
        header = ''
        sequence = ''

        with self.doOpen() as fileH:
            # initialize return containers
            header = ''
            sequence = ''

            # skip to first fasta header
            line = fileH.readline()
            while not line.startswith('>') :
                line = fileH.readline()
            header = line[1:].rstrip()

            # header is saved, get the rest of the sequence
            # up until the next header is found
            # then yield the results and wait for the next call.
            # next call will resume at the yield point
            # which is where we have the next header
            for line in fileH:
                if line.startswith ('>'):
                    yield header,sequence
                    header = line[1:].rstrip()
                    sequence = ''
                else :
                    sequence += ''.join(line.rstrip().split()).upper()
        # final header and sequence will be seen with an end of file
        # with clause will terminate, so we do the final yield of the data
        yield header,sequence

def main():
    #placeholder
    fastaReader = FastAreader()
    for header, seq in fastaReader.readFasta():
        helixcrunch = crunchHelices(seq, length)
        print(header)
        helixcrunch.printResults(helixcrunch.dataList)

if __name__ == '__main__':
    main()
