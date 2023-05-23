# Readme MinimalTube

# MinimalTube

This app offers a minimalist design and allows users to easily download YouTube videos. With its user-friendly interface, users can quickly input the video link and initiate the download process. It provides a clean and efficient experience for saving YouTube videos on their devices.

---

---

## Features

- Allows you to download videos from YouTube for offline viewing.
- Choose the desired video quality for the download (360p, 720p).
- Provides an easy-to-use interface, delivering a pleasant user experience.

---

![image (4).png](https://res.craft.do/user/full/99febbde-991f-0e46-0b3e-2ef8a021c90f/doc/73E9FBC4-E445-4167-94D1-0B9A86E7FDCA/e0623256-2c51-4025-8d65-9e1716b70bb0)

---

## Requirements

To run the application, you need to have Python 3 installed and the following libraries:

[⬛️](https://www.python.org/)  `Python`

[🔳](https://pypi.org/project/Pillow/)  `Pillow`

[🟩](https://github.com/pytube/pytube)  `Pytube`

[🟥](https://github.com/TomSchimansky/CustomTkinter)  `Custom Tkinter`

⬜  `tkinter, os and webbrowser`

---

## Usage

1. Clone the `REPOSITORY` or `DOWNLOAD` the application.
2. Install the required libraries with the following commands:

![image (5).png](https://res.craft.do/user/full/99febbde-991f-0e46-0b3e-2ef8a021c90f/doc/73E9FBC4-E445-4167-94D1-0B9A86E7FDCA/ee69b02f-32fd-4574-a4d0-e325dade6aa4)

> ❗ To use the themes, it is necessary to clone the repository on your machine

3. Choose your theme (standard, reddish, forest, cappuccino)
4. Open the (`main.py`) file and modify this line of code:

![image.png](https://res.craft.do/user/full/99febbde-991f-0e46-0b3e-2ef8a021c90f/doc/73E9FBC4-E445-4167-94D1-0B9A86E7FDCA/848ed8f7-b3bf-46ec-992f-e7a23d15f40c)

5. Now, just run your application and enjoy! ✨

---

## Customization

This project can be customized to your liking. If you didn't like any of the available themes, feel free to customize it your own way!

+ ⚙️ Used settings
   - Open the project folder and navigate to `themes > standard.json` then make a copy of this file.
   - Now you can edit each parameter as desired.
   - Here are some parameters that I usually edit (the first color refers to the **light mode** and the second color to the **dark mode**).

```other
{
  "CTkButton": {
    "corner_radius": 10,
    "fg_color": ["blue", "blue"],
    "hover_color": ["gray", "gray"],
    "border_color": ["gray", "gray"],
  },
  "CTkEntry": {
    "corner_radius": 10,
    "fg_color": ["red", "red"],
    "border_color": ["white", "white"],
  },
```

---

## Contributing

If you want to contribute to this project, open a new issue to discuss your idea or submit a pull request with the proposed changes.

## Credits

This project was developed by me and uses **pytube** as a data source.

?descriptionFromFileType=function+toLocaleUpperCase()+{+[native+code]+}+File&mimeType=application/octet-stream&fileName=Readme+MinimalTube.md&fileType=undefined&fileExtension=md