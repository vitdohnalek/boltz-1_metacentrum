#This sscript truncates the MSA, as the sequence for the predicted protein should not contain gaps!
#Can be used for both Boltz-1 and AlphaFold
from Bio import SeqIO
import argparse


#Reads a MSA file and writes a new MSA file with query sequence without gaps
def trim_MSA(input_file=str()):
    #Bool to switch between query and non-query sequences
    query = True
    #Stores the positions in MSA with AA positions from the query
    residue_indexes = list()
    #Stores the new fasta file information
    new_MSA = str()

    for seq_rec in SeqIO.parse(input_file, "fasta"):
        #Applies to the first sequence which should be the query
        #AlphaFold requires the first sequence to be the query!
        if query == True:
            position_index = 0
            new_MSA += f">{seq_rec.description}\n"
            #Iterates over the sequence and stores the indexes of non-gap positions
            for position in seq_rec.seq:
                if position != "-":
                    new_MSA += position
                    residue_indexes.append(position_index)
                position_index += 1
            new_MSA += "\n"
            #Switches to non-query sequences
            query = False
        #Applies to non-query sequences
        else:
            new_MSA += f">{seq_rec.description}\n"
            #Stores only positions with the proper index
            for i in residue_indexes:
                new_MSA += seq_rec.seq[i]
            new_MSA += "\n"

    #Writes the new MSA into a fasta file 
    with open(f"{'.'.join(input_file.split('.')[:-1])}_trimmed.fasta", "w") as f:
        f.write(new_MSA)

if __name__ == "__main__":
    #Parser for commandline input
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", action="store", dest="parameter_input_file", type=str)
    args = parser.parse_args()

    trim_MSA(input_file=args.parameter_input_file)
