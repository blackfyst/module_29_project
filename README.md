# module_29_project
- run.py: Takes the input data from ~/supplier-data/images/ & ~/supplier-data/descriptions/, handles that and produces a pdf report for under ~/tmp/processed.pdf
- reports.py: Called by run.py to produce a pdf report.
- report_email.py: Called by run.py to prepare and send an email with or without the pdf report.
- supplier-data.tar.gz: The compressed input data going into ~/supplier-data/.
- download_drive_file.sh: Script file to extract data into ~/supplier-data/.
- changeImage.py: Standalone script used to resize images and add arenamed (jpeg) copy into the same source folder (~/supplier-data/images/).