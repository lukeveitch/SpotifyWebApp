import os
import glob

class ImageGenerator(object):
    path_to_script_dir = None
    
    def __init__(self, path_to_script_dir, processing_script):
        self.path_to_script_dir = path_to_script_dir.removesuffix('\\').removesuffix('/')       
        self.processing_script = processing_script
        
    def makeArt(self): # !!!!!!!!!! add a more meaningful name to the file that is generated
        #run cli command
        stream = os.popen(f'java -jar {self.path_to_script_dir}\\processing-py.jar {self.path_to_script_dir}\\{self.processing_script}\n')
        output = stream.read()
        #get most recent file
        list_of_files = glob.glob(f'{self.path_to_script_dir}\\Examples\\*')
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file