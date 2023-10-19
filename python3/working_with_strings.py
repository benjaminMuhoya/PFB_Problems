#!/usr/bin/env python3
import sys
########
dna_seq = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG'

dna_seq_uppercase_only = dna_seq.upper()

print("first question",dna_seq_uppercase_only.count('A'), 'number of A', sep='\n')
print("first question",dna_seq_uppercase_only.count('C'), 'number of C', sep='\n')
print("first question",dna_seq_uppercase_only.count('G'), 'number of G', sep='\n')
print("first question",dna_seq_uppercase_only.count('T'), 'number of T', sep='\n')

replaced_seq = dna_seq_uppercase_only.replace('T','U')
print("Replaced T with U then count U =", replaced_seq.count('U'), sep='\n')

########make flexible code to make a reverse complement regardeless of case
dna_seq2 = (sys.argv[1]).upper()
tees = dna_seq2.count('T')
aaas = dna_seq2.count('A')

print("SECOND part with MATH" ,"number of T =",tees,"number of A =", aaas,"Total =", tees+aaas, sep='\n')
number_of_G = dna_seq2.count('G')
print('third part','number of G=',number_of_G, sep='\n')

sub_dna_seq2 = dna_seq2[100:201]
sub_G = sub_dna_seq2.count('G')
print('third part','subset number of G=',sub_G, sep='\n')

dna_complement = (sys.argv[1]).upper().replace('T','a').replace('A','t').replace('C','g').replace('G','c')
print(dna_seq2,dna_complement, sep='\n')

#####reversing the sequence
dna_complement_uppercase = dna_complement.upper()
reverse_complement =dna_complement_uppercase[::-1]
print('the results of the making the complement sequence',dna_complement_uppercase,'the results of the reverse complement',reverse_complement, sep='\n')

####search unique sequence
print(f'Start position of gene EcoRI =',dna_seq2.find('GAATTC'), 'endPos =',dna_seq2.find('GAATTC')+6, sep='\t')

