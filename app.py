import streamlit as st
import snowflake.connector as sc
import pandas as pd

def main():
    st.write("### Dashbord d'affichage des donnees de la table etudiants")
    
    # objet de connection
    try:
        
        con  = sc.connect(
            account ='znejkha-ui11118',
             user = 'Kadi',
            password = 'OUktra20022023'
        )
        cursor = con.cursor()
        
        def dataEtudiants():
            sql = 'SELECT * FROM rcw.persons.etudiants'
            df = cursor.execute(sql).fetchall()
            
            return pd.DataFrame(df, columns  = ['NOM', 'PRENOM', 'AGE'])
        donnees = dataEtudiants()
        st.write(donnees)
        
        
    except:
        st.warning("Une erreur c'est produit")
    
    







if __name__ == '__main__':
    main()