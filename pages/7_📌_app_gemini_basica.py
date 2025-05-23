import streamlit as st
from google import genai

# Configuración de la página
st.set_page_config(page_title="Chat Básico con Gemini", layout="centered")
col1, col2 = st.columns([3, 1])
with col1:
    st.title("📧Crea correos con Gemini")
    st.header("Escribe menos, comunica mejor")

with col2:
    st.image("assets/sobre.gif")


# Interfaz de usuario
prompt = st.text_area(
    "Ingresa el tema y los datos que quieras incluir. Nosotros redactamos tu correo por ti.",
    placeholder="Ej. Redacta un correo para mi empleado Juan Felipe Ortiz, aprobando su solicitud de vacaciones",
    height=120,
)

enviar = st.button("Generar Correo")


# Función que usa el código original
def generar_respuesta(prompt):
    if not prompt:
        return "Por favor, ingresa un tema para la redacción de tu correo."
    try:
        client = genai.Client(api_key="AIzaSyCKpWf_8l6SgKD2biCNH0G6CEiCysGCrTw")

        enfoque = "redacción de correos electrónicos"
        prompt_personalizado = (
            f"Eres un asistente experto en {enfoque}. "
            "A partir de la solicitud del usuario, redacta un correo completo que incluya:\n"
            "- Un asunto claro y apropiado.\n"
            "- Un mensaje estructurado con saludo, cuerpo y despedida.\n"
            "- Si se detectan nombres o datos personales, añade una despedida formal como 'Atentamente, [nombre]'.\n\n"
            f"Solicitud del usuario: {prompt}"
        )

        # Código original
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt_personalizado,  # Código original con prompt dinámico
        )
        return response.text  # Código original
    except Exception as e:
        return f"Error: {str(e)}"


# Lógica principal
if enviar and prompt:
    with st.spinner("Generando correo..."):
        respuesta = generar_respuesta(prompt)
        st.subheader("Correo:")
        st.markdown(respuesta)

    if st.button("🔄 Crear correo nuevo"):
        st.experimental_rerun()

else:
    st.info("Escribe un tema o palabras clave para redactar tu correo.")
