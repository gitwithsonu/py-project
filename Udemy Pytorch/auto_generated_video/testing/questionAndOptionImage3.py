from PIL import Image, ImageDraw, ImageFont
import textwrap

from moviepy.video.VideoClip import ImageClip

# Create an image

text_color = (255, 255, 255, 255)
outline_color = (0, 0, 0, 170)


def get_question_clip(question_text):
    question_canvas = Image.new('RGBA', (1700, 600), color=(255, 255, 255, 0))
    font = ImageFont.truetype('raw_material/Kalam-Regular.ttf', 96, layout_engine=ImageFont.Layout.RAQM)
    text_position = (0, 50)
    draw = ImageDraw.Draw(question_canvas)
    wrapped_text = textwrap.wrap(question_text, width=37)
    for line in wrapped_text:
        # background_coords = (text_position[0], text_position[1], text_position[0] + 900, text_position[1] + 120)
        # draw.rectangle(background_coords, fill=(0, 255, 68, 150))
        draw.text(text_position, " " + line, font=font, fill=text_color, stroke_width=1, stroke_fill=outline_color)
        text_position = (text_position[0], text_position[1] + 130)
        # line_height += line_height
    question_canvas.save('temp/question.png')
    return ImageClip("temp/question.png")


# get_question_clip("शिक्षक द्वारा अपने पुत्र को पढ़ाना कौन-सी क्रिया है ?")







def get_option_clip(options):
    option_canvas = Image.new('RGBA', (1150, 800), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(option_canvas)
    font = ImageFont.truetype('raw_material/Kalam-Regular.ttf', 70, layout_engine=ImageFont.Layout.RAQM)
    position = (50, 50)
    for option in options:
        # background_coords = (position[0], position[1], position[0] + 900, position[1] + 100)
        # draw.rectangle(background_coords, fill=(225, 225, 225))
        draw.text(position, option, font=font, fill=text_color)
        position = (position[0], position[1] + 100 + 10)
    option_canvas.save('temp/option.png')
    return ImageClip("temp/option.png")


png_image = Image.open("raw_material/tick_mark.png")
png_image = png_image.resize((140, 140), Image.ADAPTIVE)
def get_correct_option_clip(options, correct_option_index):
    option_canvas = Image.new('RGBA', (1150, 800), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(option_canvas)
    font = ImageFont.truetype('raw_material/Kalam-Regular.ttf', 70, layout_engine=ImageFont.Layout.RAQM)
    position = (50, 50)
    for i in range(len(options)):
        # background_coords = (position[0], position[1], position[0] + 900, position[1] + 100)
        if i == correct_option_index:
            # draw.rectangle(background_coords, fill=(7, 219, 63, 180))
            draw.text(position, options[i], font=font, fill=(170, 255, 235, 255))
            option_canvas.paste(png_image, (70, 120*i + 25), png_image)
        else:
            # draw.rectangle(background_coords, fill=(255, 255, 255))
            draw.text(position, options[i], font=font, fill=text_color)
        position = (position[0], position[1] + 100 + 10)
    option_canvas.save('temp/correctOption.png')
    return ImageClip("temp/correctOption.png")

o = [" अ). " + "19 अप्रैल 1854 को", " ब). " + "16 अप्रैल 1853 को", " स). " + "16 अप्रैल 1859 को",
     " द). " + "26 अप्रैल 1856 को"]
# get_option_clip(o)
# get_correct_option_clip(o, 3)
