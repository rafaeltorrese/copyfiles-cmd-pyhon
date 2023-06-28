set sourcefile=espinosa-de-los-monteros-ruiz_luis-gonzalo_00453398.docx 
set filenames=perez-palma_susana-montserrat_00478755.docx quiniones-ortega_eder-saul_00468669.docx saavedra-mercado_erwin-john_00460594.docx

for %%F in (%filenames%) do (
    copy %sourcefile% %%F
    echo File %%F was copied succesfully
)

pause