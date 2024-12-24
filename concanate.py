import os
import logging
from PyPDF2 import PdfMerger

def concatenate_pdf_files_by_patient_id(input_dir, output_dir): ## function to concatenate pdf files by patient id
    logging.basicConfig(filename='concatenate.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') ## logging to record errors
    
    for filename in os.listdir(input_dir): ## iterate through files in input directory
        if filename.endswith(".pdf"):  ## if file is a pdf
            patient_id = filename.split("_")[0] ## get patient id

            output_path = os.path.join(output_dir, f"{patient_id}_merged.pdf") ## create output path
            
            if not os.path.exists(output_path): ## if output path does not exist
                merger = PdfMerger() ## create pdf merger object
                
                try: ## try to concatenate files
                    for file_to_merge in os.listdir(input_dir): ## iterate through files in input directory
                        if file_to_merge.startswith(f"{patient_id}_"): ## if file starts with patient id
                            file_to_merge_path = os.path.join(input_dir, file_to_merge) ## create file path
                            merger.append(file_to_merge_path) ## append file to merger object
                            logging.info(f"Concatenating file: {file_to_merge}") ## log file name

                    merger.write(output_path) ## write merged files to output path
                    logging.info(f"Merged files for patient ID {patient_id} into {output_path}") ## log success
                except Exception as e:
                    logging.error(f"Failed to concatenate files for patient ID: {patient_id}. Error: {str(e)}") ## log error
                finally:
                    merger.close() ## close merger object
# some changess
# Example usage
input_directory = r"C:\Users\haske\OneDrive\Desktop\pdfs"
output_directory = r"C:\Users\haske\OneDrive\Desktop\pdfs"
concatenate_pdf_files_by_patient_id(input_directory, output_directory)
