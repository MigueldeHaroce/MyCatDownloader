from pathlib import Path
import moviepy.editor as moviepy

def detect(myPath, myOutput):
    formats = [".mp4",
               ".avi",
               ".mkv",
               ".webp",
               ".mov"]
    for i in formats:
        if i in myPath:
            print("valid format")
            input_format = i

    nameFile = Path(myPath).name
    print(input_format)
    convert(nameFile, myPath, input_format, myOutput)

def convert(name, myPath, myInput, output):
    formatsDict = {".mp4":4,
                   ".avi":4,
                   ".mkv":4,
                   ".webp":5,
                   ".mov":4}
    for i in formatsDict:
        if formatsDict[i] == formatsDict[myInput]:
            numbToEli = formatsDict[i]
    print(numbToEli)
    nameOnly = name[:numbToEli]
    pathOnly = myPath[:-numbToEli]
    print(nameOnly)

    clip = moviepy.VideoFileClip(r"" + myPath)
    result = moviepy.CompositeVideoClip([clip])
    result.write_videofile(pathOnly + output, codec='mpeg4')

if __name__ == "__main__":
    detect(r"C:\Users\migue\Desktop\myapp\test.avi", ".mkv")