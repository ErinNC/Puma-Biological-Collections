from flask import Flask
import requests
from .models import DB, Puma


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def home():
        all_pumas = Puma.query.order_by(Puma.date).all()
        return f"{all_pumas}"

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return "Database has been reset."

    @app.route('/populate')
    def populate():
        api_endpoint = 'https://search.idigbio.org/v2/search/records/?rq=%7B%22scientificname%22%3A+%22puma+concolor%22%7D&limit=5'
        response = requests.get(api_endpoint)
        response = response.json()

        for puma in response['items']:
            new_puma = Puma(
                id=puma['uuid'],
                date=puma["data"]["dwc:eventDate"],
                elevation=puma["indexTerms"]["minelevation"],
                specimen=puma["data"]["dwc:preparations"],
                state=puma["indexTerms"]["stateprovince"],
                county=puma["indexTerms"]["county"],
                locality=puma["indexTerms"]["locality"],
                collector=puma["indexTerms"]["collector"]
            )

            DB.session.add(new_puma)

        DB.session.commit()

        return "Database has been populated with data from the iDigBio API"

    return app
