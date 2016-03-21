###  temp functions for creating numbers.dat file  ###
# Returns a list of random ints. p is basically any formatting. r is the set the
#   random numbers are pulled from. l is how many elements to generate.
import random
def rin(p='{}\n',r=(1,250000),l=12):
    return ''.join([p.format(x) for x in random.sample(range(*r),l)])

def make_dat(f='numbers.dat'):
    with open(f,'w') as fo:
        fo.write(rin())
    return None

# This either creates the numbers.dat file or overwrites the old one
#   with new ints.
make_dat()