import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)


def load_job_from_db(id_val):
    with engine.connect() as conn:
        query = (f"SELECT * " 
                 f"FROM jobs "
                 f"WHERE id = {id_val}")
        result = conn.execute(text(query))
        row = result.all()
        if len(row) == 0:
            return {}
        elem = row[0]
        result_dict = {
            'id': elem[0],
            'title': elem[1],
            'location': elem[2],
            'salary': elem[3],
            'currency': elem[4],
            'responsibilities': elem[5],
            'requirements': elem[6]
        }
        return result_dict


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        result_dict = []
        for elem in result:
            result_dict.append({
                'id': elem[0],
                'title': elem[1],
                'location': elem[2],
                'salary': elem[3],
                'currency': elem[4],
                'responsibilities': elem[5],
                'requirements': elem[6]
            })

        return result_dict


