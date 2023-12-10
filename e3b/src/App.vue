<template>
  <div>
    <header>
        <h1>Outfit Showroom</h1>
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
  export default {
    data() {
      return {
        contacts: [
          {nombre: 'Iñigo', apellido: 'Fernández', telefono: '684983765', email: 'inigofernandez@opendeusto.es'},
          {nombre: 'Unai', apellido: 'Igartua', telefono: '675903210', email: 'unaiigartua@opendeusto.es'},
          {nombre: 'Nicolás', apellido: 'Llop', telefono: '619861263', email: 'nicllop@opendeusto.es'},
          {nombre: 'Jorge', apellido: 'Alcorta', telefono: '621203775', email: 'jorgealcorta@opendeusto.es'}
        ],
        contactsOnEdit: [
          {nombre: 'Iñigo', apellido: 'Fernández', telefono: '684983765', email: 'inigofernandez@opendeusto.es'},
          {nombre: 'Unai', apellido: 'Igartua', telefono: '675903210', email: 'unaiigartua@opendeusto.es'},
          {nombre: 'Nicolás', apellido: 'Llop', telefono: '619861263', email: 'nicllop@opendeusto.es'},
          {nombre: 'Jorge', apellido: 'Alcorta', telefono: '621203775', email: 'jorgealcorta@opendeusto.es'}
        ],
        editing: false,
        newContact: {
          nombre: '',
          apellido: '',
          telefono: '',
          email: ''
        }
      };
    },
    methods: {
    
      addContact() {
        if (this.newContact.nombre && this.newContact.apellido && this.newContact.telefono && this.newContact.email) {
          // All fields are filled, add the contact
          this.contactsOnEdit.push(Object.assign({}, this.newContact));
          this.newContact = { nombre: '', apellido: '', telefono: '', email: '' }; // Reset the new contact
        } else {
          // Not all fields are filled, show an error message or alert
          alert("Please fill in all fields.");
        }
      },

      saveChanges() {
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
  
  /*-------------------- HEADER CONTENT --------------------*/
  
  header {
    background-color: var(--secondary-color);
    border-radius: 10px;
    padding: 20px;
    margin: 20px 20px 20px 20px;
  }
  
  header ul {
    margin: 0;
    padding: 0;
    list-style: none;
    margin-top: 10px;
    margin-bottom: 10px;
  }
  
  header li {
    margin: 0;
    padding: 0;
    display: inline;
    margin-right: 20px;
  }
  
  header h1 {
    margin: 0;
    padding: 0;
  }
  
  nav a {
    text-decoration: none;
    padding: 12px;
    border-radius: 20px;
    background-color: var(--secondary-off-color);
    color: var(--accent-color); /* Color del texto, ajusta según sea necesario */
  }
  
  .language-selector {
    position: absolute;
    top: 20px;
    right: 20px;
  }
  
  .language-selector form {
    margin: 0;
  }
  
  
  .language-selector select:focus {
    outline: none;
    border-color: var(--accent-color);
  }
  
  .language-selector img {
    height: 20px;
    width: auto;
    vertical-align: middle;
    margin-right: 5px;
  }
  
  /*-------------------- MAIN CONTENT --------------------*/
  
  main {
    background-color: var(--secondary-color);
    padding: 20px;
    margin: 20px;
    border-radius: 5px;
  }
  
  /* homepage content */
  
  .imagen-outfit {
    width: 700px  !important;
    height: auto;
  }
  
  .initial_title{
    font-size: 50px;
    text-align: center;
  }
  
  .first_display{
    padding: 0;
    margin: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-style: italic;
    font-size: 20px;
  }
  
  .first_display table {
    height: 100%;
    width: 100%;
    border-collapse: collapse;
  }
  
  .first_display tr {
    width: 100%;
    height: 100%;
    text-align: center;
  }
  
  .first_display td {
    padding-bottom: 50px;
  }
  
  .first_display table img{
    width: 70vw;
    min-width: 400px;
    height: auto;
  }
  
  /* outfits content */
  
  .table_container table {
    width: 80%;
    margin: auto;
    border-collapse: collapse;
  }
  
  .table_container th, .table_container td {
    padding: 10px;
    text-align: center;
  }
  
  .table_container th {
    border-bottom: 3px solid var(--border-color);
  }
  
  .table_container tr:nth-child(even) {
    background-color: var(--secondary-off-color);
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