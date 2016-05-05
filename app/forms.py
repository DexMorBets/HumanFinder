from django import forms
from django.contrib.auth.models import User
from .models import Post, Post_user, Comment, Comment_user

CITY_LOT = (
    ('', ''),
    ('Минск', 'Минск'),
    ('Брест', 'Брест'),
    ('Могилёв', 'Могилёв'),
    ('Гомель', 'Гомель'),
    ('Гродно', 'Гродно'),
    ('Витебск', 'Витебск'),
    )

SEX = (
    [('Мужчина', 'Мужчина'),
    ('Женщина', 'Женщина')]
)

HAIR = (
    ('', ''),
    ('Брюнет', 'Брюнет'),
    ('Шатен', 'Шатен'),
    ('Рыжий', 'Рыжий'),
    ('Русый', 'Русый'),
    ('Блондин', 'Блондин'),
    ('Седой', 'Седой'),
    ('Другое', 'Другое'),
    ('Волос нет', 'Волос нет'),
    ('Неизвестно', 'Неизвестно'),
    )

BODY = (
    ('', ''),
    ('Худощавое', 'Худощавое'),
    ('Нормальное', 'Нормальное'),
    ('Полное', 'Полное'),
    ('Очень полное', 'Очень полное'),
    ('Неизвестно', 'Неизвестно'),
    )

EYES = (
    ('', ''),
    ('Синий', 'Синий'),
    ('Голубой', 'Голубой'),
    ('Серый', 'Серый'),
    ('Зелёный', 'Зелёный'),
    ('Янтарный', 'Янтарный'),
    ('Карий', 'Карий'),
    ('Другое', 'Другое'),
    ('Неизвестно', 'Неизвестно'),
    )

HAT = (
    ('', ''),
    ('Шапка мех.', 'Шапка мех.'),
    ('Кепка', 'Кепка'),
    ('Шляпа', 'Шляпа'),
    ('Шапка вяз.', 'Шапка вяз.'),
    ('Другое', 'Другое'),
    ('Отсутствует', 'Отсутствует'),
    )

VVERH = (
    ('', ''),
    ('Куртка', 'Куртка'),
    ('Пальто', 'Пальто'),
    ('Дублёнка', 'Дублёнка'),
    ('Шуба', 'Шуба'),
    ('Плащ', 'Плащ'),
    ('Другое', 'Другое'),
    ('Отсутствует', 'Отсутствует'),
    )

NIZ = (
    ('', ''),
    ('Любые', 'Любые'),
    ('Брюки', 'Брюки'),
    ('Джинсы', 'Джинсы'),
    ('Спорт. штаны', 'Спорт. штаны'),
    ('Шорты', 'Шорты'),
    ('Другое', 'Другое'),
    ('Отсутствует', 'Отсутствует'),
    )

BOOTS = (
    ('', ''),
    ('Сапоги', 'Сапоги'),
    ('Ботинки', 'Ботинки'),
    ('Туфли', 'Туфли'),
    ('Кроссовки', 'Кроссовки'),
    ('Кеды', 'Кеды'),
    ('Тапочки', 'Тапочки'),
    ('Сандали', 'Сандали'),
    ('Другое', 'Другое'),
    ('Отсутствует', 'Отсутствует'),
    )


COLORS = (
    ('', ''),
    ('Красный', 'Красный'),
    ('Синий', 'Синий'),
    ('Зелёный', 'Зелёный'),
    ('Серый', 'Серый'),
    ('Коричневый', 'Коричневый'),
    ('Чёрный', 'Чёрный'),
    ('Белый', 'Белый'),
    ('Другой', 'Другой'),
    )


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'surname', 'fam', 'city', 'text', 'gender', 'age', 'height',
                  'body', 'eyes_color', 'hair_color', 'shramy', 'tatu', 'protez', 'konech',
                  'hat', 'hat_color', 'vverh', 'vverh_color', 'niz', 'niz_color', 'boots',
                  'boots_color', 'hospital',)

    name = forms.CharField(required=False, label='name', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(required=False, label='surname', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    fam = forms.CharField(required=False, label='fam', widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
    age = forms.CharField(required=False, label='age', max_length='3', widget=forms.TextInput(attrs={'placeholder': 'Возраст'}))
    height = forms.CharField(required=False, label='height', max_length='3', widget=forms.TextInput(attrs={'placeholder': 'Рост'}))
    city = forms.CharField(required=False, label='city', widget=forms.Select(choices=CITY_LOT))
    body = forms.CharField(initial="Неизвестно", required=False, widget=forms.Select(choices=BODY))
    eyes_color = forms.CharField(initial="Неизвестно", required=False, widget=forms.Select(choices=EYES))
    hair_color = forms.CharField(initial="Неизвестно", required=False, widget=forms.Select(choices=HAIR))
    gender = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect())

    hat = forms.CharField(initial="Отсутствует", required=False, widget=forms.Select(choices=HAT))
    vverh = forms.CharField(initial="Отсутствует", required=False, widget=forms.Select(choices=VVERH))
    niz = forms.CharField(initial="Отсутствует", required=False, widget=forms.Select(choices=NIZ))
    boots = forms.CharField(initial="Отсутствует", required=False, widget=forms.Select(choices=BOOTS))


class PostFormUser(forms.ModelForm):

    class Meta:
        model = Post_user
        fields = ('name', 'surname', 'fam', 'city', 'text', 'gender', 'age', 'height',
                  'body', 'eyes_color', 'hair_color', 'shramy', 'tatu', 'protez', 'konech',
                  'hat', 'hat_color', 'vverh', 'vverh_color', 'niz', 'niz_color', 'boots',
                  'boots_color', 'address', 'phone_number', 'image',)

    name = forms.CharField(required=False, label='name', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(required=False, label='surname', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    fam = forms.CharField(required=False, label='fam', widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
    age = forms.CharField(required=False, label='age', max_length='3', widget=forms.TextInput(attrs={'placeholder': 'Возраст'}))
    height = forms.CharField(required=False, label='height', max_length='3', widget=forms.TextInput(attrs={'placeholder': 'Рост'}))
    city = forms.CharField(required=False, label='city', widget=forms.Select(choices=CITY_LOT))
    body = forms.CharField(initial="Неизвестно", required=False, widget=forms.Select(choices=BODY))
    eyes_color = forms.CharField(initial="Неизвестно", required=False, widget=forms.Select(choices=EYES))
    hair_color = forms.CharField(initial="Неизвестно", required=False, widget=forms.Select(choices=HAIR))
    gender = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect())
    address = forms.CharField(required=False, label='address', widget=forms.TextInput(attrs={'placeholder': 'Адрес'}))
    phone_number = forms.CharField(required=False, label='phone_number', widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    image = forms.ImageField(required=False, label='photo')

    hat = forms.CharField(initial="Отсутствует", required=False, widget=forms.Select(choices=HAT))
    vverh = forms.CharField(initial="Отсутствует", required=False, widget=forms.Select(choices=VVERH))
    niz = forms.CharField(initial="Отсутствует", required=False, widget=forms.Select(choices=NIZ))
    boots = forms.CharField(initial="Отсутствует", required=False, widget=forms.Select(choices=BOOTS))


class SearchForm1(forms.Form):
    name = forms.CharField(required=False, label='name', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(required=False, label='surname', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    fam = forms.CharField(required=False, label='fam', widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class CommentFormUser(forms.ModelForm):

    class Meta:
        model = Comment_user
        fields = ('text',)


class UserProfile(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')