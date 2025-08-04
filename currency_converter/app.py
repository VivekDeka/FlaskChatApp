import streamlit as st
import requests



st.set_page_config(page_title= "Currency Converter", page_icon= "" )

st.title(" Real Time Currency Converter")

st.markdown("""
            
            <style>
                .stApp {
                    background-color: #CCCCFF;
                    color : #17202A;
                }
                
                .stSelectBox, .stTextInput, .stButton, .stNumberInput {
                    background-color : #CCCCFF;
                }
            </style>
            
            """, unsafe_allow_html= True)


# Currency list (Simplified for First Project )

currencies = [ 'USD', 'EUR', 'INR', 'JPY', 'GBP', 'AUD', 'CAD' ]

amount = st.number_input("Enter amount: ", min_value=0.0, value= 1.0, step= 0.5)

from_currency = st.selectbox("From: ", currencies)
to_currency = st.selectbox("To:", currencies)

# Define function to Convert
def convert_currency(from_curr, to_curr, amt):
    url = f"https://open.er-api.com/v6/latest/{from_curr}"
    
    renponse = requests.get(url)
    
    data = renponse.json()
    if data.get("result") == "success":
        rate = data['rates'].get(to_curr)
        
        if rate:
            return round(rate * amt , 4)
    
    return None


if st.button("Convert"):
    with st.spinner(" Fetching exchange rate..."):
        result = convert_currency(from_currency, to_currency, amount)
        
        if result is not None:
            st.success(f"{amount} {from_currency} = {result} {to_currency}")
        else :
            st.error("Conversion failed. Try again.")
            

st.markdown("---")
st.markdown("Exchange rates powered by [open.er-api.com](https://www.exchangerate-api.com)")    
        

