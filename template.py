import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

project_name = 'churn_prediction'

list_of_files = [
	".github/workflows/.gitkeep",
	f"src/{project_name}/__init__.py",
	f"src/{project_name}/components/__init__.py",
	f"src/{project_name}/utils/__init__.py",
	f"src/{project_name}/config/config.py",
	f"src/{project_name}/pipeline/__init__.py",
	f"src/{project_name}/entities/__init__.py",
	"config/config.yml",
	"dvc.yaml",
	"params.yaml",
	"requirements.txt",
	"setup.py",
	"research/eda.ipynb"
]

# Create files and directories
for file in list_of_files:
	filepath = Path(file)
	filedir, filename = os.path.split(filepath)
	if filedir:
		os.makedirs(filedir, exist_ok=True)
	if filename:
		with open(filepath, 'w') as f:
			f.write("")
	logging.info(f"Created {filepath}")









