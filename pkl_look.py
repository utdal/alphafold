import pickle as pkl
from alphafold.common.residue_constants import ID_TO_HHBLITS_AA

file = open("/home/ceziegler/Documents/test/RBP_Protsequence/features.pkl", 'rb')
me_data = pkl.load(file)
file.close()

me_seqs = list()
for seq_mat in me_data['msa']:
    seq_str = ""
    for pos in seq_mat:
        seq_str += ID_TO_HHBLITS_AA[pos]
    me_seqs.append(seq_str)
file = open("/home/ceziegler/Documents/test/RBP_Protsequence/RBPconcat_AF_alignment.fasta","w+")
for seq in me_seqs:
    file.write('> aligned seq \n'+seq+"\n")
file.close()
