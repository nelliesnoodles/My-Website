
from converse.parsers import ParserBase, ParserResponse

class MyParser(ParserBase):
    def parse(self, query, session_id):
        # your code
       
        response = ParserResponse()
        response.text = "Hello human"
       
        response.params = {
        'code': code,
        'client_id': settings.SLACK_CLIENT_ID,
        'client_secret': settings.SLACK_CLIENT_SECRET
    }
       

        return response