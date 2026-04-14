import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO)

def create_project_dir(project_name):

    list_of_file = [
    ".github/workflows/.gitkeep",

    f"src/{project_name}/__init__.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",

    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",

    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",

    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"



]


    for filepath in list_of_file:
        filepath = Path(filepath)
        file_directory, file_name = os.path.split(filepath)
        # filepath = file_directory + file_name


        # Create directories if not exist
        if file_directory != "":
            if not os.path.exists(file_directory):
                os.makedirs(file_directory,exist_ok=True)
                logging.info(f"Creating directory: {file_directory} for the file {file_name}")

            else:
                logging.info(f"Directory already exists: {file_directory} for the file {file_name}")


        # Create files if not exist
        if (not os.path.exists(filepath)) :
            with open(filepath,'w') as f:
                pass
                logging.info(f"Creating empty file: {filepath}")

        else:
            logging.info(f"{file_name} already exists")

        

project_name = "dsproject"
create_project_dir(project_name)