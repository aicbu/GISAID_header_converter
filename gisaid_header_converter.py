#!/usr/bin/env python

from Bio import File, SeqIO
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='Replace fasta headers with GISAID style')
parser.add_argument('fasta', help='input multi fasta', type=str)
parser.add_argument('--country', help='input country', default='Sri Lanka', type=str)
parser.add_argument('--year', help= 'input sampling year (single year)', default='2021', type=int)
args = parser.parse_args()

#input fasta
input_fasta = os.path.join(args.fasta)
if not os.path.exists(args.fasta):
    sys.stderr.write(f"Error: can't find the fasta file\n")
    sys.exit(-1)

header_style = 'hCoV-19/'+args.country+'/'+'<id>/'+ str(args.year)

num_seqs = 0
lengths = []
seqs=[]
ids =[]

multi_fasta = SeqIO.parse(open(input_fasta), 'fasta')
for record in multi_fasta:
    lengths.append(len(record))
    seqs.append(record.seq)
    ids.append(record.id)
    num_seqs +=1

#check if the multi fasta is correct
if num_seqs <= 2:
    sys.stderr.write("Error: multi fasta has too few sequences\n")

output =open(os.path.join(args.fasta+"_headers_replaced.fasta"),'w')

new_fasta=""
headers_list=""
#output= open('output.fasta', 'w')
output_headers=open('replaced_headers.csv','w')

for i in range(len(ids)):
    headers_list='hCoV-19/'+args.country+ '/' +ids[i]+'/'+str(args.year)+'\n'
    new_fasta='>'+'hCoV-19/'+args.country+'/' +ids[i]+'/'+str(args.year)+'\n'+str(seqs[i])+'\n'
    output.write(new_fasta)
    output_headers.write(headers_list)


print('Successfully converted '+str(num_seqs)+ " fasta headers to "+ header_style)
print('New headers list is written to replaced headers.csv')