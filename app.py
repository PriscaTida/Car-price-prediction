import numpy as np
import pickle
import pandas as pd
import streamlit as st 



gb_model = pickle.load(open('price_predicting_model.pkl', 'rb'))

def convert_var(carburant, vitesse, etat, origine):
    Carburant_Diesel = 0
    Carburant_Essence = 0
    Carburant_Hybride = 0
    Vitesse_Boite_Automatique = 0
    Vitesse_Boite_Manuelle = 0
    Etat_Neuf = 0
    Etat_Excellent = 0
    Etat_Très_bon = 0
    Etat_Bon = 0
    Etat_Correct = 0
    Etat_Endommagé = 0
    Etat_Pour_pièces = 0
    Origine_Importée_neuve = 0
    Origine_WW_au_Maroc = 0
    Origine_Dédouanée = 0
    Origine_Pas_encore_Dédouanée = 0
    

    if carburant == 'Diesel':
        Carburant_Diesel = 1
    elif carburant == 'Essence':
        Carburant_Essence = 1
    elif carburant == 'Hybride':
        Carburant_Hybride = 1
        
    if vitesse == 'Automatique':
        Vitesse_Boite_Automatique =1
    elif vitesse == 'Manuelle':
        Vitesse_Boite_Manuelle =1
        
    if etat == 'Bon':
        Etat_Bon = 1
    elif etat == 'Correct':
        Etat_Correct = 1
    elif etat == 'Endommagé':
        Etat_Endommagé = 1
    elif etat == 'Excellent':
        Etat_Excellent = 1
    elif etat == 'Neuf':
        Etat_Neuf = 1
    elif etat == 'Pour_pièces':
        Etat_Pour_pièces = 1
    elif etat == 'Très_bon':
        Etat_Très_bon = 1

    if origine == 'Dédouanée':
        Origine_Dédouanée = 1
    elif origine == 'WW_au_Maroc':
        Origine_WW_au_Maroc = 1
    elif origine == 'Importée_neuve':
        Origine_Importée_neuve = 1
    elif origine == 'Pas_encore_Dédouanée':
        Origine_Pas_encore_Dédouanée = 1

    return (Carburant_Diesel, Carburant_Essence, Carburant_Hybride, 
            Vitesse_Boite_Automatique, Vitesse_Boite_Manuelle, 
            Etat_Bon, Etat_Correct, Etat_Endommagé, Etat_Excellent, Etat_Neuf, Etat_Pour_pièces, Etat_Très_bon, 
            Origine_Dédouanée, Origine_Importée_neuve, Origine_Pas_encore_Dédouanée, Origine_WW_au_Maroc)

def convert_km(kilometrage):
    km_A = 0
    km_B = 0
    km_C = 0
    km_D = 0
 
    
    if kilometrage in ['0 - 4 999', '5 000 - 9 999', '10 000 - 14 999', '15 000 - 19 999', '20 000 - 24 999', '25 000 - 29 999', '30 000 - 34 999', '35 000 - 39 999', '40 000 - 44 999', '45 000 - 49 999', '50 000 - 54 999', '55 000 - 59 999', '60 000 - 64 999', '65 000 - 69 999', '70 000 - 74 999', '75 000 - 79 999', '80 000 - 84 999', '85 000 - 89 999', '90 000 - 94 999', '95 000 - 99 999']:
        km_A = 1
    elif kilometrage in ['100 000 - 109 999', '110 000 - 119 999', '120 000 - 129 999', '130 000 - 139 999', '140 000 - 149 999', '150 000 - 159 999', '160 000 - 169 999', '170 000 - 179 999', '180 000 - 189 999', '190 000 - 199 999']:
        km_B = 1
    elif kilometrage in ['200 000 - 249 999', '250 000 - 299 999', '300 000 - 349 999', '350 000 - 399 999', '400 000 - 449 999', '450 000 - 499 999']:
        km_C = 1
    else:
        km_D = 1
        
    return(km_A,km_B,km_C,km_D)

def main():
    html_temp = """
    <div style = "background color:#5F4B8BFF; padding:10px">
    <h1 style="color:#E69A8DFF; text-align:center;">Car Price Prediction</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    name = st.text_input("Modele de la voiture", "Type Here")
    puissance = st.number_input("Quelle est la puissance en CV?")
    kilometrage = st.selectbox("Kilométrage",('0 - 4 999', '5 000 - 9 999', '10 000 - 14 999', '15 000 - 19 999', '20 000 - 24 999', '25 000 - 29 999', '30 000 - 34 999', '35 000 - 39 999', '40 000 - 44 999', '45 000 - 49 999', '50 000 - 54 999', '55 000 - 59 999', '60 000 - 64 999', '65 000 - 69 999', '70 000 - 74 999', '75 000 - 79 999', '80 000 - 84 999', '85 000 - 89 999', '90 000 - 94 999', '95 000 - 99 999',
                                              '100 000 - 109 999', '110 000 - 119 999', '120 000 - 129 999', '130 000 - 139 999', '140 000 - 149 999', '150 000 - 159 999', '160 000 - 169 999', '170 000 - 179 999', '180 000 - 189 999', '190 000 - 199 999', 
                                              '200 000 - 249 999', '250 000 - 299 999', '300 000 - 349 999', '350 000 - 399 999', '400 000 - 449 999', '450 000 - 499 999', 'Plus de 500 000'))
    year = st.slider("Selectionner l'année-modele", 1980, 2022)
    carburant = st.selectbox("Quel est le type de carburant?", ('Diesel', 'Essence', 'Hybride'))
    vitesse = st.radio("Quel est le type de la boite de vitesse?", ('Manuelle', 'Automatique'))
    etat = st.selectbox("Quel est l'etat de la voiture?", ('Neuf', 'Excellent', 'Très_bon', 'Bon', 'Correct','Endommagé','Pour_pièces'))                                
    origine = st.selectbox("Quelle est l'origine de la voiture?",('Importée_neuve', 'WW_au_Maroc', 'Dédouanée', 'Pas_encore_Dédouanée'))


    
    Carburant_Diesel, Carburant_Essence, Carburant_Hybride,\
    Vitesse_Boite_Automatique, Vitesse_Boite_Manuelle, \
    Etat_Très_bon, Etat_Correct, Etat_Endommagé, Etat_Neuf, Etat_Excellent, Etat_Bon, Etat_Pour_pièces,\
    Origine_Dédouanée, Origine_Importée_neuve, Origine_Pas_encore_Dédouanée, Origine_WW_au_Maroc = convert_var(carburant, vitesse, etat, origine)
    
    
    km_A,km_B,km_C,km_D = convert_km(kilometrage)
    
    
    inputs = [[puissance,year,Carburant_Diesel, Carburant_Essence, Carburant_Hybride,
               Vitesse_Boite_Automatique, Vitesse_Boite_Manuelle, 
               Etat_Très_bon, Etat_Correct, Etat_Endommagé, Etat_Neuf, Etat_Excellent, Etat_Bon, Etat_Pour_pièces,
               Origine_Dédouanée, Origine_Importée_neuve, Origine_Pas_encore_Dédouanée, Origine_WW_au_Maroc,
               km_A,km_B,km_C,km_D]]


    st.subheader("Price")
   
    
    if st.button('Calculate'):
        st.write("**Predicted Price (in DHS) is**")
        st.success("{:.2f}".format(gb_model.predict(inputs)[0]))
    else:
       pass
   


if __name__=='__main__':
    main()