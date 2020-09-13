import requests

while True : 
    try : 
        name = input("Pokemon's name : ")
        print()
        url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
        data = requests.get(url)
        output = data.json()
        #name
        insert_name = output["name"] 
        print(f'Name : {insert_name.title()}')
        #stat
        stat_name= output["stats"]
        j = 0
        for i in stat_name :
            if j != 3 and j != 4 :
                print(f'{(i["stat"]["name"].title())} : {i["base_stat"]}')
            j+=1

        #type
        type = output["types"][0]["type"]["name"]
        print(f'Type : {type.title()}')
        #url
        url_image = output['sprites']['front_default']
        print(f'URL : {url_image}')
        #abilities
        abilities = output['abilities']
        j = 1
        for i in abilities :
            print(f'Ability Name {j} : {(i["ability"]["name"]).title()}')
            j+=1   
        break 
    except : 
        print("Pokemon's name not found\n")
        continue






