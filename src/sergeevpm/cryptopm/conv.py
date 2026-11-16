from .pmdata import Record


def data_from_csv(csv: str) -> list[Record]:
    lines = csv.splitlines()[1:]
    return [Record(*line.split(';', 3)) for line in lines if line]


def data_to_csv(records: list[Record]) -> str:
    header = "site;login;tags;pass"
    lines = [f"\n{record.site};{record.login};{record.tags};{record.password}" for record in records]
    return header + "".join(lines)
