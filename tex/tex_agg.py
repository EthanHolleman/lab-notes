# aggregate all md files
import os
from pathlib import Path
from datetime import datetime

def modify(md_file, temp_dir):
    # agg all files in parent folder
    # increase the number of # in each heading
    # by two
    # add date as the first heading
    # concatenate all in date order
    # each dir in the experiments folder should become a chapter
    # make all paths to images absolute
    # change links to documents and stuff to link on the github
    # repo
    pass


def collect_chapters(experiment_dir):
    chapters = {}
    for each_chapter in Path(experiment_dir).iterdir():
        chapters[each_chapter] = [filepath for filepath in each_chapter.iterdir() 
                                  if filepath.suffix == '.md'
                                ]
    return chapters


def make_chapter_yml_header(chapter_name):
    return '\n'.join(['---', f"title: '{chapter_name}'", '---\n'])


def concatendate_chapter_content(temp_dir, chapter_name, chapter_md_files):
    chapter_md_files = sorted(chapter_md_files,
                              key=lambda p: datetime.strptime(p, '%m-%d-%y')
                              )
    concat_file = temp_dir.joinpath(f'{chapter_name}.md')
    header = make_chapter_yml_header(chapter_name)

    with open(str(concat_file), 'w') as outfile:
        outfile.write(header)
        for fname in chapter_md_files:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    
    return concat_file


def add_chapters_to_book(chapter_concat_files, main_template, temp_dir):
    main_template_str = open(str(main_template)).read()
    include_string = '\n'.join([
        f'\include{{{chapter_path.absolute()}}}' for chapter_path in chapter_concat_files
    ])
    main_template.replace('$chapter$', include_string)
    notebook_tex = temp_dir.joinpath('notebook.tex')
    with open(str(notebook_tex), 'w') as handle:
        handle.write(main_template)

    return notebook_tex


def convert_to_pdf(output_dir, notebook_tex):
    cmd = f'pdflatex {notebook_tex} -output-directory={output_dir}'
    os.system(cmd)
    return output_dir


def main():
    pass

if __name__ == '__main__':
    main()




    
    
    


