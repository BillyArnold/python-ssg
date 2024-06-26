from file_helpers import copy_directory, generate_pages_recursive


copy_directory('./static', './public')
generate_pages_recursive('./content/', './template.html', './public/')