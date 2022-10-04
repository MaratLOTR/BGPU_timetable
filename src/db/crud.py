

def insert_database(session, data: list):
    session.add_all(data)
    session.commit()
