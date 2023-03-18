from sqlalchemy import create_engine, MetaData

user = ""
password = ""
host = ""
port = ""
db_name = ""

db_uri = f"mysql://{user}:{password}@{host}:{port}/{db_name}"
engine = create_engine(db_uri)
meta = MetaData()
meta.reflect(bind=engine)


def main():
    init_text()

    for n, t in meta.tables.items():
        texts: list[str] = []
        texts.append("    " + n + "{\n")
        print("table name🌟", n)
        for c in t.columns.values():
            texts.append(create_row_per_column(c))
        texts.append("}\n")
        write_texts(texts)

    close_text()


def write_texts(lines: list[str]):
    f = open('er.md', 'a', encoding='UTF-8')
    f.writelines(lines)
    f.close()


def init_text():
    write_texts(["```mermaid\n", "erDiagram\n"])


def close_text():
    write_texts(["```"])


def create_row_per_column(column_data) -> str:
    # gettable: name, type, autoincrement, default, nullable, primary_key, foreign_key, index, comment
    line = f"        {column_data.type} {column_data.name}"
    if column_data.primary_key:
        line += " PK"
        return line + "\n"
    elif column_data.foreign_keys:
        line += " FK"
        return line + "\n"
    else:
        return line + "\n"


if __name__ == "__main__":
    main()