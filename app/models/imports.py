from sqlalchemy import Column, Integer, String, Index

from app.database.database import Base


class Import(Base):

    __tablename__ = "imports"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    month = Column(Integer)
    origin_name = Column(String)
    origin_type_name = Column(String)
    destination_name = Column(String)
    destination_type_name = Column(String)
    grade_name = Column(String)
    quantity = Column(Integer)

    __table_args__ = (Index("origin_type_and_name_idx", origin_type_name, origin_name),)

    def __repr__(self):

        return f"<Import {self.id}>"
