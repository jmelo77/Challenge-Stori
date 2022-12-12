from sqlalchemy import Column, Date, Float, Integer

from db import db


class Transaction(db.Model):
    __tablename__ = "transactions"
    id = Column(
        Integer, primary_key=True,
        autoincrement=True,
        nullable=False,
        index=True
    )
    id_transaction = db.Column(
        db.Integer, nullable=False
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, index=True
    )
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    def __init__(self, id_transaction, user_id, amount, date):
        self.id_transaction = id_transaction
        self.user_id = user_id
        self.amount = amount
        self.date = date

    def json(self):
        return {
            "id_transaction": self.id_transaction,
            "user_id": self.user_id,
            "amount": self.amount,
            "date": str(self.date),
        }

    @classmethod
    def find_all(cls) -> object:
        """
        Find all transactions by user id.
        :param user_id: The id of the user.
        :return: The transactions.
        """
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id: int) -> object:
        """
        Find a transaction by id.
        :param id: The id of the transaction.
        :return: The transaction.
        """
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user_id(cls, user_id: int) -> list:
        """
        Find all transactions by user id.
        :param user_id: The id of the user.
        :return: The transactions.
        """
        return cls.query.filter_by(user_id=user_id).all()

    def save_to_db(self):
        db.session.add(self)

    def commit(self, id: bool = False) -> int:
        """
        Commit the changes to the database.
        :return: The id of the object if required.
        """
        db.session.commit()
        if id:
            db.session.refresh(self)
            return self.id

    def rollback(self):
        db.session.rollback()

    def truncate(self):
        db.session.execute('''TRUNCATE TABLE transactions''')
        db.session.commit()
        db.session.close()
