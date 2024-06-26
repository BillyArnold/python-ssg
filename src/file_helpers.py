import os
import shutil
from markdown_helpers import markdown_to_html_node, extract_title

def copy_directory(current_path, target_path):
    #check public path exists
    if os.path.exists(current_path) == False:
        raise Exception(f'File path {current_path} not found')
    
    dir_listing = os.listdir(current_path)

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

def generate_page(from_path, template_path, dest_path):
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

    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", html_output)

    with open(dest_path, "w") as file:
        file.write(template_contents)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
   #check public path exists
    if os.path.exists(dir_path_content) == False:
        raise Exception(f'File path {dir_path_content} not found') 

    dir_listing = os.listdir(dir_path_content)

    for item in dir_listing:
        path = os.path.join(dir_path_content, item)
        file_target_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(path) and path.endswith('.md'):
            html_path = file_target_path.replace('.md', '.html')
            generate_page(path, template_path, html_path)
            continue

        #if is directory, create corresponding
        if os.path.exists(file_target_path) == False:
            os.mkdir(file_target_path)
            generate_pages_recursive(path, template_path, file_target_path)
