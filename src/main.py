from src.copystaticdirectory import copy_static_directory
from src.generatepage import generate_page

content_file_path = "../content/index.md"
template_file_path = "../template/template.html"
generated_page_file_path = "../public/index.html"

def main():
    copy_static_directory()
    generate_page(content_file_path, template_file_path, generated_page_file_path)


main()
