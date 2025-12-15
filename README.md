# Pixela UI Desktop

A desktop GUI application for [Pixela](https://pixe.la/) - a habit tracking service that lets you create graphs and record your daily activities.

## 📋 Overview

Pixela UI Desktop provides a simple, easy-to-use graphical interface to interact with the Pixela API. Track your habits, create custom graphs, and manage your progress all from a desktop application built with Python and CustomTkinter.

## ✨ Features

- **User Management**
  - Create new Pixela accounts
  - Login with existing credentials

- **Graph Management**
  - Create new habit tracking graphs
  - Delete existing graphs
  - Customize graph properties:
    - Name and ID
    - Unit of measurement
    - Data type (int or float)
    - Color themes (shibafu, momiji, sora, ichou, ajisai, kuro)
    - Timezone configuration

- **Progress Tracking**
  - Submit daily progress for your habits
  - Remove progress entries
  - Date picker for easy date selection
  - Visual feedback for all operations

## 🔧 Requirements

- Python 3.7 or higher
- Internet connection for API communication

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hamzaband4/Pixela-UI-Desktop.git
   cd Pixela-UI-Desktop
   ```

2. **Create a virtual environment and activate it**

   **For Linux/macOS:**
   ```bash
   python -m venv <your-venv-name>
   source your-venv-name/bin/activate
   ```
   Example
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   **For Windows:**
   ```bash
   python -m venv <your-venv-name>
   your-venv-name\Scripts\activate
   ```
   Example
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
5. **Install CTkDatePicker**

   **For Linux/macOS:**
   ```bash
   git clone https://github.com/hamzaband4/CTkDatePicker.git
   mv CTkDatePicker/CTkDatePicker path/to/your-venv/lib/your-python-version/site-packages/
   ```
   Example
   ```bash
   git clone https://github.com/hamzaband4/CTkDatePicker.git
   mv CTkDatePicker/CTkDatePicker .venv/lib/python3.13/site-packages/
   ```

   **For Windows:**
   ```bash
   git clone https://github.com/hamzaband4/CTkDatePicker.git
   move CTkDatePicker\CTkDatePicker path/to/your-venv\Lib\site-packages\
   ```
   Example
   ```bash
   git clone https://github.com/hamzaband4/CTkDatePicker.git
   move CTkDatePicker\CTkDatePicker .venv\Lib\site-packages\
   ```

## 🚀 Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Login screen:**
   - Enter the required credentials:
     - A username
     - A token (minimum 8 characters)
   - If you don't have an account, click "Sign up". A new account will be created with the credentials you have provided
   - If you have an existing account, simply click "Login"

3. **Managing graphs:**
   - **Create New Graph:** Set up a new habit tracker with custom settings
   - **Delete Graph:** Remove a graph you no longer need
   - **Submit Progress:** Record your daily activity for a specific graph
   - **Remove Progress:** Delete a progress entry for a specific date

## 📚 Application Structure

```
Pixela-UI-Desktop/
├── main.py           # Entry point - launches the application
├── ui.py             # User interface components and main window
├── actions.py        # API interactions with Pixela service
├── requirements.txt  # Python dependencies
└── LICENSE          # MIT License
```

## 🔑 Key Components

- **main.py**: Application entry point that initializes the interface
- **ui.py**: Contains the `Interface` class with all UI components:
  - Login/Signup window
  - Graph creation and deletion dialogs
  - Progress submission and removal forms
- **actions.py**: Handles all API communications with Pixela:
  - User authentication
  - Graph operations
  - Pixel (progress) management
  - Internet connection checking

## 🎨 Color Options

When creating a graph, you can choose from the following color themes:
- **shibafu** (green) - Default theme
- **momiji** (red) - Autumn leaves
- **sora** (blue) - Sky
- **ichou** (yellow) - Ginkgo
- **ajisai** (purple) - Hydrangea
- **kuro** (black) - Black

## 🌐 About Pixela

[Pixela](https://pixe.la/) is a habit tracking service that uses GitHub-style graphs to visualize your progress. It's perfect for tracking:
- Exercise routines
- Reading habits
- Coding practice
- Language learning
- Any daily activity you want to measure

## 🛠️ Dependencies

The application uses the following main libraries:
- **customtkinter** - Modern UI components
- **CTkMessagebox** - Dialog boxes and alerts
- **CTkDatePicker** - Date selection widget
- **requests** - HTTP requests to Pixela API
- **ipapi** - Automatic timezone detection

## ⚠️ Important Notes

- Keep your token secure - it's like a password for your Pixela account
- Minimum token length is 8 characters
- Internet connection is required for all operations
- Your data is never shared or saved
- CTkDatePicker in this project is a forked and modified version of the original [CTkDatePicker](https://github.com/maxverwiebe/CTkDatePicker) thanks to [maxverwiebe](https://github.com/maxverwiebe)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**hamzaband4**

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/hamzaband4/Pixela-UI-Desktop/issues).

## 🙏 Acknowledgments

- [Pixela API](https://docs.pixe.la/) - The habit tracking service
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI framework
- [CTkDatePicker](https://github.com/maxverwiebe/CTkDatePicker) - Original CTkDatePicker module
- All the open-source libraries that made this project possible

## 📧 Support

If you have any questions or need help, please open an issue on GitHub.

---

Made with ❤️ for habit tracking enthusiasts
