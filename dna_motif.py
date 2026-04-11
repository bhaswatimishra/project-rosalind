def dna_motif() :
    sequence= input("Enter the dna sequence").upper()
    correct_sequence="".join(sequence.split())
    valid_sequence=set(["A","T","G","C"])
    if not set(correct_sequence).issubset(valid_sequence) :
        print("Wrong sequence entered")
    else :
        motif= input("Enter the motif")
        correct_motif="".join(motif.split())
        if not set(correct_motif).issubset(valid_sequence) :
            print("Wrong sequence entered")
        else :
            if not set(correct_motif).issubset(correct_sequence) :
                print("no matched motifs found")
            else :
                number=[]
                index_number = 0
                while True :
                    #where_to_find.find(what_to_find,search_start_index)
                    positions=correct_sequence.find(correct_motif,index_number) #find search the motif in the sequence
                    #when the index number reaches to last index of sequence its index is -1
                    if positions == -1 :
                        break
                    number.append(positions+1) #position+1 tells to stores the numberss from 1 while computer indexing starts from 0
                    index_number=positions+1  #change the index number to the next one so that the loop dos not always starts from zero
                                             #if the sequence is GAGAG and the motif is GAG
                                             #then after finding 1st motif at index 1 now the search_start_index will shift to 1: 
                                             # it reads as :AGAG
                if len(number)!=0 :
                 print(f"The motif {correct_motif} is repeated at{number} positions")
dna_motif()
