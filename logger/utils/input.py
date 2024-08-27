def get_timesheet_path() -> str:
    cleaned_input: str = ''
    raw_input: str = input("Input the path to your timesheet: ")
    if "\\" in raw_input:
        cleaned_input = raw_input.replace("\\", '/')
    return cleaned_input
