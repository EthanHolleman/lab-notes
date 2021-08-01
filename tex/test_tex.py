import pytest
from pathlib import Path
import os

from tex import *

file_loc = Path(__file__).parent.resolve()


@pytest.fixture
def chapter_dirs():
    return list(file_loc.parent.joinpath('experiments').iterdir())


@pytest.fixture
def temp_dir():
    temp = file_loc.joinpath('temp')
    temp.mkdir(parents=True, exist_ok=True)
    return temp

@pytest.fixture
def notebook_path(temp_dir):
    return temp_dir.joinpath('notebook.pdf')


@pytest.fixture
def chapters(chapter_dirs, temp_dir):
    chapters = []
    for each_dir in chapter_dirs:
        c = Chapter.init_from_chapter_dir(each_dir, temp_dir)
        if c:
            chapters.append(c)
            # only add if there were markdown entries and a
            # chatper instance was created

    return chapters


def test_init_from_chapter_dir(chapter_dirs, temp_dir):
    for each_dir in chapter_dirs:
        c = Chapter.init_from_chapter_dir(each_dir, temp_dir)
        if c:
            assert len(c.entries) > 0
            assert isinstance(c, Chapter)
        if not c:
            dir_md_contents = [
                f for f in each_dir.iterdir() if f.suffix == '.md']
            assert len(dir_md_contents) == 0


def test_combine_entries(chapters):
    for each_chapter in chapters:
        output_path = each_chapter.combine_entries()
        assert output_path.is_file()
        assert len(open(str(output_path)).read())
        #os.remove(str(output_path))

def test_notebook(chapters, notebook_path):
    notebook = Notebook(chapters, notebook_path)
    notebook.write_notebook()
    assert notebook_path.is_file()
