import os
import codecs


script_dir = os.path.dirname(os.path.abspath(__file__))
final_path = os.path.join(script_dir, os.path.pardir)
print(final_path)
rela_dir = "Web_scraping\yes24.txt"
abs_file_path = os.path.join(final_path, rela_dir)
print(abs_file_path)
f = codecs.open(abs_file_path, "r", "utf-8")
print(f.read())


#C:\Users\super\git\Data_science\PYTHON_Project\Web_scraping\yes24.txt