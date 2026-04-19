import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="EcoSmart AI", page_icon="🌱")

st.title("🌱 EcoSmart AI")
st.write("Describe cualquier situación ecológica y recibirás una solución personalizada.")

texto = st.text_area("📝 Escribe tu situación:")

if st.button("🔍 Analizar"):
    if texto.strip() == "":
        st.warning("Escribe algo primero.")
    else:
        respuesta = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "Eres EcoSmart AI, experto en ecología. Das consejos prácticos, claros y personalizados."
                },
                {
                    "role": "user",
                    "content": texto
                }
            ]
        )

        st.success(respuesta.choices[0].message.content)