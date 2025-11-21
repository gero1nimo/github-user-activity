import requests, sys

def connection(method: str, url: str):
    """Connection establishment through requested method and to requested api"""
    
    try:
        response = requests.request(method.upper(), url)
        response.raise_for_status()  # Raises HTTPError for bad status codes
        return response
    
    except requests.exceptions.ConnectionError as err:
        raise requests.exceptions.ConnectionError(f"Connection is not established: {err}")
    except requests.exceptions.Timeout:
        raise requests.exceptions.Timeout("Request timed out")
    except requests.exceptions.HTTPError as err:
        raise requests.exceptions.HTTPError(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        raise requests.exceptions.RequestException(f"Request failed: {err}")
    
    
    

def fetch_data(owner: str):
    url = f"https://api.github.com/users/{owner}/events"
    response = connection("get", url)
    
    if response == None:
        return None
    
    return response.json()


def format_print_data(data: list):
    for event in data:
        print(f"Type: {event['type']}, Repo: {event['repo']['name']}, Created at: {event['created_at']}")
        
    activity_summary = {}
    for event in data:
        activity_summary[event['type']] = activity_summary.get(event['type'], 0) + 1
        
    print("\nActivity Summary:")
    print(activity_summary)
    
    
if __name__ =="__main__":
    print("GitHub User Activity Fetcher")
    print("Enter the GitHub username to fetch activity data.")

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Username: ").strip()
    data = fetch_data(username)
    if data:    
        format_print_data(data)