<h1 align="center">MinimalTube</h1>

<h3 align="center">
	<img src="https://github.com/Dimitri-Matheus/Dimitri-Matheus/assets/121637762/03ec39d0-9d1a-44cd-ba83-825681a44c3f" width="250" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	This app offers a minimalist design and allows users to easily download YouTube videos. With its user-friendly interface, users can quickly input the video link and initiate the download process. It provides a clean and efficient experience for saving YouTube videos on their devices.
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

---

## Previews
<details>
<summary>🌙 Dark mode </summary>
	<p align="center">
  	<img src="https://github.com/Dimitri-Matheus/MinimalTube/assets/121637762/d84237c1-b699-43fe-b20e-9b9e6f729004"  alt="image 1"/>
	</p>
</details>

<details>
<summary>☀️ Light mode </summary>
	<p align="center">
	<img src="https://github.com/Dimitri-Matheus/MinimalTube/assets/121637762/fdc5df48-715b-49c6-8a55-89da131681db"  alt="image 2"/>
	</p>
</details>

## Features

- Allows you to download videos from YouTube for offline viewing.
- Choose the desired video quality for the download (360p, 720p).
- Provides an easy-to-use interface, delivering a pleasant user experience.

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

![terminal 1](https://github.com/Dimitri-Matheus/MinimalTube/assets/121637762/2fcf1ccb-ecef-4082-8fd7-37e6dd4b67c9)
```
❗ To use the themes, it is necessary to clone the repository on your machine
```

3. Choose your theme (standard, reddish, forest, cappuccino)
4. Open the **`main.py`** and modify this line of code:

![terminal 2](https://github.com/Dimitri-Matheus/MinimalTube/assets/121637762/bc09b22b-9b23-46c9-9021-6e0060bce55d)

5. Now, just run your **application** and enjoy! ✨

---

## Customization

This project can be customized to your liking. If you didn't like any of the available themes, feel free to customize it your own way!
<details>
<summary>⚙️ Used settings</summary>
   
   - Open the project folder and navigate to `themes > standard.json` then make a copy of this file.
   
   - Now you can edit each parameter as desired.
   
   - Here are some parameters that I usually edit (the first color refers to the **light mode** and the second color to the **dark mode**).
<p>

```json
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
</p>
</details>

---

## Contributing

If you want to contribute to this project, open a new issue to discuss your idea or submit a pull request with the proposed changes.

## Credits

This project was developed by me and uses pytube as a data source.
