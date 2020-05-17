# Bookmark Manager

# Prerequisite

  - Django - 2.1.5
  - Django-Restframework - 3.11.0

# Database

- Sqlite

# Models

- Customer
- Bookmarks
- customer-bookmark

# API

- `/_api/create` : Create a new Database entry ( via POST request)
    > "POST" request parameters:
    > customer_name
    > customer_age
    > customer_latitude
    > customer_longitude
    > bookmark_title
    > bookmark_url
    > bookmark_source_name

- `/_api/browse` : Search/Browse Database content ( via POST request) filtered by Date range and title pattern of stored bookmarks. Also Sort the result by the bookmark field specified. 
Returns : Customer_id, latitude, longitude, title, date, source_name.
    > "POST" request parameters:
    > date_range :   (YYYY-MM-DD/YYYY-MM-DD)
    > title_contains : (string pattern to be search in bookmark_title)
    > sort_by  :  (any of bookmark_title, bookmark_url, bookmark_source_name, bookmark_date)
