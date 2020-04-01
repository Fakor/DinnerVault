from django.db import models


class Label(models.Model):
    text = models.CharField(max_length=12, unique=True)
    color_red = models.IntegerField()
    color_green = models.IntegerField()
    color_blue = models.IntegerField()

    def get_color_string(self):
        return '#{:02X}{:02X}{:02X}'.format(self.color_red, self.color_green, self.color_blue)

    def to_json(self):
        return {
            "text": self.text,
            "red": self.color_red,
            "green": self.color_green,
            "blue": self.color_blue,
            "id": self.id
        }


def create_label_db(text, red, green, blue):
    label = Label(text=text, color_red=red, color_green=green, color_blue=blue)
    label.save()
    return label
