# Requirements

- write your app using Python; you may choose the version
- use any web framework or ORM you'd like.
- adhere to a RESTful API design.
- Store and retrieve data from a database like Postgres.
- Provide an option to seed the database with fixture or generated data.
- Deploy locally using Docker; and/or Docker Compose.
- Include a README

# Interpretation of Requirements

<p>
"Store and retrieve" is interpreted to mean only writing new data and fetching existing data.
Therefore, full CRUD operations are not needed. This is common for tables that are often truncated and reloaded 
per some ETL process. Therefore a highly relational model is not needed and assumed to exist upstream.
</p>
<p>
"adhere to a RESTful API design." is interpreted to provide endpoints that retrieve data quickly with browser caching.
</p>
<p>
There is no mention of frequency of data ingestion or volume of data to process. We assume trivial data.
</p>

# Implementation

- Written using Python 3.8, Responder, and SQLAlchemy (chosen for industry standard)
- SQLite database written to disk
- Containerized with Alpine (used for small footprint)
- boot.sh to set PYTHONPATH prior to launching the app

# Database Design

<p>
There is no obvious unique identifier for database objects to index. We therefore fetch using the row number.
</p>
<p>
The provided logical data model is relational because of the 'has a' relationship between Sites per Instruments, and Freezers with Containers.
However data is stored as JSON because updating is not needed and query time is constant for any given row number.
</p>
<p>
A logical mode is provided for easy in-memory validation of incoming data. A JSON schema also provides some validationl.
</p>

# Code Design
- A DAO is provided which should could have static methods, but initialization of the database happens in its constructor.
- The JSON schema is implemented as a Python dict rather than a json file so that reading from disk is avoided
- Getters and Setters are provided in the logical model for validation of input
- Some basic testing provided using uunitest framework

# API Design

<p>
All endpoints verify correct headers and do not require any auth.
</p>
<p>
API models exist based on logical entity retrieved and to not collide with <code>/site/{id}</code>.
</p>
<p>
<code>/site/{id}</code> is implemented rather than passing the site id as a query parameter, so that it can be bookmarked in a browser.
</p>

# Getting Started

1. Run: <code>docker build .</code>.
2. Run: <code>docker run -p 5033:5033 {image}</code>.
3. Using Postman or curl, verify the app is up with the endpoint <code>/health</code>
3. Using Postman or curl, seed the database with the endpoint <code>/seed</code>
3. Using Postman or curl, list all ids with the endpoint <code>/ids</code>
4. Insert new data or fetch existing data

