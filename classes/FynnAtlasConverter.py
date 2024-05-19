from io import TextIOWrapper
import os
import re

class FynnAtlasConverter:
  def __init__(self, file_to_convert : str, to_format : str, output_file : str, end_tags_inclusion: bool) -> None:
    self.open_input_output_files(file_to_convert, output_file)
    self.handle_conversion(to_format, end_tags_inclusion)


  def open_input_output_files(self, file_to_convert, output_file) -> None:
    # File to convert
    print(f"Opening {file_to_convert}")
    self.read_file = open(file_to_convert, encoding = "utf-8")
    print("Open!")

    # Output file
    print("Creating the output file...")
    # Try to create a new "export" directory, if it already exists then that's ok
    os.makedirs("export/", exist_ok=True)
    self.write_file = open(f"export/{output_file}", "w", encoding = "utf-8")
    print(f"Created {self.write_file.name}!")

  # Executes the right methods depending on the chosen output format (atlas or fynn)
  def handle_conversion(self, to_format : str, end_tags_inclusion : bool) -> None:
    if to_format == "atlas":
      self.check_end_tags_inclusion(end_tags_inclusion)
      self.convert_fynn_to_atlas()
    elif to_format == "fynn":
      self.convert_atlas_to_fynn()
    else: print(f"Invalid format of conversion: {to_format}")
  
  # Check if you want to include <END> tags when converting to atlas
  def check_end_tags_inclusion(self, end_tag_arg : str) -> None:
    if end_tag_arg:
      print(f"End tags enabled! {end_tag_arg}")
      self.end_tags_enabled = True
    else: 
      print(f"End tags disabled! {end_tag_arg}")
      self.end_tags_enabled = False


  # Oversees the conversion of a file from fynn to atlas
  def convert_fynn_to_atlas(self) -> None:
    print("Reading the input file...")

    # Cycle through the input file
    for line in self.read_file:
      # If the line is empty, go to next one
      if line == "\n" or line == "": pass

      # Read a line and convert it
      fynn : list = self.extract_fynn_from_line(line)
      print(f"Found {fynn}")
      key : str = fynn[0]
      message : str = self.convert_fynn_line_skips_to_atlas(fynn[1])
      converted_line : str = self.convert_single_fynn_line_to_atlas(key, message)

      print(f"{fynn} converted! Writing...")
      # Write the converted content into the output file
      self.write_file.write(converted_line)
    print(f"All done! Exported converted fynn into {self.write_file.name}")
    # Close the files
    self.read_file.close()
    self.write_file.close()


  # Oversees the conversion of a file from atlas to fynn
  def convert_atlas_to_fynn(self) -> None:
    content = self.read_file.read()
    for message in content.split("#W16"):
      if message:
        message = self.remove_atlas_line_skips(message)
        message = self.remove_atlas_end_tags(message)
        message = self.convert_atlas_line_skips_to_fynn(message)
        message = (self.convert_single_message_to_fynn(message))
        print(f"------------\n{message}")
        self.write_file.write(message)
    print(f"All done! Exported converted fynn into {self.write_file.name}")
    # Close the files
    self.read_file.close()
    self.write_file.close()


  # Takes a string and outputs a list of elements that are separated by "="
  # (e.g: Input: "msg1=Legeaater" -> Output: ["msg1","Legeaater"]
  def extract_fynn_from_line(self, line : str) -> list:
    return line.replace("\n","").split("=")


  def convert_fynn_line_skips_to_atlas(self, message : str) -> str:
    return message.replace("/","<LINE>\n")


  def convert_single_fynn_line_to_atlas(self, key : str, message : str) -> str:
    end_tag = ""
    if self.end_tags_enabled:
      end_tag = "<END>"
    return f"#W16({key})\n{message}{end_tag}\n\n"


  def remove_atlas_line_skips(self ,message : str) -> str:
    return message.replace("\n", "")
  

  def remove_atlas_end_tags(self, message : str) -> str:
    return message.replace("<END>", "")


  def convert_atlas_line_skips_to_fynn(self, message : str) -> str:
    return message.replace("<LINE>","/")


  def convert_single_message_to_fynn(self, message) -> str:
    pattern = r'\((msg\d+)\)(.*?)$'
    match = re.search(pattern, message)
    if match:
      msg_number = match.group(1)
      content = match.group(2)
      return f"{msg_number}={content}\n"
    else: return None

        


