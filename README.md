# PDF Concatenation Script

## Overview

This Python script is designed to concatenate PDF files based on patient IDs. It uses the PyPDF2 library to merge PDFs and handles logging for better error tracking. The concatenated PDFs are saved in the specified output directory.

## Requirements

- Python 3.x
- PyPDF2 library

## Usage

1. Clone or download the repository to your local machine.

2. Install the required libraries using the following command:

    ```
    pip install PyPDF2
    ```

3. Modify the `input_directory` and `output_directory` variables in the script according to your file locations.

    ```python
    input_directory = r"your_input_directory_path"
    output_directory = r"your_output_directory_path"
    ```

4. Run the script:

    ```python
    python concatenate_pdfs.py
    ```

5. Check the `concatenate.log` file for information about the concatenation process, including any errors encountered.

## File Naming Convention

- The script assumes that the input PDF files follow a specific naming convention: `patient_id_filename.pdf`. For example, `123_document.pdf`.

## Logging

- The script utilizes logging to keep track of the concatenation process. Logs are saved in the `concatenate.log` file.

## Notes

- Make sure to handle large PDF files appropriately, as the script loads entire files into memory during the concatenation process.

- The script may need adjustments if your file naming convention differs from the assumed format.
