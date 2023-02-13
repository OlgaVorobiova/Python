property_transfer_xtml = """<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';
... //ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';
... //urn:multiCall/sessionId['?']</con:targetPath>
... """
>>> result = property_transfer_xtml.split('con:targetType')
>>> result[1] = result[1].strip('>''/''<')
>>> print('''result is word "''' + str(result[1]) + '''"''')

