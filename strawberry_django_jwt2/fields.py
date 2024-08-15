from typing import List, Optional

from strawberry_django.arguments import argument
from strawberry_django.fields.field import StrawberryDjangoField
from strawberry_django.arguments import StrawberryArgument


class StrawberryDjangoTokenField(StrawberryDjangoField):
    @property
    def arguments(self) -> List[StrawberryArgument]:
        return super().arguments + [argument("token", Optional[str])]


class StrawberryDjangoRefreshTokenField(StrawberryDjangoField):
    @property
    def arguments(self) -> List[StrawberryArgument]:
        return super().arguments + [argument("refresh_token", Optional[str])]
