# TNP Playwright Framework

A small Playwright + pytest framework. This version contains only the pieces
needed for login, with a working example that tests the login page of
https://www.saucedemo.com

## Folder structure

```
tnp_playwright_framework/
│
├── framework/                  # Reusable actions. No app ids here.
│   ├── __init__.py
│   ├── element_actions.py      # clear_and_fill, click_element, is_element_visible
│   ├── navigation_actions.py   # open_url, get_current_url, get_page_title
│   └── message_actions.py      # get_validation_message
│
├── config/
│   ├── __init__.py
│   └── config.py               # Framework defaults (timeout)
│
├── examples/                   # Sample project: Sauce Demo login
│   ├── pages/
│   │   ├── __init__.py
│   │   └── login_page.py       # Real ids of the site + login() flow
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py         # Opens the login page before each test
│   │   └── test_login.py       # 4 login tests
│   └── pytest.ini              # Test settings
│
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

## How it works

```
test_login.py  ->  login_page.py  ->  framework functions  ->  browser
(checks result)    (real ids, flow)   (fill, click, read)
```

- **framework/** has generic actions. They take a locator and do one thing.
- **pages/login_page.py** has the real ids of Sauce Demo and builds `login()`
  by calling the framework actions.
- **tests/test_login.py** calls `login()` and uses `assert` to check the result.

If the site changes a button id, you only fix `login_page.py`.

## Step-by-step setup

You need **Python 3.9 or newer**. Check with:

```
python --version
```

**Step 1: Unzip and open the folder**

Unzip `tnp_playwright_framework.zip`, then open a terminal in the
`tnp_playwright_framework` folder (or open the folder in VS Code / PyCharm and
use its terminal).

**Step 2: Create a virtual environment** (keeps the libraries for this project separate)

```
python -m venv .venv
```

**Step 3: Activate it**

Windows:
```
.venv\Scripts\activate
```

Mac / Linux:
```
source .venv/bin/activate
```

You should now see `(.venv)` at the start of the terminal line.

**Step 4: Install the libraries**

```
pip install -r requirements.txt
```

**Step 5: Install the browser** (only needed once)

```
playwright install chromium
```

**Step 6: Go to the examples folder**

```
cd examples
```

**Step 7: Run the tests**

```
pytest
```

To watch the browser while the tests run:

```
pytest --headed
```

To run only one test:

```
pytest -k test_valid_login
```

## Expected result

```
tests/test_login.py::test_valid_login[chromium] PASSED
tests/test_login.py::test_invalid_login[chromium] PASSED
tests/test_login.py::test_empty_username_and_password[chromium] PASSED
tests/test_login.py::test_empty_password[chromium] PASSED
```

If a test fails, a screenshot is saved in `examples/test-results/`.

## The test cases

| Test | Username | Password | Expected |
| --- | --- | --- | --- |
| test_valid_login | standard_user | secret_sauce | Goes to the inventory page |
| test_invalid_login | standard_user | wrong_password | "Username and password do not match..." |
| test_empty_username_and_password | (empty) | (empty) | "Username is required" |
| test_empty_password | standard_user | (empty) | "Password is required" |

The Sauce Demo credentials are public and shown on the site's login page.

## Common problems

- **`Executable doesn't exist` / browser not found**: run `playwright install chromium`.
- **`ModuleNotFoundError: No module named 'framework'` or `'pages'`**: make sure
  you ran `pytest` from inside the `examples` folder.
- **`pip` or `python` not found**: try `python3` and `pip3` instead.

## Adding your own project

Create your own `pages/`, `tests/` and `pytest.ini`, the same way as in
`examples/`. Put your app's ids in your page files and call the framework
functions from there. Never put app ids, URLs or passwords inside `framework/`.
