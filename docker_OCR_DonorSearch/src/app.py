# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cfOB10T7Ba7C47QdKkyLXJAXw5NTaL4a
"""

from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse
import uvicorn
import argparse
import os
from model import process_image

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "OK"}


@app.get("/")
def main():
    html_content = """
            <body>
            <form action="/ocr" enctype="multipart/form-data" method="post">
            <input name="file" type="file">
            <input type="submit">
            </form>
            </body>
            """
    return HTMLResponse(content=html_content)

@app.post("/ocr")
def process_request(file: UploadFile):
    #  save file to the local folder
    pth = os.path.join(os.path.dirname(__file__), "tmp", file.filename)

    # send the image to the process function
    res = process_image(pth)

    return {"filename": file.filename, "info": res}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=8000, type=int, dest="port")
    parser.add_argument("--host", default="0.0.0.0", type=str, dest="host")
    args = vars(parser.parse_args())

    uvicorn.run(app, **args)