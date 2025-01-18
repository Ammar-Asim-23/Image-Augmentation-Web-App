# Image Transformation Flask App

This project is a Flask-based web application that allows users to upload images, apply a series of transformations to them, and download the transformed images as a zip file. It uses the Albumentations library for applying image augmentations such as adding rain, snow, brightness adjustments, and more.

## Features

- **Multiple Image Upload**: Upload multiple images simultaneously.
- **Image Transformations**: Apply a set of predefined transformations to the uploaded images.
- **Download as Zip**: Download the transformed images as a single zip file.

## Technologies Used

- **Python**: Backend logic and transformations.
- **Flask**: Web framework.
- **HTML/CSS**: Frontend interface.
- **Albumentations**: Image transformation library.
- **OpenCV**: Image processing.
- **Bootstrap**: Styling the frontend.

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-transformation-app.git
   cd image-transformation-app
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Upload one or more images using the "Select Images" button.
2. Click the "Upload and Transform" button.
3. The app will apply the following transformations to each image:
   - Random Rain
   - Random Snow
   - Random Shadow
   - Horizontal Flip with Brightness/Contrast adjustments
   - Random Brightness/Contrast
   - Random Sun Flare
   - Random Fog
4. A zip file containing all transformed images will be downloaded automatically.

## File Structure

```
image-transformation-app/
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # HTML template for the web interface
├── uploads/                # Directory for storing uploaded images
├── transformed/            # Directory for storing transformed images and zip files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Known Issues

- **Random Rain Transformation**: The effect persists in the original image if transformations are chained. This issue has been addressed by copying the original image before each transformation.

## Dependencies

The application uses the following Python packages:

- Flask
- OpenCV
- Albumentations
- Werkzeug

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Future Enhancements

- Allow users to select specific transformations via the web interface.
- Add real-time previews of transformations.
- Optimize zip file creation for large datasets.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to contribute or report issues!

