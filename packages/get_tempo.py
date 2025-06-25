def tempo_inator(translatedsequences):

    """This function takes in a string and creates a list with values that are going to be used as multipliers to
        affect the base tempo of the music."""

    #First test whether the input is a string
    if not isinstance(translatedsequences, str):
        raise TypeError("The input must be a string.")
    
    
    else:
        #Sets a few variables to be used as counters and multipliers
        counter = 1
        multiplier = 1.15
        globalmultiplier = 1.05
        globalmultipliercounter = 1
        tempo = []

        #Interates through the string sequence to check for repeats
        for x in enumerate(translatedsequences):
            
            #The first index is accounted for
            if x[0] == 0:
                a = translatedsequences[x[0]]
                tempo.append(counter)
            
            #Checks a window of size two for repeats, if there is, increases the counters
            else:
                a = translatedsequences[x[0]-1]
                b = translatedsequences[x[0]]

                if x[1] == "*": #This is a multiplier that occurs for each instance of a repeat, and resets when there is a stop codon
                    globalmultipliercounter=1
                if a==b:
                    #Each instance of a repeat makes it faster and resets when the repeat breaks
                    globalmultipliercounter*=globalmultiplier
                    tempo.append(counter*multiplier*globalmultipliercounter)
                    counter+=1
                else:
                    #Reset regular counter
                    counter = 1
                    tempo.append(counter*globalmultipliercounter)
        return tempo
