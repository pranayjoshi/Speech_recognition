import json
import os    
a = input("enter the application name: ")
b = input(f"enter the {a}'s location: ")
b.replace('\\', '/')
dic = {}
dic[a] = b
try:
    with open("app_file.json", "r+") as file:
        data = json.load(file)
        if next(iter(dic)) not in data.keys():
            data.update(dic)
            file.seek(0)
            json.dump(data, file)
            print(data)    
        else:
            print("the application's name is already registered.\do you want to overwrite it.")
            s = input()
            s.lower()
            if "y" in s:
                data.update(dic)
                file.seek(0)
                json.dump(data, file)
                print(data)
            elif "n" in s:
                print("Okay!")
            else:
                print("not recognised")
except FileNotFoundError as fe:
    with open("app_file.json", "w+") as file:
        json.dump(dic, file)