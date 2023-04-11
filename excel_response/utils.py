from tempfile import NamedTemporaryFile
from openpyxl.writer.excel import save_workbook


def save_virtual_workbook(workbook):
    with NamedTemporaryFile() as tmp:
        tmp.close()
        save_workbook(workbook, tmp.name)
        return open(tmp.name, 'rb').read()
