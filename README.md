# make-mermaid-swim-by-db
make mermaid ER code from db (python)


# usage
- install
```
pip install DB2mermaid
```

- use
```
    dm = DB2Mermaid.DB2Mermaid()
    dm.init_db("user", "pasword", "127.0.0.1", "3306", "db_name")
    dm.generate()
```

# Caution ❗
this package is not full.
It cannot generate table relation, can only generate table definition 😢.
(And now, only mysql... 🤣)