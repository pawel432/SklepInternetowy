from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column

engine = create_engine("mysql+pymysql://pyUser:haslo@localhost/pyApplication")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    price: Mapped[int]
    quantity: Mapped[int]
    product_name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(500))

    def dodajProdukt(nowy_produkt):
        session.add(nowy_produkt)
        session.commit()

    def wyszukajProdukt(self, selected_product_name):
        stmt = select(Product).where(Product.product_name == selected_product_name)
        return stmt


Base.metadata.create_all(engine)
