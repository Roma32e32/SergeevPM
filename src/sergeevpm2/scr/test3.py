from pathlib import Path
from aes_bridge import encrypt
from backend.record import Record
from ast import literal_eval


records: list[Record] = [
    {
        "Site": "github.com",
        "Login": "ivan.petrov",
        "Tags": ["dev", "work", "git"],
        "Password": "Gh!7xQ2mPz#91Lk",
    },
    {
        "Site": "gmail.com",
        "Login": "ivan.petrov@gmail.com",
        "Tags": ["email", "personal"],
        "Password": "M@ilP4ss_2024!",
    },
    {
        "Site": "stackoverflow.com",
        "Login": "ivan_dev",
        "Tags": ["dev", "forum"],
        "Password": "St4ck!Ov3r#flow",
    },
    {
        "Site": "vk.com",
        "Login": "+79991234567",
        "Tags": ["social", "personal"],
        "Password": "Vk_Priv8t_!23",
    },
    {
        "Site": "telegram.org",
        "Login": "+79991234567",
        "Tags": ["social", "messenger"],
        "Password": "Tg$ecure#2024x",
    },
    {
        "Site": "aws.amazon.com",
        "Login": "ivan.petrov@company.io",
        "Tags": ["work", "cloud", "admin"],
        "Password": "Aw5!R00t_Adm1n#2024",
    },
    {
        "Site": "gitlab.company.io",
        "Login": "i.petrov",
        "Tags": ["work", "git", "dev"],
        "Password": "G1tl4b_W0rk!Pass",
    },
    {
        "Site": "jira.company.io",
        "Login": "i.petrov",
        "Tags": ["work", "tracker"],
        "Password": "J1r4_Tr4ck#99",
    },
    {
        "Site": "steamcommunity.com",
        "Login": "ivan_gamer",
        "Tags": ["games", "personal"],
        "Password": "St3am!G4m3r#77",
    },
    {
        "Site": "netflix.com",
        "Login": "family.acc@mail.ru",
        "Tags": ["media", "family", "subscription"],
        "Password": "N3tfl1x_F4m!ly",
    },
    {
        "Site": "yandex.ru",
        "Login": "ivan.petrov",
        "Tags": ["email", "personal", "ru"],
        "Password": "Y4nd3x_P0rtal!1",
    },
    {
        "Site": "db.company.io",
        "Login": "postgres_admin",
        "Tags": ["work", "database", "admin", "critical"],
        "Password": "P0stgr3s!Sup3rS3cret#42",
    },
    {
        "Site": "router.local",
        "Login": "admin",
        "Tags": ["home", "network", "admin"],
        "Password": "R0ut3r_H0m3!Net",
    },
    {
        "Site": "figma.com",
        "Login": "ivan.design@company.io",
        "Tags": ["work", "design"],
        "Password": "F1gm4_D3s1gn#2024",
    },
    {
        "Site": "reddit.com",
        "Login": "ivan_reads",
        "Tags": ["forum", "personal"],
        "Password": "R3dd1t!Lurk3r#x",
    },
]
s = str(records)
print(literal_eval(s))

#encrypted = encrypt(str(records), "12345")
#Path(r"E:\Roma\PythonProject\SergeevPM\test3.pwm").write_bytes(encrypted)
