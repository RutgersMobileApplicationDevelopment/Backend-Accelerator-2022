import requests, sys

server_URI = "http://127.0.0.1:5000/"
while True:
    try:
        req = input("REQTYPE (GET/POST) = ")
        if req not in ("GET","POST"):
            print("Please enter a valid request type.")
            continue

        if req == "GET":
            recipe_id = input("ID = ")
            resp = requests.get(f"{server_URI}/recipes?id={recipe_id}")
            print("-"*8)
            print(resp.json())
            print("-"*8)

        elif req == "POST":
            poster = input("Poster = ")
            name = input("Name = ")
            ingredients = input("Ingredients = ")

            resp = requests.post(
                f"{server_URI}/recipes",
                {"poster":poster,"name":name,"ingredients":ingredients}
            )
            print("-"*8)
            print(resp.json())
            print("-"*8)

        print("\n"*2)


    except KeyboardInterrupt:
        sys.exit(0)
