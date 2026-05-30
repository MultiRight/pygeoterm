# PyGeoterm

A terminal-based geometric area calculator written in Python.

---

## Description

PyGeoterm is a lightweight command-line tool that allows users to calculate the area of common geometric shapes directly from the terminal. It is designed to be simple, interactive, and accessible to anyone who needs quick geometric computations without relying on external tools or graphical interfaces.

---

## Features

- Calculate the area of six geometric shapes:
  - Square
  - Rectangle
  - Triangle
  - Circle
  - Parallelogram
  - Trapezoid
- Color-coded terminal output for better readability
- Built-in error handling with descriptive error codes
- Interactive session with reset and exit options
- No external dependencies beyond the Python standard library

---

## Requirements

- Python 3.x

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MultiRight/PyGeoterm.git
cd PyGeoterm
```

---

## Recommendation

PyGeoterm is best run on a Linux system. Linux handles terminal colors and interactive input more reliably than Windows, which may display ANSI color codes incorrectly depending on the terminal used. If you are on Windows, consider using WSL (Windows Subsystem for Linux) for the best experience.

---

## Usage

Run the script with Python:

```bash
python PyGeoterm.py
```

> **Tip:** If `python` does not work, try:
> ```bash
> python3 PyGeoterm.py
> ```

Once launched, follow the on-screen prompts to select a geometric shape and enter the required dimensions. The program will output the calculated area.

To display the help information:

```bash
--help
```

At the end of each session, type `reset` to restart or `exit` to quit the program.

---

## Error Codes

| Code   | Description                                                        |
|--------|--------------------------------------------------------------------|
| err101 | Invalid input — letters or symbols were entered instead of numbers |
| err102 | Invalid shape — the selected choice is not in the geometric menu   |
| err103 | Invalid action — the input is neither `reset` nor `exit`           |

---

## License

This project is licensed under the **GNU General Public License v3.0**.

---

## Author

**MultiRight**
GitHub: [https://github.com/MultiRight](https://github.com/MultiRight)

---

## Repository

Repository: [https://github.com/MultiRight/PyGeoterm](https://github.com/MultiRight/PyGeoterm)

---

## Copyright

Copyright (C) 2026 [MultiRight](https://github.com/MultiRight)

---

## 🐱 Special Thanks

A special thanks to mimi — the legendary, the great, the gentle cat.
