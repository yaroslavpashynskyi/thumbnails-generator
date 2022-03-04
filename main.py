import datetime
from PIL import Image, ImageFont, ImageDraw

class Subject:
    def __init__(self, name, start, interval):
        self.name = name
        self.start = start
        self.interval = interval
        self.counter = 1

    def set_end_date(end_date):
        Subject.end_date = end_date

    def generate_thumbnails(self):
        date = self.start
        end = Subject.end_date
        interval = self.interval
        if type(self.interval) == tuple:
            while date < end:
                for i in interval:
                    if date < end:
                        self.edit_pic(date, self.name, self.counter)
                        date += i
                        self.counter += 1   
        while date < end:
            self.edit_pic(date, self.name, self.counter)
            date += interval
            self.counter += 1
    
    def change_counter(self, number):
        self.counter = number
    
    def set_oop_group(self, group):
        self.oop_group = group

    def edit_pic(self, date, name, counter):
        subject_name, subject_type = name.split('_')
        im = Image.open("samples/{}.png".format(subject_name))
        
        if subject_type == 'lec':
            im_text = "Лекція №" + str(counter)
        else:
            im_text = "Практика №" + str(counter)

        if name == 'oop_prac':
            im_font = ImageFont.truetype("fonts/Rubik-Medium.ttf", 60) 
            im_editeable = ImageDraw.Draw(im)
            im_editeable.text((934, 550), date.strftime("%d.%m.%Y"), (0, 0, 0), font=im_font)
            im.save('results/{}/{}.png'.format(subject_name, str(self.oop_group) + 'group_' + str(counter) + '_' + subject_type + date.strftime("_%d-%m-%Y")))

            im_font = ImageFont.truetype("fonts/Rubik-Medium.ttf", 75)
            im_editeable = ImageDraw.Draw(im)
            im_editeable.text((10, 480), im_text, (0, 0, 0), font=im_font)
            im.save('results/{}/{}.png'.format(subject_name, str(self.oop_group) + 'group_' + str(counter) + '_' + subject_type + date.strftime("_%d-%m-%Y")))

            im_font = ImageFont.truetype("fonts/Rubik-Medium.ttf", 40)
            im_editeable = ImageDraw.Draw(im)
            im_editeable.text((14, 560), self.oop_group * 'l' + ' підгрупа', (0, 0, 0), font=im_font)
            im.save('results/{}/{}.png'.format(subject_name, str(self.oop_group) + 'group_' + str(counter) + '_' + subject_type + date.strftime("_%d-%m-%Y")))
        else:
            im_font = ImageFont.truetype("fonts/Rubik-Medium.ttf", 60) 
            im_editeable = ImageDraw.Draw(im)
            im_editeable.text((934, 550), date.strftime("%d.%m.%Y"), (0, 0, 0), font=im_font)
            im.save('results/{}/{}.png'.format(subject_name, str(counter) + '_' + subject_type + date.strftime("_%d-%m-%Y")))

            im_font = ImageFont.truetype("fonts/Rubik-Medium.ttf", 75)
            im_editeable = ImageDraw.Draw(im)
            im_editeable.text((10, 502), im_text, (0, 0, 0), font=im_font)
            im.save('results/{}/{}.png'.format(subject_name, str(counter) + '_' + subject_type + date.strftime("_%d-%m-%Y")))
    

Subject.set_end_date(datetime.date(2022, 2, 23)) # date(2022, 6, 1)

oop_lec = Subject('oop_lec', datetime.date(2022, 1, 24), datetime.timedelta(days=7))
discrete_lec = Subject('discrete_lec', datetime.date(2022, 1, 24), datetime.timedelta(days=7))
la_lec = Subject('la_lec', datetime.date(2022, 1, 25), datetime.timedelta(days=7))
ukr_lec = Subject('ukr_lec', datetime.date(2022, 1, 25), datetime.timedelta(days=14))
ukr_prac = Subject('ukr_prac', datetime.date(2022, 1, 26), datetime.timedelta(days=14))
ma_prac = Subject('ma_prac', datetime.date(2022, 1, 26), datetime.timedelta(days=14))
oop_prac = Subject('oop_prac', datetime.date(2022, 1, 27),(datetime.timedelta(days=6),
datetime.timedelta(days=2), datetime.timedelta(days=6)))
la_prac = Subject('la_prac', datetime.date(2022, 1, 28),(datetime.timedelta(days=6),
datetime.timedelta(days=8)))
discrete_prac = Subject('discrete_prac', datetime.date(2022, 1, 28),(datetime.timedelta(days=6)))
ma_lec = Subject('ma_lec', datetime.date(2022, 2, 1),(datetime.timedelta(days=14)))
oop_prac.set_oop_group(2)
oop_lec.generate_thumbnails()
ukr_lec.generate_thumbnails()
ukr_prac.generate_thumbnails()
discrete_lec.generate_thumbnails()
discrete_prac.generate_thumbnails()
ma_lec.generate_thumbnails()
oop_prac.generate_thumbnails()
ma_lec.generate_thumbnails()
la_prac.generate_thumbnails()