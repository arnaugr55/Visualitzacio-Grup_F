import pandas as pd
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



def merge_quantitat_immigracio_emmigracio(path):
    # Merge immigration and emmigration csv

    file1 = path + "Emmigracio/Emmigracio_2015-2020.csv"
    file2 = path + "Immigracio/Immigracio_2015-2020.csv"

    emmigrants = pd.read_csv(file1)
    immigrants = pd.read_csv(file2)

    immigrants_emmigrants = pd.merge(emmigrants, immigrants)
    immigrants_emmigrants.to_csv(path+"Immigracio_Emmigracio_2015-2020.csv", index=False)


def merge_edat_immigracio_emigracio(path):
    # Merge immigration and emmigration csv

    file1 = path + "Emmigracio Edat/Emmigracio_Edat_2015-2020.csv"
    file2 = path + "Immigracio Edat/Immigracio_Edat_2015-2020.csv"

    emmigrants = pd.read_csv(file1)
    immigrants = pd.read_csv(file2)

    immigrants_emmigrants = pd.merge(emmigrants, immigrants)
    immigrants_emmigrants.to_csv(path+"Immigracio_Emmigracio_Edat_2015-2020.csv", index=False)


def merge_sexe_immigracio_emmigracio(path):
    # Merge immigration and emmigration genre csv

    file1 = path + "Emmigracio Sexe/Emmigracio_sexe_2015-2020.csv" 
    file2 = path + "Immigracio Sexe/Immigracio_sexe_2015-2020.csv" 

    emmigrants = pd.read_csv(file1)
    immigrants = pd.read_csv(file2)

    immigrants_emmigrants = pd.merge(emmigrants, immigrants)
    immigrants_emmigrants = immigrants_emmigrants.drop_duplicates()
    immigrants_emmigrants.to_csv(path+"Immigracio_Emmigracio_Sexe_2015-2020.csv", index=False)


def merge_ocupacio_lloguer(path):
    # Merge immigration and emmigration csv

    file1 = path + "Ocupació Mitjana/Ocupacio_Mitjana_2015-2020.csv"
    file2 = path + "Lloguer/Mitjana_LLoguer_2015-2020.csv"

    emmigrants = pd.read_csv(file1)
    immigrants = pd.read_csv(file2)

    immigrants_emmigrants = pd.merge(emmigrants, immigrants)
    immigrants_emmigrants.to_csv(path+"Ocupacio_Lloguer_2015-2020.csv", index=False)



def emmigracio(path, paisos, paisos_angles):
    # Cleans and joins emmigration datasets

    path = path + "Emmigracio/"
    files = os.listdir(path) 

    df = pd.DataFrame()
    for file in files:
        if file.endswith('.csv') and file != "Emmigracio_2015-2020.csv":

            temp = pd.read_csv(path+file)

            temp = temp.replace("el Poble Sec", "el Poble-sec")

            if "Nacionalitats" in temp.columns:
                temp = temp.rename(columns={"Nacionalitats":"Nacionalitat"})

            df = df.append(temp, ignore_index=True) 

    del df["Codi_Districte"]
    del df["Codi_Barri"]

    #df = df[df["Nombre"] >= 1] # Elimina la fila quan no hi ha immigració

    for columna in df.columns:
        df = df[df[columna] != "No consta"]


    temp = df["Nacionalitat"].to_list()


    temp2 = [paisos_angles[paisos.index(x)] for x in temp]

    df["Nationality"] = temp2 # Posem la nacionalitat en anglés
    df = df.rename(columns={"Nombre":"Emmigrants"})

    df.to_csv(path+"Emmigracio_2015-2020.csv", index=False)


def emmigracio_sexe(path):
    # Cleans and joins emigration by genre csv

    path = path + "Emmigracio Sexe/"
    files = os.listdir(path) 

    df = pd.DataFrame()
    for file in files:
        if file.endswith('.csv') and file != "Emmigracio_sexe_2015-2020.csv":

            temp = pd.read_csv(path+file)
            temp = temp.replace("el Poble Sec", "el Poble-sec")


            if file == "2018_emigrants_sexe.csv":
                temp = temp.replace("Home", "Homes").replace("Dona", "Dones")

            df = df.append(temp, ignore_index=True) 

    del df["Codi_Districte"]
    del df["Codi_Barri"]

    for columna in df.columns:
        df = df[df[columna] != "No consta"]

    df = df.rename(columns={"Nombre":"Emmigrants"})

    df.to_csv(path+"Emmigracio_sexe_2015-2020.csv", index=False)


def immigracio(path, paisos, paisos_angles):
    # Clean and merge immigration csv

    path = path + "Immigracio/"
    files = os.listdir(path)
    

    df = pd.DataFrame()
    for file in files:
        if file.endswith('.csv') and file != "Immigracio_2015-2020.csv":

            temp = pd.read_csv(path+file)
            temp = temp.replace("el Poble Sec", "el Poble-sec")

            if "Nacionalitats" in temp.columns:
                temp = temp.rename(columns={"Nacionalitats":"Nacionalitat"})

            df = df.append(temp, ignore_index=True) 

    del df["Codi_Districte"]
    del df["Codi_Barri"]


    #df = df[df["Nombre"] >= 1] # Elimina la fila quan no hi ha immigració

    for columna in df.columns:
        df = df[df[columna] != "No consta"]

    temp = df["Nacionalitat"].to_list()
    temp2 = [paisos_angles[paisos.index(x)] for x in temp]

    df["Nationality"] = temp2 # Posem la nacionalitat en anglés
    df = df.rename(columns={"Nombre":"Immigrants"})

    df.to_csv(path+"Immigracio_2015-2020.csv", index=False)


def immigracio_sexe(path):
    # Clean and merge immigration by genre csv

    path = path + "Immigracio Sexe/"
    files = os.listdir(path)

    df = pd.DataFrame()
    for file in files:
        if file.endswith('.csv') and file != "Immigracio_sexe_2015-2020.csv":
            
            temp = pd.read_csv(path+file)
            temp = temp.replace("el Poble Sec", "el Poble-sec")

            if file == "2018_immigrants_sexe.csv":
                temp = temp.replace("Home", "Homes").replace("Dona", "Dones")

            df = df.append(temp, ignore_index=True) 

    del df["Codi_Districte"]
    del df["Codi_Barri"]

    for columna in df.columns:
        df = df[df[columna] != "No consta"]

    df = df.rename(columns={"Nombre":"Immigrants"})
    df.to_csv(path+"Immigracio_sexe_2015-2020.csv", index=False)


def lloguer(path):
    # Clean and merge rent csv

    path = path + "Lloguer/"
    files = os.listdir(path)

    df = pd.DataFrame()
    for file in files:
        if file.endswith('.csv') and file != "Lloguer_2015-2020.csv" and file != "Mitjana_LLoguer_2015-2020.csv":

            temp = pd.read_csv(path+file)
            temp = temp.replace("el Poble Sec", "el Poble-sec")
            df = df.append(temp, ignore_index=True) 

    del df["Codi_Districte"]
    del df["Codi_Barri"]

    for columna in df.columns:
        df = df[df[columna] != "No consta"]

    df = df[df["Lloguer_mitja"] == "Lloguer mitjà mensual (Euros/mes)"]

    temp = df.groupby(["Any","Nom_Districte", "Nom_Barri"], as_index=False)["Preu"].mean()
    # Calculem un df amb els preus mitjans i no per trimestre

    df.to_csv(path+"Lloguer_2015-2020.csv", index=False)
    temp.to_csv(path+"Mitjana_LLoguer_2015-2020.csv", index=False)


def ocupacio(path):
    # Clean and merge ocupation csv

    path = path + "Ocupació Mitjana/"
    files = os.listdir(path)

    df = pd.DataFrame()
    for file in files:
        if file.endswith('.csv') and file != "Ocupacio_Mitjana_2015-2020.csv":

            temp = pd.read_csv(path+file)
            temp = temp.replace("el Poble Sec", "el Poble-sec")

            df = df.append(temp, ignore_index=True) 

    del df["Codi_Districte"]
    del df["Codi_Barri"]

    df.to_csv(path+"Ocupacio_Mitjana_2015-2020.csv", index=False)


def immigracio_edat(path):
    # Clean and merge immigration csv

    path = path + "Immigracio Edat/"
    files = os.listdir(path)
    

    df = pd.DataFrame()

    for file in files:
        if file.endswith('.csv') and file != "Immigracio_Edat_2015-2020.csv":

            temp = pd.read_csv(path+file)
            temp = temp.replace("el Poble Sec", "el Poble-sec")

            if "Codi_districte" in temp.columns:
                temp = temp.rename(columns={"Codi_barri":"Codi_Barri",
                    "Codi_districte":"Codi_Districte", "Nom_barri":
                    "Nom_Barri", "Nom_districte":"Nom_Districte"})

            if "Edats_quinquennals" in temp.columns:
                temp = temp.rename(columns = {"Edats_quinquennals":"Edat_quinquennal"})

            df = df.append(temp, ignore_index=True)


    del df["Codi_Districte"]
    del df["Codi_Barri"]

    for columna in df.columns:
        df = df[df[columna] != "No consta"]

    df = df.rename(columns={"Nombre":"Immigrants"})

    df.to_csv(path+"Immigracio_Edat_2015-2020.csv", index=False)

def emmigracio_edat(path):
    # Clean and merge immigration csv

    path = path + "Emmigracio Edat/"
    files = os.listdir(path)
    

    df = pd.DataFrame()

    for file in files:
        if file.endswith('.csv') and file != "Emmigracio_Edat_2015-2020.csv":

            temp = pd.read_csv(path+file)
            temp = temp.replace("el Poble Sec", "el Poble-sec")

            if "Codi_districte" in temp.columns:
                temp = temp.rename(columns={"Codi_barri":"Codi_Barri",
                    "Codi_districte":"Codi_Districte", "Nom_barri":
                    "Nom_Barri", "Nom_districte":"Nom_Districte"})

            if "Edats_quinquennals" in temp.columns:
                temp = temp.rename(columns = {"Edats_quinquennals":"Edat_quinquennal"})

            df = df.append(temp, ignore_index=True)


    del df["Codi_Districte"]
    del df["Codi_Barri"]

    for columna in df.columns:
        df = df[df[columna] != "No consta"]

    df = df.rename(columns={"Nombre":"Emmigrants"})
    df.to_csv(path+"Emmigracio_Edat_2015-2020.csv", index=False)



paisos = ['Espanya','Itàlia','Pakistan','Xina', 'França', 'Colòmbia', 'Marroc, el',
    'Hondures', 'Veneçuela', 'Perú', 'Brasil', 'Índia', 'Equador', 'Rússia',
    'Argentina', 'Bolívia', 'Estats Units, els', 'Mèxic', 'República Dominicana',
    'Regne Unit', 'Romania', 'Ucraïna', 'Alemanya', 'Filipines', 'Xile', 'Portugal',
    'Paraguai', 'Bangladesh', 'Països Baixos', 'Geòrgia', 'Polònia', 'Cuba', 'Japó',
    'Suècia', 'Algèria', 'Bulgària', 'El Salvador', 'Bèlgica' ,'Turquia', 'Armènia',
    'Uruguai', 'Corea del Sud', 'Hongria', 'Senegal', 'Grècia', 'Canadà', 'Nepal',
    'Egipte', 'Nicaragua', 'Irlanda', 'Suïssa', 'Síria', 'Guatemala', 'Nigèria',
    'Costa Rica', 'Kazakhstan', 'Iran', 'Àustria', 'Guinea', 'Finlàndia', 'Panamà',
    'Dinamarca', 'Líban', 'Txèquia', 'Noruega', 'Lituània', 'Austràlia', 'Ghana',
    'Israel', 'Moldàvia', 'Sèrbia', 'Belarús', 'Letònia', 'Andorra', 'Albània',
    'Eslovàquia', 'Croàcia', 'Líbia', 'Gàmbia', 'Guinea Equatorial', 'Azerbaidjan',
    'Tadjikistan', 'Timor-Leste', 'Malawi', 'Eritrea', 'Txad', 'Botswana',
    'Antigua i Barbuda', 'Lao', 'Illes Salomó', 'Liechtenstein',
    'Saint Vincent i les Grenadines', 'Belize', 'Bhutan', 'Comores, les',
    'Sudan del Sud, el', 'Kirguizistan' ,'Zimbabwe',
    'República Democràtica del Congo', 'Swazilàndia', 'Tonga', 'Palestina',
    'Eslovènia','Camerun','Aràbia Saudí', 'Jordània', 'Estònia',
    'Territoris Palestins (o Palestina)', 'Mali', 'Vietnam', 'Islàndia',
    'Tunísia', 'Sud-àfrica', 'Mauritània', 'Indonèsia', "Iraq, l'", 'Tailàndia',
    'Xipre', 'Afganistan', 'Singapur', 'Bòsnia i Hercegovina', 'Kenya',
    'Macedònia', 'Nova Zelanda', 'Guinea-Bissau', 'Malàisia', 'Mongòlia',
    'Uzbekistan', 'Angola', "Costa d'Ivori", 'Kirguizstan', 'Montenegro', 'Haití',
    'Malta', 'Moçambic', 'Congo', 'Sri Lanka', 'Turkmenistan', 'Burkina Faso',
    'Kuwait', 'Luxemburg', 'Tanzània', 'Zimbàbue', 'Benín', 'Dominica', 'Etiòpia',
    'Iemen, el', 'Jamaica', 'Madagascar', 'Qatar', 'Somàlia', 'Sudan, el', 'Togo',
    'Uganda', 'Cap Verd', 'Gabon', 'Maurici' ,'República Centreafricana', 'Ruanda',
    'Bahrain', 'Barbados', 'Burundi', 'Cambodja', 'Djibouti', 'Grenada', 'Maldives',
    'Namíbia' ,'Oman' ,'Saint Kitts i Nevis', 'Seychelles', 'Sierra Leone',
    'Swaziland', 'Taiwan,Xina', 'Trinidad i Tobago',
    'Territoris Palestins [o Palestina]', 'Emirats Àrabs Units, els', 'Myanmar',
    'Zàmbia', 'Bahames, les', 'Corea del Nord', 'Guyana', 'Lesotho', 'Libèria',
    'Níger' ,'Puerto Rico', 'San Marino', 'São Tomé i Príncipe', 'Surinam', "Sudàfrica"]

paisos_angles = ["Spain", "Italy", "Pakistan", "China", "France", "Colombia",
                "Morocco", "Honduras", "Venezuela", "Peru", "Brazil", "India",
                "Ecuador", "Russia", "Argentina", "Bolivia", "United States of America",
                "Mexico", "Dominican Republic", "United Kingdom", "Romania",
                "Ukraine", "Germany", "Philippines", "Chile", "Portugal",
                "Paraguay", "Bangladesh", "Netherlands", "Georgia", "Poland",
                "Cuba", "Japan", "Sweden", "Algeria", "Bulgaria", "El Salvador",
                "Belgium", "Turkey", "Armenia", "Uruguay", "South Korea",
                "Hungary", "Senegal", "Greece", "Canada", "Nepal", "Egypt",
                "Nicaragua", "Ireland", "Switzerland", "Syria", "Guatemala",
                "Nigeria", "Costa Rica", "Kazakhstan", "Iran", "Austria", "Guinea",
                "Finland", "Panama", "Denmark", "Lebanon", "Czech Republic", 
                "Norway", "Lithuania", "Australia", "Ghana", "Israel", "Moldova",
                "Serbia", "Belarus", "Latvia", "Andorra", "Albania", "Slovakia",
                "Croatia", "Libya", "Gambia", "Equatorial Guinea", "Azerbaijan",
                'Tajikistan', 'Timor-Leste', 'Malawi', 'Eritrea', 'Chad', 'Botswana',
                'Antigua and Barbuda', 'Lao', 'Solomon Islands', 'Liechtenstein',
                'Saint Vincent and the Grenadines', 'Belize', 'Bhutan', 'Comoros',
                "South Sudan", "Kyrgyzstan", "Zimbabwe", 'Democratic Republic of the Congo',
                'Swaziland', 'Tonga', 'Palestine',                
                'Slovenia', 'Cameroon', 'Saudi Arabia', 'Jordan', 'Estonia',
                'Palestine', 'Mali', 'Vietnam', 'Iceland',
                'Tunisia', 'South Africa', 'Mauritania', 'Indonesia', 'Iraq', 'Thailand',
                'Cyprus', 'Afghanistan', 'Singapore', 'Bosnia and Herzegovina', 'Kenya',
                'Macedonia', 'New Zealand', 'Guinea-Bissau', 'Malaysia', 'Mongolia',
                'Uzbekistan', 'Angola', 'Ivory Coast', 'Kyrgyzstan', 'Montenegro', 'Haiti',
                'Malta', 'Mozambique', 'Congo', 'Sri Lanka', 'Turkmenistan', 'Burkina Faso',
                'Kuwait', 'Luxembourg', 'Tanzania', 'Zimbabwe', 'Benin', 'Dominica', 'Ethiopia',
                'Yemen', 'Jamaica', 'Madagascar', 'Qatar', 'Somalia', 'Sudan,', 'Togo',
                'Uganda', 'Cape Verde', 'Gabon', 'Mauritius', 'Central African Republic', 'Rwanda',
                'Bahrain', 'Barbados', 'Burundi', 'Cambodia', 'Djibouti', 'Grenada', 'Maldives',
                'Namibia', 'Oman', 'Saint Kitts and Nevis', 'Seychelles', 'Sierra Leone',
                'Swaziland', 'Taiwan', 'Trinidad and Tobago',
                'Palestine', 'United Arab Emirates', 'Myanmar',
                'Zambia', 'Bahamas', 'North Korea', 'Guyana', 'Lesotho', 'Liberia',
                'Niger', 'Puerto Rico', 'San Marino', 'São Tomé and Príncipe', 'Suriname',
                "South Africa"]

def update_merged_with_zones(path):

    Central_South_America = ["Antigua and Barbuda", "Argentina", "Bahamas", "Barbados", "Bolivia", "Brazil", "Colombia", 
    "Costa Rica", "Cuba", "Dominica", "El Salvador", "Ecuador", "Grenada", "Guatemala", "Haiti", 
    "Honduras", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Dominican Republic", "Saint Kitts and Nevis",
    "Trinidad and Tobago", "Uruguay", "Venezuela", "Chile", "Colmbia", "Jamaica", "Belize"]

    Welfare_Countries = ["Germany", "Andorra", "Australia", "Austria", "Belgium", "Canada", "South Korea", "Denmark", 
        "Spain", "United States of America", "Finland", "France", "Greece", "Ireland", "Iceland", "Italy", "Japan", 
        "Luxembourg", "Malta", "Norway", "New Zealand", "Netherlands", "Poland" , "Portugal", "United Kingdom", 
        "Sweden", "Switzerland", "Czech Republic"]

    Africa = ["Angola", "Botswana", "Burkina Faso", "Cameroon", "Cape Verde", "Congo", "Ivory Coast", "Djibouti", "Ethiopia", 
        "Gabon", "Gambia", "Ghana", "Equatorial Guinea", "Guinea-Bissau", "Kenya", "Liberia", "Malawi", "Mali", "Mauritania", "Mozambique",
        "Namibia", "Niger", "Nigeria", "Central African Republic", "Rwanda", "Senegal", "Somalia", "South Africa", 
        "Sudan", "Tanzania", "Togo", "Uganda", "Zimbabwe", "Guinea", "Zambia", "Sierra Leone", "Sudan,",
        "Madagascar", "Benin", "Mauritius", "Burundi", "Eritrea", "Seychelles", "Chad"]

    Arabic_Countries = ['Algeria', "Syria", 'Saudi Arabia', 'Azerbaijan', 'Egypt', 'United Arab Emirates', 'Iemen', 'Iran', 'Iraq', 
        'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Libya', "Yemen", 'Brown',"Oman",'Palestine','Qatar',"Morocco",'Tunisia']

    East_Europe_Asia_Central = ['Albania', 'Armenia', 'Belarus','Bosnia and Herzegovina','Bulgaria','Croatia','Slovakia',
        'Slovenia','Estonia','Georgia','Hungary','North Korea','Kazakhstan','Kyrgyzstan','Latvia', 'Lithuania','Macedonia',
        'Moldova','Montenegro','Romania','Russia','Serbia','Tajikistan','Turkemnistan', 'Turkey', 'Ukraine', 'Uzbekistan', 
        'Cyprus', "Turkmenistan"]

    South_Asia = ["Afghanistan", "Bangladesh", "Mongolia", "India", "Nepal", "Pakistan", "Sri Lanka", "Vietnam", "China"]

    East_Asia_Pacific = ["Cambodia", "Philippines", "Indonesia", "Malaysia",  "Myanmar", "Singapore", "Thailand"]

    zones = [Central_South_America, Welfare_Countries, Africa, Arabic_Countries, East_Asia_Pacific, East_Europe_Asia_Central, South_Asia]

    df = pd.read_csv(path + "Immigracio_Emmigracio_2015-2020.csv")
    zones_str = ["Central South America", "Welfare Countries", "Africa", "Arabic Countries", "East Asia Pacific", "East Europe Asia Central", "South Asia"]
    nationality_list = df["Nationality"].tolist()
    nationality_zone = []

    for nationality in nationality_list:
        i = 0
        appended = False
        for zone in zones:

            if nationality in zone:
                appended = True
                nationality_zone.append(zones_str[i])

            i += 1


        if appended == False:
            print(nationality)
    df["Zone"] = nationality_zone
    df.to_csv("C:/Users/Pol/OneDrive - UAB/Segon Semestre/Visualització/Projecte/Immigracio_Emmigracio_2015-2020.csv", index=False)


general_path = "C:/Users/Pol/OneDrive - UAB/Segon Semestre/Visualització/Projecte/"
# Estructura directoris:
#   - Emmigracio/
#   - Emmigracio Sexe/
#   - Immigracio/
#   - Immigracio Sexe/
#   - Immigracio percentatge/
#   - Lloguer/
#   - Ocupacio Mitjana/



emmigracio(general_path, paisos, paisos_angles)
emmigracio_sexe(general_path)
immigracio(general_path, paisos, paisos_angles)
immigracio_sexe(general_path)
lloguer(general_path)
ocupacio(general_path)
merge_quantitat_immigracio_emmigracio(general_path)
merge_sexe_immigracio_emmigracio(general_path)
update_merged_with_zones(general_path)
immigracio_edat(general_path)
emmigracio_edat(general_path)
merge_edat_immigracio_emigracio(general_path)
merge_ocupacio_lloguer(general_path)


