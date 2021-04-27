import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes": 10, "name": "hacking", "views": 1234},
        {"likes": 3213, "name": "Learn Rest API using Flask", "views": 765754},
        {"likes": 4324, "name": "Learn Python", "views": 76642},
        {"likes": 10545, "name": "learn web hacking", "views": 6534},
        {"likes": 7676, "name": "learn to write blog", "views": 99756}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.patch(
    BASE + "/video/2", {"views": 123213213})
print(response.json())
