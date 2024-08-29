from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    class Config:
        # No env_file specified, so it will rely on environment variables, for now we are loading these in run.py
        env_file = None
        env_file_encoding = 'utf-8'

    def get_database_url(self) -> str:
        print(f"DATABASE_name: {self.db_name}")
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

# Initialize the settings object
settings = Settings()

# Access the DATABASE_URL
database_url = settings.get_database_url()

if __name__ == "__main__":
    print(f"DATABASE_URL: {database_url}")
