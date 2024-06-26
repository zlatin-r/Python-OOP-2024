from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Test", 2024, 6.5)

    def test_init(self):
        self.assertEqual(self.movie.name, "Test")
        self.assertEqual(self.movie.year, 2024)
        self.assertEqual(self.movie.rating, 6.5)
        self.assertEqual(self.movie.actors, [])

    def test_setter_name_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_setter_year_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_name_already_added_returns_string_message(self):
        self.movie.actors = ["George"]

        result = self.movie.add_actor("George")

        self.assertEqual("George is already added in the list of actors!", result)

    def test_add_actor_happy_case(self):
        self.movie.add_actor("Todor")
        self.movie.add_actor("Kiro")

        self.assertEqual(["Todor", "Kiro"], self.movie.actors)

    def test__gt__first_better(self):
        m1 = Movie("Test", 2024, 6.5)
        m2 = Movie("Test2", 2020, 5.5)

        res = m1 > m2

        self.assertEqual('"Test" is better than "Test2"', res)

    def test__gt__second_better(self):
        m1 = Movie("Test", 2024, 6.5)
        m2 = Movie("Test2", 2020, 7.5)

        res = m1 > m2

        self.assertEqual('"Test2" is better than "Test"', res)

    def test__repr__no_actors(self):
        res = f"Name: {self.movie.name}\n" \
              f"Year of Release: {self.movie.year}\n" \
              f"Rating: {self.movie.rating:.2f}\n" \
              f"Cast: {', '.join(self.movie.actors)}"

        expect = f"Name: Test\n" \
                 f"Year of Release: 2024\n" \
                 f"Rating: 6.50\n" \
                 f"Cast: "

        self.assertEqual(expect, repr(self.movie))

    def test__repr__with_actors(self):
        self.movie.add_actor("Ivan")

        res = f"Name: {self.movie.name}\n" \
              f"Year of Release: {self.movie.year}\n" \
              f"Rating: {self.movie.rating:.2f}\n" \
              f"Cast: {', '.join(self.movie.actors)}"

        expect = f"Name: Test\n" \
                 f"Year of Release: 2024\n" \
                 f"Rating: 6.50\n" \
                 f"Cast: Ivan"

        self.assertEqual(expect, repr(self.movie))


if __name__ == '__main__':
    main()
