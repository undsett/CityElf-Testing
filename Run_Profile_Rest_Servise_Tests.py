# --------------imports requests modules ----------------------------
import GET_user_by_id_test
import GET_all_users_test
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
        self.assertEqual (user_by_id['id'], user_id), (user_by_id['email'], 'Rozhkoandrew@gmail.com'), (
        user_by_id['phone'], '0939055320',user_by_id['password'],'qazxsw')

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

# ---------------------DELETE test---------------------------------------
class TestDeleteResponse(unittest.TestCase):
    def test_delete_response(self):
        str_r = str(delete_r)
        self.assertTrue(str_r == '<Response [200]>'),(search_response, 404)

# --------------------------Main body-------------------------------------
if __name__ == '__main__':
    post_r = POST_user_test.post_user("Rozhkoandrey@gmail.com", '0939055320' ,"qazxsw")
    user_id = GET_all_users_test.serach_by_email('Rozhkoandrey@gmail.com')
    put_r = (PUT_test_UPDATE_user.update_user(user_id, 'email', 'Rozhkoandrew@gmail.com'))
    user_by_id = GET_user_by_id_test.get_user_by_id(user_id)
    all_users_r = (GET_all_users_test.get_users_response())
    delete_r = DELETE_test.delete_user_by_id(user_id)
    search_response = (GET_user_by_id_test.get_user_by_id(user_id)['status'])
    unittest.main()







































