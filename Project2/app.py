import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# Database Setup								#
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/youtube.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Samples_Metadata = Base.classes.yt_data
Samples = Base.classes.yt_data


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/subscribers")
def subscribers():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

   #sorting descending so that top values are at the top
    df = df.sort_values("Subscribers", ascending=False)


    # Format the data to send as json
    data = {
        "Subscribers": df.Subscribers.values.tolist(),
        "Channelname": df.Channelname.values.tolist(),
        "Rank": df.Rank.values.tolist()
        }
    return jsonify(data)


@app.route("/videoviews")
def videoviews():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

   #sorting descending so that top values are at the top
    df = df.sort_values("Videoviews", ascending=False)


    # Format the data to send as json
    data = {
        "Channelname": df.Channelname.values.tolist(),
        "Rank": df.Rank.values.tolist(),
        "Videoviews": df.Videoviews.values.tolist()
        }
    return jsonify(data)

@app.route("/videouploads")
def videouploads():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

   #sorting descending so that top values are at the top
    df[['Videouploads']] = df[['Videouploads']].replace('--',0)
    df = df.sort_values("Videouploads", ascending=False)


    # Format the data to send as json
    data = {
        "Channelname": df.Channelname.values.tolist(),
        "Rank": df.Rank.values.tolist(),
        "Videouploads": df.Videouploads.values.tolist()
        }
    return jsonify(data)
	
if __name__ == "__main__":
    app.run()
