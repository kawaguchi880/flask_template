from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    NumberRange,
    ValidationError,
    length,
)


class NoWhitespace(DataRequired):
    """
    フィールド値に空白文字を一切含ませないバリデータ。
    """

    def __call__(self, form, field):
        super(NoWhitespace, self).__call__(form, field)
        if any(char.isspace() for char in field.data):
            raise ValidationError("空白文字を含めることはできません。")


class HiraganaOnly(NoWhitespace):
    """
    フィールド値にひらがな以外の文字を含ませないバリデータ。
    """

    def __call__(self, form, field):
        super().__call__(form, field)
        if not all("ぁ" <= char <= "ん" for char in field.data):
            raise ValidationError("ひらがなで入力してください。")


class BasicInfoForm(FlaskForm):
    school_name = SelectField(
        "学校名", coerce=int, validators=[DataRequired(message="学校名は必須項目です")]
    )
    grade = IntegerField(
        "学年",
        validators=[
            DataRequired(message="学年は必須項目です"),
            NumberRange(
                min=1, max=6, message="学年は1から6の範囲でなければなりません。"
            ),
        ],
        render_kw={"min": 1, "max": 6, "type": "number"},
    )
    class_number = IntegerField(
        "組",
        validators=[
            DataRequired(message="組は必須項目です"),
            NumberRange(min=1, max=6, message="組は1から6の範囲でなければなりません。"),
        ],
        render_kw={"min": 1, "max": 6, "type": "number"},
    )
    attendance_number = IntegerField(
        "出席番号",
        validators=[
            DataRequired(message="出席番号は必須項目です"),
            NumberRange(
                min=1, max=60, message="出席番号は1から60の範囲でなければなりません。"
            ),
        ],
        render_kw={"min": 1, "max": 60, "type": "number"},
    )
    family_name = StringField(
        "姓",
        validators=[
            DataRequired(message="姓は必須項目です"),
            NoWhitespace(message="姓に空白文字を含めることはできません。"),
            length(min=1, max=20),
        ],
    )
    family_name_kana = StringField(
        "せい",
        validators=[
            DataRequired(message="必須項目です"),
            HiraganaOnly(message="ひらがなを入力してください。"),
            length(min=1, max=20),
        ],
    )
    given_name = StringField(
        "名",
        validators=[
            DataRequired(message="名は必須項目です"),
            NoWhitespace(message="名に空白文字を含めることはできません。"),
            length(min=1, max=20),
        ],
    )
    given_name_kana = StringField(
        "めい",
        validators=[
            DataRequired(message="必須項目です"),
            HiraganaOnly(message="ひらがなを入力してください。"),
            length(min=1, max=20),
        ],
    )
    gender = SelectField(
        "性別",
        choices=[("male", "男性"), ("female", "女性")],
        validators=[DataRequired(message="性別は必須項目です")],
    )
    submit = SubmitField("送信")

    birth_date = DateField(
        "生年月日",
        format="%Y-%m-%d",
        validators=[
            DataRequired(message="生年月日は必須項目です"),
        ],
    )
