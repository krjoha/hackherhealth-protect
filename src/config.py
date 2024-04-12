from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="PROTECT",
    settings_files=["src/settings.toml", "src/.secrets.toml"],
)
