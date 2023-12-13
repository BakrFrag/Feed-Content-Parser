## RSS Feed Parser 
REST API for extracting content from user submitted URL and parse RSS feed items

### Database & Schema Design 
- ![Schema Design](./schema.png)
- 3 entities as the following 
   - `User` for register user with their encrypted passwords 
   - `FeedURL` for store feed URL object with attributes like `id , url , number_of_parsed and last_parsed_datetime' 
   - `FeedContent` keep track of parsed content from feed url , include attributes as `id , url_id , title , description , link , publish_date`
   
- Relations 
     - their relations between `FeedURL` have one-to-many relation with `FeedContent` 

#### Business Logic 
- user must be register 
- every request must include `JWT Bearer Token` in `Authorization` Header for http request 
- if token is valid , start parse submitted URL
- check if URL is valid  , start parse url and extract Feed Content data 
- if exception happen while parse like `internet connection` or `rss feed content can't be parsed` , exception with `400 Bad Request` 
- if submitted url already exists , check if `last_parsed_datetime` within 10 minutes , them return content direct from database 
- if more than 10 minutes start parse rss feed url , remove feed content attached with url and insert new feed content items in database and increase the field `number_of_parsed` by 1 
- if the submitted url is not exists , then start parse and add feed url and feed content store in DB 
#### API End Point 
| URL | HTTP Method   |Description|
|--|--|--|
|  http://127.0.0.1:8000/user/add/|POST  |register new user with username & password|
|http://127.0.0.1:8000/user/login/|POST| login user and return access token valid for 10 minutes|
|http://127.0.0.1:8000/rss/parse/|POST|Submit url for parse and get rss items data|
|http://127.0.0.1:8000/rss/parse/|GET|list submitted url data|
|http://127.0.0.1:8000/rss/parse/{id}|GET|get list of feed content attached to feed url id |
|http://127.0.0.1:8000/docs| GET| Docs for app|

#### API Testing 
- for various request response cycle and different responses in different testcases
- check attached postman collection , you can directly loaded it direct in postman 
- Link : https://api.postman.com/collections/6749950-7b38a061-4741-4f1f-a71e-ae78c1e8b55b?access_key=PMAT-01HHGZ7VXXDA8QK9SWVMVH6RKQ

#### Tech Stack 
1. `Python` Programming language 
2. `FastAPI` as backend framework 
3. `feedparser` for rss feed 
4. `uvicorn` as asgi server 
5. `Sqlite3` as Database 
6. `pipenv` as virtual environment tool


#### Build & Run 
this will assume that you have a machine with internet connection and python interpreter and git as version control 
1. clone project from GITHUB 
    -  `git clone https://github.com/BakrFrag/Feed-Content-Parser`
2. move to clone directory 
    - `cd Feed-Content-Parser`
    
3. activate virtual env 
    - `pipenv shell`
    - if `pipenv` not installed , simply run `pip install pipenv`
4. install requirements 
    - `pipenv install -r requirements.txt` 
 5. move and run app 

    - `uvicorn app.main:app --reload`
5. start play with API 




