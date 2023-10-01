import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)


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


