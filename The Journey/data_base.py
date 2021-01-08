import sqlite3
import sys

show = "data_base.py"


def save_to_db(player_id, score):
    conn = sqlite3.connect("db_test.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS ALL_SCORES
                                (Score integer, 
                                Pseudo varchar(100))""")

    sql = "INSERT INTO ALL_SCORES (Score, Pseudo) VALUES (:score,:id)"
    c.execute(sql, {'score': score, 'id': player_id})
    conn.commit()

    sql = "SELECT * FROM ALL_SCORES"
    c.execute(sql)

    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()


def show_score(player_id):
    conn = sqlite3.connect("db_test.db")
    c = conn.cursor()
    if player_id == "all":
        sql_best = "SELECT Pseudo, Score FROM ALL_SCORES order by Pseudo"
    else:
        sql_best = "SELECT Pseudo, Score FROM ALL_SCORES WHERE Pseudo = '" + player_id + "' order by Pseudo"
    c.execute(sql_best)
    rows = c.fetchall()
    for row in rows:
        print(row)


if len(sys.argv) == 1:
    print("Enter command 'python data_base.py help' for more help")
elif sys.argv[0] == "data_base.py" and (sys.argv[1] == "?" or sys.argv[1] == "help"):
    print("for a list of command enter 'command'")
elif sys.argv[1] == "command":
    print("For best score enter: best  player_name\n"
          "For all score enter: show_all")
elif sys.argv[1] == "show_all":
    show_score("all")
elif sys.argv[1] == "best":
    show_score(sys.argv[2])
