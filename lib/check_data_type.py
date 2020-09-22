import logging
import os

from werkzeug.datastructures import FileStorage

logger = logging.getLogger(__name__)


def check_csv_format(filename: str):
    """ Check if the file extension is csv

    Args:
        filename (str): the input filename

    Returns:
        bool -> True if the file's extension is among : jpg, jpeg, gif, false otherwise.
    """
    file_extension = "." in filename and filename.rsplit(".", 1)[1].lower()
    logger.info("File has extension [{}]".format(file_extension))
    return file_extension == "csv"


def check_document_size(input_document: FileStorage):
    """ Checks if the size of the input file is less than 20 Mb

    Args:
        input_document (FileStorage):

    Returns:
        True if size is less than 20, False otherwise
    """
    input_document.flush()
    size = os.fstat(input_document.fileno()).st_size  # The size is in bits
    logger.info("Input document's size is : {}".format(size))
    if size < 19999999:  # 19999999 is equal to 19,9 Mb
        return True
    else:
        return False
