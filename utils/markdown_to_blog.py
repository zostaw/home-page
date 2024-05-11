from argparse import ArgumentParser
from pathlib import Path
import datetime
import markdown

def convert_md_to_html(markdown_inputfile, html_outputfile, with_br):
    """
    Takes path of markdown and converts it to html format.

    :param markdown_inputfile: str, the name of the markdown file to read the text intended for conversion.
    :param html_outputfile: str, the name of the HTML file to save the converted text.
    :param with_br: bool, defines if double space at the end of line is converted
    """
    
    def add_boilerplate(text):
        """
        Appends date stamp and boilerplate
        """
        today_date = datetime.date.today()
        date_stamp = f"{today_date.day}.{today_date.month}.{today_date.year}"

        complete_text = "{% block content %}\n\n" + date_stamp + "\n\n" + text + "{% endblock %}"

        return complete_text

    def lists_handler(text_with_dashed_lists):
        """
        replaces dashed lists with html <ul> </ul> sections
        """

        text_with_ul_style_lists = ""
        list_started = False
        for line in text_with_dashed_lists.split("\n"):
            if list_started:
                # list continues
                if line.startswith("- "): 
                    line = "<li>" + line.lstrip("- ") + "</li>"
                else: # end of list
                    line = "</ul><br>\n" + line
                    list_started = False
            elif line.startswith("- "): # beginning of a list
                line = "<ul>\n<li>" + line.lstrip("- ") + "</li>"
                list_started = True

            text_with_ul_style_lists += line + "\n"


        return text_with_ul_style_lists

    with open(file=markdown_inputfile, mode='r', encoding="utf-8") as md_file:
        markdown_text = md_file.read()
    # convert
    html_content = markdown.markdown(markdown_text)

    # convert "- " lists into <ul>
    html_content = lists_handler(html_content)

    # add headers and date
    html_content = add_boilerplate(html_content)

    # convert double-space at the end - should/not have <br/>
    if not with_br: html_content = html_content.replace("<br />", "")


    with open(file=html_outputfile, mode="w", encoding="utf-8", errors="xmlcharrefreplace") as html_file:
        html_file.write(html_content)


if __name__ == "__main__":


    parser = ArgumentParser()
    parser.add_argument('inputfile_path')
    parser.add_argument('outputfile_name')
    parser.add_argument("--with_br", dest="with_br",
                    help="switch <BR/> mode True/False", default="False")
    args = parser.parse_args()

    if Path(args.inputfile_path).suffix != ".md":
        raise ValueError("Must provide *.md file (path) as input.")
    if Path(args.outputfile_name).suffix != ".html":
        raise ValueError("Must provide *.html file (name) as output.")
    match args.with_br:
        case "True":
            with_br = True
        case "False":
            with_br = False
        case _:
            raise ValueError(f"--with_br must be True/False, but is {args.with_br}")


    outputfile = Path("../app/templates/blog/") / (args.outputfile_name)
    print(f"Output file path: {outputfile}")
    convert_md_to_html(args.inputfile_path, outputfile, with_br)



