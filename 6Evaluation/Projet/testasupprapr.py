import numpy as np  
import pandas as pd
import os


def main():

    df = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+"/newscrawler/titlelink.csv").to_dict()

    #On récupère le dictionnaire de chaque page qui relie titre et lien sous la forme d'une string par page
    l = list(list(df.values())[0].values())
    
    #On découpe toute la string de manière à isoler tous les liens
    links = [l[i].strip().split("'") for i in range (len(l))]
    #Nous avions une liste de liste pour chacunes de pages, on rassemble tout sous une grande liste
    links = [string for l in links for string in l]
    #On garde uniquement les éléments étant des liens
    links = [ x for x in links if 'https' in x]


    print(links)

    return None


if __name__ == '__main__':
    main()