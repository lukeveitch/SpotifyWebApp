import os
import glob
from pathlib import Path
    
class ImageGenerator(object):
    path_to_script_dir = None
    
    def __init__(self, path_to_script_dir, processing_script):
        self.path_to_script_dir = Path.cwd() / path_to_script_dir
        self.processing_script = processing_script




    def makeArt(self): # !!!!!!!!!! add a more meaningful name to the file that is generated

        jar_file_path = Path(self.path_to_script_dir / "processing-py.jar")
        sketch_path = Path(self.path_to_script_dir / self.processing_script)

        command = f'java -jar {jar_file_path} {sketch_path}'
        save_image_path = f'{self.path_to_script_dir}/Examples/*'
        
        stream = os.popen(command)
        output = stream.read()

        list_of_files = glob.glob(save_image_path)
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
