
# Pynubank was made by: andreoroggeri at https://github.com/andreroggeri/pynubank :)

import pandas as pd

import os as os

from pynubank import Nubank

cd = os.getcwd()

#path to security certificate
path = cd + "/cert.p12"

nu = Nubank()


#the login and password of your nubank account
nu.authenticate_with_cert("seuCPF_apenas_numeros", "suasenha", path)


# get all the credit card transactions ever made
transactions = nu.get_card_statements()

# parse only what we need from the json
df = pd.DataFrame(transactions)

path_save = cd + "/data/"

pd.DataFrame.to_csv(df, path_save + "/data.csv")