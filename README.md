# AWS Rekognition Object Detection with OpenCV
![Example Image](data/zebras_detected.png)

This code demonstrates how to use AWS Rekognition, an image and video analysis service, to perform object detection on a video using Python and OpenCV. Specifically, it detects instances of a target class (in this case, 'Zebra') in each frame of the input video ('zebras.mp4') and saves the bounding box coordinates of the detected objects to a text file, along with saving the frames with detected objects as images.

## Prerequisites

1. **AWS Account**: You need an AWS account to use the AWS Rekognition service. Ensure you have access to AWS credentials (access key and secret key) with appropriate permissions to use Rekognition.

2. **Python and Libraries**: Make sure you have Python installed on your system. Additionally, you need the following Python libraries:
   - `boto3`: AWS SDK for Python to interact with AWS services.
   - `opencv-python`: OpenCV library for image and video processing.
   - `credentials.py`: A Python file containing your AWS access key and secret key as variables (`access_key` and `secret_key`). Ensure this file is present in the same directory as your script.

   You can install these libraries using `pip`:
   ```
   pip install boto3 opencv-python
   ```

## Getting Started

1. **AWS Configuration**: Replace `'us-east-1'` in the `aws_region` variable with your appropriate AWS region code if it's different. Make sure your AWS credentials (access key and secret key) are correctly set in the `credentials.py` file.

2. **Input Video**: Ensure that the input video file is named `zebras.mp4` and is present in the same directory as your Python script.

3. **Output Directories**: The detected frames with bounding boxes and annotation files will be saved in the `./data/imgs/` and `./data/anns/` directories, respectively. Make sure these directories exist in your project folder.

## Running the Code

Run the Python script (`your_script_name.py`) in your terminal or command prompt. The script will read frames from the input video, detect instances of the target class ('Zebra') using AWS Rekognition, and save the frames with detected objects as images in the `./data/imgs/` directory. The bounding box coordinates of the detected objects will be saved in annotation files in the `./data/anns/` directory.

## Notes

- The confidence threshold for object detection is set to 50% (`MinConfidence=50`). You can adjust this threshold according to your requirements in the `reko_client.detect_labels` call.
  
- The detected frames are saved with bounding boxes drawn around the detected objects. The code for drawing bounding boxes on the frames is commented out. If you want to visualize the bounding boxes on the frames, uncomment the relevant lines in the code.

- Make sure to handle AWS credentials securely and avoid hardcoding them directly in your code for security reasons.

- For more information about AWS Rekognition and its capabilities, refer to the [official AWS Rekognition documentation](https://aws.amazon.com/rekognition/).

Happy coding!
