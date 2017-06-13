class mainSpace(object):
    """ generated source for class mainSpace """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        poly_deg = 5
        #  you can only put 6 and 7.
        seq_length = mSeqlength.seq_length(poly_deg)
        print("The Sequences length is: " + seq_length)
        #  Initialising the shift registers
        init_state = [None] * poly_deg
        init_state[poly_deg - 1] = 1
        #  Generating the two m-sequences
        seqA = mSeqGenA.PNseq(poly_deg, seq_length, init_state)
        seqB = mSeqGenB.PNseq(poly_deg, seq_length, init_state)
        print("")
        #  Generating the Gold Code
        gold = goldCodeGen.gold(seq_length, seqA, seqB)

#  calculating the sequences length
class mSeqlength(object):
    """ generated source for class mSeqlength """
    @classmethod
    def seq_length(cls, deg):
        """ generated source for method seq_length """
        length = int((pow(2, deg) - 1))
        print("")
        return length

#  generating the first m-sequence (make sure to XOR the right taps)
class mSeqGenA(object):
    """ generated source for class mSeqGenA """
    @classmethod
    def PNseq(cls, poly_deg, seq_length, taps_seed):
        """ generated source for method PNseq """
        i = int()
        j = int()
        xor1 = int()
        xor2 = int()
        PNseq = [None] * seq_length
        temp = [None] * poly_deg
        temp = taps_seed
        print("the first m-sequence is: ")
        if seq_length < 32:
            while i < seq_length:
                xor2 = taps_seed[3] ^ taps_seed[poly_deg - 1]
                xor2 = xor2 ^ taps_seed[2]
                xor1 = xor2 ^ taps_seed[1]
                # shifting the taps
                while j > 0:
                    temp[j] = taps_seed[j - 1]
                    j -= 1
                j = 0
                temp[j] = xor1
                PNseq[i] = taps_seed[poly_deg - 1]
                taps_seed = temp
                i += 1
            while i > 0:
                print(PNseq[i - 1], end="")
                i -= 1
            print("")
        elif seq_length > 32:
            if seq_length < 64:
                while i < seq_length:
                    xor2 = taps_seed[4] ^ taps_seed[poly_deg - 1]
                    xor2 = xor2 ^ taps_seed[1]
                    xor1 = xor2 ^ taps_seed[0]
                    # shifting the sequence
                    while j > 0:
                        temp[j] = taps_seed[j - 1]
                        j -= 1
                    j = 0
                    temp[j] = xor1
                    PNseq[i] = taps_seed[poly_deg - 1]
                    taps_seed = temp
                    i += 1
                while i < seq_length:
                    print(PNseq[i], end="")
                    i += 1
                print("")
            elif seq_length > 64:
                while i < seq_length:
                    xor2 = taps_seed[5] ^ taps_seed[poly_deg - 1]
                    xor2 = xor2 ^ taps_seed[4]
                    xor1 = xor2 ^ taps_seed[3]
                    # shifting the sequence
                    while j > 0:
                        temp[j] = taps_seed[j - 1]
                        j -= 1
                    j = 0
                    temp[j] = xor1
                    PNseq[i] = taps_seed[poly_deg - 1]
                    taps_seed = temp
                    i += 1
                while i < seq_length:
                    print(PNseq[i], end="")
                    i += 1
                print("")
        return PNseq

#  generating the second m-sequence (make sure to XOR the right taps)
class mSeqGenB(object):
    """ generated source for class mSeqGenB """
    @classmethod
    def PNseq(cls, poly_deg, seq_length, taps_seed):
        """ generated source for method PNseq """
        i = int()
        j = int()
        xor1 = int()
        PNseq = [None] * seq_length
        temp = [None] * poly_deg
        temp = taps_seed
        print("the second m-sequence is: ")
        if seq_length <= 32:
            while i < seq_length:
                xor1 = taps_seed[2] ^ taps_seed[poly_deg - 1]
                # shifting the taps
                while j > 0:
                    temp[j] = taps_seed[j - 1]
                    j -= 1
                j = 0
                temp[j] = xor1
                PNseq[i] = taps_seed[poly_deg - 1]
                taps_seed = temp
                i += 1
            while i > 0:
                print(PNseq[i - 1], end="")
                i -= 1
            print("")
        elif seq_length > 31:
            if seq_length <= 64:
                while i < seq_length:
                    xor1 = taps_seed[0] ^ taps_seed[poly_deg - 1]
                    while j > 0:
                        temp[j] = taps_seed[j - 1]
                        j -= 1
                    j = 0
                    temp[j] = xor1
                    PNseq[i] = taps_seed[poly_deg - 1]
                    taps_seed = temp
                    i += 1
                while i < seq_length:
                    print(PNseq[i], end="")
                    i += 1
                print("")
            elif seq_length > 64:
                while i < seq_length:
                    xor1 = taps_seed[3] ^ taps_seed[poly_deg - 1]
                    while j > 0:
                        temp[j] = taps_seed[j - 1]
                        j -= 1
                    j = 0
                    temp[j] = xor1
                    PNseq[i] = taps_seed[poly_deg - 1]
                    taps_seed = temp
                    i += 1
                while i < seq_length:
                    print(PNseq[i], end="")
                    i += 1
                print("")
        return PNseq

#  where gold codes are generated
class goldCodeGen(object):
    """ generated source for class goldCodeGen """
    @classmethod
    def gold(cls, seq_length, seqA, seqB):
        """ generated source for method gold """
        i = int()
        j = int()
        d = int()
        gold_code = [None] * seq_length
        while d < seq_length:
            temp = [None] * seq_length
            #  generating the gold code
            while i < seq_length:
                gold_code[i] = seqA[i] ^ seqB[i]
                i += 1
            #  showing the gold code
            while i > 0:
                print(gold_code[i - 1], end="")
                i -= 1
            # checking if the gold sequence is balanced
            zeros = 0
            ones = 0
            while i < seq_length:
                if gold_code[i] == 0:
                    zeros = zeros + 1
                else:
                    ones = ones + 1
                i += 1
            if (zeros == ones) or (zeros == (ones - 1)):
                print(" 'Balanced'")
            else:
                print(" 'NOT balanced'")
            # shifting the second m-sequence
            while j > 0:
                temp[j] = seqB[j - 1]
                j -= 1
            j = 0
            temp[j] = seqB[(seq_length - 1)]
            seqB = temp
            d += 1
        return gold_code
