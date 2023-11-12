import re
import requests

import gradio as gr
from torch import topk
from torch.nn.functional import softmax
from transformers import ViTImageProcessor, ViTForImageClassification


def load_label_data():
    file_url = "https://gist.githubusercontent.com/yrevar/942d3a0ac09ec9e5eb3a/raw/238f720ff059c1f82f368259d1ca4ffa5dd8f9f5/imagenet1000_clsidx_to_labels.txt"
    response = requests.get(file_url)
    labels = []
    pattern = '["\'](.*?)["\']'
    for line in response.text.split('\n'):
        try:
            tmp = re.findall(pattern, line)[0]
            labels.append(tmp)
        except IndexError:
            pass
    return labels


def run_model(image, nb_classes):
    processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    outputs = softmax(outputs.logits, dim=1)
    outputs = topk(outputs, k=nb_classes)
    return outputs


def classify_image(image, labels, nb_classes):
    top10 = run_model(image, nb_classes=nb_classes)
    return {labels[top10[1][0][i]]: float(top10[0][0][i]) for i in range(nb_classes)}


def main():
    nb_classes = 10
    labels = load_label_data()
    examples=[
        ['https://github.com/andreped/INF1600-ai-workshop/releases/download/Examples/cat.jpg'],
        ['https://github.com/andreped/INF1600-ai-workshop/releases/download/Examples/dog.jpeg'],
    ]

    # define UI
    image = gr.Image(height=512)
    label = gr.Label(num_top_classes=nb_classes)
    interface = gr.Interface(
        fn=lambda x: classify_image(x, labels, nb_classes), inputs=image, outputs=label, title='Vision Transformer Image Classifier', examples=examples,
    )
    interface.launch(debug=True, share=False, height=600, width=1200)  # by setting share=True you can serve the website for others to access


if __name__ == "__main__":
    main()
