import mysql.connector


class database:
    # Setup a connection to the mysql database
    def __init__(self):
        self.mysql = mysql.connector.connect(host="148.251.68.245", user="skole", database="skole")
        self.curs = self.mysql.cursor(buffered=True)

        # With a dictionary for conversion used later
        self.dict = {
            "GameID": 0,
            "kryds": 1,
            "bolle": 2,
            "turn": 3,
            "moves": 4
        }

        # and add necessary tables
        self.curs.execute("SHOW TABLES")
        tables = self.curs.fetchall()
        if ('game',) not in tables:
            self.curs.execute(
                "CREATE TABLE game (gameid int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, kryds VARCHAR(255), bolle VARCHAR(255), turn INT(2), moves INT(255))")

    # Do a database interaction and commit it
    def _do(self, cmd: str, val: tuple = None):
        if val is None:
            self.curs.execute(cmd)
        else:
            self.curs.execute(cmd, val)

        if val != {"nocom": "yeet"}:
            self.mysql.commit()

    # Add a row to the table.
    def add(self, navn: str, dato: str):
        add = "INSERT INTO game (name, dato) VALUES (%s, %s)"
        val = (navn, dato)
        self._do(add, val)

    # Deletes a row in the table
    def delete(self, ting: str, place: str = "name"):
        delete = "DELETE FROM game WHERE {place} = '{ting}'"
        self._do(delete.format(ting=ting, place=place))

    # Pull a row from the table
    def pull(self, hvad: str, ting: str = "name"):
        pull = "SELECT * FROM game"
        self._do(pull.format(name=ting), {"nocom": "yeet"})
        row = self.curs.fetchone()

        while row is not None:
            if row[self.dict.get(ting)] == hvad:
                return row
            else:
                row = self.curs.fetchone()

    # Pull all rows
    def pullall(self):
        pull = "SELECT * FROM game"
        self._do(pull)
        pAll = self.curs.fetchall()
        return pAll

    # Ændre en værdi i en bestemt række.
    # Search er data'en du søger efter.
    # replace er det som du godt vil ændre den gamle værdi til.
    # whatchange bestemmer hvilken værdi i rækken du ændre.
    # whatsearch bestemmer hvilken værdi i rækken du søger efter.
    def modify(self, search: str, replace: str, whatchange: str = "dato", whatsearch: str = "name"):
        result = self.pull(search, whatsearch)
        yeet = "" + result[self.dict.get(whatchange)]
        modify = "UPDATE game SET {change} = '{replace}' WHERE {change} = '{ree}'"
        self._do(modify.format(change=whatchange, replace=replace, ree=yeet))

    def loop(self, move):
        while True:
            self.pull("move")



    # Close the connection to the database
    def close(self):
        self.mysql.close()

    # Open a connection to the database
    def connect(self):
        self.mysql.connect()
