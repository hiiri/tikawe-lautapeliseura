import db

def get_events():
    sql = """SELECT e.id, e.title, COUNT(e.id) total, MAX(e.date) newest
             FROM events e
             GROUP BY e.id
             ORDER BY e.id DESC"""
    return db.query(sql)

def add_event(title, date, num_players, user_id):
    sql = "INSERT INTO events (title, date, num_players, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, date, num_players, user_id])
    event_id = db.last_insert_id()
    return event_id