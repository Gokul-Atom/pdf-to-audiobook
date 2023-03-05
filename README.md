# PDF to Audiobook
This app extracts text from PDF file and the extracted text can be modified for correction. This modified text can then be saved as mp3 file.

![](https://img.shields.io/badge/python-v3.9.5-blue) ![](https://img.shields.io/badge/PyPDF2-v3.0.1-darkgreen) ![](https://img.shields.io/badge/Pyttsx3-v2.90-darkgreen)

## Technologies Used
### Languages Used
* Python 3.9.5

### Modules Used
* Sys
* Tkinter
* PyPDF2 3.0.1
* Pyttsx3 2.90

## Modules Installation
**PyPDF2** and **pyttsx3** are not pre-installed with python.

To install these modules, type the following commands in terminal.

```
pip install pypdf2==3.0.1
```
```
pip install pyttsx3==2.90
```
or use the **requirements.txt** file.
```
pip install -r requirements.txt
```

## Instructions
* **Run** the program.
* A new window will be opened.

![](https://github.com/Gokul-Atom/pdf-to-audiobook/blob/main/Screenshots/screenshot%2001.png)

* This window shows the **currently selected voice** and the **play demo** button.
* Expanding the currently selected voice shows the list of available voices in system.

![](https://github.com/Gokul-Atom/pdf-to-audiobook/blob/main/Screenshots/screenshot%2002.png)

* Click **Open File** button to open the PDF file.

![](https://github.com/Gokul-Atom/pdf-to-audiobook/blob/main/Screenshots/screenshot%2003.png)

* Once the PDF file is opened, the **Extract Text** button is displayed.

![](https://github.com/Gokul-Atom/pdf-to-audiobook/blob/main/Screenshots/screenshot%2004.png)

* Click **Extract Text** button to extract text from the PDF file.

![](https://github.com/Gokul-Atom/pdf-to-audiobook/blob/main/Screenshots/screenshot%2005.png)

* The text from the PDF file is now extracted and displayed.
* The extracted text can be modified by editing it directly in the window.
* Once necessary changes are made, click **Save Audiobook** to save as **mp3 file**.

![](https://github.com/Gokul-Atom/pdf-to-audiobook/blob/main/Screenshots/screenshot%2006.png)

* **Close** the window to close the app and **terminate** the program.

## License
This repository is licensed under **GNU General Public License** family.

![](https://img.shields.io/badge/License-GPL-color)
