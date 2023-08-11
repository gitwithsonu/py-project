from moviepy.editor import *
from moviepy.audio.fx.volumex import volumex
import pandas as pd

from questionAndOptionImage3 import get_question_clip, get_option_clip, get_correct_option_clip
from textToSpeech import get_saved_audio

df = pd.read_csv("gk_questions/ramayan-gk.csv")
start = 1
till = 10
for i in range(4):
    overAllClip = []
    t = 0
    for index, row in df.iterrows():
        if int(row['index']) < start:
            continue
        elif int(row['index']) > till:
            break
        print(row['index'])
        allClipPerQuiz = []
        questionText = str(row['question']).strip()
        options = [" अ). " + str(row['o1']).strip()[3:], " ब). " + str(row['o2']).strip()[3:],
                   " स). " + str(row['o3']).strip()[3:], " द). " + str(row['o4']).strip()[3:]]
        correctOption = ['a', 'b', 'c', 'd'].index(str(row['c_option']).strip())
        opt = ["A", "B", "C", "D"]

        '''-----------------------Audio--------------------------------------------------------'''
        textToSpeak = questionText + "Option A " + options[0][2:] + ", Option B " + options[1][2:] + ", Option C " + \
                      options[2][2:] + ", Option D " + options[3][2:]
        ansToSpeak = "सही जबाब Option " + opt[correctOption] + "," + options[correctOption][2:]
        question_audio = get_saved_audio(f"question{str(row['index'])}")
        ans_audio = get_saved_audio(f"ans{str(row['index'])}")
        question_audio = volumex(question_audio, 1.3)
        ans_audio = volumex(ans_audio, 1.3)
        # nextQuestion_audio = AudioFileClip(f"temp/audio/next_question.mp3")
        # nextQuestion_audio = volumex(nextQuestion_audio, 1.3)
        # question_audio = AudioFileClip(f"temp/q.mp3")
        # ans_audio = AudioFileClip(f"temp/a.mp3")

        background_music = AudioFileClip("raw_material/background_music.mp3")
        background_music = background_music.set_duration(question_audio.duration + 5 + ans_audio.duration)
        count_timer = AudioFileClip("raw_material/clock_count.mp3")
        count_timer = count_timer.subclip(8, 12)
        count_timer = count_timer.set_duration(4)
        count_timer = count_timer.set_start(question_audio.duration)
        count_timer = volumex(count_timer, 0.2)
        # os.system("start audio.mp3")
        print(question_audio.duration)
        print(ans_audio.duration)

        '''----------------------Main Canvas------------------------------------------------------'''
        # OutWidth = 1080
        # OutHeight = 1920
        # mainCanvas = ColorClip(size=(OutWidth, OutHeight), color=(0, 0, 0))
        # mainCanvas = mainCanvas.set_opacity(0).set_fps(3)

        '''----------------------Background_Picture and question -----------------------------------------------'''
        image_clip = ImageClip("raw_material/ramayan_1080.jpeg").set_fps(3).set_duration(
            question_audio.duration + 5 + ans_audio.duration + 0.4).set_start(0)
        '''For now removing Image Mask'''
        imageMask = ColorClip(size=(image_clip.size[0], image_clip.size[1]), color=(0, 0, 0))
        imageMask = imageMask.set_opacity(.3).set_fps(3).set_duration(
            question_audio.duration + 5 + ans_audio.duration).set_start(0)
        # starting_video = VideoFileClip("raw_material/Indian_economy.mp4")
        # starting_video = starting_video.set_start(0).set_duration(starting_video.duration).set_fps(10)
        # image_clip = CompositeVideoClip([image_clip, starting_video])
        image_clip = image_clip.set_position("center")
        # image_clip = image_clip.resize(OutWidth / image_clip.size[0])
        allClipPerQuiz.append(image_clip)
        allClipPerQuiz.append(imageMask)
        # allClipPerQuiz.append(starting_video)
        # mainCanvas = CompositeVideoClip([mainCanvas, image_clip])
        # mainCanvas = mainCanvas.set_position((0, 0)).set_duration(
        #     question_audio.duration + 5 + ans_audio.duration).set_start(0)
        # allClipPerQuiz.append(mainCanvas)

        question_frame = get_question_clip(questionText).set_fps(3)
        question_frame = question_frame.set_position((70, 100)).set_duration(
            question_audio.duration + 5 + ans_audio.duration).set_start(0)
        allClipPerQuiz.append(question_frame)

        '''---------------------Option Image-----------------------------------------'''

        option_frame = get_option_clip(options)
        option_frame = option_frame.set_position((250, 450)).set_duration(
            question_audio.duration + 5).set_start(0).set_fps(3)
        allClipPerQuiz.append(option_frame)

        correct_option_frame = get_correct_option_clip(options, correctOption)
        correct_option_frame = correct_option_frame.set_position((250, 450)).set_duration(
            ans_audio.duration).set_start(question_audio.duration + 5).set_fps(3)
        allClipPerQuiz.append(correct_option_frame)

        # finalClip.save_frame("final.png")

        '''--------------------------Timer for wait-----------------------------------------------'''
        timerParent = ColorClip(size=(250, 300), color=(0, 0, 0))
        timerParent = timerParent.set_opacity(0)
        s = 0
        for time in range(int(question_audio.duration) + 5, 0, -1):
            cl = TextClip(
                str(time),
                font="ArialUnicode",
                fontsize=150.0,
                color="white",
                bg_color="transparent",
                stroke_color="green",
                stroke_width=1.0,
                align='Center',
                # size=(80, 60)
            )
            if time < 10:
                cl = cl.set_position((1627, 720))
            else:
                cl = cl.set_position((1580, 720))
            # x = CompositeVideoClip([timerParent, cl])
            x = cl.set_duration(1.0).set_start(s).set_fps(3)
            allClipPerQuiz.append(x)
            # timeClipList.append(x)
            s += 1

        V = CompositeVideoClip(allClipPerQuiz)
        background_music.set_start(0)
        background_music = volumex(background_music, 0.02)
        q = question_audio.set_start(0)
        a = ans_audio.set_start(question_audio.duration + 5)
        A = CompositeAudioClip([background_music, q, count_timer, a])
        # V = V.resize(newsize=(OutWidth,OutHeight))
        V.audio = volumex(A, 1.7)
        try:
            V.write_videofile("temp/video/ramayan-gk/long/" + str(row['index']) + ".mp4", codec="libx264")
        except:
            V.write_videofile("temp/video/ramayan-gk/long/" + str(row['index']) + ".mp4", codec="libx264")

        vid = VideoFileClip("temp/video/ramayan-gk/long/" + str(row['index']) + ".mp4")
        vid = vid.set_start(t).set_duration(question_audio.duration + 5 + ans_audio.duration + 0.4).set_fps(3)
        overAllClip.append(vid)
        t += question_audio.duration + 5 + ans_audio.duration + 0.4

        # Music by <a href="https://pixabay.com/users/daddy_s_music-22836301/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=9923">Daddy_s_Music</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=9923">Pixabay</a>

    V = CompositeVideoClip(overAllClip)
    try:
        V.write_videofile("videos/ramayan-gk/long/" + str(start) + "_" + str(till) + ".mp4", codec="libx264")
    except:
        V.write_videofile("videos/ramayan-gk/long/" + str(start) + "_" + str(till) + ".mp4", codec="libx264")
    start += 10
    till += 10