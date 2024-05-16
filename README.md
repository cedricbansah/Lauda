# Lauda Fleet Management System

Welcome to Lauda Fleet Management System, a Django web application designed to streamline and manage your fleet operations efficiently. Lauda offers a comprehensive suite of features including Chartjs graphs for vehicle information visualization, user authentication with a login screen for drivers/users, email verification for new driver accounts, importing vehicles using Excel, and exporting data to Excel and PDF formats.

## Features

1. **Chartjs Graphs**: Visualize vehicle information such as mileage, fuel consumption, and maintenance schedules with interactive Chartjs graphs.

2. **User Authentication**: Secure login screens for drivers and users ensure that only authorized personnel can access the system.

3. **Email Verification**: New driver accounts are verified via email to ensure authenticity and security.

4. **Excel Import**: Easily import vehicles and their details into the system using Excel spreadsheets, streamlining the setup process.

5. **Export to Excel and PDF**: Export your fleet data to Excel and PDF formats for easy sharing and analysis.

## Installation

To get started with Lauda Fleet Management System, follow these steps:

1. Clone the repository (production branch):

   ```bash
   git clone https://github.com/cedricbansah/lauda-fleet-management.git
   ```

2. Navigate into the project directory:

   ```bash
   cd lauda-fleet-management
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your web browser and navigate to `http://localhost:8000` to access Lauda Fleet Management System.

## Usage

Once the application is running, you can perform the following actions:

- Log in with your credentials to access the dashboard.
- View Chartjs graphs for vehicle information.
- Import vehicle data using Excel spreadsheets.
- Export fleet data to Excel and PDF formats.
- Manage user accounts and permissions.

## Contributing

Contributions to Lauda Fleet Management System are welcome! If you have any ideas, suggestions, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Chartjs - for providing an excellent charting library.
- Django - for making web development in Python simple and efficient.
- Tailwind CSS - for the responsive design components.

## Contact

For any inquiries or support, please contact [cedibans@gmail.com](mailto:cedibans@gmail.com).

Thank you for choosing Lauda Fleet Management System! I hope it helps streamline your fleet operations.
