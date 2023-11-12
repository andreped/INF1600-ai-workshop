---
title: 'ViT: Image Classifier'
colorFrom: indigo
colorTo: indigo
sdk: gradio
app_port: 7860
emoji: 🫁
pinned: false
license: mit
app_file: app.py
---


# INF-1600 AI Deployment workshop

This workshop was developed for the _"Intro to Artificial Intelligence"_ course with
code INF-1600 at UiT: The Arctic University of Norway.

The workshop was a collaboration with UiT and Sopra Steria.

In this workshop, you will get a prior on:
* Cloning and pushing code from/to GitHub
* Load and run a pretrained image classification model from [Transformers]().
* Develop a simple web application to enable users to test the model using [Gradio]().
* Making a web app accessible on the local network
* Making a public web app anyone can access using [Hugging Face Spaces]().

## Getting Started

1. Make your first GitHub account by going [here](https://github.com/) and signing up.

2. After logging in to GitHub, go to the code repository [here](https://github.com/andreped/INF1600-ai-workshop).

3. Make a fork of the repository and make your own copy of the code by making a fork.

4. Now you are ready to clone your own fork to your own laptop by opening a terminal and running (remember to replace `<username>` with your own GitHub user name):
```
git clone git+https://github.com/<username>/INF1600-ai-workshop.git
```

5. After cloning, go inside the repository, and from the terminal run these lines to create a virtual environment and activate it:
```
virtualenv -ppython3 venv --clear
source venv/bin/activate
```

6. **TASK:** Analyse the `app.py` script which python packages are required, and
add the missing dependencies to the `requirements.txt` file.

7. Install dependencies to the virtual environment by:
```
pip install -r requirements.txt
```

8. To test if everything is working, try to run the `app.py` script to launch the web server.

9. You can then access the web app by going to [http://127.0.0.1:7860](http://127.0.0.1:7860) in your favourite web browser.

10. From the prompted website, try clicking one of the image examples and clicking the orange `Submit` button. The model results should show on the right after a few seconds.

10. Try accessing this address from your mobile phone.

11. This should not work, to access the app from a different device, you need to serve it.
Try setting `share=True` in the `interface.launch()` call in the `app.py` script.
When running `app.py` now, you should be given a different web address. Try using that one instead.

But of course, hosting the app yourself from your laptop is not ideal. What if there was some alternative way to do this **completely for free**...

12. Click [here](https://huggingface.co/join) to go to the Hugging Face sign up page and make an account.

13. After making an account and logging in, click the `+ New` button on the left of the website and choose `Space` from the dropdown.

14. In the `Create a new Space` tab, choose a `Space name` for the app, choose a License (preferably `MIT`), among the `Space SDKs` choose `Gradio`, and finally, click `Create Space`.

15. At the bottom of the page, click the `Create` hyperlink at the `(Hunt: Create the app.py file (...))`

16. Name the file `app.py`, copy-paste the `app.py` code

## Workshop Organizers

* [André Pedersen](https://github.com/andreped), Apps, Sopra Steria
* [Tor-Arne Schmidt Nordmo](https://uit.no/ansatte/person?p_document_id=581687), IFI, UiT: The Arctic University of Norway

## License

The code in this repository is released under [MIT license](https://github.com/andreped/INF1600-ai-workshop).
