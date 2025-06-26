# Loan Verification & Management System

## Project Overview

This project is a robust, web-based Loan Verification and Management System designed to streamline the loan application, approval, and management processes. It incorporates modern technologies like **biometric facial recognition** for secure user authentication and **Optical Character Recognition (OCR)** for automated document processing, enhancing both efficiency and security in financial transactions.

The system provides separate portals for administrators and users, enabling comprehensive management of loan applications, user registrations, and waiver requests.

## Key Features

* **User Management**: Secure user registration and login with biometric (face) verification.
* **Loan Application**: Users can apply for various loan types through a guided interface.
* **Loan Status Tracking**: Users can monitor the real-time status of their loan applications.
* **Admin Dashboard**: Administrators can review, approve, or reject loan applications and manage user accounts.
* **Biometric Authentication**: Live face recognition (powered by Luxand FaceSDK) for enhanced user verification during registration and potentially other critical actions.
* **OCR for Document Processing**: Automated extraction of key information (e.g., certificate numbers) from scanned documents for processes like loan waivers.
* **Email & SMS Notifications**: Integrated system for sending OTPs and other alerts.
* **Loan Waiver Process**: Functionality for processing loan waivers with document verification.

## Technologies Used

* **Backend**: Python (Flask Framework)
* **Database**: MySQL
* **Biometrics**: Luxand FaceSDK (Python wrapper `fsdk` and `ctypes` for Windows API interaction)
* **OCR**: EasyOCR, OpenCV (`cv2`)
* **Frontend**: HTML, CSS, JavaScript (standard web technologies within Flask templates)
* **Dependencies**: `mysql.connector`, `requests`, `smtplib` (for email), `re` (regex)

## Architecture Overview

The system follows a multi-tiered architecture:

* **Presentation Layer**: User interactions via web browsers, rendering Flask templates.
* **Application Layer**: The core Flask application handles all business logic, user/admin requests, and orchestrates interactions with other modules. It integrates:
    * A dedicated **Face Recognition Module** for biometric operations.
    * An **OCR Module** for document analysis.
    * **Notification Services** for email and SMS.
* **Data Layer**: A MySQL database serves as the central repository for all application data, including user profiles, loan records, and administrative logs.

+-------------------+             +---------------------------------+             +---------------------+
|                   |             |                                 |             |                     |
|  User / Client    |             |       Application Layer         |             |     Data Layer      |
|  (Web Browser)    |             |     (Python Flask App)          |             |   (MySQL Database)  |
|                   |             |                                 |             |                     |
+--------+----------+             +---------------+-----------------+             +---------+-----------+
         | HTTP/S                                   | API Calls / SQL                       |
         |                                          |                                       |
         |                                          |                                       |
         |         +-------------------+            |         +---------------------+       |
         |         |                   |            |         |                     |       |
         |         |   Flask Backend   |<--------------------->| Database Connector |       |
         |         | - Core Logic      |            |         | (mysql.connector)   |       |
         |         | - API Endpoints   |            |         +---------+-----------+       |
         |         +---------+---------+            |                   | SQL               |
         |                   |                      |                   |                   |
         |                   | Calls Modules        |                   v                   |
         |                   |                      |         +-----------------------+     |
         |        +----------+----------+           |         |  Loan Verification DB |     |
         |        | Face Recognition    |           |         | (Tables: regtb, loantb,|    |
         |        | (Luxand FaceSDK)    |           |         |   temptb, etc.)       |     |
         |        +---------------------+           |         +-----------------------+     |
         |                   |                      |
         |                   |                      |
         |        +----------+----------+           |
         |        |     OCR Module      |           |
         |        | (EasyOCR, OpenCV)   |           |
         |        +---------------------+           |
         |                   |                      |
         |                   |                      |
         |        +----------+----------+           |
         |        |  Email/SMS Notif.   |<--------------------+--------------------+
         |        |  (smtplib, requests)|           |         | External APIs        |
         |        +---------------------+                     | (Email/SMS Gateways) |
         |                                                    +--------------------+



## Setup & Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* **Python 3.x**: Ensure Python is installed (preferably 3.8+).
* **MySQL Server**: A running MySQL database instance.
* **Windows OS**: The Luxand FaceSDK integration (via `win.py` and `ctypes`) requires a Windows operating system for the face recognition module to function correctly.
* **Internet Connection**: Required for SMS and Email notification functionalities.

### 1. Database Setup

1.  Create a new MySQL database named `1loanverficationdb`.
    ```sql
    CREATE DATABASE 1loanverficationdb;
    ```
2.  Import the provided SQL schema:
    ```bash
    mysql -u root -p 1loanverficationdb < 1loanverficationdb.sql
    ```
    *(Note: The project's code currently uses 'root' with no password for the MySQL connection. For production environments, it's crucial to use a dedicated database user with a strong password and restrict privileges.)*

### 2. Python Dependencies

Navigate to the project root directory and install the required Python packages:

```bash
pip install Flask mysql-connector-python easyocr opencv-python requests
