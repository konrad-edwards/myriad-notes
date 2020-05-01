import os
import music21
import glob


def corpus_iterator(composer=None):
    if composer is None:
        for path in music21.corpus.getPaths():
            try:
                yield music21.corpus.parse(path)
            except:
                continue
    else:
        for path in music21.corpus.getComposer(composer):
            try:
                yield music21.corpus.parse(path)
            except:
                continue


def file_iterator(base_path, patterns=("**.mid", "**.midi")):
    for pattern in patterns:
        for f in glob.glob(os.path.join(base_path, pattern), recursive=True):
            try:
                yield music21.converter.parse(f)
            except Exception as e:
                print(f"Error on file [{f}], {e}")
                continue
