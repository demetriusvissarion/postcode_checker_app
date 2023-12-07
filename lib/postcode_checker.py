import re

class PostcodeChecker():
    def check(self, postcode):
        if postcode is None:
            return False
        stripped_postcode = postcode.replace(" ", "")
        # print('stripped_postcode: ' + '[start]' + stripped_postcode + '[end]')
        return re.match(
            r"^[a-z]{1,2}\d[a-z\d]?\s*\d[a-z]{2}$",
            stripped_postcode,
            re.IGNORECASE) is not None
        #     r"^[a-z]\d[a-z\d]?\s*\d[a-z]{2}$",
        #     r"/^[a-z]{1,2}\d[a-z\d]?\s*\d[a-z]{2}$/i",
