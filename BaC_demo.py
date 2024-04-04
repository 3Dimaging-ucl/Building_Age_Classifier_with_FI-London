import argparse
from Classifier.BaClassifier import BaClassfier

parser = argparse.ArgumentParser("Building Age Classifier", description="Building Age Claffier using GPT-4 Vision.", add_help=True)

parser.add_argument('image', type=str, help='image path')
parser.add_argument('api_key', type=str, help='Open API Key')
parser.add_argument('--output', type=str, default='./Result_FI-London/predicted_result.json', help='Output path (default: ./Result_FI-London/predicted_result.json).')
parser.add_argument('--img_mode', type=str, default='FI-London', help="Options = 'single' for single image prediction,'multiple' for multiple images prediction, and 'FI-London' for FI-London prediction (default: FI-London).")
parser.add_argument('--BaC_mode', type=str, default=1, help='Classfier modes with prompt at 1 or 5 (default: 1).')

args = parser.parse_args()

img_path = args.image
output_path = args.output
img_mode = args.img_mode
BaC_mode = args.BaC_mode
api_key = args.api_key

classfier = BaClassfier(img_path, output_path, img_mode, BaC_mode, api_key)
classfier.Ba_classification()

