from django import forms
from .models import Post, Comment

#입력받을 data는 post model의 내용인 caption, image field를 받는다 label도 같이 작성


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "image"]

        labels = {
            "caption": "내용",
            "image": "사진"
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption"]


class CommentForm(forms.ModelForm):
    contents = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Comment
        fields = ["contents"]