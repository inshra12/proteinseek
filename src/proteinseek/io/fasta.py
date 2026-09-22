# with open("../../data/small/proteins.fasta","r") as file:
#     content = file.readlines()

# sequence = {}
# current_id = ""
# current_sequence = []
# for c in content:
#     c = c.strip()
#     if c.startswith(">"):
#         current_id = c[1:]
#         sequence[current_id] = ""
#     else:
#         sequence[current_id] += c
# print(sequence)
        
def read_fasta(filename):
    sequence = {}
    current_id = ""

    with open(filename,"r") as file:
        content = file.readlines()
   
    for c in content:
        c = c.strip()
        if c.startswith(">"):
            current_id = c[1:]
            sequence[current_id] = ""
        else:
            sequence[current_id] += c
    return sequence

