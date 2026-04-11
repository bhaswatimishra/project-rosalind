def faasta_sequence() :
    sequences=[] 
    valid_sequence= set(["A","T","G","C"]) 

    n= int(input("Enter the number of sequences"))   # number of sequences to input

    # taking input sequences one by one
    for i in range(n) :
        seq=input("Enter the sequene without FAASTA header :").upper().replace(" ","")
        if not set(seq).issubset(valid_sequence) :
            return 
        sequences.append(seq)
    for seq in sequences :
        if len(seq)!= len(sequences[0]) :
            print("All sequences must be of equal length")
            return

    end= len(sequences[0]) 
    count_A,count_T,count_G,count_C=[],[],[],[]

    # loop over each position (column-wise processing)
    for i in range(end) :
        column=[]   # temporary list to store ith position of all sequences
        for seq in sequences :
          column.append(seq[i])
        count_A.append(column.count("A"))
        count_T.append(column.count("T"))
        count_G.append(column.count("G"))
        count_C.append(column.count("C"))

    final_list=[] 
    for values in zip(count_A,count_T,count_G,count_C) :
         m = max(values)   # maximum count at this position
         position= values.index(m)   # index of max value
         nucleotides=['A','T','G','C']   # mapping index to nucleotide
         final_list.append(nucleotides[position])   # add to consensus

    print(f"The profile is :\n")   
    print(f"{count_A}\n")
    print(f"{count_T}\n")
    print(f"{count_G}\n")
    print(f"{count_C}\n")
    print("Consencus :\n")   
    print(f"{final_list}")  


faasta_sequence()