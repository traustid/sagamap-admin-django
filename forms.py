from django import forms
from .models import Chapters, Placeattr, Places, Sagaplace, Sagas, Users


class ChaptersForm(forms.ModelForm):

    class Meta:
        model = Chapters
        fields = ['title', 'chapter', 'text', 'saga']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ChaptersForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ChaptersForm, self).is_valid()

    def full_clean(self):
        return super(ChaptersForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_chapter(self):
        chapter = self.cleaned_data.get("chapter", None)
        return chapter

    def clean_text(self):
        text = self.cleaned_data.get("text", None)
        return text

    def clean_saga(self):
        saga = self.cleaned_data.get("saga", None)
        return saga

    def clean(self):
        return super(ChaptersForm, self).clean()

    def validate_unique(self):
        return super(ChaptersForm, self).validate_unique()

    def save(self, commit=True):
        return super(ChaptersForm, self).save(commit)


class PlaceattrForm(forms.ModelForm):

    class Meta:
        model = Placeattr
        fields = ['type', 'place', 'attr1', 'attr2']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PlaceattrForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PlaceattrForm, self).is_valid()

    def full_clean(self):
        return super(PlaceattrForm, self).full_clean()

    def clean_type(self):
        type = self.cleaned_data.get("type", None)
        return type

    def clean_place(self):
        place = self.cleaned_data.get("place", None)
        return place

    def clean_attr1(self):
        attr1 = self.cleaned_data.get("attr1", None)
        return attr1

    def clean_attr2(self):
        attr2 = self.cleaned_data.get("attr2", None)
        return attr2

    def clean(self):
        return super(PlaceattrForm, self).clean()

    def validate_unique(self):
        return super(PlaceattrForm, self).validate_unique()

    def save(self, commit=True):
        return super(PlaceattrForm, self).save(commit)


class PlacesForm(forms.ModelForm):

    class Meta:
        model = Places
        fields = ['lat', 'lng', 'name', 'type', 'info', 'info2', 'pkey', 'parish', 'county']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PlacesForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PlacesForm, self).is_valid()

    def full_clean(self):
        return super(PlacesForm, self).full_clean()

    def clean_lat(self):
        lat = self.cleaned_data.get("lat", None)
        return lat

    def clean_lng(self):
        lng = self.cleaned_data.get("lng", None)
        return lng

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_type(self):
        type = self.cleaned_data.get("type", None)
        return type

    def clean_info(self):
        info = self.cleaned_data.get("info", None)
        return info

    def clean_info2(self):
        info2 = self.cleaned_data.get("info2", None)
        return info2

    def clean_pkey(self):
        pkey = self.cleaned_data.get("pkey", None)
        return pkey

    def clean_parish(self):
        parish = self.cleaned_data.get("parish", None)
        return parish

    def clean_county(self):
        county = self.cleaned_data.get("county", None)
        return county

    def clean(self):
        return super(PlacesForm, self).clean()

    def validate_unique(self):
        return super(PlacesForm, self).validate_unique()

    def save(self, commit=True):
        return super(PlacesForm, self).save(commit)


class SagaplaceForm(forms.ModelForm):

    class Meta:
        model = Sagaplace
        fields = ['place', 'saga', 'chapter']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SagaplaceForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SagaplaceForm, self).is_valid()

    def full_clean(self):
        return super(SagaplaceForm, self).full_clean()

    def clean_place(self):
        place = self.cleaned_data.get("place", None)
        return place

    def clean_saga(self):
        saga = self.cleaned_data.get("saga", None)
        return saga

    def clean_chapter(self):
        chapter = self.cleaned_data.get("chapter", None)
        return chapter

    def clean(self):
        return super(SagaplaceForm, self).clean()

    def validate_unique(self):
        return super(SagaplaceForm, self).validate_unique()

    def save(self, commit=True):
        return super(SagaplaceForm, self).save(commit)


class SagasForm(forms.ModelForm):

    class Meta:
        model = Sagas
        fields = ['title', 'info', 'defaultsaga', 'type', 'visible']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SagasForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SagasForm, self).is_valid()

    def full_clean(self):
        return super(SagasForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_info(self):
        info = self.cleaned_data.get("info", None)
        return info

    def clean_defaultsaga(self):
        defaultsaga = self.cleaned_data.get("defaultsaga", None)
        return defaultsaga

    def clean_type(self):
        type = self.cleaned_data.get("type", None)
        return type

    def clean_visible(self):
        visible = self.cleaned_data.get("visible", None)
        return visible

    def clean(self):
        return super(SagasForm, self).clean()

    def validate_unique(self):
        return super(SagasForm, self).validate_unique()

    def save(self, commit=True):
        return super(SagasForm, self).save(commit)


class UsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['uname', 'name', 'pass_field', 'type']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(UsersForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(UsersForm, self).is_valid()

    def full_clean(self):
        return super(UsersForm, self).full_clean()

    def clean_uname(self):
        uname = self.cleaned_data.get("uname", None)
        return uname

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_pass_field(self):
        pass_field = self.cleaned_data.get("pass_field", None)
        return pass_field

    def clean_type(self):
        type = self.cleaned_data.get("type", None)
        return type

    def clean(self):
        return super(UsersForm, self).clean()

    def validate_unique(self):
        return super(UsersForm, self).validate_unique()

    def save(self, commit=True):
        return super(UsersForm, self).save(commit)

