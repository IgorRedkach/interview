Scenario: check Bearer
	Given I do GET from /bearer
	Then status code is 200
	And Tokens are the same

Scenario: check UUID
	Given I do GET from /uuid
	Then status code is 200
	And UUID are not empty