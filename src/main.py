from file_helpers import copy_directory, generatePage

copy_directory('./static', './public')
generatePage('./content/index.md', './template.html', './public/index.html')