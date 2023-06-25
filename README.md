<h1 align="center">MinimalTube</h1>

<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	This app features a minimalist design and enables easy downloading of YouTube videos. With an intuitive interface, users can input the video link and initiate the download process quickly and efficiently.
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

---

## Previews
<details>
<summary>☀️ Light mode </summary>
	<p align="center">
	<img src="https://github.com/Dimitri-Matheus/MinimalTube/assets/121637762/74fc9a10-0a93-4e72-b76c-5208e7906e18"  alt="light"/>
	</p>
</details>

<details>
<summary>🌙 Dark mode </summary>
	<p align="center">
  	<img src="https://github.com/Dimitri-Matheus/MinimalTube/assets/121637762/51f6bf6a-5b84-448e-98de-474488cb1dff"  alt="dark"/>
	</p>
</details>

## Features

- Allows you to download videos from YouTube for offline viewing.
- Choose the desired video quality for the download (360p, 720p).
- Provides an easy-to-use interface, delivering a pleasant user experience.

---

## Requirements

To run the application, you need to have Python 3 installed and the following libraries:

[🟥](https://www.python.org/)  `Python`

[🟨](https://pypi.org/project/Pillow/)  `Pillow`

[🟩](https://github.com/pytube/pytube)  `Pytube`

[🟦](https://github.com/TomSchimansky/CustomTkinter)  `Custom Tkinter`

⬜  `tkinter, os and webbrowser`

---

## Usage

1. Clone the [repository](https://github.com/Dimitri-Matheus/MinimalTube) or [download](https://github.com/Dimitri-Matheus/MinimalTube/releases) the application.
2. Install the required libraries with the following commands:

![terminal 1](https://github.com/Dimitri-Matheus/MinimalTube/assets/121637762/84e1a070-85ba-49c5-abcf-f0dd7ebb6560)

```
❗ To use the themes, it is necessary to clone the repository on your machine
```

3. Choose your theme (standard, grayline, mint, reddish)
4. Open the **`main.py`** and modify this line of code:

![terminal 2](https://github.com/Dimitri-Matheus/MinimalTube/assets/121637762/10ad0cbc-69b7-43d6-ab0b-be995f2db34f)

5. Now, just run your **application** and enjoy! ✨

---

## Customization

This project can be customized to your liking. If you didn't like any of the available themes, feel free to customize it your own way!
<details>
<summary>⚙️ Used settings</summary>
   
   - Open the project folder and navigate to `minimaltube > themes > standard.json` then make a copy of this file.
   
   - Now you can edit each parameter as desired.
   
   - Here are some parameters that I usually edit (the initial color corresponds to the ``light mode``, while the second color corresponds to the ``dark mode``).
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

#

## Contributing

If you want to contribute to this project, open a new issue to discuss your idea or submit a pull request with the proposed changes.

## Credits

This project was developed by me and uses pytube as a data source.
