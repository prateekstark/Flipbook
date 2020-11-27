import re
import os
import argparse


def removeComments(string: str) -> str:
    string = re.sub(
        re.compile("/\*.*?\*/", re.DOTALL), "", string
    )  # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(
        re.compile("//.*?\n"), "", string
    )  # remove all occurrence single-line comments (//COMMENT\n ) from string
    return string


class Book(object):
    def __init__(self):
        self.dict = {}

    def read_flipbook(self, file_path):
        bookfile = open(file_path, "r")
        while True:
            line = bookfile.readline()
            if len(line) == 0:
                break
            line = removeComments(line)
            from_, to_, photo_ = line.split()
            from_ = int(from_)
            to_ = int(to_)
            for i in range(from_, to_ + 1):
                self.dict[i] = photo_
        bookfile.close()
        self.dict = dict(sorted(self.dict.items()))

    def printbook(self):
        print(self.dict)

    def write_pdf(self, outputfile_name):
        import fpdf

        pdf = fpdf.FPDF("P", "mm", "A4")
        for image in self.dict.values():
            pdf.add_page()
            pdf.image(image, 0, 0, 210, 297)
        pdf.output(outputfile_name, "F")

    def write_gif(self, outputfile_name):
        from PIL import Image

        frames = []
        for image_filename in self.dict.values():
            frame = Image.open(image_filename)
            frame = frame.resize((360, 500), Image.ANTIALIAS)
            frames.append(frame)
        frames[0].save(
            outputfile_name,
            save_all=True,
            append_images=frames[1:],
            duration=100,
            loop=0,
        )
        del frames
