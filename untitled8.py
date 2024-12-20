# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s07a_8ovfMbBt9wVj2inI3Erb_BJnat-
"""

import pandas as pd

# Define the data
Akramov = {
    "FI": ["Soliyev Bahmanyor", "Ro'zaliyev Elshodbek", "Erqo'ziyev Abduvohid", "Xabibullayev Otabek",
           "Meliqo'ziyev Muhammadjon", "Malikov Og'abek", "Qodirov Oyatbek", "Amakixonova Madina",
           "Komiljonova Dinorabonu", "Saminova Aziza"],
    "Yoshi": ["19", "16", "17", "13", "11", "21", "23", "24", "31", "20"],
    "Maktabi": ["38-maktab", "Prezident maktabi", "21*maktab", "Litsey", "Akademiya", "1-IDUM",
                "2-IDUM", "Ziyo", "1-maktab", "2-maktab"],
    "Jinsi": ["Erkak", "Erkak", "Erkak", "Erkak", "Erkak", "Erkak", "Erkak", "Ayol", "Ayol", "Ayol"],
    "Manzili": ["Farg'ona", "Farg'ona", "Farg'ona", "Farg'ona", "Farg'ona", "Farg'ona",
                "Farg'ona", "Uchko'prik", "Uchko'prik", "Uchko'prik"]
}

# Create the DataFrame
df = pd.DataFrame(Akramov)

# Display the DataFrame
print(df)

filtr =df[df['Jinsi'] =="Ayol"]
print(filtr)

filtr =df[df['Jinsi'] =="Erkak"]
print(filtr)