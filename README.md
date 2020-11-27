# Flipbook

Flipbook is a special-language compiler for describing flipbooks and implement a compiler for this language that can convert a flipbook description into a printable PDF or GIF.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flipbook.

```bash
pip install -e .
```

## Usage

```python
flipc /path/to/flipfile -o /path/to/output_file
#Example: flipc human_life_span.flip -o human_life_span.pdf
```
## Supported Extensions:
Currently, the only supported extensions are:
- PDF
- GIF

## Flipfile Format
Every line of the flipfile is of form XX YY /path/to/abc.jpg, where XX is the starting page index and YY is the ending page index of flipbook. Example of a flipfile is:

```
01 05 child.jpg // Display a child's picture from pages 1 to 5
06 10 adolescent.jpg
11 15 young-adulthood.jpg
16 20 adulthood.jpg
21 25 old-age.jpg
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.