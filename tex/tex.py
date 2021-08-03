from pathlib import Path
import os
import subprocess
import yaml
import re
from datetime import datetime
import subprocess

MD_TITLE_RE = r'^# (.*)'  # captures top level titles 
MD_HEADERING_RE = r'(#+) (.*)'  # captures all headings
MD_LINK_RE = r'(\[.*\])\((.*)\)'  # captures links


class Entry():

    temp_dir = Path(os.getcwd()).joinpath('entry_temp')
    temp_dir.mkdir(parents=True, exist_ok=True)

    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.content = self._content()

    
    def _content(self):
        # markdown content
        with open(str(self.filepath)) as handle:
            return handle.read()
    
    def _update_link_paths(self):
        # update links to local files so that they work when file is
        # rendered from parent directory

        def update_local_path(match):
            full_path = self._is_local_link(match[2])
            if full_path:
                return f'{match[1]}({full_path})'
            else:
                return match[0]  # not local file make no change
        
        self.content = re.subn(MD_LINK_RE, update_local_path, self.content)[0]
    

    def _demote_all_headings(self):

        def demote_heading(match):
            heading_level = match[1]  # number of #s
            demoted_level = heading_level + '#'
            return f'{demoted_level} {match[2]}'  # match 2 is heading text
        
        self.content = re.subn(MD_HEADERING_RE, demote_heading, self.content)[0]



    def _is_local_link(self, link_path):
        full_path = self.filepath.parent.joinpath(link_path)
        if full_path.is_file():
            return full_path
        else:
            return False


    @property
    def entry_name():
        re.search(MD_TITLE_RE)[0]

    @property
    def date(self):
        # extract date from filepath, should always the last item before the
        # file extension with "_" delimiter
        date_string = self.filepath.stem.split('_')[-1]
        return datetime.strptime(date_string, '%m-%d-%y')
    
    def processed_content(self):
        self._update_link_paths()
        self._demote_all_headings()
        return self.content


class Chapter():

    tex_template = 'template_path'


    @classmethod
    def init_from_chapter_dir(cls, dir_path, output_dir):
        entries = [Entry(fp) for fp in Path(dir_path).iterdir() if fp.suffix=='.md']
        if entries:
            return cls(entries, output_dir)

    def __init__(self, entries, output_dir):
        self.entries = entries
        self._sort_entries()
        self.output_dir = Path(output_dir)

    @property
    def title(self):
        title = self.entries[0].filepath.parent.name
        return title

    @property
    def formated_title(self):
        return self.title.replace('_', ' ')
    
    @property
    def markdown_title(self):
        # markdown formated chapter title
        return f'# {self.formated_title}'

    @property
    def output_path(self):
        return self.output_dir.joinpath(self.title).with_suffix('.md')

    def _sort_entries(self):
        # if entries have index number use that
        if self._entries_are_indexed():
            self.entries = self._order_entries_by_index()
        else:
            self.entries = self._order_entries_by_date()

    def _entries_are_indexed(self):
        # entries are indexed if they start with an integer
        for each_entry in self.entries:
            index = each_entry.filepath.name.split('_')
            try:
                index = int(index[0])
            except ValueError as e:
                return False

        return True

    def _order_entries_by_index(self):
        return sorted(
            self.entries, key=lambda e: int(e.filepath.name.split('_')[0])
        )

    def _order_entries_by_date(self):
        # assume date format of m-d-y
       return sorted(
            self.entries,
            key=lambda e: e.date
        )

    def _entry_filepaths(self):
        return [str(e.filepath) for e in self.entries]
    

    def combine_entries(self):
        entry_content = [entry.processed_content() for entry in self.entries]
        with open(str(self.output_path), 'w') as handle:
            # write chapter title
            handle.write(self.markdown_title)
            handle.write('\n\n')
            for each_entry in entry_content:
                handle.write(each_entry)
                handle.write('\n')
        return self.output_path

    # def convert_to_tex(self):
    #     cmd = ['pandoc', '-s'] + self._entry_filepaths() + \
    #         ['-o'] + [str(self.output_path), '--template', 'tex/chap_template.tex']
    #     subprocess.call(cmd)
    #     assert self.output_path.is_file()
    #     return self.output_path


class Notebook():

    template = ''

    def __init__(self, chapters, output_path):
        self.chapters = chapters
        self.output_path = Path(output_path)
    
    def write_chapters(self):
        return [str(c.combine_entries()) for c in self.chapters]
    
    def write_notebook(self):
        chapters = self.write_chapters()
        cmd = [
            'pandoc', '-s', *chapters, '-o', str(self.output_path),
            '--top-level-division=chapter --template', '/home/ethan/Documents/github/lab-notes/tex/template.tex'
            # update template path 
        ]
        print(' '.join(cmd))
        os.system(' '.join(cmd))




