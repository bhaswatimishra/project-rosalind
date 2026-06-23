sample = {}
header = None
seq=[]
with open("sample.faasta", "r") as f :
    for line in f :
        if line.startswith(">") :
            if header is not None :
                sample[header] = "".join(seq)
            header = line.strip()[1:]
            seq=[]
        else :
            seq.append(line.strip())
if header is not None :
    sample[header] = "".join(seq)
def get_motif(sample) :
    short_seq = None
    for header in sample :
        if short_seq is None or len(sample[header]) < len(short_seq) :
            short_seq = sample[header]
    motif_len = len(short_seq)
    k = motif_len
    while k > 0 :
        for i in range(motif_len-k+1) :
            motif = short_seq[i:i+k]
            present_to_all = True
            for header in sample :
                if motif not in sample[header] :
                    present_to_all = False
                    break
        if present_to_all == True :
            print(f"Motif found: {motif}")
            break
        k -= 1
get_motif(sample)
