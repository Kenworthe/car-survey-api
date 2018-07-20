# To do: 

- on front end: 
  - import jquery
  - add a "form" which lets you POST
  - write jquery code that takes JSON response and edits DOM (html page) depending on response.

- on back end: 
  - open API to receive POST
  - process logic upon receiving POST
  - return next question JSON to front end
  - OR return final answer jSON to front end.

# To run: 
- start mongodb with `mongod`
- run `python3 app.py`

# To run with Docker: 
`docker build -t car-survey-api`  

`docker run -p 5000:5000 car-survey-api`  

Then navigate to 0.0.0.0:5000  