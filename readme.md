# Capstone Project

This is a project for the Slightly Techie School Backend. I am in the Caramel Group

## Requirements
 - API Users must be able to create an account and log in.
 
 - All API calls must be authenticated
 
 - A user should be able to create, read, update and delete their calorie entry
 
 - A user should have a username, email, password, created_at fields
 
 - Each calorie entry has a date, time, text, and number of calories.
 
 - If the number of calories is not provided, the API should connect to a Calories API provider (for example, [Nutritionix](https://www.nutritionix.com)) and try to get the number of calories for the entered meal.
 
 - Implement foreign key constraints to enforce the relationship between users and calorie entry.
 
 - Use Postgres as the database


 ## About the Calorie Tracker
 These apps help users track their daily caloric intake and also offer insights into nutritional content, exercise routines, and overall health management.

 It uses a method that involves tracking and quantifying the energy content of the foods and beverages we consume.

 This is the main feature of the calorie tracking app, with this feature you can easily log your daily food and beverage intake to monitor your calorie consumption accurately.

 # Notes

 ## Indexing
 For the start, I needed to start numbering the indexes at 1 instead of the usual 0. 
 My research took me to an SQLalchemy module called `Sequence` which takes 2 arguments:
 1. The variable to be indexed `item_id_seq`
 2 The number to start at

 ### Outcome
 The `Sequence` module worked well if there is one and only one table. If there is an additional table, the index will continue where the first table ended in the second table.
 Example if Table_1 ended at index 8 and Table_2 is engaged, first item in Table2 will be 9 is Table_1 ended at 8

 This is not my use case so I discarded this module

 I had to use `autoincrement=True` in the id field of the table. This works very well

 ## Module bcrypt
 The current version of `bcryp` gave an error when hashing the password. 
 
 From the checks in the forum, there is a bug on `passlib` and therefore the version must be maintained at 4.0.1.
 
 This information is found [here](https://github.com/langflow-ai/langflow/issues/1173).

 Command to revert the version of **bcrypt**

 `pip install bcrypt==4.0.1`

 ## Metadata Tags
 These are very nice UI tags used for the routs that display the enpoints

 For this, It is displaying the __two__ main table routes namely
  - _Entries_
  - _Users_
  
 [Metadata Tags](https://fastapi.tiangolo.com/tutorial/metadata/?h=metadata#use-your-tags) link provides a lot of information.

 You can do that by adding the tag name into the decorator parameter like so: 

 ```py
 @api_router.get("/entries", tags=["entries"])
def get_entries_(db: Session = Depends(get_db)):
    entries = db.query(models.Entry).all()
    return entries
 ```

 ### Looks

 #### With tags

 <img src="/assets/tags.png" alt="Tags Showing" width="500" height="350">

 #### Collapsed tags

 <img src="/assets/tag_collapse.png" alt="collapsed tags" width="500" height="350">


## Relationships

### Theory

A relation is used to describe the relationship that exists between tables in a relational database. 

The __relationship__ between two tables presuposses that one one of them has a foreign key that references the primary key of another table.

_One-to-many_ is when one record in Table_1 is related to one or more records in Table_2. The reverse is `False`. One record in Table_2 cannot be related to more than one record in Table_1.

__How to:__ For one city, we could have many different customers located in it. And the other way around — For one customer, we can have only one city it’s located in.

__Example__: **Customer and City**
Storing a list of all customers in the database
For each customer, we want to store their city of location
__Fact is__ A customer will be in exactly __one__ city.

__Current Case : Calory Entry__
A user can make many entries. For every entry, there is _one_ user

Some key terms to be searched from the __[SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/relationship_api.html#sqlalchemy.orm.relationship)__ website. The compiled document is on the [FASTapi relation section](https://fastapi.tiangolo.com/tutorial/sql-databases/). These are

- relationship

- Foreign Key

#### Steps


## Security

### OAuth2 with Password and Hashing

- [Link Here](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

#### Verifying the Hashed Password.

In the `hashing.py` module, the method `verify()` needs to be created in the `class Hash:`

In here, `hashed_password` and `plain_password` are passed as positional parameters.

These parameters are __interchanged__ in the `.verify()` module in this way:

```py
def verify(hashed_password, plain_password):
    return pwd_context.verify(plain_password, hashed_password)
```
Back in the Authentication decorator, existing password in the table comes before the requested password like so:

```py
if not Hash.verify(user.password, request.password):
```

### JWT - JSON Web Tokens

It's a standard to codify a JSON object in a long dense string without spaces.

It is not encrypted, so, anyone could recover the information from the contents.

But it's signed. So, when you receive a token that you emitted, you can verify that you actually emitted it.

That way, you can create a token with an expiration of, let's say, 1 week. And then when the user comes back the next day with the token, you know that user is still logged in to your system.

After a week, the token will be expired and the user will not be authorized and will have to sign in again to get a new token. And if the user (or a third party) tried to modify the token to change the expiration, you would be able to discover it, because the signatures would not match.


