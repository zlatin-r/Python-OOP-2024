from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_correct_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_invalid_value_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_but_already_hired_raise_exception(self):
        self.plantation.workers = ["Worker"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Worker")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_happy_case(self):
        res = self.plantation.hire_worker("Worker")

        self.assertEqual("Worker successfully hired.", res)
        self.assertEqual(["Worker"], self.plantation.workers)

    def test__len__(self):
        self.plantation.plants = {"Iva": "flower"}
        self.assertEqual(6, len(self.plantation))


if __name__ == '__main__':
    main()
