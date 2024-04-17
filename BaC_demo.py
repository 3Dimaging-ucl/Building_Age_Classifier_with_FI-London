import argparse

# Import the Building Age Classfier
from Classifier.BaClassifier import BaClassfier

parser = argparse.ArgumentParser("Building Age Classifier", description="Building Age Claffier using GPT-4 Vision.", add_help=True)

# Define a positional argument for the image path where the input image is located
parser.add_argument('image', type=str, help='image path')

# Define an argument for the OpenAI API key for the GPT-4 Vision model
parser.add_argument('api_key', type=str, help='Open API Key')

# Define an optional argument for the output file path where results will be saved
# The default value is set to ./Result_FI-London/predicted_result.json
parser.add_argument('--output', type=str, default='./Result_FI-London/predicted_result.json', help='Output path (default: ./Result_FI-London/predicted_result.json).')

# Define an optional argument to specify the image mode for processing
# It controls how many images are input: single, multiple, or 'FI-London'
parser.add_argument('--img_mode', type=str, default='FI-London', help="Options = 'single' for single image prediction,'multiple' for multiple images prediction, and 'FI-London' for FI-London prediction (default: FI-London).")

# Define an optional argument to specify the classifier mode which influences the type of prompt used
# It can be set to 1 or 5 depending on the desired numbers of output age epochs
parser.add_argument('--BaC_mode', type=str, default=1, help='Classfier modes with prompt at 1 or 5 (default: 1).')

# Parse the arguments
args = parser.parse_args()

img_path = args.image
output_path = args.output
img_mode = args.img_mode
BaC_mode = args.BaC_mode
api_key = args.api_key

# Create the BaClassfier object and call the classification function
classfier = BaClassfier(img_path, output_path, img_mode, BaC_mode, api_key)
classfier.Ba_classification()

