from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions, status
from .models import College, Section, Stage, Subject, Chapter, WatchHistory
from .API import CollegeSerializer, SectionSerializer, StageSerializer, SubjectSerializer, ChapterSerializer, WatchHistorySerializer, RegisterWatchHistorySerializer
from rest_framework.decorators import api_view

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all().order_by('id')
    serializer_class = CollegeSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all().order_by('id')
    serializer_class = SectionSerializer

    def get_queryset(self):
        queryset = Section.objects.all().order_by('id')
        college_id = self.request.query_params.get('college_id')
        if college_id:
            queryset = queryset.filter(college_id=college_id)
        return queryset

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all().order_by('id')
    serializer_class = StageSerializer
    def get_queryset(self):
        queryset = Stage.objects.all().order_by('id')
        section_id = self.request.query_params.get('section_id')
        if section_id:
            queryset = queryset.filter(section_id=section_id)
        return queryset

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('id')
    serializer_class = SubjectSerializer
    def get_queryset(self):
        queryset = Subject.objects.all().order_by('id')
        stage_id = self.request.query_params.get('stage_id')
        if stage_id:
            queryset = queryset.filter(stage_id=stage_id)
        return queryset

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all().order_by('id')
    serializer_class = ChapterSerializer


class WatchHistoryListView(generics.ListAPIView):
    serializer_class = WatchHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WatchHistory.objects.filter(user=self.request.user) 
    


class RegisterWatchHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = RegisterWatchHistorySerializer(data=request.data)
        if serializer.is_valid():
            chapter_id = serializer.validated_data['chapter_id']
            try:
                chapter = Chapter.objects.get(id=chapter_id)
            except Chapter.DoesNotExist:
                return Response({"error": "Chapter not found"}, status=status.HTTP_404_NOT_FOUND)

            WatchHistory.objects.get_or_create(user=request.user, chapter=chapter)
            return Response({"message": "Watch history recorded"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ChapterListFilteredView(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        queryset = Chapter.objects.all().order_by('id')
        college_id = self.request.query_params.get('college')
        section_id = self.request.query_params.get('section')
        stage_id = self.request.query_params.get('stage')
        subject_id = self.request.query_params.get('subject')

        if college_id:
            queryset = queryset.filter(college_id=college_id)
        if section_id:
            queryset = queryset.filter(section_id=section_id)
        if stage_id:
            queryset = queryset.filter(stage_id=stage_id)
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)
        return queryset
    

@api_view(['GET'])
def get_sections_by_college(request):
    college_id = request.GET.get('college_id')
    sections = Section.objects.filter(college_id=college_id).order_by('id')
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_stages_by_section(request):
    section_id = request.GET.get('section_id')
    stages = Stage.objects.filter(section_id=section_id).order_by('id')
    serializer = StageSerializer(stages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_subjects_by_stage(request):
    stage_id = request.GET.get('stage_id')
    subjects = Subject.objects.filter(stage_id=stage_id).order_by('id')
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)

