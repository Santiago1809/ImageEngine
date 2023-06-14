import os
import replicate

token = "r8_IFZfweFebgGQ3XRa581ZFYhzdSChkdJ0f05tt"

# Establecer el token de API como variable de entorno
os.environ["REPLICATE_API_TOKEN"] = token


# Crear un cliente de replicate.Client
def crear_imagen_con_calidad(file_path):
    client = replicate.Client()

    output = client.run(
        "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
        input={"image": open(file_path, "rb")},
    )

    return output
