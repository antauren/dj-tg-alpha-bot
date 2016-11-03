""""Special config for using pytest."""

import pytest


@pytest.fixture(scope="session", autouse=True)
def auto_session_resource(request):
    """
    Auto session resource fixture.
    Starts once at the start of the session.
    """
    pass


@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests(request):
    print("callattr_ahead_of_alltests called")
    seen = set([None])
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        if cls not in seen:
            if hasattr(cls.obj, "callme"):
                cls.obj.callme()
            seen.add(cls)
