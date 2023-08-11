import gtts
from gtts import gTTS
from moviepy.editor import *
from moviepy.audio.fx.volumex import volumex
import pandas as pd

df = pd.read_csv("gk_questions/rail-gk.csv")
start = 39
for index, row in df.iterrows():
    if int(row['index']) < start:
        continue
    print(row['index'])
    overAllClip = []

    questionText = str(row['question']).strip()
    options = ["अ " + str(row['o1']).strip()[3:], "ब " + str(row['o2']).strip()[3:], "स " + str(row['o3']).strip()[3:], "द " + str(row['o4']).strip()[3:]]

    print(options)
    correctOption = 0
    if str(row['c_option']).strip() == 'b':
        correctOption = 1
    elif str(row['c_option']).strip() == 'c':
        correctOption = 2
    elif str(row['c_option']).strip() == 'd':
        correctOption = 3
    # questionText = "देश में माल परिवहन के लिए निम्नांकित में से कौन सबसे बड़े माध्यम के रूप में प्रयुक्त होता है? "
    # options = ['अ वायु सेवा', 'ब रेलवे', 'स बस', 'द नौ परिवहन सेवा']
    # correctOption = 1
    opt = ["A", "B", "C", "D"]

    font = "Samyak-Devanagari"
    '''-----------------------Audio--------------------------------------------------------'''
    textToSpeak = questionText + " ऑप्शन A, " + options[0][2:] + ", ऑप्शन B " + options[1][2:] + \
                                 ", ऑप्शन C " + options[2][2:] + ", ऑप्शन D " + options[3][2:]
    language = "hi"
    output = gTTS(text=textToSpeak, lang=language, slow=False)

    output.save("temp/audio.mp3")
    question_audio = AudioFileClip("temp/audio.mp3")
    question_audio = question_audio.fx(vfx.speedx, 1.5)
    question_audio_duration = question_audio.duration

    ans_text_to_speech = "सही जबाब ऑप्शन " + opt[correctOption] + options[correctOption][2:]
    output2 = gTTS(text=ans_text_to_speech, lang=language, slow=False)
    output2.save("temp/audio2.mp3")
    ans_audio = AudioFileClip("temp/audio2.mp3")
    ans_audio = ans_audio.set_duration(ans_audio.duration/3)
    ans_audio_duration = ans_audio.duration

    background_music = AudioFileClip("raw_material/background_music.mp3")

    count_timer = AudioFileClip("raw_material/clock_count.mp3")
    count_timer = count_timer.subclip(8, 12)
    count_timer = count_timer.set_duration(4)
    count_timer = count_timer.set_start(question_audio_duration)
    count_timer = volumex(count_timer, 0.06)
    # os.system("start audio.mp3")
    print(question_audio_duration)
    print(ans_audio_duration)

    '''----------------------Main Canvas------------------------------------------------------'''
    OutWidth = 1080
    OutHeight = 1920
    mainCanvas = ColorClip(size=(OutWidth, OutHeight), color=(0, 0, 0))
    mainCanvas = mainCanvas.set_opacity(0)
    # overAllClip.append(mainCanvas.set_position((0, 0)).set_duration(0.01).set_start(0))
    '''----------------------Background_Picture-----------------------------------------------'''
    image_clip = ImageClip("train.jpeg")
    imageMask = ColorClip(size=(image_clip.size[0], image_clip.size[1]), color=(0, 0, 0))
    imageMask = imageMask.set_opacity(.6)
    image_clip = CompositeVideoClip([image_clip, imageMask])
    image_clip = image_clip.set_position("center")
    image_clip = image_clip.resize(OutWidth / image_clip.size[0])

    '''----------------------Question and Option text-----------------------------------------'''

    words = questionText.split(" ")
    lines = []
    lenW = 0
    for i in range(0, len(words)):
        if len(words[i]) + 1 + lenW > 29:
            lines.append(i)
            lenW = len(words[i]) + 1
        else:
            lenW += len(words[i]) + 1
    if len(lines) == 0:
        lines.append(len(words))
    elif lines[-1] is not len(words):
        lines.append(len(words))

    wordLines = []

    lastIndex = 0
    for i in lines:
        s = ""
        for j in range(lastIndex, i):
            s += words[j] + " "
        lastIndex = i
        wordLines.append(s)

    print(words)
    print(lines)
    print(wordLines)

    allQuestionClip = []
    i = 0
    for wordLine in wordLines:
        questionTextClip = TextClip(txt=wordLine.encode('utf-8'),
                                    fontsize=50,
                                    font=font,
                                    # size=(0.9 * OutWidth, 0),
                                    color="white",
                                    bg_color="transparent",
                                    # stroke_color="black",
                                    stroke_width=2.0,
                                    align='North',
                                    )

        questionTextClip = questionTextClip.set_position((15, 0))
        questionTextClipWidth, questionTextClipHeight = questionTextClip.size
        QuestionBoundaryColourClip = ColorClip(size=(questionTextClipWidth + 10, questionTextClipHeight + 10),
                                               color=(0, 200, 0))
        QuestionBoundaryColourClip = QuestionBoundaryColourClip.set_opacity(.7)
        finalQuestionTextClip = CompositeVideoClip([QuestionBoundaryColourClip, questionTextClip])
        finalQuestionTextClip = finalQuestionTextClip.set_position((100, 100 + 110 * i))
        allQuestionClip.append(finalQuestionTextClip)
        i += 1

    # finalQuestionTextClips = CompositeVideoClip(allQuestionClip)

    # Options

    optionClips = []
    for clip in allQuestionClip:
        optionClips.append(clip)
    print(len(allQuestionClip))
    for option in options:
        optionClip = TextClip(txt=option.encode('utf-8'),
                              fontsize=50,
                              font=font,
                              # size=(.7*OutWidth, 0),
                              color="black",
                              bg_color="transparent",
                              # stroke_color="black",
                              # stroke_width=2.0,
                              align='West',
                              )
        optionClip = optionClip.set_position((10, 22))
        optionClipWidth, optionClipHeight = optionClip.size
        optionBoundaryColourClip = ColorClip(size=(800, 150), color=(225, 225, 255))
        x = CompositeVideoClip([optionBoundaryColourClip, optionClip])
        x = x.set_position((120, 1000 + options.index(option) * 160))
        optionClips.append(x)
    # CompositeVideoClip(optionClips).save_frame("final.png")

    # optionClips.append(finalQuestionTextClips)
    optionClips.insert(0, image_clip)
    optionClips.insert(0, mainCanvas)
    finalClip = CompositeVideoClip(optionClips)
    finalClipWithoutOption = finalClip.set_position((0, 0)).set_duration(question_audio_duration + 1 + 4).set_start(
        0).set_fps(3)
    overAllClip.append(finalClipWithoutOption)
    # finalClip.save_frame("final.png")


    '''--------------------------Timer for wait-----------------------------------------------'''
    timerParent = ColorClip(size=(OutWidth, OutHeight), color=(0, 0, 0))
    timerParent = timerParent.set_opacity(0)
    s = 0
    for time in range(int(question_audio_duration) + 1 + 4, 0, -1):
        cl = TextClip(
            str(time),
            font="ArialUnicode",
            fontsize=150.0,
            color="white",
            bg_color="transparent",
            stroke_color="black",
            stroke_width=2.0,
            align='Center',
            # size=(80, 60)
        )
        cl = cl.set_position((600, 500))
        x = CompositeVideoClip([timerParent, cl])
        x = x.set_duration(1.0).set_start(s).set_fps(3)
        overAllClip.append(x)
        # timeClipList.append(x)
        s += 1

    '''--------------------------On Correct Answer change Option Color------------------------'''
    optionClips2 = []
    for clip in allQuestionClip:
        optionClips2.append(clip)
    print(len(allQuestionClip))
    for option in options:
        onCorrectOptionClip = TextClip(txt=option.encode('utf-8'),
                                       fontsize=50,
                                       font=font,
                                       # size=(.7*OutWidth, 0),
                                       color="white" if options[correctOption] == option else "black",
                                       bg_color="transparent",
                                       # stroke_color="black",
                                       # stroke_width=2.0,
                                       align='West',
                                       )
        onCorrectOptionClip = onCorrectOptionClip.set_position((10, 22))
        onCorrectOptionBoundaryColourClip = ColorClip(size=(800, 150),
                                                      color=(225, 225, 255) if options[correctOption] is not option else (
                                                          8, 140, 15))
        x2 = CompositeVideoClip([onCorrectOptionBoundaryColourClip, onCorrectOptionClip])
        x2 = x2.set_position((120, 1000 + options.index(option) * 160))
        optionClips2.append(x2)
    # CompositeVideoClip(optionClips).save_frame("final.png")

    # optionClips.append(finalQuestionTextClips)
    optionClips2.insert(0, image_clip)
    optionClips2.insert(0, mainCanvas)
    finalClipWithOption = CompositeVideoClip(optionClips2)
    finalClipWithOption = finalClipWithOption.set_position((0, 0)).set_duration(ans_audio_duration + 0.7).set_start(
        question_audio_duration + 1 + 4).set_fps(3)
    overAllClip.append(finalClipWithOption)

    # finalClip.save_frame("final.png")
    # CompositeVideoClip(timeClipList).write_videofile('temp/timerVideo.mp4')
    # V.write_videofile("TestVideoProcessed.mp4")
    # V = VideoFileClip("TestVideo.mp4")
    # clipList = [V]
    # s = 0
    # for time in range(A.duration, 0, -1):
    #     cl = TextClip(
    #         str(time),
    #         font="ArialUnicode",
    #         fontsize=50.0,
    #         color="white",
    #         bg_color="transparent",
    #         stroke_color="black",
    #         stroke_width=2.0,
    #         align='Center',
    #         size=(80, 60)
    #     )
    #     cl = cl.set_position(("center", "center")).set_duration(1.0).set_start(s)
    #     s += 1
    #     cl = cl.set_position("center")
    #     clipList.append(cl)
    # print(len(clipList))
    V = CompositeVideoClip(overAllClip)
    background_music.set_start(0)
    background_music = volumex(background_music, 0.03)
    q = question_audio.set_start(0)
    a = ans_audio.set_start(question_audio_duration + 5)
    A = CompositeAudioClip([background_music, q, count_timer, a])
    # V = V.resize(newsize=(OutWidth,OutHeight))
    V.audio = volumex(A, 1.7)
    V.write_videofile("videos/rail-gk/" + questionText + ".mp4")

    # new_audioClip = CompositeAudioClip([videoclip.audio, audioclip])
    # videoclip.audio = new_audioclip
    # videoclip.write_videofile("new_filename.mp4")
    # clip = VideoFileClip("TestVideoProcessed.mp4")
    # videoClip = clip.set_audio(A)


    # Music by <a href="https://pixabay.com/users/daddy_s_music-22836301/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=9923">Daddy_s_Music</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=9923">Pixabay</a>
