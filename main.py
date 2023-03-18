from sqlalchemy import create_engine, MetaData
# from sqlalchemy.sql import text
# import pymysql

user = "root"
password = "pass"
host = "127.0.0.1"
port = "3307"
db_name = "charamane"

db_uri = f"mysql://{user}:{password}@{host}:{port}/{db_name}"
engine = create_engine(db_uri)
meta = MetaData()
meta.reflect(bind=engine)
print(meta.tables.keys())


def write_texts(lines: list):
    f = open('er.md', 'a', encoding='UTF-8')
    f.writelines(lines)
    f.close()


def init_text():
    write_texts(["```mermaid\n", "erDiagram\n"])


def close_text():
    write_texts(["```"])


def create_row_per_column(column_data):
    print(column_data)
    line = f"        {column_data.type} {column_data.name}"
    if column_data.primary_key:
        line += " PK"
        return line + "\n"
    elif column_data.foreign_keys:
        line += " FK"
        return line + "\n"
    else:
        return line + "\n"


init_text()

for n, t in meta.tables.items():
    texts = []
    texts.append("    " + n + "{\n")
    print("table name🌟", n)
    print("record", t.c)
    for c in t.columns.values():
        # print(c.name, c.type, c.autoincrement, c.default, c.nullable, c.primary_key, c.index, c.comment)
        texts.append(create_row_per_column(c))
    texts.append("}\n")
    print(texts)
    write_texts(texts)

close_text()