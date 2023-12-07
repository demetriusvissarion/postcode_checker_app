# (Broken) Postcode Checker app

This web application is broken. You have three objectives:

* Find the bugs and fix them.
* You need to get **all the tests passing**.
* You need to **run the app manually with your browser** and make sure it works.
  You can have a look at the user stories below to understand how the program is
  expected to behave (without bugs).

Start by setting up the project and running the tests.

> **Warning**  
> We've made this one a bit more realistic — you can no longer entirely trust
> the tests. You'll need to ensure you understand the behaviour of the
> application and how it should work.

<details>
  <summary>:speech_balloon: Can I have some extra challenge?</summary>

  After finding and addressing the bugs, try to work out what mistakes the
  original engineer made in the way they went about their work. 
  
  What changes could you make to the way this program is built in order to help
  future engineers avoid making the same mistakes?

</details>

## Setup

Clone this repository and enter this directory.

```shell
# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# To run the tests
; pytest

# To run the app
; python app.py
# Visit http://localhost:5001/ in your browser
```

## User stories

Note that these user stories are **already implemented** by the app — they're here as guidance for you to understand what the program is about and how it should behave when correct.

```
As a Maker,
I would like to enter a postcode on the homepage
And see whether it is valid or not on a result page.

As a Maker,
I would like to click on a link on the result page
So I can go back on the homepage.
```

