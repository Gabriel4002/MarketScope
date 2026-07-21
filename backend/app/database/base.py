from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Classe base de todos os modelos do banco de dados.

    Toda entidade (User, Company, Product, etc.)
    herdará desta classe para que o SQLAlchemy
    consiga mapear automaticamente as tabelas.
    """
    pass