import os
import shutil


srcfile = "file0.docx",

filenames = [    
    "file1.docx",
    "file2.docx",
    "file3.docx",
]



for filename in filenames:
    shutil.copy2(srcfile, filename)
