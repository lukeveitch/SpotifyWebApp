import os
import glob

class ImageGenerator(object):
    path_to_script_dir = None
    
    def __init__(self, path_to_script_dir, processing_script):
        self.path_to_script_dir = path_to_script_dir.removesuffix('\\').removesuffix('/')       
        self.processing_script = processing_script

        print(self.path_to_script_dir)
        
    def makeArt(self): # !!!!!!!!!! add a more meaningful name to the file that is generated

        processing_cli_command = f'java -jar {self.path_to_script_dir}/processing-py.jar {self.path_to_script_dir}/{self.processing_script}'
        print(processing_cli_command)
        #run cli command
        stream = os.popen(processing_cli_command)
        output = stream.read()
        #get most recent file
        list_of_files = glob.glob(f'{self.path_to_script_dir}\\Examples\\*') 
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file

dir_path = "/PietMondrian/"
script_name = "PietMondrian.pyde"
imageGenerator = ImageGenerator(dir_path, script_name)
