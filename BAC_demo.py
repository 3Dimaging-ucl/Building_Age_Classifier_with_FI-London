import argparse
from BAC import BAC

parser = argparse.ArgumentParser("Building Age Classifier", description="Building Age Claffier using GPT-4 Vision.", add_help=True)

parser.add_argument('--image', type=str, required=True, help='image path')
parser.add_argument('--api_key', type=str,  required=True, help='Open API Key')
parser.add_argument('--output', type=str, default='./output', help='Output path (default: ./output).')

args = parser.parse_args()


input_img = args.image
api_key = args.api_key
output_folder = args.output

