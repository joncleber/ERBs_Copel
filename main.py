import pandas as pd

tabela = pd.read_excel("Nov22.xlsx")

imprime = tabela.loc[tabela["SiglaUf"] == "PR"] # Pega todos valores referente estado do PR

"""
 <wpt lat="-25.4186444444444" lon="-49.2892083333333">
    <name>Antena TIM 2G 3G 4G</name>
    <category>Antena</category>
  </wpt>
  
  ## https://www.telecocare.com.br/mapaerbs/index.php
"""
Text_Format = ''

i = 0

for index,row in imprime.iterrows():
    Text_Format = str("<wpt lat=""\""+str(row["Latitude"])+"\""+" lon=""\"" +str(row["Longitude"])+"\">"+"\n"
          +"\t<name> Operadora " + row["Operadora"] + "\t" + row["Tecs"]+"</name>\n"+
          "\t <category>Antenas</category>"+ "\n"+
          "</wpt>")
    i = i + 1
    print(Text_Format)


"""
f = open('favourites.txt', 'r+', encoding="utf-8")
f.write('\n'+Text_Format)
f.close()
"""