# --------------imports requests modules ----------------------------
import GET_requests
import PUT_requests_UPDATE_user
import POST_user_requests
import DELETE_request
import unittest
# ---------------Test POST module--------------------------------------
class TestcorrectPostResponse(unittest.TestCase):
    def test_post_resonse(self):
        str_r = str(post_r)
        self.assertTrue(str_r == '<Response [200]>')
# ----------------Test PUT module--------------------------------------
class TestCorrectPutResponse(unittest.TestCase):
    def test_response(self):
        str_r = str(put_r)
        self.assertTrue(str_r == '<Response [200]>')
#-----------------------------------------------------------------------
class TestFOrgorPassword(unittest.TestCase):
    def test_response(self):
        str_r = str(forgot_password)
        self.assertTrue(str_r == '<Response [200]>')
# ----------------TEST GET by id module----------------------------------
class TestGetModule(unittest.TestCase):
    def test_is_correct_id(self):
        self.assertEqual (user_by_id['id'], user_id), (user_by_id['email'], user_email), (
        user_by_id['phone'], user__correct_phone,user_by_id['password'],first_user_password)

    def test_is_correct_notification_response(self):
        str_r = str(notifications_by_id[0])
        self.assertEqual(str_r ,'<Response [200]>',)

    def test_is_rerurn_notifications(self):
        lst_of_keys = []
        for key,value in notifications_by_id[1].items():
            lst_of_keys.append(key)
        self.assertEqual(lst_of_keys[0] ,'sms') ,(lst_of_keys[1] ,'email'), (lst_of_keys[2] ,'push')

    def test_is_return_users(self):
        get_users_check = GET_requests.get_users()
        for dct in get_users_check:
            for key, value in dct.items():
                self.assertTrue(key == 'id')
                break

    def test_is_correct_response(self):
        str_r = str(all_users_r)
        self.assertTrue(str_r == '<Response [200]>',)

    def test_all_water_forecast_response(self):
        str_r = str(all_water_forecast)
        self.assertEqual(str_r ,'<Response [200]>',)
# ---------------------DELETE test---------------------------------------
class TestDeleteResponse(unittest.TestCase):
    def test_delete_response(self):
        str_r = str(delete_r)
        self.assertTrue(str_r == '<Response [200]>',),(search_response, 404 )
# --------------------------Main body-------------------------------------
if __name__ == '__main__':
#-----------------------USER info ---------------------------------------------------------------------------
    user_email = "Rozhkoandrew@gmail.com"
    user_false_phone = '0939055329'
    user__correct_phone = "0939055320"
    first_user_password = "qazxsw"
#------------------MAke sure that such user deleted before testing -------------------------------------------
    user_id_for_first_del = GET_requests.serach_by_email(user_email)
    delete_r = DELETE_request.delete_user_by_id(user_id_for_first_del)
#-----------------Create user and test------------------------------------------------------------------------
    post_r = POST_user_requests.post_user(user_email,  user_false_phone, first_user_password)
    user_id = GET_requests.serach_by_email(user_email)
    put_r = (PUT_requests_UPDATE_user.update_user(user_id, 'phone', user__correct_phone))
    forgot_password = POST_user_requests.post_for_forgot_password('Rozhkoandrew@gmail.com')
    user_by_id = GET_requests.get_user_by_id(user_id)
    notifications_by_id = GET_requests.get_notifications_by_id(user_id)
    all_users_r = (GET_requests.get_users_response())
#------------------Water forecast-------------------------------------------------------------------------------
    all_water_forecast = GET_requests.search_all_water_forecast()



#------------------Delete all------------------------------------------------------------------------------------
    delete_r = DELETE_request.delete_user_by_id(user_id)
    search_response = (GET_requests.get_user_by_id(user_id)['status'])
    unittest.main()







































