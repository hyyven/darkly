from requests import get

def main():
    url = "http://localhost:8080/index.php?page=signin&username=admin&password=shadow&Login=Login#"

    response = get(url)
    print(response.text)

if __name__ == "__main__":
	main()