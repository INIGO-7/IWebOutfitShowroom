// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app"
import { getFirestore } from "firebase/firestore"

const firebaseConfig = {
  apiKey: "AIzaSyAXqpyCZ_VVFWzbYtjgZzvG_GgiDVjcLec",
  authDomain: "iweb-e3b.firebaseapp.com",
  projectId: "iweb-e3b",
  storageBucket: "iweb-e3b.appspot.com",
  messagingSenderId: "817634488968",
  appId: "1:817634488968:web:f20aee7d5dbfd6a5ef653d",
  measurementId: "G-CH9M6Y016T"
}

// Initialize Firebase
const app = initializeApp(firebaseConfig)

// Initialize Firestore
const db = app.getFirestore()
export default db