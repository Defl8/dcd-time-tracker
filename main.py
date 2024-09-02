from logger.classes.logger import Logger


def main() -> None:
    logger = Logger("testdata.xls")
    print(*logger.get_sheets())


if __name__ == "__main__":
    main()
