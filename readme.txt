Libraries:
            pillow for image processing, use "pip install pillow" to install.
            "xml.etree.ElementTree"(xml file reading), "math" (basic calculate), "random" (basic calculate) from Python standard library, so you do not need to install it

Tested environments:
            Compiler: PyCharm 2023.2.5 (Professional Edition)
            OS: windows 10
            Python version: 3.11.9

Claim:
            T1, T2, T3, T4, T5: completed

            Implementation Details:
                Reading the XML File
                Using the xml.etree.ElementTree module to parse the XML file and extract parameters for the camera, light sources, and spheres.

                Ray Tracing Algorithm
                The core logic of ray tracing is implemented in camera.py. By recursively calculating the intersection points of rays with objects, it traces the reflection and refraction of rays to generate the final image.

                Phong Shading Model
                The Phong shading model is implemented in material.py, calculating the diffuse reflection, specular reflection, and ambient light on the surface of objects.

                Image Processing
                The Pillow library is used to save the rendered result as an image file. The image data is stored in the ImageData class and processed and saved through the PIL Image class.

Additional and general remarks:

                The generated image is a bit dark because the light intensity is not given in the XML file. I gave it a default value.
                Output file type is .png file.