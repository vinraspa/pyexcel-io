"""
    pyexcel_io.constants
    ~~~~~~~~~~~~~~~~~~~

    Constants appeared in pyexcel

    :copyright: (c) 2015 by Onni Software Ltd.
    :license: New BSD License
"""
DEFAULT_NAME = 'pyexcel'
DEFAULT_SHEET_NAME = 'pyexcel_sheet1'
DEFAULT_SEPARATOR = '__'

MESSAGE_INVALID_PARAMETERS = "Invalid parameters"
MESSAGE_ERROR_03 = "cannot handle unknown content"
MESSAGE_CANNOT_WRITE_STREAM_FORMATTER = "Cannot write content of file type %s to stream"
MESSAGE_CANNOT_READ_STREAM_FORMATTER = "Cannot read content of file type %s from stream"
MESSAGE_CANNOT_WRITE_FILE_TYPE_FORMATTER = "Cannot write content of file type %s to file %s"
MESSAGE_CANNOT_READ_FILE_TYPE_FORMATTER = "Cannot read content of file type %s from file %s"
MESSAGE_LOADING_FORMATTER = "The plugin for file type %s is not installed. Please install %s"

FILE_FORMAT_CSV = 'csv'
FILE_FORMAT_TSV = 'tsv'
FILE_FORMAT_CSVZ = 'csvz'
FILE_FORMAT_TSVZ = 'tsvz'
FILE_FORMAT_ODS = 'ods'
FILE_FORMAT_XLS = 'xls'
FILE_FORMAT_XLSX = 'xlsx'
FILE_FORMAT_XLSM = 'xlsm'
DB_SQL = 'sql'
DB_DJANGO = 'django'

