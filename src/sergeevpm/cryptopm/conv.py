from pmdata import PMData


def data_from_csv(csv: str) -> PMData:
    lines = csv.split('\n')[1:]
    sites = [line.split(";")[0] for line in lines]
    logins = [line.split(";")[1] for line in lines]
    tags = [line.split(";")[2] for line in lines]
    tags = [tag.split(",") for tag in tags]
    pwds = [line.split(";")[3] for line in lines]
    return PMData(sites, logins, tags, pwds)

def data_to_csv(data: PMData) -> str:
    header = "site;login;tags;pass"
    lines = [f"\n{data.sites[i]};{data.logins[i]};{",".join(data.tags[i])};{data.pwds[i]}" for i in range(len(data.pwds))]
    return header + "".join(lines)