# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import requests
import json



def getHouseData(loc):

    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

    querystring = {"location": loc, "home_type": "Houses,Multi-family,Apartments,Condos,LotsLand"}

    headers = {
        "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com",
        "X-RapidAPI-Key": "User your Own"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()["props"]
    return data

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

def getRentalData(address, property_type):


    url = "https://zillow-com1.p.rapidapi.com/rentEstimate"

    querystring = {"propertyType": property_type, "address": address}

    headers = {
        "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com",
        "X-RapidAPI-Key": "User your Own"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    return data







if __name__ == '__main__':

    rental = dict()
    house_datas = getHouseData("dallas,tx")

    for house_data in house_datas:
        renta_data = getRentalData(house_data['address'], house_data['propertyType'].title())
        rental[house_data['address']] = (int(renta_data['median'])/int(house_data['price'])) * 100.0
    sorted_res = dict(sorted(rental.items(), key=lambda item: item[1]))


