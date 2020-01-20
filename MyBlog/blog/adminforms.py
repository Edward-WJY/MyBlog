#from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Post

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label = '摘要', required=False)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=True)
    """
    content_ck = forms.CharField(widget=CKEditorUploadingWidget(), label = '正文', required=False)

    content_md = forms.CharField(widget=forms.Textarea(),label='正文',required=False)

    content = forms.CharField(widget=forms.HiddenInput() , required= False)

    # class Meta:
    #     model = Post
    #     fields = (
    #         'is_md','content', 'content_md', 'content_ck'
    #     )

    def __init__(self, instance=None, initial=None, **kwargs):
        initial =  initial or {}
        if instance:
            if instance.is_md:
                initial['content_md'] = instance.content
            else:
                initial['content_ck'] = instance.content

        super().__init__(instance=instance, initial=initial, **kwargs)


    def clean(self):
        is_md = self.cleaned_data.get('is_md')
        if is_md:
            content_field_name = 'content_md'
        else:
            content_field_name = 'content_ck'
        content = self.cleaned_data.get(content_field_name)
        # if not content:
        #     self.add_error(content_field_name, '必填项')

        #self.cleaned_data['content']
        return super().clean()

    class Media:
        js = ('js/post_editor.js',)
    """