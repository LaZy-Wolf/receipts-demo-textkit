from textkit import snake_case


def test_camel():
    assert snake_case("helloWorld") == "hello_world"


def test_pascal():
    assert snake_case("UserProfile") == "user_profile"


def test_spaces_and_dashes():
    assert snake_case("hello big-world") == "hello_big_world"


def test_digits_stay_attached():
    assert snake_case("version2Update") == "version2_update"


def test_kebab():
    from textkit import kebab_case

    assert kebab_case("helloWorld") == "hello-world"
