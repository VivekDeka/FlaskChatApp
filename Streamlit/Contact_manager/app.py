import streamlit as st 
import sqlite3
import pandas as pd


#DB Initialization
DB_NAME = 'contact.db'


def init_db():
    # Connect to the SQLite database files. 
    conn = sqlite3.connect(DB_NAME)
    
    cursor = conn.cursor()
    
    # Execute an SQL command to create the contacts table if it does not already exist.
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT NOT NULL,                   
                    phone TEXT,                           
                    email TEXT  
                )                                          
        ''')
    
    #save the changes to DB
    conn.commit()
    
    #Close the db connection
    conn.close()
    
#Ensure the DB and table exist when the app starts

init_db()


# Set Streamlit page configuration
st.set_page_config(layout="centered", page_title="Simple Contact Manager")

#Display the main title of the Description
st.title("Simple Contact Manager")

#Function to add Contact
def add_contact(name, phone, email):
    conn = sqlite3.connect(DB_NAME)
    
    cursor = conn.cursor()
    
    #Insert new contact data
    cursor.execute("INSERT INTO contacts(name, phone, email) VALUES(?, ?, ?)", (name, phone, email))
    
    conn.commit()
    conn.close()
    
    st.success("Contact Added Successfully!")
    
    
# FUnction to View Contacts
def view_contact(search_term=""):
    conn = sqlite3.connect(DB_NAME)
    
    cursor = conn.cursor()
    
    if search_term:
        cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?",
                       ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))

    else:
        cursor.execute("SELECT * FROM contacts")
        
    contacts = cursor.fetchall()
    conn.close()
    return contacts
    
# Function to Update Contact
def update_contact(contact_id, name, phone, email):
    conn = sqlite3.connect(DB_NAME)
    
    cursor = conn.cursor()
    
    cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ? ", (name, phone, email, contact_id))
    
    conn.commit()
    conn.close()
    
    st.success(f"Contact ID {contact_id} Updated Successfully")
    
#Function to Delete contact
def delete_contact(contact_id):
    conn = sqlite3.connect(DB_NAME)
    
    cursor = conn.cursor()
    
    #Delete a contact based on its ID
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    
    conn.commit()
    conn.close()
    
    st.warning(f"Contact ID {contact_id} Deleted!")
    

#Add Contact Section
st.header("Add New Contact")

# Create a Streamlit form
with st.form("contact_form", clear_on_submit= True):
    new_name = st.text_input("Name: ")
    new_phone = st.text_input("Phone (Optional)")
    new_email = st.text_input("Email (Optionsl)")
    
    submitted = st.form_submit_button("Add Contacct")

if submitted:
    if new_name:
        add_contact(new_name, new_phone,new_email)
    
    else:
        st.error("Name cannot be empty")
        

#View Contacts System
st.header("View Contacts")

search_query = st.text_input("Search Contacts (Name, Phone, Email):")

all_contacts = view_contact(search_query)

if all_contacts:
     df= pd.DataFrame(all_contacts, columns=["ID", "name", "Phone", "Email"])
     
     st.dataframe(df, hide_index=True)
     
     # Manage Contacts Sections
     st.subheader("Manage Contacts")
     
     #Create two Columns to arrange edit and delete forms 
     col1, col2 = st.columns(2)
     
     with col1 :
         st.write("Edit Contacts")
         
         #get a list of just the IDs from all contactss for the selectbox
         
         contacts_id = [contact[0] for contact in all_contacts]
         
         #Dropdown to select which contact ID to edit
         edit_id = st.selectbox("Select Contact ID to Edit: ", contacts_id, key = "edit_select")
         
         #Find the full details of the selected contact to pre-fill the form
         selected_contact = next((c for c in all_contacts if c[0]== edit_id), None)
         
         if selected_contact:
            # selected_contact is a tuple: (id, name, phone, email)
            default_name = selected_contact[1]
            default_phone = selected_contact[2]
            default_email = selected_contact[3]
         else: # Fallback if no contact is selected (shouldn't happen with default)
            default_name = ""
            default_phone = ""
            default_email = ""
     
         with st.form("edit_form", clear_on_submit= False):
             edited_name = st.text_input("New Name:", value=default_name)
             edited_phone = st.text_input("New Phone (Optional):", value=default_phone)
             edited_email = st.text_input("New Email (Optional):", value=default_email)
             
             update_submitted = st.form_submit_button("Update Contact")
             
             if update_submitted:
                 if edited_name:
                    update_contact(edit_id, edited_name, edited_phone, edited_email)
                    st.rerun() # Re-run the app to refresh the displayed contacts table
                 else:
                    st.error("Name cannot be empty for update!")

    
     with col2:
        st.write("Delete Contact")
        
        #dropdown to select which contact ID to delete
        delete_id = st.selectbox("Select contact it to delete", contacts_id,key = "delete select" )
        
        #button to delete the selected contact:
        
        if st.button("Delete Contact", help = "Parmently delete the selected contact"):
        
            delete_contact(delete_id)
        
            st.rerun()
        else:
            st.info("No contact found")            

    

    
    