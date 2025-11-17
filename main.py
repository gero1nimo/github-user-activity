import requests, json



########################
# Connection Establishment
# Fetching Datas
# Parsing Data 
# Listing Accordingly

def connection(method: str, url: str):
    session = requests.Session()
    try:
        request = session.request(method=method, url=url)
        return request if request.status_code == 200 else None
    
    except requests.exceptions.RequestException as err:
        print(err)
    
    return None

def fetch_data(owner: str):
    url = f"https://api.github.com/users/{owner}/events"
    try:
        request = connection("Get", url)
        return request.json() if request != None else None
        
    except requests.exceptions.RequestException as err:
        print(err.args)
    
    return None
    

def format_data(data):
    activity_types = {}
    for d in data:
        activity_types[d['type']] = activity_types.get(d['type'], 0) +1
        print(activity_types)

# format_data(fetch_data("gero1nimo"))
    
  
# username = str(input("Enter the username: "))        
username = "gero1nimo"        

data = fetch_data(username)
if data != None:
    print(len(fetch_data(username))) 
    print(type(fetch_data(username)))
    format_data(data)



# with open("response.json", "a") as file:
#     json.dump(fetch_data(username),file, indent=4)
    
# file.close()