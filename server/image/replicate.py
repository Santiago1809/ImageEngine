import os
import replicate

token = "r8_IFZfweFebgGQ3XRa581ZFYhzdSChkdJ0f05tt"

os.environ["REPLICATE_API_TOKEN"] = token


# Crear un cliente de replicate.Client
"""
This function uses a client to run a specific version of the real-ESRGAN algorithm on an input image
file and returns the output.

:param file_path: The file path parameter is a string that represents the path to the image file
that needs to be processed
:return: the output of the client's run method, which is the result of processing the input image
file using the specified ESRGAN model. The output could be an image file with improved quality or
some other data depending on the implementation of the client's run method.
"""
def crear_imagen_con_calidad(file_path):
    client = replicate.Client()

    output = client.run(
        "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
        input={"image": open(file_path, "rb")},
    )

    return output
