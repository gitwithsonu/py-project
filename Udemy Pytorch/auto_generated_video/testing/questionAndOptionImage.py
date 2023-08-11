from PIL import Image, ImageDraw, ImageFont
import textwrap

from moviepy.video.VideoClip import ImageClip

# Create an image

text_color = (0, 0, 0)
outline_color = (0, 0, 0, 170)


def get_question_clip(question_text):
    question_canvas = Image.new('RGBA', (950, 800), color=(255, 255, 255, 0))
    font = ImageFont.truetype('raw_material/NotoSans-Bold.ttf', 88, layout_engine=ImageFont.Layout.RAQM)
    text_position = (0, 50)
    draw = ImageDraw.Draw(question_canvas)
    wrapped_text = textwrap.wrap(question_text, width=21)
    for line in wrapped_text:
        # background_coords = (text_position[0], text_position[1], text_position[0] + 900, text_position[1] + 120)
        # draw.rectangle(background_coords, fill=(0, 255, 68, 150))
        draw.text(text_position, " " + line, font=font, fill=text_color, stroke_width=1, stroke_fill=outline_color)
        text_position = (text_position[0], text_position[1] + 120)
        # line_height += line_height
    question_canvas.save('temp/question.png')
    return ImageClip("temp/question.png")

# get_question_clip("िम्नलिखित में से किस फसल के लिए भारत का कृषि क्षेत्र सबसे अधिक है ?")


option_canvas = Image.new('RGBA', (950, 800), color=(255, 255, 255, 0))
draw = ImageDraw.Draw(option_canvas)


def get_option_clip(options):
    font = ImageFont.truetype('raw_material/NotoSans-Bold.ttf', 53, layout_engine=ImageFont.Layout.RAQM)
    position = (50, 50)
    for option in options:
        background_coords = (position[0], position[1], position[0] + 900, position[1] + 100)
        draw.rectangle(background_coords, fill=(225, 225, 225))
        draw.text(position, option, font=font, fill=(0, 0, 0))
        position = (position[0], position[1] + 100 + 30)
    option_canvas.save('temp/option.png')
    return ImageClip("temp/option.png")


def get_correct_option_clip(options, correct_option_index):
    font = ImageFont.truetype('raw_material/NotoSans-Bold.ttf', 53, layout_engine=ImageFont.Layout.RAQM)
    position = (50, 50)
    for i in range(len(options)):
        background_coords = (position[0], position[1], position[0] + 900, position[1] + 100)
        if i == correct_option_index:
            draw.rectangle(background_coords, fill=(7, 219, 63, 180))
            draw.text(position, options[i], font=font, fill=(255, 255, 255))
        else:
            draw.rectangle(background_coords, fill=(255, 255, 255))
            draw.text(position, options[i], font=font, fill=(0, 0, 0))
        position = (position[0], position[1] + 100 + 30)
    option_canvas.save('temp/correctOption.png')
    return ImageClip("temp/correctOption.png")


# o = [" अ. " + "19 अप्रैल 1854 को", " ब. " + "16 अप्रैल 1853 को", " स. " + "16 अप्रैल 1859 को",
#      " द. " + "26 अप्रैल 1856 को"]
#
# get_correct_option_clip(o, 1)
