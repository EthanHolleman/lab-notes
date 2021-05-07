# aggregate all md files
import os
from pathlib import Path
from datetime import datetime


def collect_chapters(experiment_dir):
    '''Collect dirs located in the experiment dir. Each of these
    will become a chapter in the final output. 

    Args:
        experiment_dir (Path): Path to experiment directory.

    Returns:
        dict: Dictionary mapping chapter directories to lists of
              markdown files. The markdown files should be titled
              with a mm-dd.yy date and represent the work done
              on one day pertaint to the name of the parent
              dir.

    '''
    chapters = {}
    for each_chapter in Path(experiment_dir).iterdir():
        chapters[each_chapter] = [filepath for filepath in each_chapter.iterdir()
                                  if filepath.suffix == '.md'
                                  ]
    return chapters


def make_chapter_yml_header(chapter_name):
    '''Get a yml formated header for a concatenated
    chapter file. This info if used by pandoc to
    correctly assign chapter names.

    Args:
        chapter_name (str): Name of chapter.

    Returns:
        str: Yml header as a string.
    '''
    return '\n'.join(['---', f"title: '{chapter_name}'", '---\n'])


def concatendate_chapter_content(temp_dir, chapter_name, chapter_md_files):
    '''Concatenate individual work day markdown files into one larger
    chapter markdown files. Files will be ordered by their date (title).

    Args:
        temp_dir (str): Temp directory to write concat file to.
        chapter_name (str): Name of chapter.
        chapter_md_files (list): List of Paths to work day markdown files.

    Returns:
        Path: Path to concatenated chaper file.
    '''
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


def concatenated_chapter_to_tex(concat_md, output_dir, chapter_template):
    '''Convert a concatenated chapter file to a tex file using
    pandoc. Pandoc must be available in the PATH variable.

    Args:
        concat_md (Path): Path to concatenated chapter file.
        output_dir (Path): Path to temp dir to write file to.
        chapter_template (Path): Template tex file to use with pandoc.

    Returns:
        Path: Path to converted tex file.
    '''
    chapter_tex = concat_md.with_suffix('.tex')
    cmd = f'pandoc -f markdown -r latex --template={chapter_template} {concat_md} {chapter_tex}'
    os.system(cmd)
    return chapter_tex


def add_chapters_to_book(chapter_concat_files, main_template, temp_dir):
    '''Add paths to chapter files created by calling 
    `concatenated_chapter_to_tex` to a main template tex file. The main
    template tex file should have the string `$chapter$` where the include
    chapter statements should be located.

    Args:
        chapter_concat_files (list): List of all chapter tex files in include.
        main_template (Path): Path to tex book template.
        temp_dir (Path): Temp dir to write book tex file to.

    Returns:
        Path: Path to book tex file.
    '''
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
    '''Convert completed tex book file to a pdf using pdflatex. 
    pdflatex must be available in PATH.

    Args:
        output_dir (Path): Path to directory to write pdf to.
        notebook_tex (Path): Path to final tex book file.

    Returns:
        Path: Path to pdf file produced by pdflatex.
    '''
    cmd = f'pdflatex {notebook_tex} -output-directory={output_dir}'
    os.system(cmd)
    return output_dir


def main():
    pass


if __name__ == '__main__':
    main()
