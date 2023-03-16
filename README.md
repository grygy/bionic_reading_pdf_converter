# Bionic reading pdf converter

## Installation

#### 1. Install `python3`
Fist of all you need to have `python3.6` or higher installed.
#### 2. Install `pdftohtml`

https://pdftohtml.sourceforge.net/

- Homebrew (macOS):
```sh
brew install pdftohtml
```

#### 3. Install `ghostscript`

- Homebrew (macOS)
```sh
brew install ghostscript
```

#### 4. Install `wkhtmltopdf`

- Debian/Ubuntu:
```sh
sudo apt-get install wkhtmltopdf
```
- macOS:
```sh
brew install homebrew/cask/wkhtmltopdf
```

#### 5. Install requirements

```sh
pip install -r requirements.txt
```

## Usage

```sh
python3 pdf_converter.py <filename>
```

Example:
```sh
python3 pdf_converter.py file.pdf
```