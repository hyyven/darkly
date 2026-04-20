from requests import get

def main():
    url = "http://localhost:8080/whatever/htpasswd"

    response = get(url)
    print(response.text, end="")

if __name__ == "__main__":
	main()