import os
import shutil
from markdown_helpers import markdown_to_html_node, extract_title

def copy_directory(current_path, target_path):
    #check public path exists
    if os.path.exists(current_path) == False:
        raise Exception(f'File path {current_path} not found')
    
    dir_listing = os.listdir(current_path)
    print(dir_listing)

    for item in dir_listing:
        path = os.path.join(current_path, item)
        file_target_path = os.path.join(target_path, item)
        if os.path.isfile(path):
            shutil.copyfile(path, file_target_path)
            continue

        #if is directory, create corresponding
        if os.path.exists(file_target_path) == False:
            os.mkdir(file_target_path)
            copy_directory(path, file_target_path)

def generatePage(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    if os.path.getsize(from_path) == 0:
        print('Markdown file is empty')
    
    with open(from_path, 'r', encoding="utf-8") as file:
        markdown = file.read()

    with open(template_path, 'r', encoding="utf-8") as template:
        template_contents = template.read()

    html_nodes = markdown_to_html_node(markdown)
    html_output = html_nodes.to_html()
    title = extract_title(markdown)

    template_contents.replace("{{ Title }}", title)
    template_contents.replace("{{ Contents }}", html_output)



    print(template_contents)
