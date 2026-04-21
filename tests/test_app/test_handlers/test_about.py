import pytest
from app.handlers.about import about_text_handler


@pytest.mark.asyncio
async def test_about_text_handler():
    """
    Test: about_text_handler: success
    """
    class MockMessage:

        def __init__(self):
            self.answer_count = 0

        async def answer(self, *args, **kwargs):
            self.answer_count += 1

    message = MockMessage()
    assert message.answer_count == 0
    await about_text_handler(message)
    assert message.answer_count == 1
