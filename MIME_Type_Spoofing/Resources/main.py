import requests

def main():
    url = "http://localhost:8080/index.php?page=upload"
    file_path = "screen.png"

    with open(file_path, "rb") as f:
        files = {"uploaded": ("screen.png", f, "image/jpeg")}
        data = {"MAX_FILE_SIZE": "100000", "Upload": "Upload"}
        response = requests.post(url, files=files, data=data)
        print(response.text)

if __name__ == "__main__":
	main()