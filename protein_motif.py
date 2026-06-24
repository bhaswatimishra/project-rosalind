import requests
def get_protein_sequence():
    protein_id = input(f"Enter the id :").split("_")[0] # if protein id is P07204_TRBM_HUMAN
    # then it will only take P07204
    #split will create a list - ["P07204","TRBM","HUMAN"]
    url = f"https://rest.uniprot.org/uniprotkb/{protein_id}.fasta"
    sample_data = requests.get(url)
    with open("protein.faasta", "a") as f :
       f.write(sample_data.text)
while True :
    response = input("Do you have a sequence ?").upper()
    if response == "YES" :
       get_protein_sequence()
    else :
        break
header = None
seq = []
sample = {}
with open ("protein.faasta", "r") as f :
    for line in f :
        if line.startswith(">") :
            if header is not None :
               sample[header] = "".join(seq)
            header= line.strip()[1:]
            seq = []
        else :
            seq.append(line.strip())
    if header is not None :
       sample[header] = "".join(seq)
def glycosylation(sample) :
    for header in sample :
        print(f"Protein id : {header}")
        sequennce = sample[header]
        length = len(sample[header])
        position=[]
        for i in range(0,length-3):
            if sequennce[i] == "N" and sequennce[i+1] != "P" and (sequennce[i+2] == "S" or sequennce[i+2] == "T") and sequennce[i+3] != "P" :
                position.append(i+1)
        print(f"motif found at : {position}")
glycosylation(sample)
