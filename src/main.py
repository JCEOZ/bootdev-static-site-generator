from src.copystaticdirectory import copy_static_directory
from src.generatepage import generate_page_recursively

content_directory_path = "../content"
template_file_path = "../template/template.html"
generated_pages_directory_path = "../public"

def main():
    copy_static_directory()
    generate_page_recursively(content_directory_path, template_file_path, generated_pages_directory_path)


main()
