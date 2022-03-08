import sqlite3 as sql
import pandas as pd



def get_like(word, con, exclude_nou = False) :
    
    # Søk etter ord i tittelfeltet
    # Uttrykk som inneholder "nou" og "/" sammen i "subjects" blir ekskludert
    query = f"""
    SELECT *
    FROM   metadata_core
    WHERE  title LIKE "%{word}%"
        AND year >= 1960
        AND year <= 2021
        AND doctype LIKE "digibok"

            """

    exclude_nou = """
        AND NOT ( subjects LIKE "%nou /%"
                    OR subjects LIKE "%/ nou" ) 
    """

    if exclude_nou:
        query = query + exclude_nou

    df = pd.read_sql(query, con)
    df.to_excel(f"{word.lower().replace(' ', '_')}.xlsx", sheet_name='Sheet_1')
    #df.to_csv(f"{word.lower().replace(' ', '_')}.xlsx")
    


if __name__ == "__main__":
    # SQLITE connection
    con = sql.connect("/mnt/disk1/metadata/metadata.db")

    # uttrykk å søke etter
    terms = [
       "evaluering av",
        "evaluering",
  
    ]
    # Uttrykk der man vil ekskludere NOUer
    terms_exclude_nou = [
        "utredning av",
        "utredning"
    ]

    for term in terms:
        get_like(term, con)
    
    for term in terms_exclude_nou:
        get_like(term, con, exclude_nou=True)
