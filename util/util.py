import locale


def format_number(number, format="%0.0f"):
    return locale.format(format, number, grouping=True)
