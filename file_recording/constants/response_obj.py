# -*- coding: utf-8 -*-
class ReturnObj:

    @staticmethod
    def ret(x):
        return {
            200: {'content': {'result': {},
                              'message': 'Success', 'error': False}, 'status': 200},
            201: {'content': {'result': {},
                              'message': 'Successfully Created', 'error': False}, 'status': 201},
            204: {'content': {'result': {},
                              'message': 'No Content', 'error': False}, 'status': 204},
            304: {'content': {'result': {},
                              'message': 'No Modified', 'error': True}, 'status': 304},
            400: {'content': {'result': {},
                              'message': 'Bad Request', 'error': True}, 'status': 400},
            401: {'content': {'result': {},
                              'message': 'Unauthorized Access', 'error': True}, 'status': 401},
            402: {'content': {'result': {},
                              'message': 'Something is Missing', 'error': True}, 'status': 402},
            403: {'content': {'result': {},
                              'message': 'Forbidden', 'error': True}, 'status': 403},
            404: {'content': {'result': {},
                              'message': 'Not Found', 'error': True}, 'status': 404},
            405: {'content': {'result': {},
                              'message': 'Method Not Allowed', 'error': True}, 'status': 405},
            409: {'content': {'result': {},
                              'message': 'Conflict Occurred', 'error': True}, 'status': 409},
            500: {'content': {'result': {},
                              'message': 'Internal Server Error', 'error': True}, 'status': 500},
            502: {'content': {'result': {},
                              'message': 'Bad Gateway', 'error': True}, 'status': 502},
            503: {'content': {'result': {},
                              'message': 'Service Unavailable', 'error': True}, 'status': 503},
        }[x]
