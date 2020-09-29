import os

from weasyprint import HTML


def convert_html_to_pdf(html_path, output_path, encoding='utf-8'):
    try:
        html = HTML(html_path, encoding=encoding)
        html.write_pdf(output_path)
        return True
    except Exception as e:
        print("exception occurred: {}".format(str(e)))
        return False


if __name__ == "__main__":
    base_path = "./htmlfile"
    folders = [os.path.join(base_path, x) for x in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, x))]
    for folder in folders:
        html_files = [os.path.join(folder, x) for x in os.listdir(folder) if x.split(".")[-1] == "html"]
        for html_file in html_files:
            new_path = html_file.replace(".html", ".pdf")
            convert_html_to_pdf(html_file, new_path)
