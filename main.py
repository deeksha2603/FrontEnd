from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

dataset = [
    {
        "login": "mojombo",
        "id": 1,
        "node_id": "MDQ6VXNlcjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/1?v=4",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/mojombo",
            "repos_url": "https://api.github.com/users/mojombo/repos",
            "received_events_url": "https://api.github.com/users/mojombo/received_events"
        },
        "type": "Admin"
    },
    {
        "login": "defunkt",
        "id": 2,
        "node_id": "MDQ6VXNlcjI=",
        "avatar_url": "",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/defunkt",
            "repos_url": "https://api.github.com/users/defunkt/repos",
            "received_events_url": "https://api.github.com/users/defunkt/received_events"
        },
        "type": "User"
    },
    {
        "login": "pjhyett",
        "id": 3,
        "node_id": "MDQ6VXNlcjM=",
        "avatar_url": "",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/pjhyett",
            "repos_url": "https://api.github.com/users/pjhyett/repos",
            "received_events_url": "https://api.github.com/users/pjhyett/received_events"
        },
        "type": "User"
    },
    {
        "login": "wycats",
        "id": 4,
        "node_id": "MDQ6VXNlcjQ=",
        "avatar_url": "",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/wycats",
            "repos_url": "https://api.github.com/users/wycats/repos",
            "received_events_url": "https://api.github.com/users/wycats/received_events"
        },
        "type": "User"
    },
    {
        "login": "ezmobius",
        "id": 5,
        "node_id": "MDQ6VXNlcjU=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5?v=4",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/ezmobius",
            "repos_url": "https://api.github.com/users/ezmobius/repos",
            "received_events_url": "https://api.github.com/users/ezmobius/received_events"
        },
        "type": "User"
    },
    {
        "login": "ivey",
        "id": 6,
        "node_id": "MDQ6VXNlcjY=",
        "avatar_url": "https://avatars.githubusercontent.com/u/6?v=4",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/ivey",
            "repos_url": "https://api.github.com/users/ivey/repos",
            "received_events_url": "https://api.github.com/users/ivey/received_events"
        },
        "type": "Admin"
    },
    {
        "login": "evanphx",
        "id": 7,
        "node_id": "MDQ6VXNlcjc=",
        "avatar_url": "",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/evanphx",
            "repos_url": "https://api.github.com/users/evanphx/repos",
            "received_events_url": "https://api.github.com/users/evanphx/received_events"
        },
        "type": "Admin"
    },
    {
        "login": "vanpelt",
        "id": 17,
        "node_id": "MDQ6VXNlcjE3",
        "avatar_url": "",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/vanpelt",
            "repos_url": "https://api.github.com/users/vanpelt/repos",
            "received_events_url": "https://api.github.com/users/vanpelt/received_events"
        },
        "type": "User"
    },
    {
        "login": "wayneeseguin",
        "id": 18,
        "node_id": "MDQ6VXNlcjE4",
        "avatar_url": "https://avatars.githubusercontent.com/u/18?v=4",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/wayneeseguin",
            "repos_url": "https://api.github.com/users/wayneeseguin/repos",
            "received_events_url": "https://api.github.com/users/wayneeseguin/received_events"
        },
        "type": "User"
    },
    {
        "login": "brynary",
        "id": 19,
        "node_id": "MDQ6VXNlcjE5",
        "avatar_url": "https://avatars.githubusercontent.com/u/19?v=4",
        "gravatar_id": "",
        "url": {
            "html_url": "https://github.com/brynary",
            "repos_url": "https://api.github.com/users/brynary/repos",
            "received_events_url": "https://api.github.com/users/brynary/received_events"
        },
        "type": "User"
    }
]

@app.route('/', methods=['GET'])
def index():
    global dataset
    newdataset = []
    for i in dataset:
        var1 = i['login']
        var2 = i['avatar_url']
        var3 = i['url']['html_url']
        var4 = i['type']

        tempdict = {
            'login': var1,
            'avatar_url': var2,
            'html_url': var3,
            'type': var4
        }
        newdataset.append(tempdict)

    return str(newdataset)
if __name__ == '__main__':
    app.run(debug=True)