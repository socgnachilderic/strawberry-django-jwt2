from datetime import datetime

import strawberry

from strawberry_django_jwt2.object_types import TokenPayloadType


@strawberry.type
class RefreshedTokenType:
    payload: TokenPayloadType
    token: str
    refresh_token: str
    refresh_expires_in: int


@strawberry.type
class RevokeType:
    revoked: datetime
