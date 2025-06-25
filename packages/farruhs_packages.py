from packages.multiplier import multiply
from packages.get_tempo import tempo_inator

def farruhs_packages(string, df):
   """Calls the two functions imported above. 
      This package was created to reduce clutter in main."""

   tempomultipliers = tempo_inator(string) #Makes a list of multipliers for the tempo

   #Modifies the dataframe to have varying tempo by sending in a list of the default tempo and multiplying it with a list of multiplying factor list that was made in reference to repeats
   df['Tempo'] = multiply(df['Tempo'].to_list(), tempomultipliers) 

   return df