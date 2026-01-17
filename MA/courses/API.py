from rest_framework import serializers
from .models import College, Section, Stage, Subject, Chapter, WatchHistory

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    college = serializers.StringRelatedField()
    section = serializers.StringRelatedField()
    stage = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    class Meta:
        model = Chapter
        fields = ['id', 'chapter_name', 'youtube_link', 'college', 'section', 'stage', 'subject']


class WatchHistorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    chapter = serializers.StringRelatedField()

    class Meta:
        model = WatchHistory
        fields = ['id', 'user', 'chapter', 'watched_at']

class RegisterWatchHistorySerializer(serializers.Serializer):
    chapter_id = serializers.IntegerField()

    def validate_chapter_id(self, value):
        from .models import Chapter
        if not Chapter.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid chapter_id")
        return value

