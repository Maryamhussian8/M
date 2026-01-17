from django import forms
from .models import College, Section, Stage, Subject

class CourseSelectionForm(forms.Form):
    college = forms.ModelChoiceField(queryset=College.objects.all())
    section = forms.ModelChoiceField(queryset=Section.objects.none())
    stage = forms.ModelChoiceField(queryset=Stage.objects.none())
    subject = forms.ModelChoiceField(queryset=Subject.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.data.get('college'):
            try:
                college_id = int(self.data.get('college'))
                self.fields['section'].queryset = Section.objects.filter(college_id=college_id)
            except (ValueError, TypeError):
                self.fields['section'].queryset = Section.objects.none()
        else:
            self.fields['section'].queryset = Section.objects.none()

        if self.data.get('section'):
            try:
                section_id = int(self.data.get('section'))
                self.fields['stage'].queryset = Stage.objects.filter(section_id=section_id)
            except (ValueError, TypeError):
                self.fields['stage'].queryset = Stage.objects.none()
        else:
            self.fields['stage'].queryset = Stage.objects.none()

        if self.data.get('stage'):
            try:
                stage_id = int(self.data.get('stage'))
                self.fields['subject'].queryset = Subject.objects.filter(stage_id=stage_id)
            except (ValueError, TypeError):
                self.fields['subject'].queryset = Subject.objects.none()
        else:
            self.fields['subject'].queryset = Subject.objects.none()
