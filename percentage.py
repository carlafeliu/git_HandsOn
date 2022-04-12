import sys, re
from argparse import ArgumentParser 

parser = ArgumentParser(description = 'computes the percentage of each nucleotide from a DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") 

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
    
args = parser.parse_args()
args.seq = args.seq.upper()  
if "U" in args.seq and "T" in args.seq: #if T and U are in the same sequence, this is not RNA or DNA
    print("The sequence is not DNA nor RNA")
    sys.exit()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq): #if it find T, there are DNA
        A=args.seq.count("A")
        T=args.seq.count("T")
        C=args.seq.count("C")
        G=args.seq.count("G")
        percent_A=float(float(A*100)/float(len(args.seq)))
        percent_T=float(float(T*100)/float(len(args.seq)))
        percent_C=float(float(C*100)/float(len(args.seq)))
        percent_G=float(float(G*100)/float(len(args.seq)))
        print("Percentages of nucleotides of DNA sequence:")
        print("% of A in sequence:", percent_A, "%")
        print("% of T in sequence:", percent_T, "%")
        print("% of C in sequence:", percent_C, "%")
        print("% of G in sequence:", percent_G, "%")
    elif re.search('U', args.seq):
        A=args.seq.count("A")
        U=args.seq.count("U")
        C=args.seq.count("C")
        G=args.seq.count("G")
        percent_A=float(float(A*100)/float(len(args.seq)))
        percent_U=float(float(U*100)/float(len(args.seq)))
        percent_C=float(float(C*100)/float(len(args.seq)))
        percent_G=float(float(G*100)/float(len(args.seq)))
        print("Percentages of nucleotides of RNA sequence:")
        print("% of A in sequence:", percent_A, "%")
        print("% of U in sequence:", percent_U, "%")
        print("% of C in sequence:", percent_C, "%")
        print("% of G in sequence:", percent_G, "%")
    else:
        print ("Percentages of nucleotides of sequence:")
        A=args.seq.count("A")
        T=args.seq.count("T")
        U=args.seq.count("U")
        C=args.seq.count("C")
        G=args.seq.count("G")
        percent_A=float(float(A*100)/float(len(args.seq)))
        percent_C=float(float(C*100)/float(len(args.seq)))
        percent_G=float(float(G*100)/float(len(args.seq)))
        print("Percentages of nucleotides of DNA sequence:")
        print("% of A in sequence:", percent_A, "%")
        print("% of C in sequence:", percent_C, "%")
        print("% of G in sequence:", percent_G, "%")
else:
    print("The sequence is not DNA nor RNA")
    