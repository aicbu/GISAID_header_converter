# GISAID_header_converter
Quick code to speed up SARS-CoV-2 data uploading for my day to day work.

This simple Python script can convert FASTA headers to GISAID style.<hCoV-19/COUNTRY/SEQ_ID/YEAR>

New fasta headers will be written to a csv.



Usage: gisaid_header_converter.py <input_fasta> [options]


Optional arguments:

  -h               	    	help
  
  --country         	    sampling country (default = Sri Lanka)
  
  --year              	  sampling year (default = 2021)
  
