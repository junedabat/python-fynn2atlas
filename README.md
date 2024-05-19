# 🐍🖥️ Fynn to Atlas Converter ⚔️
#### 🐍 [See my other Python projects](https://github.com/junedabat/My-Python-Projects) 


### 🖥️ This is a terminal-based Python application to convert text data files from Fynn to Atlas

#### Made on the request of my friend, Chatty, for their [FF2](https://en.wikipedia.org/wiki/Final_Fantasy_II) translations

## Requirements
- 🐍 [Python 3](https://www.python.org/downloads/) (tested on [Python 3.12.2](https://www.python.org/downloads/release/python-3122/))
## 📥 Setup
- ### 📁 Clone the repository
  - #### Method 1: Github's interface
    - Click the green "Code" button on the repository's page on Github
    - Click the "Download ZIP" option
    - Extract the newly downloaded ZIP file

  - #### Method 2: Git command-line
    - Type the following command on your command-line interface (e.g.: cmd, powershell, bash, etc... ):
    ```
    git clone https://github.com/junedabat/python-fynn2atlas
    ```
## ▶️ Usage
- Place the file you want to convert in the same directory as the `fynn2atlas.py` file
- Execute the following command, where:
    - `<file_to_convert.txt>` is the name of the file you want to convert
    - `<format_to_convert_to>` is the name of the format you want to convert your file to (either `fynn` or `atlas`)
    - `<output_file.txt>` is the name of the output file, created from the conversion
    - `[--include_end_tags]` is the option to add `<END>` tags, when converting from Fynn to Atlas
```
python3 <file_to_convert.txt> <format_to_convert_to> <output_file.txt> [--include_end_tags]
```
- **Once converted, you'll find the output file in the `export` subdirectory**

## 📝 Examples
- ### Convert `data_enemy.txt` from Fynn to Atlas (output: `atlas_data_enemy.txt`):
```
python3 fynn2atlas.py data_enemy.txt atlas atlas_data_enemy.txt
```
- ### Convert `data_enemy.txt` from Fynn to Atlas, and include `<END>` tags (output: `atlas_data_enemy.txt`):
```
python3 fynn2atlas.py data_enemy.txt atlas atlas_data_enemy.txt --include_end_tags
```
- ### Convert `atlas_data_attack.txt` from Atlas to Fynn:
```
python3 fynn2atlas.py atlas_data_attack.txt fynn data_attack.txt
```