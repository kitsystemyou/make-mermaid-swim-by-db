from sqlalchemy import create_engine, MetaData


class DB2Mermaid:
    _user = ""
    _password = ""
    _host = ""
    _port = ""
    _db_name = ""
    _db_uri = ""

    def __init__(self):
        self._user = "user"
        self._password = "password"
        self._host = "host"
        self._port = "3306"
        self._db_name = "db_name"
        self._db_uri = f"mysql://{self._user}:{self._password}@{self._host}:{self._port}/{self._db_name}"

        engine = create_engine(self._db_uri)
        self.meta = MetaData()
        self.meta.reflect(bind=engine)

    def set_db_config(self, user, password, host, port, db_name):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name

    def write_texts(self, lines: list[str]):
        f = open('er.md', 'a', encoding='UTF-8')
        f.writelines(lines)
        f.close()

    def init_text(self):
        self.write_texts(["```mermaid\n", "erDiagram\n"])

    def close_text(self):
        self.write_texts(["```"])

    def create_row_per_column(self, column_data) -> str:
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

    def generate(self):
        self.init_text()

        for n, t in self.meta.tables.items():
            texts: list[str] = []
            texts.append("    " + n + "{\n")
            print("table name🌟", n)
            for c in t.columns.values():
                texts.append(self.create_row_per_column(c))
            texts.append("}\n")
            self.write_texts(texts)

        self.close_text()


if __name__ == "__main__":
    d = DB2Mermaid()
    d.set_db_config("user", "pass", "localhost", "3306", "db_name")
    print(d._db_uri)
    d.generate()
