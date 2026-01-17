from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey


class College(models.Model):
    college_name = models.CharField(max_length=255)

    def __str__(self):
        return self.college_name

class Section(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    sec_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sec_name} ({self.college.college_name})"

class Stage(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.stage_name} ({self.section.sec_name})"

class Subject(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    section = ChainedForeignKey(
        Section,
        chained_field="college",
        chained_model_field="college",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
    )

    stage = ChainedForeignKey(
        Stage,
        chained_field="section",
        chained_model_field="section",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    section = ChainedForeignKey(
        Section,
        chained_field="college",
        chained_model_field="college",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
    )

    stage = ChainedForeignKey(
        Stage,
        chained_field="section",
        chained_model_field="section",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
    )

    subject = ChainedForeignKey(
        Subject,
        chained_field="stage",
        chained_model_field="stage",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
    )

    chapter_name = models.CharField(max_length=255)
    youtube_link = models.URLField()

    def __str__(self):
        return self.chapter_name


class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)  
    watched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} watched {self.chapter.chapter_name}"
    class Meta:
        ordering = ['-watched_at']  
