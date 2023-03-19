# make-mermaid-swim-by-db
make mermaid ER code from db (python)

# Require
- Python3.10
- sqlalchemy
- mysqlclient
- **your (mysql)DB**

# usage
- install
```
pip install DB2mermaid
```

- use
```
from db2mermaid.db2mermaid import DB2Mermaid
    dm = DB2Mermaid()
    dm.init_db("user", "pasword", "127.0.0.1", "3306", "db_name")
    dm.generate()
```

then, you will get `er.md`

# Caution ❗
this package is not full.
It cannot generate table relation, can only generate table definition 😢.
(And now, only mysql... 🤣)

# Future
Make CLI