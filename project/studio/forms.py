from wtforms import (
    StringField,
    TextAreaField,
    SelectField
)

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Length,Optional,Regexp
from models import Authors,Category
from flask_pagedown.fields import PageDownField



class ArticleForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    body = PageDownField(validators=[InputRequired()])


class AuthorForm(FlaskForm):
    name = StringField(validators=[InputRequired(),
           Length(2, 300),
        Regexp(
                "^[A-Za-z][A-Za-z0-9_. ]*$",
                0,
                "Titles must have only letters, " "numbers, dots or underscores",
            ),

        ])

    
class CategoryForm(FlaskForm):
    c_title = StringField(validators=[InputRequired(),
        Length(2, 300),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_. ]*$",
                0,
                "Titles must have only letters, " "numbers, dots or underscores",
            ),
        ])