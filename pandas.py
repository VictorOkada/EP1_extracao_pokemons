""" import pandas as pd
import csv

#############################################################
###########      converte para csv final pandas    ##########
#############################################################

file = pd.read_csv(' resultado.csv')
file.to_csv("resultado_final.csv", sep=",", index=False)

#############################################################
#######   converte de csv para txt para uso no mapreduce    
#############################################################
csv_file = "resultado.csv"
txt_file = "resultado.txt"

with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()  """