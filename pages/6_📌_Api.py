# import requests
# import pandas as pd

# def obtener_datos_api(url):
#     """
#     Realiza una solicitud GET a la API y retorna los datos como DataFrame.
#     """
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         df = pd.DataFrame(data)
#         return df
#     except requests.exceptions.HTTPError as http_err:
#         print(f"Error HTTP: {http_err}")
#     except requests.exceptions.ConnectionError as conn_err:
#         print(f"Error de conexión: {conn_err}")
#     except requests.exceptions.Timeout as timeout_err:
#         print(f"Error de timeout: {timeout_err}")
#     except requests.exceptions.RequestException as req_err:
#         print(f"Error en la solicitud: {req_err}")
#     except ValueError as json_err:
#         print(f"Error al procesar JSON: {json_err}")
#     return None

# def guardar_csv(df, ruta_csv):
#     """
#     Guarda el DataFrame como un archivo CSV.
#     """
#     try:
#         df.to_csv(ruta_csv, index=False)
#         print(f"Datos guardados en '{ruta_csv}'")
#     except Exception as e:
#         print(f"Error al guardar CSV: {e}")

# if __name__ == "__main__":
#     url = "http://localhost:8081/api-docs"
#     ruta_csv = "pages/static/dataset/Defunciones_ocurridas_en__en_el_Hospital_General_de_Medell_n_20250502.csv"
#     df = obtener_datos_api(url)
#     if df is not None:
#         print("Primeras 5 filas del DataFrame:")
#         print(df.head())
#         guardar_csv(df, ruta_csv)