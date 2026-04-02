from requests import post

def main():
    url = "http://localhost:8080/index.php?page=survey"

    data = {
        "sujet": "2",
        "valeur": "15"
    }

    response = post(url, data=data)
    print(response.text)

if __name__ == "__main__":
	main()