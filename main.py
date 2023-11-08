import boto3
import cv2
import os
import credentials
# Specify the AWS region
aws_region = 'us-east-1'  # Replace 'your_aws_region' with the appropriate AWS region, e.g., 'us-east-1'

output_dir = './data'
output_dir_imgs = os.path.join(output_dir, 'imgs')
output_dir_anns = os.path.join(output_dir, 'anns')

# Create AWS Reko client
reko_client = boto3.client('rekognition', aws_access_key_id=credentials.access_key, aws_secret_access_key=credentials.secret_key, region_name=aws_region)

# Set the target class
target_class = 'Zebra'

# load video
cap = cv2.VideoCapture('./zebras.mp4')
frame_num = -1

# read frames
ret = True
while ret:
    ret, frame = cap.read()

    if ret:
        frame_num += 1
        H, W, _ = frame.shape
        # convert video to jpg
        _, buffer = cv2.imencode('.jpg', frame)

        # convert buffer to bytes
        image_bytes = buffer.tobytes()

        # detect objects
        response = reko_client.detect_labels(Image={'Bytes': image_bytes}, MinConfidence=50)

        with open(os.path.join(output_dir_anns, 'frame.{}.txt'.format(str(frame_num).zfill(6))), 'w') as f:
            for label in response['Labels']:
                if label['Name'] == target_class:
                    for instance_nmr in range(len(label['Instances'])):
                        bbox = label['Instances'][instance_nmr]['BoundingBox']
                        x1 = bbox['Left']
                        y1 = bbox['Top']
                        width = bbox['Width']
                        height = bbox['Height']
                        #print(x1, y1, width, height)
                        #cv2.rectangle(frame, (x1, y1), (x1 + width, y1 + height), (0, 255, 0), 3) #mark bbox on each frame

                        # write detections
                        f.write('{} {} {} {} {}\n'.format(0, (x1 + width / 2), (y1 + height / 2), width, height))

            f.close()
    #save images with detection
    cv2.imwrite(os.path.join(output_dir_imgs, 'frame.{}.jpg'.format(str(frame_num).zfill(6))), frame)

    #cv2.imshow('frame', frame) #show the image with the bbox
    #cv2.waitKey(0) #show the image with the bbox

