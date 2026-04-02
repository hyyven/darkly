from requests import post

def main():
    url = "http://localhost:8080/index.php?page=feedback"

    data = {
        "txtName": "ffffffffffffffffffffffffffffffff",
        "mtxtMessage": "f"
    }

    response = post(url, data=data)
    print(response.text)

if __name__ == "__main__":
	main()