//import firebase from "firebase/app";
import { initializeApp } from "firebase/app";
import { getFirestore, collection} from "firebase/firestore";


export const firebaseApp = initializeApp({
  apiKey: "AIzaSyAXqpyCZ_VVFWzbYtjgZzvG_GgiDVjcLec",
  authDomain: "iweb-e3b.firebaseapp.com",
  projectId: "iweb-e3b",
  storageBucket: "iweb-e3b.appspot.com",
  messagingSenderId: "817634488968",
  appId: "1:817634488968:web:f20aee7d5dbfd6a5ef653d",
  measurementId: "G-CH9M6Y016T"
})

// used for the firestore refs
export const db = getFirestore(firebaseApp)

// here we can export reusable database references
export const contactos_db = collection(db, 'contactos')