
def test_create_expense(create_expense):
    assert create_expense.status_code == 200

    data = create_expense.json()
    assert data["title"] == "Test Expense"
    assert data["amount"] == 100.0



def test_get_expense(get_expense):
    assert get_expense.status_code == 200

    data = get_expense.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["title"] == "Test Expense"
    assert data[0]["amount"] == 100.0



def test_update_expense(update_expense):
    assert update_expense.status_code == 200

    data = update_expense.json()
    assert data["title"] == "Updated Expense"
    assert data["amount"] == 150.0


def test_delete_expense(delete_expense):
    assert delete_expense.status_code == 200

    data = delete_expense.json()
    assert delete_expense.status_code == 200


def test_get_unauthorized(test_get_expenses_unauthorized):
    assert test_get_expenses_unauthorized.status_code == 401



def test_get_non_existent_expense(test_get_non_existent_expense):
    assert test_get_non_existent_expense.status_code == 404