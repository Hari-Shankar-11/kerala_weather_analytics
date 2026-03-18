import sqlite3
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_to_db(df, db_path="kerala_weather.db"):
    conn = sqlite3.connect(db_path)

    df.to_sql("forecast", conn, if_exists="replace", index=False)

    count = pd.read_sql("SELECT COUNT(*) as total FROM forecast", conn)
    logger.info(f"Loaded {count['total'][0]} records into database")

    conn.close()
