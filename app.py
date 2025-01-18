from flask import Flask, request, send_file, render_template, redirect, url_for
import os
import cv2
import albumentations as A
import random
from zipfile import ZipFile
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
TRANSFORMED_FOLDER = 'transformed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TRANSFORMED_FOLDER'] = TRANSFORMED_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TRANSFORMED_FOLDER, exist_ok=True)

# Define transformations
transformations = [
    A.RandomRain(brightness_coefficient=0.9, drop_width=1, blur_value=5, p=1),
    A.RandomSnow(brightness_coeff=2.5, p=1),
    A.RandomShadow(shadow_dimension=5, shadow_roi=(0, 0.5, 1, 1), p=1),
    A.Compose([A.HorizontalFlip(p=0.5), A.RandomBrightnessContrast(p=0.2)]),
    A.RandomBrightnessContrast(brightness_limit=1, contrast_limit=1, p=1.0),
    A.RandomSunFlare(flare_roi=(0, 0, 1, 0.5), p=1),
    A.RandomFog(alpha_coef=0.1, p=1)
]

def apply_transformations(image_path):
    """Apply all transformations to an image and save results."""
    # Read the original image using OpenCV
    image_name = os.path.basename(image_path).split('.')[0]
    original_image = cv2.imread(image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    transformed_files = []
    for i, transform in enumerate(transformations):
        # Use a copy of the original image for each transformation
        image_copy = original_image.copy()

        # Apply transformation
        random.seed(7)  # Ensure reproducibility
        transformed = transform(image=image_copy)
        transformed_image = transformed['image']

        # Convert back to BGR for saving with OpenCV
        transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR)

        # Save the transformed image
        transformed_file = os.path.join(app.config['TRANSFORMED_FOLDER'], f'{image_name}_transformed_{i}.jpg')
        cv2.imwrite(transformed_file, transformed_image)
        transformed_files.append(transformed_file)

    return transformed_files


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if files are in the request
        if 'files[]' not in request.files:
            print("No files part in request.")
            return redirect(request.url)

        files = request.files.getlist('files[]')
        if not files or all(file.filename == '' for file in files):
            print("No selected files.")
            return redirect(request.url)

        transformed_files = []

        for file in files:
            if file:
                # Save each uploaded file
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                print(f"Uploaded file saved to: {file_path}")

                # Apply transformations
                transformed_files += apply_transformations(file_path)

        # Create a zip of all transformed files
        zip_path = os.path.join(app.config['TRANSFORMED_FOLDER'], 'transformed_images.zip')
        with ZipFile(zip_path, 'w') as zipf:
            for tf in transformed_files:
                if os.path.exists(tf):
                    print(f"Adding to zip: {tf}")
                    zipf.write(tf, os.path.basename(tf))
                else:
                    print(f"File does not exist: {tf}")

        print(f"Zip file created at: {zip_path}")
        return send_file(zip_path, as_attachment=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
