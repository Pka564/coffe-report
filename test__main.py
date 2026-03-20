from main import median_coffee_report


def test_median_table_output(capsys):
    data = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "200"},
        {"student": "B", "coffee_spent": "300"},
        {"student": "B", "coffee_spent": "500"},
    ]

    median_coffee_report(data)

    output = capsys.readouterr().out

    assert "Student" in output
    assert "Median Coffee" in output

    assert "A" in output
    assert "B" in output

    assert "150" in output
    assert "400" in output


def test_sorting_in_table(capsys):
    data = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "200"},
        {"student": "B", "coffee_spent": "1000"},
        {"student": "B", "coffee_spent": "1000"},
    ]

    median_coffee_report(data)

    output = capsys.readouterr().out

    lines = output.splitlines()

    data_lines = [line for line in lines if "A" in line or "B" in line]

    assert "B" in data_lines[0]