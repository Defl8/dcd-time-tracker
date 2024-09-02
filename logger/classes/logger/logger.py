import xlrd

class Logger:
    def __init__(self, workbook_path: str) -> None:
        self.__workbook_path = workbook_path
        self.__workbook: xlrd.Book = xlrd.open_workbook(filename=self.__workbook_path)


    @property
    def workbook(self) -> xlrd.Book | None:
        return self.__workbook

    def get_sheets(self) -> list[xlrd.Sheet]:
        return self.workbook.sheets()
