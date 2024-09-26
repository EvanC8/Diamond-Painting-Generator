# Diamond Painting Generator

Welcome! This program generates custom diamond painting templates from uploaded images. Diamond painting is a popular relaxing DIY craft that involves placing shiny colored rhinestones over a pre-made template to create a decorative art piece. More information about diamond painting can be found [here](https://www.diamondartclub.com/blogs/diamond-painting/what-is-diamond-painting). The program allows users to create their own diamond painting templates for a fun leisure activity and wall decor. Hope you enjoy!<br>
<!-- <img src="https://github.com/EvanC8/2D-Physics-Engine/assets/137731839/75f1ae1c-479b-4091-96eb-5752c00d31d9" width="200"> -->

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li>
      <a href="#how-it-works">How it works</a>
      <ul>
        <li><a href="#pillow">Pillow</a></li>
        <li><a href="#abstraction">Abstraction</a></li>
        <li><a href="#quantization">Quantization</a></li>
      </ul>
    </li>
    <li><a href="#next-steps">Next Steps</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

# Installation
* Clone the repo
   ```sh
   git clone https://github.com/EvanC8/Diamond-Painting-Generator.git
   ```
# Usage
1. Upload desired image to the `images` folder.
2. Create a new python file under the folder `PaintingsData`.
3. Follow the example file template named `StarryNight.py` to create an `ImageData` object to specific all parameters for the template creation.
4. In the `main.py` file, import your PaintingsData file and set `selected_image` to your ImageData object.
5. Run `main.py` and see the results!

# How it works
### Pillow
This program was created using Pillow, an imaging library for Python. More information about Pillow can be found [here](https://pillow.readthedocs.io/en/stable/). 

### Abstraction


### Quantization


# Next Steps
* Numbering
  * Overlaying the template's rhinestone squares with numbers that correspond to the color in each square. This will allow for easier usage of the template on the user-end.
* Creating a website
  * A graphical interface will allow users to easily upload images and download their templates.
* 

# License
Destributed under the MIT License. See `LICENSE.txt` for more information.

# Contact
Evan Cedeno - escedeno8@gmail.com

Project Link: [Diamond Painting Generator](https://github.com/EvanC8/Diamond-Painting-Generator)

# Acknowledgments 
* [Pillow](https://pillow.readthedocs.io/en/stable/)
