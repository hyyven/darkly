import requests

def main():
	payload = "ca c'est du payload"
	response = requests.get(f"http://localhost:8080/index.php?page=redirect&site={payload}")
	print(response.text)

if __name__ == "__main__":
	main()