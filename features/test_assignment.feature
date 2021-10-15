# Created by rana at 15/10/2021
Feature: user can search from home page successfully.


  Scenario: User should able to search and get search result
    Given I am on Homepage
    And I search for "House"
    Then I verify result page

  Scenario: Clicking on login should redirect user to login page.
    Given I am on Homepage
    And I click on Navigation bar
    And I click on Login button
    Then I verify login page

  Scenario:  User should able to swtich language in landlord faq page
    Given I am on Landlord FAQ page
    Then I verify changing language works
