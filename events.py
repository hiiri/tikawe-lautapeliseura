import db

def get_events():
    sql = """SELECT e.id, e.title, COUNT(e.id) total, MAX(e.date) newest
             FROM events e
             GROUP BY e.id
             ORDER BY e.id DESC"""
    return db.query(sql)