import requests
key = "73e884c97ab06d5bed50133ead907eb8"
opsi ={'1' : "Mencari Resto", '2' : "Daily Menu"}

while True :
    print("Selamat Datang di Aplikasi Tomatos")
    for keys,values in opsi.items():
        print(f"{keys}.{values}")
    menu = input('Input menu opsi : ')
    if opsi.get(menu) == 'Mencari Resto' :
        kota = input("Masukkan nama kota : ")
        input1 = False
        host = f"https://developers.zomato.com/api/v2.1/locations?query={kota}"
        HeadInfo = {"user-key" : key}
        data = requests.get(host, headers = HeadInfo)
        output = data.json()
        kota_id = output['location_suggestions'][0]['entity_id']
        kota_type = output['location_suggestions'][0]['entity_type']
        res_count = input("Masukkan Jumlah Restoran yang akan ditampilkan : ")
        print()
        host = f"https://developers.zomato.com/api/v2.1/search?entity_id={kota_id}&entity_type={kota_type}&count={res_count}"
        data = requests.get(host, headers = HeadInfo)
        output = data.json()
        res = output["restaurants"]
        
        j = 1
        if res_count.isnumeric():
            for i in res :
                input1 = True
                print(f'{j} Nama Restauran : {i["restaurant"]["name"]}')
                print(f'Establishment : {" ".join(i["restaurant"]["establishment"])}')
                print(f'Cuisines : {i["restaurant"]["cuisines"]}')
                print(f'Alamat : {i["restaurant"]["location"]["address"]}')
                print(f'No Telepon : {i["restaurant"]["phone_numbers"]}')
                print(f'Rating : {i["restaurant"]["user_rating"]["aggregate_rating"]}')
                print(f'Review : {i["restaurant"]["all_reviews_count"]}')
                j+=1
                print()
        else :
            print("Masukkan jumlah restoran dengan benar atau Nama kota yang benar\n")
            continue
        if input1 == False :
            print("Masukkan nama kota yang tersedia atau jumlah restoran yang benar\n")
            continue
        else :
            break
    elif  opsi.get(menu) == 'Daily Menu' :
        resto_name = input("Masukkan nama resto : ")
        kota = input("Masukkan nama kota : ")
        # input1 = False
        host = f"https://developers.zomato.com/api/v2.1/locations?query={kota}"
        HeadInfo = {"user-key" : key}
        data = requests.get(host, headers = HeadInfo)
        output = data.json()
        kota_id = output['location_suggestions'][0]['entity_id']
        kota_type = output['location_suggestions'][0]['entity_type']
        host = f"https://developers.zomato.com/api/v2.1/search?entity_id={kota_id}&entity_type={kota_type}&q={resto_name}"
        data = requests.get(host, headers = HeadInfo)
        output = data.json()
        resto = output["restaurants"]
        for i in resto : 
            print(f"id {i['restaurant']['R']['res_id']}")
        host = f"https://developers.zomato.com/api/v2.1/search?entity_id={kota_id}&entity_type={kota_type}&q={resto_name}"
        data = requests.get(host, headers = HeadInfo)
        output = data.json()
        break
    else :
        print("Masukkan menu opsi dengan benar\n")
    
        

    




# kategori = output['categories']
# print(len(output['categories']))
# daftar_kategori = []
# for i in range(len(kategori)) :
#     daftar_kategori.append(kategori[i]['categories']['name'])
# print(daftar_kategori)

# for i in kategori :
#     print(i['categories']['name'])

    #kalo gaada daily menu gimana, kalo tutup gimana
    #bikin while loop, kalo gaada nanti keluar lagi menunya