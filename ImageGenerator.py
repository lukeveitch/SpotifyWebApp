import os
import glob

    
class ImageGenerator(object):
    path_to_script_dir = None
    
    def __init__(self, path_to_script_dir, processing_script):
        self.path_to_script_dir = os.getcwd() + path_to_script_dir.removesuffix('\\').removesuffix('/')       
        self.processing_script = processing_script

    def makeArt(self): # !!!!!!!!!! add a more meaningful name to the file that is generated
        command = f'java -jar {self.path_to_script_dir}\\processing-py.jar {self.path_to_script_dir}\\{self.processing_script}\n'
        save_image_path = f'{self.path_to_script_dir}\\Examples\\*'
        
        stream = os.popen(command)
        output = stream.read()

        list_of_files = glob.glob(save_image_path)
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file
