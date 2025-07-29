import main, unittest

# class TestMain(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(main.add(7, 2), 9)
#         self.assertEqual(main.add(-7, 2), -5)
#         self.assertEqual(main.add(77, 33), 110)
#         self.assertNotEqual(main.add(7, 2), 0)
#
#     def test_subtract(self):
#         self.assertEqual(main.sub(7, 2), 5)
#         self.assertEqual(main.sub(-7, 2), -9)
#         self.assertEqual(main.sub(77, 33), 44)
#         self.assertNotEqual(main.sub(7, 2), 0)
#
#     def test_multiply(self):
#         self.assertEqual(main.mul(7, 2), 14)
#         self.assertEqual(main.mul(-7, 2), -14)
#         self.assertEqual(main.mul(-5, -3), 15)
#         self.assertNotEqual(main.mul(7, 2), 0)
#
#     def test_divide(self):
#         self.assertEqual(main.div(7, 2), 3.5)
#         self.assertEqual(main.div(-7, 2), -3.5)
#         self.assertEqual(main.div(10, 5), 2)
#         self.assertNotEqual(main.div(7, 2), 0)
#
#         # self.assertRaises(ValueError, main.div, 10, 0)
#
#         with self.assertRaises(ValueError):
#             main.div(2, 0)
#
#     def test_is_even(self):
#         self.assertTrue(main.is_even(2))
#         self.assertFalse(main.is_even(1))
#         self.assertFalse(main.is_even(3))


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student1 = main.Student("John", "Doe", 1000)
        self.student2 = main.Student("Jane", "Smith", 1500)


    def test_get_email(self):

        # print("Test get email")

        self.assertEqual(self.student1.get_email("gmail.com"), "John.Doe@gmail.com")
        self.assertEqual(self.student2.get_email("yahoo.com"), "Jane.Smith@yahoo.com")

        self.student1.first_name = "Nicolas"
        self.student2.last_name = "White"

        self.assertEqual(self.student1.get_email("gmail.com"), "Nicolas.Doe@gmail.com")
        self.assertEqual(self.student2.get_email("yahoo.com"), "Jane.White@yahoo.com")

    def test_full_name(self):

        # print("Test full name")

        self.assertEqual(self.student1.full_name, "John Doe")
        self.assertEqual(self.student2.full_name, "Jane Smith")

        self.student1.first_name = "Nicolas"
        self.student2.last_name = "White"

        self.assertEqual(self.student1.full_name, "Nicolas Doe")
        self.assertEqual(self.student2.full_name, "Jane White")

    def test_apply_discount(self):

        # print("Test apply discount")

        self.student1.apply_discount()
        self.student2.apply_discount()

        self.assertEqual(self.student1.pay, 900)
        self.assertEqual(self.student2.pay, 1350)

    # def tearDown(self):
    #     print("Tear down")

if __name__ == '__main__':
    unittest.main()