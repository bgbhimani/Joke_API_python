import requests

base_url = "https://v2.jokeapi.dev/joke"

def get_joke(type):
    url = f"{base_url}/{type}"
    response = requests.get(url)
    if response.status_code == 200:
        # print("Get Connected")
        print(url)
        joke = response.json()
        if joke["error"] == False:
            print(f'Joke-Id:  {joke["id"]}')
            if joke["type"] == "single":
                print(joke["joke"])
            else:
                print(joke["setup"])
                print(joke["delivery"])
        else:
            print(f"Joke Not Found on {type[13:]}")
    else:
        print(f"Not Connected Error:{response.status_code}")

print("::::Enjoy and Laugh::::")


choice = input("Enter Your Choice:\n1.Programming  2.Dark 3.Christmas 4.Random\n")
type= "Any"
match (choice):
    case "1":
        type = "Programming"
    case "2":
        type = "Dark"
    case "3": 
        type = "Christmas"
    case "4":
        type = "Any"
    case _:
        type = f"Any?contains={choice}"
        # print("Enter Valid Input..")
get_joke(type=type)