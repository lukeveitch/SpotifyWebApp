import os
import subprocess


dir_path = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\PietMondrian\\"
script_name = "PietMondrian.pyde"
command = f'java -jar {dir_path}\\processing-py.jar {dir_path}\\{script_name}'

subprocess.call(f"{command}", shell=True)