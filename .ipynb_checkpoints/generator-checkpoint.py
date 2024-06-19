
import os
import re
import subprocess

def extract_imports_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Import statements regex
    imports = re.findall(r'^\s*(?:import|from)\s+([^\s]+)', content, re.MULTILINE)
    return imports

def get_installed_packages():
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    installed_packages = result.stdout.decode('utf-8').split('\n')
    return installed_packages

def create_requirements_file(project_path, output_file='requirements.txt'):
    # Get all Python files in the project directory
    py_files = [os.path.join(root, file)
                for root, _, files in os.walk(project_path)
                for file in files if file.endswith('.py')]
    
    # Extract imports from all Python files
    all_imports = set()
    for py_file in py_files:
        all_imports.update(extract_imports_from_file(py_file))
    
    # Get installed packages
    installed_packages = get_installed_packages()
    
    # Filter installed packages to include only those that are imported in the project
    required_packages = []
    for package in installed_packages:
        package_name = package.split('==')[0]
        if package_name in all_imports:
            required_packages.append(package)
    
    # Write the requirements to a file
    with open(output_file, 'w') as file:
        for package in required_packages:
            file.write(package + '\n')
    print(f'Requirements file created: {output_file}')

# Define the project directory (change this to your project's root directory)
project_directory = '.'

# Create the requirements file
create_requirements_file(project_directory)