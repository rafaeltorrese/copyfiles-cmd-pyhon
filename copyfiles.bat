set sourcefile=source_file.docx 
set filenames=file1.docx file2.docx file3.docx

for %%F in (%filenames%) do (
    copy %sourcefile% %%F
    echo File %%F was copied succesfully
)

pause
