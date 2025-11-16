import requests

api_url = "https://api.github.com/users/{owner}/events"


def fetch_events(owner, api_url):
    api_url = api_url.format(owner=owner)
    try:
        request = requests.get(api_url)
        data = request.json()
        activity_count = len(data)
        activity_types = {}
        repo_activities = {}
        for d in data:
            activity_types[d["type"]] = activity_types.get(d["type"], 0) + 1
            data_repo = d["repo"]["name"]
            repo_activities[data_repo] = repo_activities.get(data_repo, list(d['type'])) + d['type']
            
        return request.status_code, data, activity_count, activity_types, repo_activities

    except requests.exceptions.RequestException as err:
        print("The username is not valid:", err)
        return None


name = str(input("Enter the username: "))
result = fetch_events(name, api_url)
if result != None:
    print("Request Status Code:", result[0])
    print(result[-1])
    # print(result)
