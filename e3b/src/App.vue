<template>
  <div>
    <header>
        <h1>Agenda de contactos</h1>
    </header>
    <main>
      <table class="contact-table">
        <thead>
          <tr>
            <th v-if="editing"></th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Teléfono</th>
            <th>Correo electrónico</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(contact, index) in currentContacts" :key="contact.id">
            <td v-if="editing" class="delete-button-cell">
              <button class="delete-button" @click="deleteContact(index)">Borrar</button>
            </td>
            <td>{{ contact.nombre }}</td>
            <td>{{ contact.apellido }}</td>
            <td>{{ contact.telefono }}</td>
            <td>{{ contact.email }}</td>
          </tr>
          <tr v-if="editing">
            <td></td>
            <td><input type="text" v-model="newContact.nombre" @keyup.enter="addContact"/></td>
            <td><input type="text" v-model="newContact.apellido" @keyup.enter="addContact"/></td>
            <td><input type="tel" v-model="newContact.telefono" @keyup.enter="addContact"/></td>
            <td><input type="email" v-model="newContact.email" @keyup.enter="addContact"/></td>
          </tr>
        </tbody>
      </table>
      <div class="contact-buttons">
        <div v-if="editing">
          <button @click="addContact">Añadir contacto</button>
          <button @click="saveChanges">Guardar cambios</button>
          <button @click="cancelChanges">Cancelar</button>
        </div>
        <div v-else>
          <button @click="toggleEditingMode">Modificar contactos</button>
        </div>
      </div>
    </main>
    <footer>
      <div class="footer_authors">
        <ul>
          <li><a href="https://www.linkedin.com/in/unaiigartua/" target="_blank">Unai Igartua</a></li>
          <li><a href="https://www.linkedin.com/in/jorge-alcorta-berasategui/" target="_blank">Jorge Alcorta</a></li>
          <li><a href="https://www.linkedin.com/in/nicol%C3%A1s-llop-030978223/" target="_blank">Nicolás Llop</a></li>
          <li><a href="https://www.linkedin.com/in/i%C3%B1igo-fern%C3%A1ndez-sope%C3%B1a-090564194/" target="_blank">Iñigo Fernández-Sopeña</a></li>
        </ul>
      </div>
      <div class="footer_links">
        <ul>
          <li><a target="_blank" href="https://github.com/INIGO-7/IWebOutfitShowroom">GitHub</a></li>
          <li><a target="_blank" href="https://www.deusto.es/">Deusto</a></li>
        </ul>
      </div>
    </footer>
  </div>
</template>

<script>

  import { addDoc, deleteDoc, doc, getDocs} from 'firebase/firestore';
  import { contactos_db } from './firebase';

  // Function to find the difference between two arrays of contacts
  function findContactsDifferences(original, edited) {
    const toAdd = edited.filter(editedContact => 
      !original.some(originalContact => 
        originalContact.nombre === editedContact.nombre &&
        originalContact.apellido === editedContact.apellido &&
        originalContact.telefono === editedContact.telefono &&
        originalContact.email === editedContact.email
      )
    );

    const toDelete = original.filter(originalContact => 
      !edited.some(editedContact => 
        originalContact.nombre === editedContact.nombre &&
        originalContact.apellido === editedContact.apellido &&
        originalContact.telefono === editedContact.telefono &&
        originalContact.email === editedContact.email
      )
    );

    return { toAdd, toDelete };
  }
 
  export default {
    data() {
      return {
        contacts: [],
        contactsOnEdit: [],
        editing: false,
        newContact: {
          nombre: "",
          apellido: "",
          telefono: "",
          email: ""
        }
      };
    },

    async mounted() {
      try {
        const querySnapshot = await getDocs(contactos_db);
        this.contacts = querySnapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }));

        // deep copy the contacts to OnEdit variable
        this.contactsOnEdit = JSON.parse(JSON.stringify(this.contacts));

      } catch (error) {
        console.error("Error fetching documents: ", error);
      }
    },

    methods: {
    
      addContact() {
        if (this.newContact.nombre && this.newContact.apellido && this.newContact.telefono && this.newContact.email) {
          
          this.contactsOnEdit.push(Object.assign({}, this.newContact));
          this.newContact = { nombre: "", apellido: "", telefono: "", email: "" }; // Reset the new contact

        } else {
          alert("Please fill in all fields.");
        }
      },

      async saveChanges() {
        const { toAdd, toDelete } = findContactsDifferences(this.contacts, this.contactsOnEdit);
        
        // Add new contacts to Firestore
        try {
          for (const contact of toAdd) {
            await addDoc(contactos_db, contact); // Assumes contactos_db is a reference to your collection
          }
        } catch (error) {
          console.error("Error adding documents: ", error);
        }

        // Delete contacts from Firestore
        try {
          for (const contact of toDelete) {
            if (contact.id) {
              const docRef = doc(contactos_db, contact.id);
              await deleteDoc(docRef);
            }
          }
        } catch (error) {
          console.error("Error deleting documents: ", error);
        }
        
        this.contacts = JSON.parse(JSON.stringify(this.contactsOnEdit)); // Overwrite existing contacts with the new edited ones
        this.toggleEditingMode();
      },

      cancelChanges() {
        this.contactsOnEdit = JSON.parse(JSON.stringify(this.contacts)); // Overwrite edited contacts with the previous ones
        this.toggleEditingMode();
      },

      deleteContact(index) {
        this.contactsOnEdit.splice(index, 1); // Remove the contact at the specified index
      },

      toggleEditingMode() {
        this.newContact = { nombre: '', apellido: '', telefono: '', email: '' }; // Reset the new contact
        this.editing = !this.editing;
      }
    },

    computed: {
      currentContacts() {
          return this.editing ? this.contactsOnEdit : this.contacts;
      }
    }
  }
</script>

<style>
    
:root{
    margin: 0;
    padding: 0;
    --primary-color: #f9f6f8;
    --secondary-color: #CCCCCC;
    --secondary-off-color: #DDDDDD;
    --accent-color: #7c766d;
    --text-color: #637388;
    --border-color: #333;
  }
  
  body {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
    background-color: var(--primary-color);
    color: var(--text-color);
  }
  
  a {
    color: var(--text-color);
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  h1 {
    font-size: 70px;
    color: var(--accent-color);
  }
  h2 {
    font-size: 32px;
    color: var(--accent-color);
  }

button {
  background-color: var(--secondary-off-color);
  color: var(--text-color);
  font-size: 16px;
  margin: 4px 2px;
  padding: 15px 32px;
  border: none;
  text-align: center;
  text-decoration: none;
  transition: background-color 0.3s, color 0.1s, box-shadow 0.3s;
  cursor: pointer;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}

button:hover {
  background-color: var(--text-color);
  color: var(--secondary-off-color);
  box-shadow: 0 6px 12px rgba(0,0,0,0.4);
}
  
  /*-------------------- HEADER CONTENT --------------------*/
  
  header {
    background-color: var(--secondary-color);
    border-radius: 10px;
    padding: 20px;
    margin: 20px;
  }
  
  header h1 {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
  }
  
  /*-------------------- MAIN CONTENT --------------------*/
  
  main {
    background-color: var(--secondary-color);
    padding: 20px;
    margin: 20px;
    border-radius: 5px;
  }
  
  /* contacts SPA content */
  
  .contact-table {
    width: 80%;
    margin: 20px auto;
    border-collapse: collapse;
    font-size: 1.2em;
    position: relative;
  }
  
  .contact-table th {
    background-color: var(--secondary-off-color);
  }
  
  .contact-table th, .contact-table td {
    border: 2px solid var(--secondary-off-color);
    padding: 10px;
    text-align: center;
  }
  
  .contact-buttons {
    text-align: center;
    margin-top: 20px;
  }
  
  .contact-buttons button {
    margin: 5px;
  }
  
  /*-------------------- FOOTER CONTENT --------------------*/
  
  footer {
    background-color: var(--border-color);
    padding: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: fixed;
    bottom: 0;
    width: 100%;
  }
  
  footer ul{
    list-style: none;
    padding-left: 10px;
  }
  
  footer li {
    padding: 10px 10px 10px 0;
    margin-right: 20px;
    display: inline;
    color: var(--secondary-off-color);
  }
  
  footer a{
    color: var(--secondary-off-color);
  }
</style>