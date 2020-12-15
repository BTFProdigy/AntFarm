import unittest
import boto3

class basic_integration_test(unittest.TestCase):

    def test_connection(self):
        # get resource and table
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Student')

        # AWS updates table indexes every 6 hours could be missing recent changes
        count = table.item_count()
        created = table.creation_date_time
        self.assertEqual(str(created), "2020-11-10 19:29:46.245000-05:00")
        self.assertGreaterEqual(count, 3)
        print(table.query_count())


if __name__ == '__main__':
    unittest.main()
