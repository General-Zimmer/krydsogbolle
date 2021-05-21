import mysql.connector


class mysql_connector:
    # Setup a connection to the mysql database
    def __init__(self):
        self.mysql = mysql.connector.connect(host="148.251.68.245", user="skole", database="skole")
        self.curs = self.mysql.cursor(buffered=True)

        # With a dictionary for conversion used later
        self.dict = {
            "gameid": 0,
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
                "CREATE TABLE game (gameid int(11), "
                "kryds VARCHAR(255), "
                "bolle VARCHAR(255), "
                "turn INT(1), "
                "moves INT(255))")

    # Make a database interaction and commit it
    def _do(self, cmd: str, val = None):
        if val is None:
            self.curs.execute(cmd, multi=True)
        else:
            self.curs.execute(cmd, val, multi=True)

        if val != "no commit":
            self.mysql.commit()
            row = self.curs.fetchone()
            if row is not None:
                return row[0]

    def testrow(self, gid):
        test = "SELECT 1 FROM game WHERE gameid = {id}"
        return self._do(test.format(id=gid))

    # Add a row to the table.
    def add(self, gameid, turn, moves, kryds: str = "", bolle: str = ""):
        add = "INSERT INTO game (gameid, kryds, bolle, turn, moves) VALUES (%s, %s, %s, %s, %s)"
        val = (gameid, kryds, bolle, turn, moves)
        self._do(add, val)

    # Deletes a row in the table
    def delete(self, ting: str, column: str = "gameid"):
        delete = "DELETE FROM game WHERE {column} = '{ting}'"
        self._do(delete.format(ting=ting, place=column))

    # Pull a row from the table
    def pull(self, hvad: str, column: str = "gameid"):
        pull = "SELECT * FROM game"
        self._do(pull, "no commit")
        row = self.curs.fetchone()
        while row is not None:
            if str(row[self.dict.get(column)]) == hvad:
                return row
            else:
                row = self.curs.fetchone()

    # Pull all rows
    def pullall(self):
        pull = "SELECT * FROM game"
        self._do(pull)
        pAll = self.curs.fetchall()
        return pAll

        # Search is the exact value in a column you're using to find a row
        # replace is the value you're using to replace
        # whatchange is the column you're editing
        # whatsearch is the column you're searching for

    def modify(self, search, replace, whatchange: str = "moves", whatsearch: str = "gameid"):
        print(replace)
        modify = "UPDATE game SET {whatchange} = '{replace}' WHERE {whatsearch} = '{_}'"
        self._do(modify.format(whatsearch=whatsearch, whatchange=whatchange, replace=replace, _=search))

    # Close the connection to the database
    def close(self):
        self.mysql.close()

    # Open a connection to the database
    def connect(self):
        self.mysql.connect()
