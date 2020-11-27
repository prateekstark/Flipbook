# Flipbook

Flipbook is a special-language compiler for making small flipbooks in "GIFs" and "PDFs".

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


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.