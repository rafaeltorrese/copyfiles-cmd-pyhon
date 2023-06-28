import os
import shutil


srcfile = "alcantara-lopez_luis-antonio_00185817.docx",

filenames = [    
    "andrade-madrigal_israel_00463414.docx",
    "bernal-lopez_axel_00481753.docx",
    "campos-medina_julieta-esmeralda_00469295.docx",
    "cortes-olvera_erika_00283583.docx",
    "espinosa-de-los-monteros-ruiz_luis-gonzalo_00453398.docx",
    "jimenez-fuentes_jesus-saidh_00488794.docx",
    "lilly-jimenez_eduardo-francisco-javier_00489500.docx",
    "medina-canche_renier-arsenio_00462821.docx",
    "perez-palma_susana-montserrat_00478755.docx",
    "puente-arevalo_andre-marx_00478756.docx",
    "quiñones-ortega_eder-saul_00468669.docx",
    "rojas-miranda_salvador_00508019.docx",
    "rubí-vargas_carolina-lizbeth_0061779.docx",
    "saavedra-mercado_erwin-john_00460594.docx",
    "soto-esquivel_david-ricardo_00469297.docx",
    "vazquez-jimenez_sofía_00506584.docx",
]



for filename in filenames:
    shutil.copy2(srcfile, filename)