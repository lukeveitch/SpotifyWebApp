import os
from pathlib import Path
import glob

script_dir_name = "PietMondrian" # write the name of the directory with no leading or trailing slashes
path_to_script_dir = Path.cwd() / script_dir_name
save_image_path = Path(path_to_script_dir / "Examples" / "*")

print(script_dir_name)
print(path_to_script_dir)
print(save_image_path)
p = r"C:\Users\Lenovo\Desktop\SpotifyWebApp\PietMondrian\Examples\*"
print(p)
list_of_files = glob.glob(p)
list_of_files2 = glob.glob(rf"{save_image_path}")
print(list_of_files)
print(list_of_files2)