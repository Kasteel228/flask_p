import sqlite3

from apppi import app


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
    pass

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self, title, url):
        try:
            self.__cur.execute('INSERT INTO mainmenu VALUES(NULL, ?, ?)', (title, url))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления в БД', e)
            return False
        return True

    def delMenu(self, title, url):
        try:
            if id == 0:
                self.__cur.execute('INSERT INTO mainmenu')
            else:
                pass
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления в БД', e)
            return False
        return True

if __name__ == '__main__':
        db = connect_db()
        db = FDataBase(db)
        print(db.getMenu('Разработчик', 'about'))