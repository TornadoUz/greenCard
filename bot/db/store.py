from sqlalchemy import create_engine
from datetime import datetime

import config as c
import db.queries as q


engine = create_engine(
    f'postgresql+psycopg2://{c.DB_USERNAME}:{c.DB_PASSWORD}@{c.DB_HOST}:{c.DB_PORT}/{c.DB_NAME}', 
    echo=True
)

# Check db connection
conn = engine.connect()
conn.close()

def get_or_create_user(full_name, telegram_id):
    params = {
        "full_name": full_name,
        "telegram_id": telegram_id,
        "added_at": datetime.now(),
        "updated_at": datetime.now()
    }
    with engine.connect() as conn:
        conn.execute(q.get_or_create_user_query, params)
        conn.commit()
