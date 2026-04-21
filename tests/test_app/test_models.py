from app.models import PersonForm, create_person_form


def test_create_person_form():
    """
    Test: create_person_form: success
    """
    expected_person = PersonForm(
        name='Leo',
        city='Perm',
        tg_id=666,
    )
    result = create_person_form(
        expected_person.name,
        expected_person.city,
        expected_person.tg_id)
    assert result == expected_person
