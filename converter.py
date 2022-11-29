from pathlib import Path
import moviepy.editor as moviepy

def detect(myPath, myOutput):
    formats = [".mp4",
               ".avi",
               ".mkv",
               ".webm",
               ".mov",
               ".png",
               ".jpg",
               ".jpeg",
               ".webp",
               ".tiff",
               ".mp3",
               ".wac",
               ".acc",
               ".flac",
               ".aiff"]
    for i in formats:
        if i in myPath:
            print("valid format")
            input_format = i

    nameFile = Path(myPath).name
    print(input_format)
    convert(nameFile, myPath, input_format, myOutput)

def convert(name, myPath, myInput, output):
    
    formatsDict = len(myInput)
    print(formatsDict)
    nameOnly = name[:formatsDict]
    pathOnly = myPath[:-formatsDict]
    print(nameOnly)
    
    if myInput == ".mp4" or myInput == ".avi" or myInput == ".mkv" or myInput == ".webm" or myInput == ".mov":
        if output == ".mp4" or output == ".avi" or output == ".mkv" or output == ".mov":
            if output != ".webp":
                if myInput != output:
                    clip = moviepy.VideoFileClip(r"" + myPath)
                    result = moviepy.CompositeVideoClip([clip])
                    result.write_videofile(pathOnly + output, codec='mpeg4')
                else:
                    # TODO POPUP
                    print("idk")
        elif output == ".webm":
            if myInput != output:
                clip = moviepy.VideoFileClip(r"" + myPath)
                result = moviepy.CompositeVideoClip([clip])
                result.write_videofile(pathOnly + output, codec='libvpx')

    elif myInput == ".png" or myInput == ".jpg" or myInput == ".jpeg" or myInput == ".webp" or myInput == ".tiff":
        if output == ".png" or output == ".jpg" or output == ".jpeg" or output == ".webp" or output == ".tiff":
            if myInput != output:
                pass
                # TODO
            # TODO
        # TODO
    elif myInput == ".mp3" or myInput == ".wac" or myInput == ".acc" or myInput == ".flac" or myInput == ".aiff":
        if output == ".mp3" or output == ".wac" or output == ".acc" or output == ".flac" or output == ".aiff":
            if myInput != output:
                pass
            # TODO
        # TODO

        


if __name__ == "__main__":
    detect(r"C:\Users\migue\Desktop\myapp\test.avi", ".mkv")