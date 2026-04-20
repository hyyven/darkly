from requests import post

def main():
    url = "http://localhost:8080/admin/"

    data = {
        "username": "root",
        "password": "qwerty123@",
        "Login": "Login"
    }

    response = post(url, data=data)
    print(response.text)

if __name__ == "__main__":
	main()