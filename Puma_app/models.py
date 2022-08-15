from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Puma(DB.Model):
    # ID items["uuid"]
    id = DB.Column(DB.String, primary_key=True)
    # Date collected: items["data"]["dwc:eventDate"]
    date = DB.Column(DB.String, nullable=False)
    # Elevation: items["data"]["dwc:verbatimElevation"]
    elevation = DB.Column(DB.Integer, nullable=False)
    # Body part: items["data"]["dwc:preparations"]
    specimen = DB.Column(DB.String, nullable=False)
    # State: items["indexTerms"]["stateprovince"]
    state = DB.Column(DB.String, nullable=False)
    # County: items["indexTerms"]["county"]
    county = DB.Column(DB.String, nullable=False)
    # Location: items["indexTerms"]["locality"]
    locality = DB.Column(DB.String, nullable=False)
    # Collector: items["indexTerms"]["collector"]
    collector = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return f"""</p>
                Date Found: {self.date},
                Bone: {self.specimen},
                State: {self.state},
                County: {self.county},
                Location: {self.locality},
                Elevation (m): {self.elevation},
                Collector: {self.collector}
                </p>"""
