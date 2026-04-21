import pytest
import pytest_asyncio
from app.db.models import Person
from app.db.repository import get_person_list, save_person
from app.db.session import session_cls
from app.models import PersonForm, create_person_form
from sqlalchemy import delete


@pytest_asyncio.fixture
async def session():
    async with session_cls() as session:
        stmt = delete(Person)
        await session.execute(stmt)
        await session.commit()
        yield session


@pytest.mark.asyncio
async def test_get_person_list_empty_db(session):
    """
    Test get_person_list: success: empty database
    """
    person_list = await get_person_list(
        session,
        0,
    )
    assert person_list == []


@pytest.mark.asyncio
async def test_get_person_list(session):
    """
    Test get_person_list: success: after save_person
    """
    person_form: PersonForm = create_person_form(
        name='Leo',
        city='Perm',
        tg_id=666,
    )
    _: Person = await save_person(session, person_form)
    person_list = await get_person_list(session, person_form.tg_id)
    assert person_list == [person_form]
