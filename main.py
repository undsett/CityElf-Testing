# --------------imports requests modules ----------------------------
import GET_user_by_id_test
import GET_all_users_test
import GET_adresses_test
import PUT_test_UPDATE_user
import POST_user_test
import DELETE_test
import unittest


# ---------------Test POST module-------------------------------------
class TestcorrectPostResponse(unittest.TestCase):
    def test_post_resonse(self):
        str_r = str(post_r)
        self.assertTrue(str_r == '<Response [200]>')


# ----------------Test PUT module--------------------------------------
class TestCorrectPutResponse(unittest.TestCase):
    def test_response(self):
        str_r = str(put_r)
        self.assertTrue(str_r == '<Response [200]>')


# ----------------TEST GET by id module----------------------------------
class TestIsReturnUserById(unittest.TestCase):
    def test_is_correct_id(self):
        self.assertEqual(user_id['id'], 42), (user_id['firstname'], 'Artem'), (user_id['lastname'], 'Rozhko'), (
        user_id['email'], 'Rozhkoandrey@gmail.com')


# ---------------------TEST GET all users------------------------------------
class TestIsReturnUsers(unittest.TestCase):
    def test_is_return_users(self):
        get_users_check = GET_all_users_test.get_users()
        for dct in get_users_check:
            for key, value in dct.items():
                self.assertTrue(key == 'id')
                break

    def test_is_correct_response(self):
        str_r = str(all_users_r)
        self.assertTrue(str_r == '<Response [200]>')


# -----------------------TEST GET adresses---------------------------------
class Test_is_return_adresses(unittest.TestCase):
    def test_is_correct_address(self):
        self.assertEqual(get_adresses_check[0], 'Deribasovskaya 1', ), (get_adresses_check[1], 'Gagarina 20'),(type(get_adresses_check), type([]))
# ---------------------DELETE test---------------------------------------
class TestDeleteResponse(unittest.TestCase):
    def test_delete_response(self):
        str_r = str(delete_r)
        self.assertTrue(str_r == '<Response [200]>'),(search_response, 404)


# --------------------------Main body-------------------------------------
if __name__ == '__main__':
    post_r = POST_user_test.post_user(42, 'Andrew', 'Rozhko', 'Pishonovskaya 22', 'Rozhkoandrey@gmail.com',
                                      '0935549520',
                                      False, True,
                                      False,
                                      'Deribasovskaya 1', 'Gagarina 20')
    put_r = (PUT_test_UPDATE_user.update_user(42, 'firstname', 'Artem'))

    user_id = GET_user_by_id_test.get_user_by_id(42)
    all_users_r = (GET_all_users_test.get_users_response())
    get_adresses_check = GET_adresses_test.get_adresses_by_id(42)

    user_id_for_del = 42
    delete_r = DELETE_test.delete_user_by_id(user_id_for_del)
    search_response = (GET_user_by_id_test.get_user_by_id(user_id_for_del)['status'])
    unittest.main()







































