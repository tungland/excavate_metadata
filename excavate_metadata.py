import sqlite3 as sql
import pandas as pd



def get_like(word, con) :
    
    # Søk etter ord i tittelfeltet
    # Uttrykk som inneholder "nou" og "/" sammen i "subjects" blir ekskludert
    query = f"""
            SELECT * 
            FROM metadata_core
            WHERE title like "%{word}%" AND NOT (subjects like "%nou /%" OR subjects like "%/ nou") 
        

            """
    df = pd.read_sql(query, con)
    df.to_csv(f"{word.lower().replace(' ', '_')}.csv")
    


if __name__ == "__main__":
    
    con = sql.connect("/mnt/disk1/metadata/metadata.db")

    # uttrykk å søke etter
    terms = [
       "evaluering av",
        "evaluering",
        "utredning av",
        "utredning"
    ]

    for term in terms:
        get_like(term, con)
