import requests



########################
# Connection Establishment
# Fetching Datas
# Parsing Data 
# Listing Accordingly

def connection(method: str, url: str):
    session = requests.Session()
    try:
        request = session.request(method=method, url=url)
        return request
    except requests.exceptions.RequestException as err:
        print(err)
    
    return None

def fetch_data(owner: str):
    url = f"https://api.github.com/users/{owner}/events"
    try:
        request = connection("Get", url)
    
    except requests.exceptions.RequestException as err:
        print(err.args)
        return None
    
    return request.json() if request.status_code == 200 else None

def format_data(data):
    for d in data:
        print(d)

# format_data(fetch_data("gero1nimo"))
    
  
username = str(input("Enter the username: "))        

print(fetch_data(username))

