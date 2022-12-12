from flask import make_response, render_template
from flask_pydantic import validate
from flask_restful import Resource

from helpers.utils import MailBox, parse_date, read_csv
from models.transaction import Transaction as TransactionModel
from models.user import User as UserModel
from settings import config

headers = {'Content-Type': 'text/html'}


class Transaction(Resource):
    @validate()
    def get(self):
        try:
            TransactionModel.truncate(self)
            UserModel.truncate(self)
            user = UserModel(
                first_name='Jhon',
                last_name='Doe',
                email='jhondoe@gmail.com'
            )
            global first_name
            first_name = user.first_name
            global last_name
            last_name = user.last_name
            user.save_to_db()
            user.commit()
            df_txns = read_csv(r'txns.csv')
            self.calculate_quantities(df_txns)
            rendered = self.render_html()
        except Exception as e:
            print(e)
            return {"msg": "email not sent"}, 500
        emailer = MailBox(config=config["email"])
        emailer.send(
            render_template(
                'email.html',
                first_name=first_name,
                last_name=last_name,
                transactions=transactions,
                total_balance=self.calculate_totals(
                    debitAmounts,
                    creditAmounts
                )[0],
                transactionsAmount=transactionsAmount.items(),
                debitAverage=self.calculate_totals(
                    debitAmounts,
                    creditAmounts
                )[1],
                creditAverage=self.calculate_totals(
                    debitAmounts,
                    creditAmounts
                )[2]
            )
        )
        return rendered

    def render_html(self):
        rendered = make_response(
            render_template(
                'email.html',
                first_name=first_name,
                last_name=last_name,
                transactions=transactions,
                total_balance=self.calculate_totals(
                    debitAmounts,
                    creditAmounts
                )[0],
                transactionsAmount=transactionsAmount.items(),
                debitAverage=self.calculate_totals(
                    debitAmounts,
                    creditAmounts
                )[1],
                creditAverage=self.calculate_totals(
                    debitAmounts,
                    creditAmounts
                )[2]
            ),
            200,
            headers
        )
        return rendered

    def calculate_quantities(self, df):
        global transactions
        global creditAmounts
        global debitAmounts
        global transactionsAmount
        transactionsAmount = {}
        creditAmounts = []
        debitAmounts = []
        transactions = []

        for ind in df.index:
            if (df['Transaction'][ind] < 0):
                debitAmounts.append(df['Transaction'][ind])
            else:
                creditAmounts.append(df['Transaction'][ind])
            transactionsAmount[parse_date(
                    df['Date'][ind]).strftime("%B")
            ] = transactionsAmount.get(
                    parse_date(df['Date'][ind]).strftime("%B"),
                    0
                ) + 1
            transactions.append([
                    parse_date(df['Date'][ind]),
                    str(df['Transaction'][ind]),
                    int(df['User_Id'][ind])
            ])
            txn = TransactionModel(
                id_transaction=ind,
                user_id=df['User_Id'][ind],
                amount=df['Transaction'][ind],
                date=parse_date(df['Date'][ind])
            )
            txn.save_to_db()
            txn.commit()
        return

    def calculate_totals(self, debitAmounts, creditAmounts):
        global debitAverage
        debitAverage = 0
        debitTotal = 0
        debitCount = 0

        global creditAverage
        creditAverage = 0
        creditTotal = 0
        creditCount = 0
        totalBalance = 0

        for debitAmount in debitAmounts:
            totalBalance += debitAmount
            debitTotal += debitAmount
            debitCount = debitCount + 1

        for creditAmount in creditAmounts:
            totalBalance += creditAmount
            creditTotal += creditAmount
            creditCount = creditCount + 1

        debitAverage = debitTotal / debitCount
        creditAverage = creditTotal / creditCount

        return [totalBalance, debitAverage, creditAverage]
