import os
from pypdf import PdfMerger
folder_name = "SS"
folder_path = os.path.join(os.path.expanduser("~"), "Desktop", folder_name)
pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
pdf_files.sort()
merger = PdfMerger()
for pdf in pdf_files:
    full_path = os.path.join(folder_path, pdf)
    merger.append(full_path)
output_file = os.path.join(folder_path, "merged_output.pdf")
merger.write(output_file)
merger.close()
print(f"PDF files merged successfully! File saved at:\n{output_file}")
