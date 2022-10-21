#!/usr/bin/python

# User     : ltcastelnuovo
# Challenge: https://ringzer0ctf.com/challenges/156

import os, filecmp, requests
from shutil import rmtree
from PIL import Image
from progress.bar import Bar

GIF_PATH = "./data.gif"
FRAMES_PATH = "./frames"
COMBINED_PATH = "./combined"


def download(url):
    print("Task 1/4: Downloading gif  |################################| 1/1")
    response = requests.get(url)

    open(GIF_PATH, "wb").write(response.content)


def splitGif():
    os.mkdir(FRAMES_PATH)

    with Image.open(GIF_PATH) as tvGif:
        with Bar("Task 2/4: Splitting gif   ", max=tvGif.n_frames) as bar:
            for frame in range(tvGif.n_frames):
                tvGif.seek(frame)
                tvGif.save(FRAMES_PATH + "/" + str(frame) + ".png")

                bar.next()


def combineFrames():
    os.mkdir(COMBINED_PATH)

    framesLength = len(os.listdir(FRAMES_PATH))

    with Bar("Task 3/4: Combining frames", max=(framesLength * framesLength)) as bar:
        for i in range(framesLength):
            for j in range(framesLength):
                backPath = FRAMES_PATH + "/" + str(i) + ".png"
                frontPath = FRAMES_PATH + "/" + str(j) + ".png"

                backImage = Image.open(backPath).convert("RGBA")
                frontImage = Image.open(frontPath).convert("RGBA")

                # Overlay front image on back image
                combinedImage = Image.blend(backImage, frontImage, 0.5)
                combinedImagePath = COMBINED_PATH + "/" + str(i) + "-" + str(j) + ".png"

                # Save combined image if special
                entropy = combinedImage.entropy()

                # Random black and white images have an entropy between 2 and 3.12
                if entropy > 3.13:
                    combinedImage.save(combinedImagePath, "PNG")

                bar.next()


def filterCombinedFrames():
    combinedFrames = os.listdir(COMBINED_PATH)
    combinedFramesLength = len(combinedFrames)

    for i in range(combinedFramesLength):
        for j in range(combinedFramesLength):
            file1 = COMBINED_PATH + "/" + combinedFrames[i]
            file2 = COMBINED_PATH + "/" + combinedFrames[j]

            if file1 == file2:
                continue

            if not os.path.isfile(file1) or not os.path.isfile(file2):
                continue

            if filecmp.cmp(file1, file2):
                os.remove(file1)

    print("Task 4/4: Filtering frames |################################| 100/100")


def showResultingFrames():
    combinedFrames = os.listdir(COMBINED_PATH)

    for frame in combinedFrames:
        framePath = COMBINED_PATH + "/" + frame
        frameImage = Image.open(framePath)

        frameImage.show()


def cleanup():
    os.remove(GIF_PATH)
    rmtree(FRAMES_PATH)
    rmtree(COMBINED_PATH)


def main():
    download("https://ringzer0ctf.com/images/tv.gif")

    splitGif()
    combineFrames()
    filterCombinedFrames()
    showResultingFrames()

    cleanup()


main()
