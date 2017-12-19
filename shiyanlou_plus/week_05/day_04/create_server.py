import requests


REQUEST_SITE = "http://127.0.0.1:5000/servers/"


def create_server(name, host):
    data = {"name": name, "host": host}
    result = requests.post(REQUEST_SITE, json=data)
    return result.json()


if __name__ == "__main__":
    create_server("t2", "127.0.0.1")
