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
  * **Dependencies**: `mysql.connector`, `requests`, `smtplib`, `re`

## Architecture Overview

The system follows a multi-tiered architecture to ensure separation of concerns and maintainability.

  * **Presentation Layer**: Handles all user interactions via web browsers, rendering Flask templates.
  * **Application Layer**: The core Flask application manages all business logic, handles user/admin requests, and orchestrates interactions with other specialized modules.
  * **Data Layer**: A MySQL database serves as the central repository for all persistent application data.

Here is a high-level component diagram illustrating the system's architecture:

```
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
         |         |   Flask Backend   |<--------------------->| Database Connector  |       |
         |         | - Core Logic      |            |         | (mysql.connector)   |       |
         |         | - API Endpoints   |            |         +---------+-----------+       |
         |         +---------+---------+            |                   | SQL                 |
         |                   |                        |                   |                     |
         |                   | Calls Modules          |                   v                     |
         |                   |                        |         +-----------------------+     |
         |        +----------+----------+             |         |  Loan Verification DB   |     |
         |        | Face Recognition    |             |         | (Tables: regtb, loantb, |     |
         |        | (Luxand FaceSDK)    |             |         |   temptb, etc.)       |     |
         |        +---------------------+             |         +-----------------------+     |
         |                   |                        |
         |                   |                        |
         |        +----------+----------+             |
         |        |     OCR Module      |             |
         |        | (EasyOCR, OpenCV)   |             |
         |        +---------------------+             |
         |                   |                        |
         |                   |                        |
         |        +----------+----------+             |
         |        |  Email/SMS Notif.   |<--------------------+--------------------+
         |        |  (smtplib, requests)|             |       | External APIs      |
         |        +---------------------+                     | (Email/SMS Gateways) |
         |                                                    +--------------------+
```

## Setup & Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

  * **Python 3.x**: Ensure Python is installed (preferably 3.8+).
  * **MySQL Server**: A running MySQL database instance.
  * **Windows OS**: The Luxand FaceSDK integration (via `win.py` and `ctypes`) requires a Windows operating system for the face recognition module to function correctly.
  * **Internet Connection**: Required for SMS and Email notification functionalities.

### 1\. Database Setup

1.  Create a new MySQL database named `1loanverficationdb`.
    ```sql
    CREATE DATABASE 1loanverficationdb;
    ```
2.  Import the provided SQL schema:
    ```bash
    mysql -u root -p 1loanverficationdb < 1loanverficationdb.sql
    ```
    *(Note: The project's code currently uses 'root' with no password for the MySQL connection. For production environments, it's crucial to use a dedicated database user with a strong password and restrict privileges.)*

### 2\. Python Dependencies

Navigate to the project root directory and install the required Python packages:

```bash
pip install Flask mysql-connector-python easyocr opencv-python requests
```

### 3\. Luxand FaceSDK Integration (Windows Specific)

1.  Download and install the **Luxand FaceSDK** for Windows from their official website.
2.  Ensure the `fsdk.dll` (or equivalent library files) and its Python wrapper are accessible to your Python environment. This typically involves placing them in your system's PATH or directly in the project directory where `LiveRecognition.py` is located.
3.  **License Key**: The license key is hardcoded in `LiveRecognition.py` and `LiveRecognition1.py`. Replace the placeholder key with your valid Luxand FaceSDK license key.

### 4\. Configure Email & SMS (Optional but Recommended)

  * **Email**: In `App.py` and `LiveRecognition1.py`, update the `fromaddr` and the app-specific password for the SMTP configuration to use your own email service (e.g., Gmail with an app password).
  * **SMS**: The `sendmsg` function in `App.py` uses `http://sms.creativepoint.in/api/push.json`. You will need to obtain an API key and register with this or a similar SMS gateway provider and update the code accordingly.

### 5\. Running the Application

From the project root directory, execute the Flask application:

```bash
python App.py
```

The application should now be accessible in your web browser at `http://127.0.0.1:5000` (or `localhost:5000`).

## Usage

  * **Admin Login**: Navigate to `/AdminLogin`. (Check `1loanverficationdb.sql` for default admin credentials if any).
  * **User Login/Registration**: Navigate to `/UserLogin` or `/NewUser`. Follow the prompts for registration, which will involve live face verification.
  * Explore the various functionalities for loan application, status tracking, and admin management.

## Future Enhancements

  * **Containerization**: Implement Docker for easier deployment and environment consistency.
  * **Cloud Deployment**: Deploy the application on a cloud platform (AWS, Azure, GCP).
  * **Enhanced Security**: Implement environment variables for sensitive credentials (database, API keys) instead of hardcoding. Add robust input validation and error handling.
  * **Improved UI/UX**: Modernize the frontend design for a more intuitive user experience.
  * **Testing**: Implement unit and integration tests for core functionalities.
  * **API for External Services**: Develop a RESTful API for external systems to interact with the loan management system.
  * **Robust Logging**: Implement a comprehensive logging strategy.

## Contribution

Contributions are welcome\! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-source. Please refer to the `LICENSE` file for details.
*(If you don't have a LICENSE file, consider adding one, e.g., MIT, Apache 2.0.)*
