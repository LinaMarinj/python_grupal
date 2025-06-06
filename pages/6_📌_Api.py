import requests
import pandas as pd
import streamlit as st
import json
import os

import plotly.express as px



API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8081/api")
AUTH_EMAIL = os.getenv("AUTH_EMAIL", "mariagomez@gmail.com")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", "maria123")

st.set_page_config(layout="wide")

# --- Clase Cliente API ---
class QuickWashAPIClient:
    def __init__(self, base_url, email, password):
        self.base_url = base_url
        self.email = email
        self.password = password
        self.access_token = None

    def _login(self):
        """
        Intenta autenticar con la API y almacena el token de acceso.
        Muestra mensajes de error en Streamlit si falla.
        """
        url = f"{self.base_url}/auth/login"
        payload = json.dumps({"email": self.email, "password": self.password})
        headers = {"Content-Type": "application/json", "Accept": "*/*"}
        
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()  
            data = response.json()
            self.access_token = data.get("accessToken")
            if not self.access_token:
                st.error("Error de autenticación: No se recibió un token de acceso válido.")
            return self.access_token
        except requests.exceptions.HTTPError as http_err:
            st.error(f"Error HTTP de autenticación: {http_err}. Verifica las credenciales o la URL del servidor.")
        except requests.exceptions.ConnectionError as conn_err:
            st.error(f"Error de conexión: No se pudo conectar al servidor de autenticación en **{url}**. Asegúrate de que la API esté corriendo.")
        except requests.exceptions.Timeout as timeout_err:
            st.error(f"Error de tiempo de espera: La solicitud de autenticación excedió el límite de tiempo.")
        except requests.exceptions.RequestException as req_err:
            st.error(f"Error en la solicitud de autenticación: {req_err}.")
        except ValueError as json_err:
            st.error(f"Error al procesar la respuesta JSON de autenticación: {json_err}.")
        self.access_token = None
        return None

    @st.cache_data(ttl=3600)  
    def get_registers(self):
        """
        Obtiene los datos de registro de la API, los procesa para aplanar estructuras
        y los devuelve como un DataFrame de Pandas.
        """
        if not self.access_token:
            self._login()
        
        if not self.access_token:
            return None

        url = f"{self.base_url}/registers"
        headers = {
            "Accept": "*/*",
            "Authorization": "Bearer " + str(self.access_token),
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            processed_data = []
            for item in data:
                processed_item = item.copy()

                processed_item.pop("user", None)

                if "services" in processed_item and isinstance(processed_item["services"], list):
                    processed_item["services"] = ", ".join(serv.get("name", "") for serv in processed_item["services"])
                else:
                    processed_item["services"] = ""

                if "vehicle" in processed_item and isinstance(processed_item["vehicle"], dict):
                    vehicle = processed_item.pop("vehicle")
                    vehicle.pop("id", None) 

                    processed_item["typeVehicle_name"] = vehicle.get("typeVehicle", {}).get("name", "")
                    processed_item["brand_name"] = vehicle.get("brand", {}).get("name", "")
                    processed_item["plate"] = vehicle.get("plate", "")
                    processed_item["model"] = vehicle.get("model", "")
                    processed_item["color"] = vehicle.get("color", "")
                
              
                if "createdAt" not in processed_item: 
                    processed_item["createdAt"] = "2025-05-15T10:30:00-05:00" 
                

                processed_data.append(processed_item)

            df = pd.DataFrame(processed_data)
            
            
            if 'createdAt' in df.columns:
                df['createdAt'] = pd.to_datetime(df['createdAt'], errors='coerce') 
                df = df.dropna(subset=['createdAt']) 
                
                df['Mes'] = df['createdAt'].dt.strftime('%Y-%m') 
            else:
                st.warning("La columna 'createdAt' no se encontró. No se podrá generar el gráfico de visitas por mes.")

            return df
        except requests.exceptions.HTTPError as http_err:
            st.error(f"Error HTTP al obtener datos: {http_err}. Podría ser un problema con los permisos o la URL.")
        except requests.exceptions.ConnectionError as conn_err:
            st.error(f"Error de conexión: No se pudo conectar a la API de registros en **{url}**. Asegúrate de que la API esté corriendo.")
        except requests.exceptions.Timeout as timeout_err:
            st.error(f"Error de tiempo de espera: La solicitud de datos excedió el límite de tiempo.")
        except requests.exceptions.RequestException as req_err:
            st.error(f"Error en la solicitud de datos: {req_err}.")