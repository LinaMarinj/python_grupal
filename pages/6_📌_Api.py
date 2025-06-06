import requests
import pandas as pd
import streamlit as st
import json


def login():
    try:
        url = "http://localhost:8081/api/auth/login"
        payload = json.dumps({"email": "mariagomez@gmail.com", "password": "maria123"})
        headers = {"Content-Type": "application/json", "Accept": "*/*"}
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("accessToken")
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Error de timeout: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
    except ValueError as json_err:
        print(f"Error al procesar JSON: {json_err}")
    return None


def obtener_datos_api():
    """
    Realiza una solicitud GET a la API y retorna los datos como DataFrame.
    """
    try:
        url = "http://localhost:8081/api/registers"
        payload = {}
        token = login()
        headers = {
            "Accept": "*/*",
            "Authorization": "Bearer " + str(token),
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        data = response.json()

        # Eliminar el campo 'password' de cada usuario
        for item in data:
            if "user" in item:
                del item["user"]
            # Convertir la lista de servicios a una cadena de nombres
            if "services" in item and isinstance(item["services"], list):
                item["services"] = ", ".join(serv["name"] for serv in item["services"])
            # Aplanar el diccionario vehicle y eliminar sus 'id'
            if "vehicle" in item and isinstance(item["vehicle"], dict):
                vehicle = item.pop("vehicle")
                # Eliminar los id de vehicle y subdiccionarios
                vehicle.pop("id", None)
                if "typeVehicle" in vehicle and isinstance(vehicle["typeVehicle"], dict):
                    vehicle["typeVehicle"] = vehicle["typeVehicle"].get("name", "")
                if "brand" in vehicle and isinstance(vehicle["brand"], dict):
                    vehicle["brand"] = vehicle["brand"].get("name", "")
                # Agregar cada campo de vehicle como columna
                for k, v in vehicle.items():
                    item[k] = v

        df = pd.DataFrame(data)
        return df
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Error de timeout: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
    except ValueError as json_err:
        print(f"Error al procesar JSON: {json_err}")
    return None

st.title("Consumo de API y visualizaciones")
st.subheader("API Registro de visitas Autolavado Quick Wash")

def guardar_csv(df, ruta_csv):
    """
    Guarda el DataFrame como un archivo CSV.
    """
    try:
        df.to_csv(ruta_csv, index=False)
        print(f"Datos guardados en '{ruta_csv}'")
    except Exception as e:
        print(f"Error al guardar CSV: {e}")


ruta_csv = "pages/static/dataset/vehiculos_ingresados_quick_wash.csv"
df = obtener_datos_api()
if df is not None:
    st.write(df)
    guardar_csv(df, ruta_csv)

    
    st.write("### Filtros")
    columnas = df.columns.tolist()

    
    if "date" in columnas:
        fechas = pd.to_datetime(df["date"], errors="coerce")
        fecha_min = fechas.min()
        fecha_max = fechas.max()
        fecha_inicio, fecha_fin = st.date_input(
            "Rango de fechas",
            [fecha_min, fecha_max]
        )
        df = df[(fechas >= pd.to_datetime(fecha_inicio)) & (fechas <= pd.to_datetime(fecha_fin))]

    
    if "typeVehicle" in columnas:
        tipos = df["typeVehicle"].dropna().unique()
        tipo_sel = st.multiselect("Tipo de vehículo", tipos, default=list(tipos))
        df = df[df["typeVehicle"].isin(tipo_sel)]

  
    if "brand" in columnas:
        marcas = df["brand"].dropna().unique()
        marca_sel = st.multiselect("Marca", marcas, default=list(marcas))
        df = df[df["brand"].isin(marca_sel)]

    
    if "services" in columnas:
        servicios = set()
        df["services"].dropna().str.split(", ").apply(servicios.update)
        servicios = sorted(servicios)
        serv_sel = st.multiselect("Servicios", servicios, default=servicios)
        df = df[df["services"].apply(lambda x: any(s in x for s in serv_sel))]

    st.write("### Datos filtrados")
    st.dataframe(df)
