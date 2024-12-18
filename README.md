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
- POST `/import/` - Import accounts from a CSV/JSON/XSLX file.
<p align="center">
  <div>
    <strong>Import CSV</strong><br /> 
    <img src="https://github.com/user-attachments/assets/d393c15e-00e2-4487-a4d0-1c8f13e2fed6" width="600" /> <br /> <br /> 
  </div>
  <div>
    <strong>Import JSON</strong><br />
    <img src="https://github.com/user-attachments/assets/e8f0fa98-2107-47f1-8161-3a1b7d08e88c" width="600" /> <br /> <br />
  </div>
  <div>
    <strong>Import XSLX</strong><br />
    <img src="https://github.com/user-attachments/assets/aaa4039b-4062-4a52-bc11-b19c9fc4afe2" width="600" /> <br /> <br />
  </div>
</p>


- GET `/accounts/` - View all accounts.
  **Note:** You need to import a file first to be able to view accounts
  ![Screenshot (68)](https://github.com/user-attachments/assets/ad11cdef-a019-44ac-acc3-af0d6e6208c4)


- GET `/accounts/{id}/` - View account by ID.
  
  ![Screenshot (75)](https://github.com/user-attachments/assets/dcc314c2-94bf-425b-8017-6fc9b4ef75cb)


- POST `/transfer/` - Transfer funds between accounts.
![Screenshot (76)](https://github.com/user-attachments/assets/987e1989-3319-4868-aab7-8142303f7c77)

![Screenshot (80)](https://github.com/user-attachments/assets/a574b89c-d850-4364-be53-8c3079caa690)

![Screenshot (78)](https://github.com/user-attachments/assets/891e857f-7030-4335-953a-b10a2070ba00)

![Screenshot (79)](https://github.com/user-attachments/assets/42005e25-c289-4764-af4b-409e7d4d2231)


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

