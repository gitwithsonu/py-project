from moviepy.editor import *
#
# timeClipList = []
# timerParent = ColorClip(size=(1080, 1920), color=(0, 0, 0))
# timerParent = timerParent.set_opacity(0)
# s = 0
# for time in range(7, 0, -1):
#     cl = TextClip(
#         str(time),
#         # font="ArialUnicode",
#         fontsize=150.0,
#         color="white",
#         bg_color="transparent",
#         stroke_color="black",
#         stroke_width=2.0,
#         align='Center',
#         # size=(80, 60)
#     )
#     cl = cl.set_position((300, 400))
#     x = CompositeVideoClip([timerParent, cl])
#     x = x.set_duration(1.0).set_start(s).set_fps(2)
#     # overAllClip.append(x)
#     timeClipList.append(x)
#     s += 1
# CompositeVideoClip(timeClipList).write_videofile('temp/timerVideo.mp4')



# textClip = TextClip(txt="MoviePy is awesome",
#                     fontsize=40,
#                     font="Lane",
#                     size=(0, 100),
#                     color="black",
#                     bg_color="white",
#                     )
#
# textClip = textClip.set_position("center")
# textClipWidth, textClipHeight = textClip.size
#
# colourClip = ColorClip(size=(textClipWidth+10, textClipHeight+10), color=(0,0,255))
#
# finalClip = CompositeVideoClip([colourClip, textClip])
# finalClip.save_frame("final.png")

# textClip.save_frame("out.png")


'''----------------------Main Canvas------------------------------------------------------'''
OutWidth = 1080
OutHeight = 1920
mainCanvas = ColorClip(size=(OutWidth, OutHeight), color=(0, 0, 0))

'''----------------------Background_Picture-----------------------------------------------'''
image_clip = ImageClip("bihar-map.jpg")
imageMask = ColorClip(size=(image_clip.size[0], image_clip.size[1]), color=(0, 0, 0))
imageMask = imageMask.set_opacity(.6)
image_clip = CompositeVideoClip([image_clip, imageMask])
image_clip = image_clip.set_position("center")
image_clip = image_clip.resize(OutWidth/image_clip.size[0])


'''----------------------Question and Option text-----------------------------------------'''

print(len("निम्नलिखित में से कौन मुक्केब"))

questionTextClip = TextClip(txt="निम्नलिखित में से कौन मुक्केबाजी के खेल से संबंधित है?",
                            fontsize=70,
                            font="Samyak-Devanagari",
                            # size=(0.9*OutWidth, 0),
                            color="white",
                            bg_color="transparent",
                            # stroke_color="black",
                            stroke_width=2.0,
                            align='North',
                            )

questionTextClip = questionTextClip.set_position((0, 0))
questionTextClipWidth, questionTextClipHeight = questionTextClip.size
QuestionBoundaryColourClip = ColorClip(size=(questionTextClipWidth + 10, questionTextClipHeight + 10), color=(0, 200, 0))
QuestionBoundaryColourClip = QuestionBoundaryColourClip.set_opacity(.7)
finalQuestionTextClip = CompositeVideoClip([QuestionBoundaryColourClip, questionTextClip])
finalQuestionTextClip = finalQuestionTextClip.set_position((50, 50))

# Options
options = ['A Gaya', 'B Buxar', 'C Patna', 'D Bhagalpur']
optionClips = []
correctOption = 2
for option in options:
    onCorrectOptionClip = TextClip(txt=option,
                                   fontsize=90,
                                   # font="Lane",
                                   # size=(.7*OutWidth, 0),
                                   color="white" if options[correctOption] == option else "black",
                                   bg_color="transparent",
                                   # stroke_color="black",
                                   # stroke_width=2.0,
                                   align='West',
                                   )
    onCorrectOptionClip = onCorrectOptionClip.set_position((20, 50))
    onCorrectOptionClipWidth, onCorrectOptionClipHeight = onCorrectOptionClip.size
    onCorrectOptionBoundaryColourClip = ColorClip(size=(800, 150), color=(225, 225, 255) if options[correctOption] is not option else (8, 140, 15))
    x = CompositeVideoClip([onCorrectOptionBoundaryColourClip, onCorrectOptionClip])
    x = x.set_position((120, 1000 + options.index(option) * 160))
    optionClips.append(x)
# CompositeVideoClip(optionClips).save_frame("final.png")

optionClips.append(finalQuestionTextClip)
optionClips.insert(0, image_clip)
optionClips.insert(0, mainCanvas)
finalClip = CompositeVideoClip(optionClips)
finalClip.save_frame("final.png")

