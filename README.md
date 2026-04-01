
# API Ethics Assignment

## Project Overview

This repository contains solutions for the **API Ethics Assignment**,
which focuses on responsible handling of Personally Identifiable
Information (PII) and ethical use of public APIs in a healthcare data
environment.

The project demonstrates how a data analyst should:

-   Identify and classify PII
-   Apply anonymization and masking techniques
-   Follow ethical data-sharing practices
-   Secure API credentials
-   Respect API Terms of Service (TOS)
-   Implement responsible data collection

This assignment simulates a real-world healthcare data workflow where
sensitive patient data must be prepared safely before sharing with an
external research partner.

------------------------------------------------------------------------

## Repository Structure

api-ethics-assignment/

├── README.md\
├── answers.md

------------------------------------------------------------------------

## Tasks Completed

### Task 1 --- Classify and Handle PII Fields

The dataset fields were analyzed and categorized into:

-   Direct PII
-   Indirect PII
-   Sensitive Health Data

Privacy protection techniques applied:

-   Drop --- Remove unnecessary direct identifiers
-   Mask --- Reduce precision of identifying fields
-   Pseudonymize --- Replace identifiers with secure hashes
-   Generalize --- Convert detailed values into broader categories

------------------------------------------------------------------------

### Task 2 --- Audit the API Script for Ethical Compliance

Two ethical and security violations were identified:

1.  Hardcoded API Key
2.  Excessive Data Collection and Storage

Solutions implemented:

-   Use environment variables for secure API keys
-   Limit number of API requests
-   Add rate limiting
-   Store only cleaned data
-   Follow data minimization principles

------------------------------------------------------------------------

## Technologies Used

-   Python
-   pandas
-   requests
-   hashlib
-   GitHub

------------------------------------------------------------------------

## Skills Demonstrated

-   Data Privacy and Protection
-   Ethical API Usage
-   Secure Coding Practices
-   Data Anonymization
-   Compliance Awareness
-   Responsible Data Handling

------------------------------------------------------------------------

## How to Run the Anonymization Script

Install dependencies:

pip install pandas

Run your Python script:

python anonymize_data.py

------------------------------------------------------------------------

## Author

Name: Sundaravinayagam G
Role: Data Analyst Student\
Project: API Ethics Assignment

------------------------------------------------------------------------

## License

This project is created for educational purposes only.

