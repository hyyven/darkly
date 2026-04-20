from requests import get

# Use this to get it faster

def main():
    url = "http://localhost:8080/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README"

    response = get(url)
    print(response.text, end="")

if __name__ == "__main__":
	main()