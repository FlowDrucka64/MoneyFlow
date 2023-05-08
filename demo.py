import yaml
import json
from pprint import *
from yaml.loader import SafeLoader



# returns a tuple (juri_cnt,cnt) where juri_cnt is the amount
# entries that have at least one jursisdiction set
# and cnt is the overall amount of entries
def countJurisdictionsSet(data):
    cnt =0
    juri_cnt = 0
    for actor in data["actors"]:
        cnt += 1
        if 'jurisdictions' in actor.keys():
            if actor["jurisdictions"] != []:
                if len(actor['jurisdictions'])>1:
                    juri_cnt +=1
                    pprint(actor)
    return (juri_cnt,cnt)


# returns a dict of all the countries which are set as 
# jurisdictions with their occurence counts
def countCountriesSet(data):
    countries =  dict()
    for actor in data["actors"]:
        if 'jurisdictions' in actor.keys():
            if len(actor['jurisdictions'])>0:
                for country in actor['jurisdictions']:
                    if country not in countries.keys():
                        countries[country] = 0
                    countries[country] +=1
    return countries

# returns a dict of all the occuring catagories
# with their occurence counts
def countCategoriesSet(data):
    categories =  dict()
    for actor in data["actors"]:
        if 'categories' in actor.keys():
            if len(actor['categories'])>0:
                for category in actor['categories']:
                    if category not in categories.keys():
                        categories[category] = 0
                    categories[category] +=1
    return categories

# returns a dict of all the occuring catagories of entries having jurisdiction set
# with their occurence counts
def countCategoriesSetWithJursidictionSet(data,juricnt):
    categories =  dict()
    for actor in data["actors"]:
        if 'jurisdictions' in actor.keys():
            if len(actor['jurisdictions'])>0:
                if 'categories' in actor.keys():
                    if len(actor['categories'])>juricnt:
                        for category in actor['categories']:
                            if category not in categories.keys():
                                categories[category] = 0
                            categories[category] +=1
    return categories

if __name__ == '__main__':
    with open('graphsense.actorpack.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
        (juri_cnt,cnt) = countJurisdictionsSet(data)
        print("{}/{} juristdictions set".format(juri_cnt,cnt))

        countryDict = countCountriesSet(data)
        pprint(countryDict)

        categoryDict = countCategoriesSet(data)
        pprint(categoryDict)

        for i in range(10):
            print(">{} juri".format(i))
            categoryDict = countCategoriesSetWithJursidictionSet(data,i)
            pprint(categoryDict)
