class TestLoginEndpoint:
    """
     This test verifies the correct operation of the login endpoint
     using the following test cases:
       - Valid endpoint request responds with status 200 and login information
       - Request endpoint with unregistered user responds with status code 400
       - Making an incomplete request to the endpoint responds with status 400 and error information
       - Request endpoint with registered name and invalid password return status 400 


    A valid request consists of
        - Valid reqbody
          * name: Not registered name and length > 3
          * password: String length > 8
   """
    endpoint_url = "/auth/login"

    def test_valid_request_responds_with_status_200_and_login_information(self, client, employee_user):
        """
            Verify that sending a valid request to the 'login' endpoint responds
            with a status code of 200 and user_id

            Expected behavior:
                - The response should have a status code of 200
                - The response should contain a status, message and user_id
        """
        response = client.post(self.endpoint_url, json={
            "name": employee_user["name"],
            "password": employee_user["password"]
        })

        assert response.status_code == 200

        login_information = response.get_json()

        assert login_information["status"] == "success"
        assert login_information["message"] == "Successful login"
        assert login_information["token"] != None

    def test_request_with_unregistered_user_responds_with_status_code_400(self, client):
        """
            Verify that sending a request with unregistered name to the 'login' endpoint responds
            with a status code of 400 and error json

            Expected behavior:
                - The response should have a status code of 400
                - The response should contain error json
        """
        response = client.post(self.endpoint_url, json={
            "name": 'unregisteredUserLG',
            "password": "unregisteredUserLG"
        })

        assert response.status_code == 400

        json_error = response.get_json()

        assert json_error["status"] == "error"
        assert json_error["message"] == "Invalid login credentials"

    def test_making_a_incomplete_request_to_endpoint_responds_with_status_400(self, client):
        """
            Verify that sending a valid request to the 'login' endpoint responds
            with a status code of 400 and error json

            Expected behavior:
                - The response should have a status code of 400
                - The response should contain error json
        """
        response = client.post(self.endpoint_url, json={
            "password": "unregisteredUserLG"
        })
        assert response.status_code == 400

        response = client.post(self.endpoint_url, json={
            "name": 'unregisteredUserLG'
        })
        assert response.status_code == 400

    def test_request_with_registered_name_and_invalid_password_responds_with_status_code_400(self, client, employee_user):
        """
            Verify that sending a request with registered name but invalid password
            to the 'login' endpoint responds with a status code of 400 and json_error

            Expected behavior:
                - The response should have a status code of 200
                - The response should contain a status, message and user_id
        """
        response = client.post(self.endpoint_url, json={
            "name": employee_user["name"],
            "password": "a invalid password for user"
        })

        assert response.status_code == 400
