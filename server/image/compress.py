import cloudconvert
import base64

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYjBhM2M1ZDMwYzRmMmNhMTQ4MmUwZmIyYzcyZWQyMjJlMmUyMDkwZjc5ZmNiZmJlYzA1ZmE5NGNmOGQxMTcwODE2YzA2YWQ2MDFlYmZmZWMiLCJpYXQiOjE2ODY3MDQwMTIuNzcwODAyLCJuYmYiOjE2ODY3MDQwMTIuNzcwODAzLCJleHAiOjQ4NDIzNzc2MTIuNzY2NjAyLCJzdWIiOiI2Mzk5MDE5MyIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsInByZXNldC5yZWFkIiwicHJlc2V0LndyaXRlIl19.IEMWE7C19om9sviEZFuLMQuN75Dj0p2PAkO_rCZ7rfHMq964PDyGxmzv0mCSxq95zesoXvQCq-SXwrrUxDT8dqiku5GTA4vWp-NYZpmikPaqlqjDZIbr6fCQ0uTzaMQb05Ulkb1WHWEjdeo9qfecg1o9_viKY6BoPZ5dnSKnwKLahJcw46BKoM6YM3saKfuuQvoNXqJWvfUCrUq9luEO6tbI1h6YaOYrJfWcvidH24vPKVAkKm7I5dxjTzx4FCxJBkc4u1FlBG7RabDjCkfmXjpNKjDDabCeP9VM9-32px34Qy37LFsr7UFodzAi2w_L5qN9l7wb2-23H72ywVPd399jC06SE5S1oBJyh6___MGqiA8rQT9iS6-7LHdQ7O58GJewdoTkCfMdsAk8jEWcsnP1vB4xKUmuQdBTJ1mYIx1r1ibcG3vBFHyyc9kIbnjDQFpEtTYWZeiDoDThn6Rt1O1VmQrQoJc55CBLl_QG7zCt_kPm7rpudjvbxOx1Me12VVyS1S-rYwsdndUF-LikzyUkRAaq2Phnf0KnR3oQJp_L0YusXMtpxhaEi_cT1iqYnGZi1SgQpI1AQRcWaQNysEEcHmUo4BbEi8sQv308lY0X2i-5oOc8LENsryEBO3xG3ApH8K0nKiUu2Ebe-GV4hjdQd2I9-VziA7GInSTZU9Y"

cloudconvert.configure(api_key=API_KEY, sandbox=False)


"""
This function compresses an image file by converting it to a specified file format using
CloudConvert API.

:param file_path: The path to the file that needs to be compressed
:param file_ext: The file extension of the desired output format for the compressed image
:return: the name of the compressed file.
"""
def comprimir_imagen(file_path, file_ext):
    with open(file_path, "rb") as input_file:
        input_data = input_file.read()

    base64_encoded_data = base64.b64encode(input_data).decode("utf-8")

    job = cloudconvert.Job.create(
        payload={
            "tasks": {
                "import-my-file": {
                    "operation": "import/upload",
                    "file": base64_encoded_data,
                },
                "convert-my-file": {
                    "operation": "convert",
                    "input": "import-my-file",
                    "output_format": file_ext,
                    "region": "us",
                },
                "export-my-file": {
                    "operation": "export/url",
                    "input": "convert-my-file",
                },
            },
            "tag": "myjob-123",
        }
    )

    output_url = job["tasks"]["export-my-file"]["result"]["files"][0]["url"]
    output_url = output_url.split("/")[-1]
    return output_url
