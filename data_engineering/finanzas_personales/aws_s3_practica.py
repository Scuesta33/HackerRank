"""
Practica de boto3 (la libreria oficial de AWS para Python) usando S3.
No requiere cuenta ni credenciales reales: @mock_aws intercepta las
llamadas de boto3 y las responde en memoria, simulando un S3 real.
"""
import boto3
from moto import mock_aws


@mock_aws
def practicar_s3():
    s3 = boto3.client("s3", region_name="us-east-1")

    bucket_name = "finanzas-personales-bucket"
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket creado: {bucket_name}")

    s3.upload_file("data/gastos.csv", bucket_name, "gastos.csv")
    print("Archivo subido: gastos.csv")

    print("\nObjetos dentro del bucket:")
    respuesta = s3.list_objects_v2(Bucket=bucket_name)
    for obj in respuesta["Contents"]:
        print(f"  - {obj['Key']} ({obj['Size']} bytes)")

    s3.download_file(bucket_name, "gastos.csv", "gastos_descargado.csv")
    print("\nArchivo descargado como: gastos_descargado.csv")


if __name__ == "__main__":
    practicar_s3()
