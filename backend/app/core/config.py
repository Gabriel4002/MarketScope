from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "MarketScope"

    database_url: str

    jwt_secret: str

    jwt_algorithm: str = "HS256"

    mercadolivre_client_id: str | None = None

    mercadolivre_client_secret: str | None = None

    mercadolivre_redirect_uri: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


settings = Settings()