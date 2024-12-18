# Django Fund Transfer Web Application

This Django-based web application facilitates transferring funds between accounts. It also supports importing accounts via CSV/JSON/XSLX, viewing accounts, getting account details, and performing fund transfers. Below is the documentation for how to run the app, interact with the API routes, and use the import feature.

## Features

- **Import Accounts**: Import account details from CSV/JSON/XSLX files either via an API route or command line.
- **View Accounts**: View a list of all accounts and their balances.
- **List Account Detail** View account detail by account ID
- **Transfer Funds**: Transfer funds between accounts.

---

## API Routes

### 1. Import Accounts
- **Route:** `/import/`  
- **Method:** `POST`  
- **Description:** This endpoint allows you to import accounts from a CSV/JSON/XSLX file.

**CSV Format Example:**
| account_number | holder_name   | balance |
|----------------|---------------|---------|
| 12345          | John Doe      | 500.00  |
| 67890          | Alice Smith   | 300.00  |


### 2. View Accounts
- **Route:** `/accounts/`
- **Method:** `GET`
- **Description:** Retrieve a list of all accounts with their details, such as account number, holder name, and balance.

### 3. View Account by ID
- **Route:** `/accounts/{id}/`
- **Method:** `GET`
- **Description:** Retrieve the details of a specific account using its account ID.

### 4. Transfer Funds
- **Route:** `/transfer/`
- **Method:** `POST`
- **Description:** Initiate a transfer of funds between two accounts.


## Running the Application With Docker Compose
### 1. Clone the repository:

`git clone https://github.com/salmaelsayed15/account_transfer.git`
`cd account_transfer`

### 2. Build and start the application using Docker Compose:

`docker-compose up --build`

### 3. Open your browser and navigate to:

http://localhost:8000/

### 4. Access the following routes in your browser or use an API testing tool (e.g., Postman):
- POST /import/ - Import accounts from a CSV/JSON/XSLX file.
- ![Screenshot (70)](https://github.com/user-attachments/assets/152e1ad2-2115-4635-a04b-d0fe0e99c281)

- GET /accounts/ - View all accounts.
- GET /accounts/{id}/ - View account by ID.
- POST /transfer/ - Transfer funds between accounts.

### 5. Importing Accounts
You can import accounts using either of these two methods:

#### a. API Route - POST /import/

Send a POST request with a CSV/JSON/XSLX file containing account data to the /import/ route.


#### b. Command Line - python manage.py import_accounts

You can also import accounts directly via the command line by running the following command:

`python manage.py import_accounts your_file.csv`

Replace `your_file.csv` with the path to the CSV file.

## Running Tests
To run the tests for this application, execute the following command:

`python manage.py test`

This will run all test cases to ensure the application is functioning as expected.

