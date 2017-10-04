#Remove Duplicate entries in a FASTA file
#Jacob Wolff

class RemoveDuplicates:
    '''
    Class that will remove duplicates from a list of sequences stored in FASTA format
    '''
    def __init__(self):
        fastaReader = FastAreader()
        backHeader = ""
        backSeq = ""
        newFasta = ""
        for header, sequence in fastaReader:
            if self.compare(backHeader, backSeq):
                continue
            else:
            newFasta = newFasta + "\n" + header + "\n" + sequence            
        print(newFasta)    
                

    def compare(self, bhead, bseq, head, seq):
        matchHead = False
        matchSeq = False
        if len(bhead) = len(head) and len(bseq) = len(bseq):
            for i in range(0,len(bhead)):
                if bhead[i:i] = head[i:i]:
                    matchHead = True
                    continue
                else:
                    matchHead = False
                    break
            for i in range(0,len(bseq)):
                if bseq[i:i] = seq[i:i]:
                    matchSeq = True
                    continue
                else:
                    matchSeq = False
                    break
        return matchHead & matchSeq
        
        
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
    rd = RemoveDuplicates()       
            
if __name__ == "__main__":
    main()
        
        
        
        
        
        
 